// BM-03 HUD checker. Usage (from _tools/ui): node bm03_check.js <out_dir>
// Renders bm03_before.html and bm03_after.html at a phone and a tablet viewport, measures every .hud element,
// checks it against reserved zones and house rules, writes JSON results and screenshots with the zones drawn.
//
// Reserved zones: approximate fractions measured by eye from Roblox's illustration
// "Touch-Reserved-Zones.png" (creator-docs, ui/position-and-size.md), one phone screenshot, 1680x806 px.
// They are NOT official dimensions; on tablets they are an extrapolation.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');

const ZONES = {
  coreTopLeft: { x0: 0.058, y0: 0.013, x1: 0.294, y1: 0.13 },   // Roblox menu/chat/mic buttons
  thumbstick:  { x0: 0.0,   y0: 0.43,  x1: 0.406, y1: 1.0 },    // dynamic thumbstick zone
  jump:        { cx: 0.868, cy: 0.832, rH: 0.10 },               // jump button circle, radius as fraction of height
};
const RULES = { minFontPx: 12, minTapPx: 44, maxInfoAreaPct: 15, thumbReachH: 0.35 }; // house rules

const VIEWPORTS = [
  { name: 'phone-landscape-844x390', width: 844, height: 390 },
  { name: 'tablet-landscape-1024x768', width: 1024, height: 768 },
];

function rectsOverlap(a, b) { return a.x0 < b.x1 && a.x1 > b.x0 && a.y0 < b.y1 && a.y1 > b.y0; }
function rectCircle(r, cx, cy, rad) {
  const nx = Math.max(r.x0, Math.min(cx, r.x1)), ny = Math.max(r.y0, Math.min(cy, r.y1));
  return (nx - cx) ** 2 + (ny - cy) ** 2 < rad ** 2;
}

async function check(page, file, vp, outDir) {
  await page.setViewportSize({ width: vp.width, height: vp.height });
  await page.goto('file://' + path.resolve(__dirname, file));
  const els = await page.$$eval('.hud', ns => ns.map(n => {
    const b = n.getBoundingClientRect(), cs = getComputedStyle(n);
    const fonts = [n, ...n.querySelectorAll('*')].map(e => parseFloat(getComputedStyle(e).fontSize));
    return { id: n.id, role: n.dataset.role, priority: +n.dataset.priority,
      x0: b.left, y0: b.top, x1: b.right, y1: b.bottom, w: b.width, h: b.height, minFont: Math.min(...fonts) };
  }));
  const W = vp.width, H = vp.height;
  const z = k => ({ x0: ZONES[k].x0 * W, y0: ZONES[k].y0 * H, x1: ZONES[k].x1 * W, y1: ZONES[k].y1 * H });
  const jcx = ZONES.jump.cx * W, jcy = ZONES.jump.cy * H, jr = ZONES.jump.rH * H;
  const issues = [];
  let infoArea = 0;
  for (const e of els) {
    if (rectsOverlap(e, z('coreTopLeft'))) issues.push([e.id, 'overlaps Roblox top-left core UI']);
    if (rectsOverlap(e, z('thumbstick'))) issues.push([e.id, 'inside thumbstick zone']);
    if (rectCircle(e, jcx, jcy, jr)) issues.push([e.id, 'overlaps jump button']);
    if (e.x0 < 0 || e.y0 < 0 || e.x1 > W || e.y1 > H) issues.push([e.id, 'outside viewport']);
    if (e.minFont < RULES.minFontPx) issues.push([e.id, `font ${e.minFont}px < ${RULES.minFontPx}px`]);
    if (e.role === 'action' && Math.min(e.w, e.h) < RULES.minTapPx) issues.push([e.id, `tap target ${Math.round(Math.min(e.w, e.h))}px < ${RULES.minTapPx}px`]);
    if (e.role === 'info') infoArea += e.w * e.h;
    if (e.priority === 1) {
      const d = Math.hypot((e.x0 + e.x1) / 2 - jcx, (e.y0 + e.y1) / 2 - jcy);
      if (d > RULES.thumbReachH * H) issues.push([e.id, `primary action ${Math.round(d)}px from jump centre > ${Math.round(RULES.thumbReachH * H)}px`]);
    }
  }
  // v2: HUD elements must not overlap each other (v1 of this checker did not test this).
  for (let i = 0; i < els.length; i++) for (let k = i + 1; k < els.length; k++)
    if (rectsOverlap(els[i], els[k])) issues.push([els[i].id, `overlaps ${els[k].id}`]);
  const infoPct = 100 * infoArea / (W * H);
  if (infoPct > RULES.maxInfoAreaPct) issues.push(['(info panels)', `cover ${infoPct.toFixed(1)}% of screen > ${RULES.maxInfoAreaPct}%`]);

  // Screenshot with zones drawn on top.
  await page.evaluate(({ Z, W, H }) => {
    const mk = (s) => { const d = document.createElement('div'); Object.assign(d.style, { position: 'absolute', pointerEvents: 'none', ...s }); document.body.appendChild(d); };
    for (const k of ['coreTopLeft', 'thumbstick']) { const r = Z[k]; mk({ left: r.x0 * W + 'px', top: r.y0 * H + 'px', width: (r.x1 - r.x0) * W + 'px', height: (r.y1 - r.y0) * H + 'px', outline: '2px dashed #00e5ff', background: 'rgba(0,229,255,.12)' }); }
    const j = Z.jump, r = j.rH * H; mk({ left: j.cx * W - r + 'px', top: j.cy * H - r + 'px', width: 2 * r + 'px', height: 2 * r + 'px', borderRadius: '50%', outline: '2px dashed #00e5ff', background: 'rgba(0,229,255,.12)' });
  }, { Z: ZONES, W, H });
  const shot = path.join(outDir, `${path.basename(file, '.html')}_${vp.name}.png`);
  await page.screenshot({ path: shot });
  return { file, viewport: vp.name, elements: els.map(e => ({ id: e.id, rect: [e.x0, e.y0, e.w, e.h].map(Math.round), minFont: e.minFont })), infoAreaPct: +infoPct.toFixed(1), issues, screenshot: path.basename(shot) };
}

(async () => {
  const outDir = path.resolve(process.argv[2] || '.');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const results = [];
  for (const f of ['bm03_before.html', 'bm03_after.html']) for (const vp of VIEWPORTS) results.push(await check(page, f, vp, outDir));
  await browser.close();
  fs.writeFileSync(path.join(outDir, 'bm03_results.json'), JSON.stringify({ zones: ZONES, rules: RULES, results }, null, 1));
  for (const r of results) {
    console.log(`${r.file} @ ${r.viewport}: ${r.issues.length} issues (info area ${r.infoAreaPct}%)`);
    for (const [id, msg] of r.issues) console.log(`   - ${id}: ${msg}`);
  }
})();
