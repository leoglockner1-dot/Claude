"use strict";
const $ = (s) => document.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmt = (n) => (n == null ? "–" : Number(n).toLocaleString());
const pct = (x, signed) => (x == null ? "–" : (signed && x > 0 ? "+" : "") + Math.round(x * 100) + "%");
const ago = (ts) => {
  if (!ts) return "never";
  const m = Math.round((Date.now() / 1000 - ts) / 60);
  return m < 60 ? `${m} min ago` : m < 1440 ? `${Math.round(m / 60)} h ago` : `${Math.round(m / 1440)} d ago`;
};
const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();

let report = null, selected = null, chart = null, wasRunning = false, mode = "niches";
const age = (d) => (d == null ? "–" : Math.round(d));

async function api(path, opts) {
  const r = await fetch(path, opts);
  return r.json();
}

async function loadStatus() {
  const s = await api("/api/status");
  const m = s.meta;
  const keys = [s.keys.anthropic ? "Claude ✓" : "Claude key missing", s.keys.youtube ? "YouTube ✓" : "YouTube key missing"];
  $("#status-line").textContent = `${m.runs} snapshots · ${m.history_hours} h of history · last collected ${ago(m.last_run_ts)} · ${keys.join(" · ")}`;
  const job = s.job, box = $("#job");
  $("#btn-collect").disabled = $("#btn-recommend").disabled = !!job.running;
  $("#btn-recommend").title = s.keys.anthropic ? "" : "Add ANTHROPIC_API_KEY to the .env file first";
  if (job.running) {
    box.className = "job";
    box.textContent = `${job.running === "collect" ? "Collecting data" : "Asking Claude"}…\n` + job.log.join("\n");
  } else if (job.last_error) {
    box.className = "job error";
    box.textContent = "Error: " + job.last_error;
  } else {
    box.className = "job hidden";
  }
  if (wasRunning && !job.running) { await loadTrends(); await loadPick(); }
  wasRunning = !!job.running;
}

async function loadTrends() {
  report = await api("/api/trends");
  $("#notes").innerHTML = report.notes.map((n) => `<div class="note">${esc(n)}</div>`).join("");
  renderTable();
}

function renderTable() {
  const niches = mode === "niches";
  const r = report.niche_rules || {};
  $("#mode-help").textContent = niches
    ? `Ideas from games under ${r.max_age_days} days old with ${fmt(r.min_demand)}+ players, where a Roblox search finds at most ${r.max_competitors} games with ${r.real_players}+ players.`
    : "Big themes (keywords and subgenres) ranked by momentum. Mostly crowded already; useful for context.";
  $("#genre-toggle").classList.toggle("hidden", niches);
  $("#trend-table thead").innerHTML = niches
    ? '<tr><th>#</th><th>Niche</th><th class="num">Score</th><th class="num">Games</th><th class="num">Leader</th><th class="num">Age (d)</th></tr>'
    : '<tr><th>#</th><th>Trend</th><th class="num">Score</th><th class="num">Games</th><th class="num">New</th><th class="num">Players</th></tr>';
  const hide = $("#hide-genres").checked;
  const rows = niches ? report.niches : report.trends.filter((t) => !hide || t.kind !== "genre");
  const bar = (t) => `<td class="num"><div class="scorecell"><div class="scorebar"><span style="width:${t.score}%"></span></div>${t.score.toFixed(0)}</div></td>`;
  const empty = niches
    ? "No niches found yet. Press <b>Collect now</b>; each run checks up to 150 new phrases, so more appear over the first day."
    : "No data yet. Press <b>Collect now</b> (takes ~4 minutes).";
  $("#trend-table tbody").innerHTML = rows.length ? rows.map((t, i) => niches ? `
    <tr data-id="${esc(t.id)}" class="${selected === t.id ? "active" : ""}">
      <td class="muted">${i + 1}</td>
      <td>${esc(t.label)}<span class="sub">${esc(t.lead_name)}</span></td>${bar(t)}
      <td class="num">${t.n_games}</td><td class="num">${fmt(t.lead_playing)}</td><td class="num">${age(t.lead_age_days)}</td>
    </tr>` : `
    <tr data-id="${esc(t.id)}" class="${selected === t.id ? "active" : ""}">
      <td class="muted">${i + 1}</td><td>${esc(t.label)}</td>${bar(t)}
      <td class="num">${t.n_games}</td><td class="num">${t.n_young}</td><td class="num">${fmt(t.total_ccu)}</td>
    </tr>`).join("") : `<tr><td colspan="6" class="muted">${empty}</td></tr>`;
  document.querySelectorAll("#trend-table tbody tr[data-id]").forEach((tr) =>
    tr.addEventListener("click", () => selectTrend(tr.dataset.id)));
  if (rows.length && !rows.some((t) => t.id === selected)) selectTrend(rows[0].id);
}

async function selectTrend(id) {
  selected = id;
  const niches = mode === "niches";
  const t = (niches ? report.niches : report.trends).find((x) => x.id === id);
  if (!t) return;
  const weights = niches ? report.niche_weights : report.weights;
  const labels = niches ? report.niche_labels : report.labels;
  document.querySelectorAll("#trend-table tbody tr").forEach((tr) => tr.classList.toggle("active", tr.dataset.id === id));
  $("#detail-title").textContent = t.label;
  $("#detail-sub").textContent = niches
    ? `Score ${t.score} · ${t.n_games} game${t.n_games === 1 ? "" : "s"} with real players · led by “${t.lead_name}” (${age(t.lead_age_days)} days old, ${fmt(t.lead_playing)} players)`
    : `Score ${t.score} · ${t.n_games} games by ${t.n_creators} creators · median age ${t.median_age_days} days · biggest game has ${pct(t.leader_share)} of players`;
  $("#breakdown").innerHTML = Object.entries(weights).map(([k, w]) => `
    <div class="brow" title="Weight ${Math.round(w * 100)}% of the score. Percentile vs the others in this list.">
      <span>${esc(labels[k])}</span>
      <div class="btrack"><div class="bfill" style="width:${t.breakdown[k]}%"></div></div>
      <span class="num">${t.breakdown[k]}</span>
    </div>`).join("");
  $("#signals").innerHTML = t.signals.map((s) => `<li>${esc(s)}</li>`).join("");
  $("#games-table tbody").innerHTML = t.games.map((g) => `
    <tr>
      <td>${g.url ? `<a href="${esc(g.url)}" target="_blank" rel="noopener">${esc(g.name)}</a>` : esc(g.name)}
        ${g.charts.includes("up-and-coming") ? '<span class="tag">up-and-coming</span>' : ""}</td>
      <td class="num">${fmt(g.playing)}</td><td class="num">${age(g.age_days)}</td>
      <td class="num">${pct(g.like_ratio)}</td>
      <td class="num ${g.ccu_dod > 0 ? "up" : g.ccu_dod < 0 ? "down" : ""}">${pct(g.ccu_dod, true)}</td>
    </tr>`).join("");
  drawHistory(t.games.slice(0, 5));
}

async function drawHistory(games) {
  const hist = await api("/api/history?ids=" + games.map((g) => g.universe_id).join(","));
  const colors = ["--s1", "--s2", "--s3", "--s4", "--s5"].map(css);
  const datasets = games.map((g, i) => ({
    label: g.name.length > 32 ? g.name.slice(0, 31) + "…" : g.name,
    data: (hist[g.universe_id] || []).map(([ts, p]) => ({ x: ts * 1000, y: p })),
    borderColor: colors[i], backgroundColor: colors[i], borderWidth: 2, pointRadius: 3, pointHoverRadius: 5, tension: 0.2,
  }));
  const points = Math.max(0, ...datasets.map((d) => d.data.length));
  $("#history-note").textContent = points < 3
    ? "Only a few snapshots so far. Lines fill in as the tool collects every few hours."
    : "Player counts swing by time of day; compare the same hour across days.";
  const xs = datasets.flatMap((d) => d.data.map((p) => p.x));
  const pad = 3 * 3600 * 1000;
  const xMin = xs.length ? Math.min(...xs) - (points < 2 ? pad : 0) : undefined;
  const xMax = xs.length ? Math.max(...xs) + (points < 2 ? pad : 0) : undefined;
  if (chart) chart.destroy();
  const grid = css("--border"), text = css("--text-2");
  chart = new Chart($("#history-chart"), {
    type: "line",
    data: { datasets },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false,
      interaction: { mode: "nearest", axis: "x", intersect: false },
      plugins: {
        legend: { position: "bottom", labels: { color: text, boxWidth: 10, boxHeight: 10, font: { size: 11 } } },
        tooltip: { callbacks: {
          title: (items) => new Date(items[0].parsed.x).toLocaleString([], { month: "short", day: "numeric", hour: "numeric", minute: "2-digit" }),
          label: (it) => ` ${it.dataset.label}: ${fmt(it.parsed.y)} players`,
        } },
      },
      scales: {
        x: { type: "linear", min: xMin, max: xMax, grid: { color: grid }, ticks: { color: text, maxTicksLimit: 6,
             callback: (v) => new Date(v).toLocaleString([], { month: "short", day: "numeric", hour: "numeric" }) } },
        y: { beginAtZero: true, grid: { color: grid }, ticks: { color: text, callback: (v) => Number(v).toLocaleString() } },
      },
    },
  });
}

function list(items, ordered) {
  const tag = ordered ? "ol" : "ul";
  return `<${tag}>${(items || []).map((i) => `<li>${esc(i)}</li>`).join("")}</${tag}>`;
}

async function loadPick() {
  const r = await api("/api/recommendation");
  if (!r) return;
  const p = r.top_pick, c = r.game_concept;
  $("#pick-body").classList.remove("muted");
  p.existing_games = p.existing_games || [];
  c.how_to_beat_existing_games = c.how_to_beat_existing_games || [];
  $("#pick-body").innerHTML = `
    <div class="pick-head">
      <span class="pick-title">${esc(p.trend_label)}</span>
      <span class="conf">Confidence ${p.confidence}/10 · window: ${esc(p.window_estimate)} · ${esc(r.served_by)} · ${ago(r.ts)}</span>
    </div>
    <p><b>${esc(p.one_line_verdict)}</b></p>
    <p>${esc(p.why_now)}</p>
    <div class="pick-cols">
      <div><h3>Already in this niche</h3>${list(p.existing_games)}<h3>How to beat them</h3>${list(c.how_to_beat_existing_games)}</div>
      <div><h3>Evidence</h3>${list(p.evidence)}</div>
      <div><h3>Risks</h3>${list(p.risks)}</div>
      <div><h3>Game concept: ${esc((c.working_titles || []).join(" / "))}</h3>
        <p>${esc(c.pitch)}</p><p><b>Twist:</b> ${esc(c.original_twist)}</p><p><b>Players:</b> ${esc(c.target_players)}</p></div>
      <div><h3>Core loop</h3>${list(c.core_loop, true)}<h3>Monetization</h3>${list(c.monetization)}</div>
      <div><h3>Build plan</h3>${(r.build_plan || []).map((ph) => `<p><b>${esc(ph.phase)}</b></p>${list(ph.goals)}`).join("")}</div>
      <div><h3>Icon &amp; thumbnail</h3>${list(c.icon_and_thumbnail_ideas)}<h3>Launch checklist</h3>${list(r.launch_checklist)}</div>
      <div><h3>Runner-ups</h3>${list((r.runner_ups || []).map((x) => `${x.trend_label}: ${x.reason}`))}
        <h3>Avoid</h3>${list((r.avoid || []).map((x) => `${x.trend_label}: ${x.reason}`))}</div>
      <div><h3>Data caveats</h3>${list(r.data_caveats)}</div>
    </div>`;
}

async function startJob(path) {
  const r = await api(path, { method: "POST" });
  if (!r.started) alert("Something is already running. Please wait for it to finish.");
  wasRunning = true;
  loadStatus();
}

$("#btn-collect").addEventListener("click", () => startJob("/api/collect"));
$("#btn-recommend").addEventListener("click", () => startJob("/api/recommend"));
$("#hide-genres").addEventListener("change", renderTable);
document.querySelectorAll(".tab").forEach((b) => b.addEventListener("click", () => {
  mode = b.dataset.mode;
  document.querySelectorAll(".tab").forEach((x) => x.classList.toggle("active", x === b));
  renderTable();
}));

(async () => {
  await Promise.all([loadStatus(), loadTrends(), loadPick()]);
  setInterval(loadStatus, 2500);
})();
