import json, html, os
R='/workspace/sites/red-polish/'; B='/red-polish/'; SITE='https://answerfirstai-ai.github.io/red-polish/'
C=json.load(open('/workspace/clients/la-salon-red-polish/content.json'))
FRESHA='https://www.fresha.com/a/red-polish-los-angeles-3324-west-6th-street-pw7nx5bw'
BOOK=FRESHA+'?utm_source=site'
TEL='tel:+12133871777'; PHONE='(213) 387-1777'
MAPS='https://www.google.com/maps/search/?api=1&query=Red+Polish+Nail+Salons+3324+W+6th+St+Los+Angeles+CA+90020'
DIR='https://www.google.com/maps/dir/?api=1&destination=3324+W+6th+St+Suite+F+Los+Angeles+CA+90020'
SETS=[(3,'Pearl studs','Silver pearl 3D studs','pearl'),(4,'Gold 3D chrome','Sculpted gold swirls on French','chrome'),(1,'White line art','Hand-drawn swirl French','line'),
 (5,'Tortoise & amber','Tortoiseshell, amber, gold charm','color'),(7,'Black stiletto','Gold charms on black','line'),(8,'Icy chrome','Aurora cat-eye shimmer','chrome'),
 (6,'Hot pink gloss','One bold coat','color'),(9,'Tiny painted','Hand-painted fruit & stars','line'),(10,'Milky nude','Glazed pearl almond','pearl')]
FILT=[('all','All'),('chrome','Chrome & cat-eye'),('pearl','Pearl & nude'),('line','Line art & painted'),('color','Color')]
I=lambda n:{'book':'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 2v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2H7Zm-2 8h14v10H5V10Z"/></svg>',
 'call':'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8Z"/></svg>',
 'pin':'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>'}[n]
def bookbtn(label='Book an appointment',cls='btn btn-primary',place='x'):
  return f'<a class="{cls}" href="{BOOK}&amp;utm_content={place}" target="_blank" rel="noopener" data-track="fresha-{place}">{I("book")}{label}<span class="sr"> (opens Fresha)</span></a>'
def callbtn(cls='btn btn-ghost'): return f'<a class="{cls}" href="{TEL}">{I("call")}Call {PHONE}</a>'
def dirbtn(cls='btn btn-ghost'): return f'<a class="{cls}" href="{DIR}" target="_blank" rel="noopener">{I("pin")}Directions</a>'
UL='<svg viewBox="0 0 100 8" preserveAspectRatio="none" aria-hidden="true"><path d="M2 5 C 30 1, 60 8, 98 3"/></svg>'
LD={"@context":"https://schema.org","@type":"NailSalon","@id":SITE+"#salon","name":"Red Polish","alternateName":["Red Polish Nail Salons","레드폴리쉬"],
 "url":SITE,"telephone":"+1-213-387-1777","image":[SITE+"assets/img/og.jpg",SITE+"assets/img/storefront.jpg"],
 "description":C['about']['value'],
 "address":{"@type":"PostalAddress","streetAddress":"3324 W 6th St, Suite F","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90020","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":34.0632103,"longitude":-118.2949821},"hasMap":MAPS,"areaServed":"Koreatown, Los Angeles",
 "sameAs":[FRESHA],"potentialAction":{"@type":"ReserveAction","target":FRESHA},"priceRange":"$$"}
def page(path,title,desc,body,extra_ld=None,cur=''):
  can=SITE+path
  ld=[LD]+([extra_ld] if extra_ld else [])
  nav=''.join(f'<li><a href="{B}{p}"{" aria-current=\"page\"" if cur==p else ""}>{t}{UL}</a></li>' for p,t in [('gallery/','Nail art'),('services/','Services'),('visit/','Visit')])
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{can}">
<meta name="theme-color" content="#B5121B"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{can}"><meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:site_name" content="Red Polish"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{B}favicon.ico" sizes="32x32"><link rel="icon" type="image/png" href="{B}assets/img/icon-512.png"><link rel="apple-touch-icon" href="{B}assets/img/icon-180.png"><link rel="manifest" href="{B}site.webmanifest">
<link rel="preload" href="{B}assets/fonts/bodoni-moda-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{B}assets/fonts/jost-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
{EXTRA_HEAD.get(path,'')}<link rel="stylesheet" href="{B}assets/css/site.css">
<script>document.documentElement.className=matchMedia('(prefers-reduced-motion: reduce)').matches?'rm':'js'</script>
<script type="application/ld+json">{json.dumps(ld if len(ld)>1 else LD,ensure_ascii=False)}</script>
<style>.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}</style></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap"><a class="wordmark" href="{B}" aria-label="Red Polish home"><i></i>Red Polish</a><nav aria-label="Main"><ul>{nav}</ul></nav>{bookbtn("Book on Fresha","btn btn-primary btn-sm","nav")}</div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><div><a class="wordmark" href="{B}"><i></i>Red Polish</a><p>Gel nails, extensions and nail art in Koreatown, Los Angeles.</p><p>{bookbtn("Book on Fresha","btn btn-white btn-sm","footer")}</p></div>
<div><h3>Visit</h3><address class="nap" style="font-size:.95rem;margin:0">Red Polish<br>3324 W 6th St, Suite F<br>Los Angeles, CA 90020<br><a href="{TEL}">{PHONE}</a></address><p><a href="{DIR}" target="_blank" rel="noopener">Get directions</a></p></div>
<div><h3>Hours</h3><p><span class="need">[NEED: hours, Google and Fresha differ]</span></p><p>Mon 10–6 (both sources)<br>Tue–Sun: open 10 AM, closing 7 or 8 PM. <a href="{B}visit/#hours">See both</a></p></div>
<p class="fine">Photos: Red Polish via Fresha. Prices from Red Polish's Fresha menu (October 2026) and may change. Confirm at booking. © 2026 Red Polish.</p></div></footer>
<div class="mbar" aria-label="Quick actions">{bookbtn("Book","btn btn-primary btn-sm","mbar")}<a class="btn btn-ghost btn-sm" href="{TEL}">{I("call")}Call</a></div>
<div class="toast" role="status" aria-live="polite"></div>
<script src="{B}assets/js/gsap.min.js" defer></script><script src="{B}assets/js/ScrollTrigger.min.js" defer></script>{'<script src="'+B+'assets/js/Flip.min.js" defer></script>' if path=='gallery/' else ''}<script src="{B}assets/js/app.js" defer></script>
</body></html>'''
EXTRA_HEAD={'':f'<link rel="preload" as="image" href="{B}assets/img/set-3-640.webp" imagesrcset="{B}assets/img/set-3-640.webp 640w, {B}assets/img/set-3-1200.webp 1200w" imagesizes="(max-width:820px) 92vw, 460px" fetchpriority="high">'}
def img(i,alt,sizes,cls='',lazy=True,w=1200):
  return f'<img src="{B}assets/img/set-{i}-1200.webp" srcset="{B}assets/img/set-{i}-640.webp 640w, {B}assets/img/set-{i}-1200.webp 1200w" sizes="{sizes}" width="1200" height="675" alt="{html.escape(alt)}"{" loading=\"lazy\" decoding=\"async\"" if lazy else " fetchpriority=\"high\""}{" class=\""+cls+"\"" if cls else ""}>'
SV={s['name']:s for s in C['services']}
def svc(n): return SV[n]
FEAT=[('Gel Manicure','Shaping, cuticle care, hand massage with organic lotion, chip-resistant gel.'),('Gel Manicure - Design','Your gel mani with nail art.'),
 ('Gel X (Short $75 / Medium $85 / Long $95)','Gel extensions. Short $75, medium $85, long $95.'),('Gel X with nail art','Add art to your Gel X set.'),('Gel Pedicure','Sea salt soak, mask, cuticle care, exfoliation, massage.'),
 ('Gel mani - French tip','Classic French in gel.'),('Gel Mani & Gel Pedi Combo (sale, same visit)','Hands and feet, same visit.'),('Regular Pedicure','The full pedicure ritual with regular polish.')]
def short(n): return n.split(' (')[0] if n.startswith('Gel X (') or 'Combo' in n else n
cards=''.join(f'<article class="card"><span class="dur">{svc(n)["duration"]}</span><h3>{html.escape(short(n))}</h3><p>{d}</p><div class="price">{svc(n)["price"]}</div></article>' for n,d in FEAT)
pan=''
for k,(i,t,s,f) in enumerate(SETS):
  pan+=f'<figure class="set"><div class="ph gloss"><span class="num">{k+1:02d} / 09</span>{img(i,f"Red Polish nail set: {t}, {s}","(max-width:820px) 78vw, 60vw")}</div><figcaption><b>{t}</b><span>{s}</span></figcaption></figure>'
  if k in (2,5): pan+=f'<div class="set-cta"><p>Like this one?</p><span>Save the photo and bring it to your appointment.</span>{bookbtn("Book this look","btn btn-white btn-sm",f"pan-{k+1}")}</div>'
NAIL='''<svg viewBox="0 0 200 320" role="img" aria-label="Illustrated almond nail changing finish"><defs>
<clipPath id="nc"><path d="M100 8C150 8 182 60 182 140v120c0 32-22 52-82 52s-82-20-82-52V140C18 60 50 8 100 8Z"/></clipPath>
<linearGradient id="gch" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f6f9"/><stop offset=".35" stop-color="#9aa1ad"/><stop offset=".5" stop-color="#ffffff"/><stop offset=".7" stop-color="#7b828e"/><stop offset="1" stop-color="#dfe3e9"/></linearGradient>
<radialGradient id="gce" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#e8f4ff"/><stop offset=".25" stop-color="#9fb6d8"/><stop offset="1" stop-color="#1d2a44"/></radialGradient>
<linearGradient id="gpe" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff6f4"/><stop offset=".3" stop-color="#f3d7e4"/><stop offset=".55" stop-color="#dfeaf6"/><stop offset=".8" stop-color="#f7ead2"/><stop offset="1" stop-color="#f1d6d9"/></linearGradient>
<linearGradient id="ggl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d9262f"/><stop offset=".6" stop-color="#B5121B"/><stop offset="1" stop-color="#4A0710"/></linearGradient>
<linearGradient id="ghl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<g clip-path="url(#nc)"><rect class="lay l0" width="200" height="320" fill="url(#gch)"/><g class="lay l1"><rect width="200" height="320" fill="url(#gce)"/><rect class="ce-band" x="-40" y="120" width="280" height="40" fill="#fff" opacity=".55" transform="rotate(-18 100 140)"/></g>
<g class="lay l2"><rect width="200" height="320" fill="url(#gpe)"/><circle class="pearl" cx="70" cy="230" r="13" fill="#fff"/><circle class="pearl" cx="100" cy="255" r="13" fill="#fff"/><circle class="pearl" cx="130" cy="230" r="13" fill="#fff"/></g>
<rect class="lay l3" width="200" height="320" fill="url(#ggl)"/><rect class="hl" x="-120" y="0" width="90" height="320" fill="url(#ghl)" transform="skewX(-14)"/></g></svg>'''
FIN=[('Chrome.','Mirror metal, like their sculpted gold swirls.'),('Cat-eye.','A band of light that moves when you do, like their icy aurora set.'),('Pearl.','Iridescent and soft, sometimes with real 3D studs.'),('Gloss.','One perfect coat of red. The name says it.')]
home=f'''<section class="hero" aria-labelledby="h1"><svg class="stroke" viewBox="0 0 1400 360" preserveAspectRatio="none" aria-hidden="true"><defs>
<linearGradient id="lac" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d4202b"/><stop offset=".55" stop-color="#B5121B"/><stop offset="1" stop-color="#7a0b13"/></linearGradient>
<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".8"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="bm"><path class="bpath" d="M-40 230 C 220 120, 460 300, 720 190 S 1180 120, 1440 170" stroke="#fff" stroke-width="150" fill="none" stroke-linecap="round"/></mask></defs>
<g mask="url(#bm)"><path d="M-60 150 C 200 60, 470 230, 720 120 S 1190 50, 1460 100 L 1460 250 C 1190 210, 980 300, 720 270 S 220 330,-60 300Z" fill="url(#lac)"/>
<path d="M-60 165 C 200 80, 470 245, 720 140 S 1190 70, 1460 118" stroke="#ff6b73" stroke-width="5" fill="none" opacity=".5"/><path d="M-60 285 C 220 312, 470 250, 720 255 S 1190 195,1460 235" stroke="#4A0710" stroke-width="7" fill="none" opacity=".35"/>
<rect class="shine" x="-300" y="40" width="260" height="300" fill="url(#shine)" transform="skewX(-20)"/></g></svg>
<div class="wrap"><div><p class="eyebrow h-in">Nail art · 3324 W 6th St, Koreatown</p><h1 id="h1"><span class="ln">Red</span><span class="ln"><em>Polish.</em></span></h1>
<p class="sub h-in">Nail art in Koreatown. Pearls, chrome, cat-eye, hand-painted detail.</p>
<div class="ctas h-in">{bookbtn(place="hero").replace('btn btn-primary','btn btn-primary js-fill')}{callbtn()}</div>
<div class="chips h-in"><a class="chip" href="{MAPS}" target="_blank" rel="noopener"><b>4.4★</b> Google · 177 reviews</a><span class="chip">Book instantly on Fresha</span></div></div>
<div class="frame gloss" id="heroframe">{img(3,"Silver pearl 3D stud nail art by Red Polish","(max-width:820px) 92vw, 460px",lazy=False)}<span class="tag">Set 01 · Pearl studs</span></div></div></section>
<section class="pan" id="sets" aria-labelledby="sets-h"><div class="wrap sec-head"><div><p class="eyebrow">Chapter 1 · The sets</p><h2 id="sets-h">Ten tiny <em>canvases.</em></h2></div><p class="muted">Pick a look and bring it to your appointment. Every photo here is Red Polish's own work.</p></div>
<div class="pan-track">{pan}</div><div class="wrap"><p class="credit">Photos: Red Polish via Fresha.</p></div></section>
<section class="finishes" id="finishes" aria-labelledby="fin-h"><h2 id="fin-h" class="sr">The finishes</h2><div class="fin-stage"><div class="fin-text"><p class="eyebrow">Chapter 2 · The finishes</p>
<div class="fin-words" aria-hidden="true">{''.join(f"<span>{w}</span>" for w,_ in FIN)}</div><div class="fin-copy">{''.join(f"<p>{d}</p>" for _,d in FIN)}</div></div>
<div class="nail" id="nail">{NAIL}</div></div><div class="fin-dots" aria-hidden="true"><i><b></b></i><i><b></b></i><i><b></b></i><i><b></b></i></div>
<div class="wrap fin-grid">{''.join(f"<div><b>{w}</b><p>{d}</p></div>" for w,d in FIN)}</div></section>
<section class="sec" id="services" aria-labelledby="svc-h"><div class="wrap sec-head"><div><p class="eyebrow">Services</p><h2 id="svc-h">Know the price <em>before you sit.</em></h2></div><p class="muted">From Red Polish's own Fresha menu. Swipe for more, or see the <a href="{B}services/">full menu of 29 services</a>.</p></div>
<div class="shelf" tabindex="0" aria-label="Featured services">{cards}<article class="card card-end"><h3>Ready?</h3><p>Pick your service and time on Fresha.</p>{bookbtn("Book on Fresha","btn btn-white btn-sm","shelf")}</article></div>
<div class="wrap"><p class="note">Prices from Fresha, October 2026. Prices may change, so confirm at booking.</p></div></section>
<section class="sec salon" id="salon" aria-labelledby="salon-h"><div class="wrap"><div><div class="blind"><img src="{B}assets/img/storefront.webp" width="382" height="215" loading="lazy" alt="Red Polish storefront with the NAILS RED POLISH sign on W 6th St"><div class="bands" aria-hidden="true">{"<i></i>"*6}</div></div><p class="credit">Photos: Red Polish via Fresha.</p></div>
<div><p class="eyebrow">The salon</p><h2 id="salon-h">On 6th, <em>in K-town.</em></h2><address class="nap">3324 W 6th St, Suite F<br>Los Angeles, CA 90020<br>Catalina Center, 6th &amp; Catalina</address>
<p><span class="need">[NEED: parking details]</span> <span class="need">[NEED: hours, sources differ]</span></p><div class="ctas">{dirbtn()}{callbtn()}</div></div></div></section>
<section class="book" id="book" aria-labelledby="book-h"><div class="wrap"><h2 id="book-h">Bring your <em>inspo.</em></h2><p>Book on Fresha in a minute, or call the salon.</p><div class="ctas">{bookbtn(place="book").replace("btn btn-primary","btn btn-white")}{callbtn()}{dirbtn()}</div></div></section>'''
looks=''.join(f'<figure class="look" data-f="{f}" data-flip-id="l{i}"><div class="ph">{img(i,f"Red Polish nail set: {t}, {s}","(max-width:560px) 92vw, (max-width:900px) 46vw, 380px")}</div><figcaption><div><b>{t}</b><small>{s}</small></div><a class="btn btn-primary btn-sm look-btn" href="{BOOK}&amp;utm_content=look-{i}" target="_blank" rel="noopener" data-look="Red Polish look: {t} ({s})">Book this look<span class="sr"> (opens Fresha, copies the look name)</span></a></figcaption></figure>' for i,t,s,f in SETS)
filt=''.join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{v}</button>' for k,v in FILT)
gallery=f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Nail art gallery</p><h1>Pick a <em>look.</em></h1><p>Nine real sets from Red Polish. Tap "Book this look" and we copy its name so you can paste it in your Fresha booking note.</p><div class="filters" role="group" aria-label="Filter by finish">{filt}</div></div></section>
<section><div class="wrap"><div class="masonry">{looks}</div><p class="credit" style="margin-top:-3.5rem;padding-bottom:4rem">Photos: Red Polish via Fresha.</p></div></section>
<section class="book red" style="--flood:1"><div class="wrap"><h2>Don't see <em>your idea?</em></h2><p>Bring a photo. Book on Fresha or call the salon.</p><div class="ctas">{bookbtn(place="gallery-end").replace("btn btn-primary","btn btn-white")}{callbtn()}</div></div></section>'''
GROUPS=[('Manicures',lambda n:n.startswith('Gel M') and '&' not in n or n.startswith('Gel mani')),('Pedicures',lambda n:'pedi' in n.lower() and '&' not in n),
 ('Gel X extensions',lambda n:n.lower().startswith('gel x') or n.startswith('GelX R') or n.startswith('GelX off')),('Combos & extras',lambda n:'&' in n or 'Massage' in n),('Removal & fixes',lambda n:'emoval' in n and not n.startswith('Gel pedi') and not n.startswith('Regular') or n=='Fix')]
used=set(); secs=''
for g,fn in GROUPS:
  rows=''
  for s in C['services']:
    if s['name'] in used or not fn(s['name']): continue
    used.add(s['name']); rows+=f'<div class="row"><dt>{html.escape(s["name"])}</dt><dd class="pr">{s["price"]}</dd><dd class="du">{s["duration"]}</dd></div>'
  secs+=f'<section><h2>{g}</h2><dl>{rows}</dl></section>'
assert len(used)==len(C['services']),(len(used),[s['name'] for s in C['services'] if s['name'] not in used])
notes=''.join(f'<li>{html.escape(n)}</li>' for n in C['service_notes']['value'])
services=f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Services &amp; prices</p><h1>The <em>menu.</em></h1><p>All {len(C['services'])} services from Red Polish's Fresha menu, with times. Prices may change, so confirm the final price when you book.</p><div class="ctas">{bookbtn(place="services-top")}{callbtn()}</div></div></section>
<div class="wrap"><div class="menu">{secs}<section class="incl"><h2>What's included</h2><ul>{notes}</ul><p>{bookbtn("Book on Fresha","btn btn-white btn-sm","services-incl")}</p></section></div>
<p class="note" style="padding-bottom:4rem">Source: Red Polish on Fresha, menu read October 2026. Prices and times may change. <span class="need">[NEED: owner to confirm current menu]</span></p></div>'''
HF=C['hours_fresha']['value']
rows=''.join(f'<tr class="{"diff" if d in ("Tue","Sun") else ""}"><th scope="row">{d}</th><td>{HF[d].replace("-","–")}</td><td>{"10–6" if d=="Mon" else "10–8"}</td></tr>' for d in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
visit=f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Visit</p><h1>Find <em>us.</em></h1><address class="nap">Red Polish<br>3324 W 6th St, Suite F<br>Los Angeles, CA 90020 (Koreatown)<br>Catalina Center strip mall, 6th &amp; Catalina<br><a href="{TEL}">{PHONE}</a></address><div class="ctas">{dirbtn("btn btn-primary")}{callbtn()}{bookbtn("Book on Fresha","btn btn-ghost","visit")}</div></div></section>
<section class="sec salon" style="padding-top:2rem"><div class="wrap"><div id="hours"><h2>Hours</h2><p><span class="need">[NEED: confirm hours, Fresha and Google differ on Tue and Sun]</span></p>
<table class="hours"><thead><tr><th scope="col">Day</th><th scope="col">Fresha</th><th scope="col">Google</th></tr></thead><tbody>{rows}</tbody></table><p class="muted">Calling ahead? {PHONE}. Times are AM–PM.</p></div>
<div><div class="blind"><img src="{B}assets/img/storefront.webp" width="382" height="215" loading="lazy" alt="Red Polish storefront with the NAILS RED POLISH sign"><div class="bands" aria-hidden="true">{"<i></i>"*6}</div></div><p class="credit">Photos: Red Polish via Fresha.</p>
<h2 style="font-size:2rem;margin-top:2rem">Parking</h2><p><span class="need">[NEED: parking details from the salon]</span></p><p><a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></p></div></div></section>'''
nf=f'<section class="page-hero" style="min-height:70vh"><div class="wrap"><p class="eyebrow">404</p><h1>This page <em>chipped.</em></h1><p>We couldn\'t find that page. Try the home page or book straight away.</p><div class="ctas"><a class="btn btn-ghost" href="{B}">Back home</a>{bookbtn(place="404")}</div></div></section>'
P=[('','Red Polish | Nail Art Salon in Koreatown, Los Angeles','Chrome, pearl, cat-eye and hand-painted nail art at 3324 W 6th St, Koreatown. Rated 4.4 on Google. Book online on Fresha or call (213) 387-1777.',home,''),
 ('gallery/','Nail Art Gallery | Red Polish, Koreatown LA','Real nail art sets from Red Polish in Koreatown: chrome, pearl studs, cat-eye, line art and hand-painted designs. Pick a look and book on Fresha.',gallery,'gallery/'),
 ('services/','Nail Services & Prices | Red Polish, Koreatown LA','Gel manicures from $50, gel pedicures from $60, Gel X from $75 and more. Full Red Polish menu with times. Book on Fresha or call (213) 387-1777.',services,'services/'),
 ('visit/','Visit Red Polish | 3324 W 6th St, Koreatown, Los Angeles','Find Red Polish at 3324 W 6th St, Suite F, Los Angeles, CA 90020 in Koreatown. Directions, hours and phone: (213) 387-1777.',visit,'visit/')]
for p,t,d,b,cur in P:
  os.makedirs(R+p,exist_ok=True)
  bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE}]+([{"@type":"ListItem","position":2,"name":t.split(' |')[0],"item":SITE+p}] if p else [])}
  open(R+p+'index.html','w').write(page(p,t,d,b,bc if p else None,cur))
open(R+'404.html','w').write(page('404.html','Page not found | Red Polish','This page could not be found.',nf).replace('<link rel="canonical" href="'+SITE+'404.html">','<meta name="robots" content="noindex">'))
open(R+'sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>' for p,*_ in P)+'</urlset>\n')
open(R+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
open(R+'site.webmanifest','w').write(json.dumps({"name":"Red Polish","short_name":"Red Polish","start_url":B,"display":"standalone","background_color":"#F8ECEE","theme_color":"#B5121B","icons":[{"src":B+"assets/img/icon-180.png","sizes":"180x180","type":"image/png"},{"src":B+"assets/img/icon-512.png","sizes":"512x512","type":"image/png"}]}))
open(R+'.nojekyll','w').write('')
print('ok')
