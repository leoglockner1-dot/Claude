#!/usr/bin/env python3
"""Build a video analysis sheet: 12 sampled frames + motion-energy and audio-RMS timeline.
Usage: python3 make_video_sheet.py <clip.mp4> <out.jpg> [frames=12]
Needs: ffmpeg on PATH, numpy, Pillow.
Legend: blue = motion energy (mean abs frame difference at 20 fps), orange = audio RMS (16 kHz mono),
white lines = audio onsets (RMS rises > 6 dB above the 150 ms running minimum), numbers = seconds."""
import sys, subprocess, numpy as np
from PIL import Image, ImageDraw
def frames(path, fps=20, w=160, h=90):
    raw = subprocess.run(['ffmpeg','-loglevel','error','-i',path,'-vf',f'fps={fps},scale={w}:{h}','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h,w).astype(np.float32)
def audio(path, sr=16000):
    raw = subprocess.run(['ffmpeg','-loglevel','error','-i',path,'-ac','1','-ar',str(sr),'-f','s16le','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.int16).astype(np.float32)/32768
def main(src, out, n=12):
    g = frames(src); fps=20; dur=len(g)/fps
    motion = np.r_[0, np.abs(np.diff(g,axis=0)).mean(axis=(1,2))]
    a = audio(src); hop=800
    rms = np.array([np.sqrt((a[i:i+hop]**2).mean()) for i in range(0,max(len(a)-hop,1),hop)]) if len(a)>hop else np.zeros(1)
    db = 20*np.log10(rms+1e-9); onsets=[]
    for i in range(3,len(db)):
        if db[i]-db[max(0,i-3):i].min()>6 and db[i]>-50 and (not onsets or i-onsets[-1]>3): onsets.append(i)
    cols, tw, th = 4, 320, 180; rows=(n+cols-1)//cols
    sheet = Image.new('RGB',(cols*tw, rows*th+160),(18,18,22)); d=ImageDraw.Draw(sheet)
    for k in range(n):
        t = dur*(k+0.5)/n
        img = subprocess.run(['ffmpeg','-loglevel','error','-ss',f'{t:.2f}','-i',src,'-frames:v','1','-vf',f'scale={tw}:{th}:force_original_aspect_ratio=decrease,pad={tw}:{th}:(ow-iw)/2:(oh-ih)/2','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
        try:
            import io; im=Image.open(io.BytesIO(img)).convert('RGB'); sheet.paste(im,((k%cols)*tw,(k//cols)*th))
        except Exception: pass
        d.text(((k%cols)*tw+6,(k//cols)*th+4),f'{t:.1f}s',fill=(255,255,0))
    y0=rows*th+10; H=130; W=cols*tw
    def plot(v,col,xscale):
        if len(v)<2 or v.max()<=0: return
        v=v/v.max(); pts=[(i*xscale, y0+H-v[i]*H) for i in range(len(v))]; d.line(pts,fill=col,width=2)
    for o in onsets: x=o*hop/16000/dur*W; d.line([(x,y0),(x,y0+H)],fill=(255,255,255),width=1)
    plot(motion,(80,150,255),W/max(len(motion)-1,1)); plot(rms,(255,150,40),W/max(len(rms)-1,1))
    for s in range(int(dur)+1): x=s/dur*W; d.text((x+2,y0+H+4),str(s),fill=(200,200,200))
    sheet.save(out,quality=85)
    return {'duration_s':round(dur,2),'onsets_s':[round(o*hop/16000,2) for o in onsets],'silent':bool(rms.max()<1e-4)}
if __name__=='__main__':
    print(main(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 12))
