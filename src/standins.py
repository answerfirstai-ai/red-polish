# Writes sl-* web images. 640/1024 from 1024px originals (downscale only); 1600/2048 only from Real-ESRGAN x4 outputs.
import os
from PIL import Image, ImageDraw, ImageFont
S='/workspace/clients/la-salon-red-polish/assets/standins/'; O='/workspace/sites/red-polish/assets/img/'
def save(im,base):
  im.save(base+'.webp',quality=80,method=6); im.save(base+'.avif',quality=55)
for i in range(1,7):
  o=Image.open(S+f'sl-{i}.jpg').convert('RGB'); W,H=o.size
  for w in (640,1024):
    save(o.resize((w,round(H*w/W)),Image.LANCZOS),O+f'sl-{i}-{w}')
  if os.path.exists(S+f'sl-{i}-x4.png'):
    x=Image.open(S+f'sl-{i}-x4.png').convert('RGB')
    for w in (1600,2048): save(x.resize((w,round(H*w/W)),Image.LANCZOS),O+f'sl-{i}-{w}')
    print(i,'full')
  else: print(i,'base only')
# OG 1200x630 from sl-1 x4 with tag burned in
x=Image.open(S+'sl-1-x4.png').convert('RGB'); W,H=x.size; t=round(W*630/1200)
og=x.crop((0,(H-t)//2,W,(H-t)//2+t)).resize((1200,630),Image.LANCZOS)
d=ImageDraw.Draw(og,'RGBA')
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22); g=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',54)
except: f=g=ImageFont.load_default()
d.rectangle((0,500,1200,630),fill=(20,6,8,190)); d.text((40,515),'Red Polish · Koreatown, LA',font=g,fill='white')
d.rectangle((900,20,1180,58),fill=(0,0,0,170)); d.text((912,26),'Illustrative (AI) image',font=f,fill='white')
og.save(O+'og.jpg',quality=85); print('og ok')
