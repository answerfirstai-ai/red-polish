import json, html, os
R='/workspace/sites/red-polish/'; B='/red-polish/'; SITE='https://answerfirstai-ai.github.io/red-polish/'
C=json.load(open('/workspace/clients/la-salon-red-polish/content.json'))
FRESHA='https://www.fresha.com/a/red-polish-los-angeles-3324-west-6th-street-pw7nx5bw'
BOOK=FRESHA+'?utm_source=site'
TEL='tel:+12133871777'; PHONE='(213) 387-1777'
MAPS='https://www.google.com/maps/search/?api=1&query=Red+Polish+Nail+Salons+3324+W+6th+St+Los+Angeles+CA+90020'
DIR='https://www.google.com/maps/dir/?api=1&destination=3324+W+6th+St+Suite+F+Los+Angeles+CA+90020'
SETS=[(3,'Pearl.','Silver 3D studs','pearl'),(4,'Gold chrome.','Sculpted gold on French tips','chrome'),(1,'White line art','Hand-drawn swirl French','line'),
 (5,'Tortoise & amber','Tortoiseshell, amber, gold charm','color'),(7,'Black stiletto','Gold charms on black','line'),(8,'Cat-eye.','Icy aurora shimmer','chrome'),
 (6,'Hot pink gloss','One bold coat','color'),(9,'Hand-painted.','Tiny fruit and stars','line'),(10,'Milky nude','Glazed pearl almond','pearl')]
FILT=[('all','All'),('chrome','Chrome & cat-eye'),('pearl','Pearl & nude'),('line','Line art & painted'),('color','Color')]
I=lambda n:{'book':'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 2v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2H7Zm-2 8h14v10H5V10Z"/></svg>',
 'call':'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8Z"/></svg>',
 'pin':'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>'}[n]
def bookbtn(label='Book an appointment',cls='btn btn-primary',place='x'):
  return f'<a class="{cls}" href="{BOOK}&amp;utm_content={place}" target="_blank" rel="noopener" data-track="fresha-{place}">{I("book")}{label}<span class="sr"> (opens Fresha)</span></a>'
def callbtn(cls='btn btn-ghost'): return f'<a class="{cls}" href="{TEL}">{I("call")}Call {PHONE}</a>'
def dirbtn(cls='btn btn-ghost'): return f'<a class="{cls}" href="{DIR}" target="_blank" rel="noopener">{I("pin")}Directions</a>'
UL='<svg viewBox="0 0 100 8" preserveAspectRatio="none" aria-hidden="true"><path d="M2 5 C 30 1, 60 8, 98 3"/></svg>'
LD={"@context":"https://schema.org","@type":"NailSalon","@id":SITE+"#salon","name":"Red Polish","alternateName":"Red Polish Nail Salons",
 "url":SITE,"telephone":"+1-213-387-1777","image":SITE+"assets/img/icon-512.png","logo":SITE+"assets/img/icon-512.png",
 "description":"Nail salon in Koreatown, Los Angeles. Book on Fresha.",
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
<header class="nav"><div class="wrap"><a class="wordmark" href="{B}" aria-label="Red Polish home"><i></i>Red Polish</a><nav aria-label="Main"><ul>{nav}</ul><details class="mnav"><summary aria-label="Menu"><span></span>Menu</summary><div class="mpanel"><a href="{B}">Home</a>{nav.replace("<li>","").replace("</li>","")}<a href="{TEL}">Call {PHONE}</a></div></details></nav>{bookbtn("Book on Fresha","btn btn-primary btn-sm","nav")}</div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><div class="gloss-line" aria-hidden="true"></div><div><a class="wordmark" href="{B}"><i></i>Red Polish</a><p>Red Polish, 3324 W 6th St, Suite F, Los Angeles 90020. <a href="{TEL}">(213) 387-1777</a>.</p><p>{bookbtn("Book on Fresha","btn btn-white btn-sm","footer")}</p></div>
<div><h2 class="fh">Visit</h2><address class="nap" style="font-size:.95rem;margin:0">Red Polish<br>3324 W 6th St, Suite F<br>Los Angeles, CA 90020<br><a href="{TEL}">{PHONE}</a></address><p><a href="{DIR}" target="_blank" rel="noopener">Get directions</a></p></div>
<div><h2 class="fh">Hours</h2><p>Per Fresha: Mon 10-6, Tue 10-7, Wed-Sat 10-8, Sun 10-7. <a href="{TEL}">Call to confirm.</a></p></div>
<p class="fine">Nail-art and storefront photos: Photos from Red Polish's Fresha page. Scenes marked "Illustrative" are AI-generated atmosphere, not photos of Red Polish. Prices from Red Polish's Fresha menu (October 2026) and may change. Confirm at booking. © 2026 Red Polish.</p></div></footer>
<div class="mbar" aria-label="Quick actions">{bookbtn("Book","btn btn-primary btn-sm","mbar")}<a class="btn btn-ghost btn-sm" href="{TEL}">{I("call")}Call</a></div>
<div class="toast" role="status" aria-live="polite"></div>
<script src="{B}assets/js/gsap.min.js" defer></script><script src="{B}assets/js/ScrollTrigger.min.js" defer></script>{'<script src="'+B+'assets/js/Flip.min.js" defer></script>' if path=='gallery/' else ''}<script src="{B}assets/js/app.js" defer></script>
</body></html>'''
EXTRA_HEAD={'':f'<link rel="preload" as="image" type="image/avif" media="(max-width:820px)" imagesrcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" imagesizes="100vw" fetchpriority="high"><link rel="preload" as="image" type="image/avif" media="(min-width:821px)" imagesrcset="{B}assets/img/hero-d-960.avif 960w, {B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" imagesizes="100vw" fetchpriority="high">'}
def img(i,alt,sizes,cls='',lazy=True,w=1200):
  return f'<img src="{B}assets/img/set-{i}-1200.webp" srcset="{B}assets/img/set-{i}-640.webp 640w, {B}assets/img/set-{i}-1200.webp 1200w" sizes="{sizes}" width="1200" height="675" alt="{html.escape(alt)}"{" loading=\"lazy\" decoding=\"async\"" if lazy else " fetchpriority=\"high\""}{" class=\""+cls+"\"" if cls else ""}>'
SV={s['name']:s for s in C['services']}
def svc(n): return SV[n]
FEAT=[('Gel Manicure','from $50','Gel polish manicure'),('Gel Manicure Design','from $51','Gel manicure with nail art'),('Gel Pedicure','from $60','Gel polish pedicure'),('Regular Pedicure','from $40','Classic pedicure'),('Add-ons','$5 / from $10','Extras added to a service'),('GelX','See Fresha','Listed on Fresha. Price on the booking page')]
def short(n): return n.split(' (')[0] if n.startswith('Gel X (') or 'Combo' in n else n
cards=''
pan='';tray=''.join(f'<figure class="set{" lead" if k==0 else ""}"><div class="ph">{img(i,f"Real nail art by Red Polish: {t} {s}","(max-width:820px) 80vw, 40vw")}</div><figcaption><b>{t.rstrip('.')}, {s[0].lower()+s[1:]}</b></figcaption></figure>' for k,(i,t,s,f) in enumerate([x for x in SETS if x[0]!=3]))
for k,(i,t,s,f) in enumerate(SETS):
  pan+=f'<figure class="set"><div class="ph"><span class="num">{k+1:02d} / 09</span>{img(i,f"Red Polish nail set: {t}, {s}","(max-width:820px) 78vw, 60vw")}</div><figcaption><b>{t}</b><span>{s}</span></figcaption></figure>'
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
def pic(n,alt,sizes,lazy=True,cls='',w=1024,h=576):
  ss=lambda e:f'{B}assets/img/{n}-640.{e} 640w, {B}assets/img/{n}-1024.{e} 1024w'
  return f'<picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}"><img src="{B}assets/img/{n}-1024.webp" srcset="{ss("webp")}" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(alt)}"{" class=\""+cls+"\"" if cls else ""}{" loading=\"lazy\" decoding=\"async\"" if lazy else " fetchpriority=\"high\""}></picture>'
ILL='<span class="ill">Illustrative scene. Not a photo of Red Polish.</span>'
REAL="Photos from Red Polish's Fresha page"
home=f"""<section class="hero" aria-labelledby="h1"><div class="hero-media"><picture><source media="(max-width:820px)" type="image/avif" srcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" sizes="100vw"><source media="(max-width:820px)" type="image/webp" srcset="{B}assets/img/hero-m-800.webp 800w, {B}assets/img/hero-m-1200.webp 1200w, {B}assets/img/hero-m-1600.webp 1600w" sizes="100vw"><source type="image/avif" srcset="{B}assets/img/hero-d-960.avif 960w, {B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" sizes="100vw"><img class="poster" src="{B}assets/img/hero-d-1920.webp" srcset="{B}assets/img/hero-d-960.webp 960w, {B}assets/img/hero-d-1280.webp 1280w, {B}assets/img/hero-d-1920.webp 1920w, {B}assets/img/hero-d-2880.webp 2880w" sizes="100vw" width="2880" height="1620" alt="Illustrative scene: a faceted bottle of red lacquer with a chrome cap in a beam of light" fetchpriority="high"></picture>{ILL}</div>
<div class="sweep" aria-hidden="true"></div>
<div class="hero-inner"><p class="eyebrow">Nail art · Koreatown, Los Angeles</p><h1 id="h1"><span>Red</span><em>Polish.</em></h1>
<div class="hero-side"><p class="sub">Nail salon at 3324 W 6th St, Suite F, Koreatown. Gel, pedicures and nail art, booked on Fresha.</p>
<div class="ctas">{bookbtn("Book on Fresha",place="hero")}{callbtn("btn btn-glass")}</div>
</div>
</div></section>
<section class="uncap" id="bead" aria-labelledby="bead-h"><div class="u-grid">
<div class="u-copy"><h2 id="bead-h">Gel manicures <em>from $50</em></h2><p>From prices on Red Polish's Fresha menu, October 2026.</p>{bookbtn("Book on Fresha","btn btn-primary btn-sm","bead")}
<figure class="u-macro">{pic("ai-2-brush","Illustrative scene. Not a photo of Red Polish. A nail polish brush with a bead of red lacquer.","(max-width:820px) 60vw, 26vw",w=768,h=768)}<span class="ill">Illustrative scene. Not a photo of Red Polish.</span></figure></div>
<figure class="u-real"><div class="focus">{img(3,"Real nail art by Red Polish: silver pearl 3D studs","(max-width:820px) 100vw, 58vw")}</div><figcaption>Pearl, silver 3D studs <span>{REAL}</span></figcaption></figure></div></section>
<section class="sets" id="sets" aria-labelledby="sets-h"><div class="sets-head"><h2 id="sets-h">Sets from Red Polish's <em>Fresha page</em></h2><p>Bring a photo of the look you want.</p></div>
<div class="rail tray" tabindex="0" role="region" aria-label="Nail sets">{tray}</div><p class="credit wrap">{REAL}</p></section>
<section class="prices" id="prices" aria-labelledby="pr-h"><div class="spec"><div class="spec-head"><h2 id="pr-h">Prices on <em>Fresha</em></h2><p>"From" prices on Red Polish's Fresha menu, October 2026. Prices may change.</p></div>
<dl class="spec-list">{''.join(f'<div><dt>{html.escape(n)}</dt><dd>{"Listed, price on Fresha" if n=="GelX" else pr}</dd></div>' for n,pr,d in FEAT)}</dl>
<div class="ctas">{bookbtn("Book on Fresha","btn btn-primary","prices")}{callbtn()}</div></div></section>
<section class="salon" id="salon" aria-labelledby="salon-h"><div class="s-grid">
<figure class="s-photo"><div class="push"><img src="{B}assets/img/storefront.webp" width="382" height="215" loading="lazy" alt="Real photo: Red Polish storefront with the NAILS RED POLISH sign"></div><figcaption>The real storefront · Photos from Red Polish's Fresha page</figcaption></figure>
<div class="s-copy"><h2 id="salon-h">3324 W 6th St, <em>Suite F</em></h2><address class="nap">Los Angeles, CA 90020<br>Koreatown</address>
<p>Hours per Fresha: Mon 10-6, Tue 10-7, Wed-Sat 10-8, Sun 10-7. <a href="{TEL}">Call to confirm.</a></p><p><span class="need">[NEED: parking details]</span></p><div class="ctas">{dirbtn("btn btn-glass")}{callbtn("btn btn-glass")}</div></div></div></section>
<section class="book" id="book" aria-labelledby="book-h"><div class="b-inner"><h2 id="book-h">Book on <em>Fresha</em></h2><div><p>Bring a photo of the set you want, or call the salon.</p><div class="ctas">{bookbtn("Book on Fresha","btn btn-white","book")}{callbtn("btn btn-glass")}</div></div></div></section>"""
looks=''.join(f'<figure class="look" data-f="{f}" data-flip-id="l{i}"><div class="ph">{img(i,f"Red Polish nail set: {t}, {s}","(max-width:560px) 92vw, (max-width:900px) 46vw, 380px")}</div><figcaption><div><b>{t}</b><small>{s}</small></div><a class="btn btn-primary btn-sm look-btn" href="{BOOK}&amp;utm_content=look-{i}" target="_blank" rel="noopener" data-look="Red Polish look: {t} ({s})">Book this look<span class="sr"> (opens Fresha, copies the look name)</span></a></figcaption></figure>' for i,t,s,f in SETS)
filt=''.join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{v}</button>' for k,v in FILT)
gallery=f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Nail art gallery</p><h1>Pick a <em>look.</em></h1><p>Nine real sets from Red Polish. Real work by Red Polish. Tap "Book this look" and we copy its name so you can paste it in your Fresha booking note.</p><div class="filters" role="group" aria-label="Filter by finish">{filt}</div></div></section>
<section><div class="wrap"><div class="masonry">{looks}</div><p class="credit" style="margin-top:-3.5rem;padding-bottom:4rem">Photos from Red Polish's Fresha page.</p></div></section>
<section class="book red" style="--flood:1"><div class="wrap"><h2>Don't see <em>your idea?</em></h2><p>Bring a photo. Book on Fresha or call the salon.</p><div class="ctas">{bookbtn(place="gallery-end").replace("btn btn-primary","btn btn-white")}{callbtn()}</div></div></section>'''
rows=''.join(f'<li><span class="pn">{html.escape(n)}</span><span class="pd">{d}</span><span class="pp">{pr}</span></li>' for n,pr,d in FEAT)
services=f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Services &amp; prices</p><h1>The <em>menu.</em></h1><p>Verified "from" prices on Red Polish's Fresha menu (October 2026). The full, current menu with every option and time is on Fresha. Prices may change, so confirm when you book.</p><div class="ctas">{bookbtn("Full menu on Fresha",place="services-top")}{callbtn()}</div></div></section>
<div class="wrap" style="padding-bottom:5rem"><ol class="plist plist-light">{rows}</ol><p class="note">Source: Red Polish on Fresha, read October 2026.</p></div>'''
HR=[('Monday','10 AM - 6 PM'),('Tuesday','10 AM - 7 PM'),('Wednesday','10 AM - 8 PM'),('Thursday','10 AM - 8 PM'),('Friday','10 AM - 8 PM'),('Saturday','10 AM - 8 PM'),('Sunday','10 AM - 7 PM')]
rows=''.join(f'<tr><th scope="row">{d}</th><td>{h}</td></tr>' for d,h in HR)
visit=f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Visit</p><h1>Find <em>us.</em></h1><address class="nap">Red Polish<br>3324 W 6th St, Suite F<br>Los Angeles, CA 90020 (Koreatown)<br>Catalina Center strip mall, 6th &amp; Catalina<br><a href="{TEL}">{PHONE}</a></address><div class="ctas">{dirbtn("btn btn-primary")}{callbtn()}{bookbtn("Book on Fresha","btn btn-ghost","visit")}</div></div></section>
<section class="sec salon" style="padding-top:2rem"><div class="wrap"><div id="hours"><h2>Hours <small style="font-size:.45em">(per Fresha)</small></h2><table class="hours"><thead><tr><th scope="col">Day</th><th scope="col">Hours</th></tr></thead><tbody>{rows}</tbody></table><p class="muted">Hours as listed on Fresha. Some Google-derived listings show Tuesday and Sunday until 8 PM. <a href="{TEL}">Call {PHONE} to confirm.</a></p></div>
<div><div class="blind"><img src="{B}assets/img/storefront.webp" width="382" height="215" loading="lazy" alt="Red Polish storefront with the NAILS RED POLISH sign"></div><p class="credit">Photos: Red Polish via Fresha.</p>
<h2 style="font-size:2rem;margin-top:2rem">Parking</h2><p><span class="need">[NEED: parking details from the salon]</span></p><p><a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></p></div></div></section>'''
nf=f'<section class="page-hero" style="min-height:70vh"><div class="wrap"><p class="eyebrow">404</p><h1>This page <em>chipped.</em></h1><p>We couldn\'t find that page. Try the home page or book straight away.</p><div class="ctas"><a class="btn btn-ghost" href="{B}">Back home</a>{bookbtn(place="404")}</div></div></section>'
P=[('','Red Polish | Nail Art Salon in Koreatown, Los Angeles','Chrome, pearl, cat-eye and hand-painted nail art at 3324 W 6th St, Koreatown. Book online on Fresha or call (213) 387-1777.',home,''),
 ('gallery/','Nail Art Gallery | Red Polish, Koreatown LA','Real nail art sets from Red Polish in Koreatown: chrome, pearl studs, cat-eye, line art and hand-painted designs. Pick a look and book on Fresha.',gallery,'gallery/'),
 ('services/','Nail Services & Prices | Red Polish, Koreatown LA','Gel manicures from $50, gel pedicures from $60, regular pedicures from $40 at Red Polish in Koreatown. Full Red Polish menu with times. Book on Fresha or call (213) 387-1777.',services,'services/'),
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
