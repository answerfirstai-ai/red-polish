(()=>{const d=document,H=d.documentElement,RM=H.classList.contains('rm');
const nav=d.querySelector('.nav'),mbar=d.querySelector('.mbar');
const onS=()=>{const y=scrollY;nav.classList.toggle('scrolled',y>20);mbar&&mbar.classList.toggle('on',y>400)};addEventListener('scroll',onS,{passive:true});onS();
const toast=d.querySelector('.toast');let tt;function say(m){toast.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="#fff" stroke-width="2.5" d="M4 12l5 5L20 6"/></svg>'+m;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>toast.classList.remove('on'),2800)}
d.querySelectorAll('[data-look]').forEach(a=>a.addEventListener('click',()=>{const t=a.dataset.look;try{navigator.clipboard&&navigator.clipboard.writeText(t).then(()=>say('Look copied. Paste it in your booking note.'),()=>{})}catch(e){}}));
d.querySelectorAll('.btn').forEach(b=>b.addEventListener('pointerdown',()=>{b.classList.remove('zip');void b.offsetWidth;b.classList.add('zip')}));
if(matchMedia('(pointer:fine)').matches&&!RM)d.querySelectorAll('.look .ph').forEach(p=>p.addEventListener('pointermove',e=>{const r=p.getBoundingClientRect();p.style.setProperty('--mx',e.clientX-r.left+'px');p.style.setProperty('--my',e.clientY-r.top+'px')}));
// gallery filter
const fb=d.querySelectorAll('[data-filter]');if(fb.length){fb.forEach(b=>b.addEventListener('click',()=>{const f=b.dataset.filter;fb.forEach(x=>x.setAttribute('aria-pressed',x===b));const items=d.querySelectorAll('.look');
 const st=window.Flip&&!RM?Flip.getState(items):null;items.forEach(i=>i.classList.toggle('hide',f!=='all'&&i.dataset.f!==f));
 if(st)Flip.from(st,{duration:.55,ease:'power2.inOut',stagger:.02,absolute:true,onEnter:e=>gsap.fromTo(e,{opacity:0,scale:.9},{opacity:1,scale:1,duration:.4}),onLeave:e=>gsap.to(e,{opacity:0,scale:.9,duration:.3})})}))}
if(!window.gsap){H.classList.add('nojs');return}
gsap.registerPlugin(ScrollTrigger);window.Flip&&gsap.registerPlugin(Flip);
if(RM){d.querySelector('.book')&&d.querySelector('.book').classList.add('red');return}
const mm=gsap.matchMedia();
mm.add({isDesktop:'(min-width:821px)',isMobile:'(max-width:820px)',fine:'(pointer:fine)'},ctx=>{const {isDesktop,fine}=ctx.conditions;
 // hero: one coat
 const hero=d.querySelector('.hero');if(hero){const bp=hero.querySelector('.bpath'),L=bp.getTotalLength();
  const h1=hero.querySelector('h1');h1.querySelectorAll('.ln').forEach(l=>{const em=l.querySelector('em'),tgt=em||l;tgt.innerHTML=[...tgt.textContent].map(c=>'<span class="ch">'+c+'</span>').join('')});
  h1.setAttribute('aria-label','Red Polish.');
  const k=isDesktop?1:.7,tl=gsap.timeline({defaults:{ease:'expo.out'}});
  gsap.set(bp,{strokeDasharray:L,strokeDashoffset:L});
  tl.from(nav,{opacity:0,duration:.3,ease:'power1.out'},0)
   .to(bp,{strokeDashoffset:0,duration:.9*k,ease:'power4.inOut'},.15*k)
   .fromTo(hero.querySelector('.shine'),{x:-300},{x:1900,duration:.7,ease:'power2.inOut'},.95*k)
   .from(h1.querySelectorAll('.ch'),{yPercent:110,duration:.8,stagger:.035},.5*k)
   .from(hero.querySelectorAll('.h-in'),{opacity:0,y:12,duration:.5,stagger:.06},1.0*k)
   .fromTo(hero.querySelector('.js-fill'),{'--fill':'0%',color:'#B5121B'},{'--fill':'100%',color:'#fff',duration:.45,ease:'power3.out'},1.3*k)
   .fromTo('#heroframe',{clipPath:'inset(14% 14% round 40px)'},{clipPath:'inset(0% 0% round 0px)',duration:.7,ease:'power3.out'},.2)
   .add(()=>gloss(d.getElementById('heroframe')),1.1*k);
  if(isDesktop)gsap.to('.stroke',{yPercent:-60,ease:'none',scrollTrigger:{trigger:hero,start:'top top',end:'bottom top',scrub:true}})}
 // ch1 pan
 const pan=d.querySelector('.pan'),track=pan&&pan.querySelector('.pan-track');if(track){
  const dist=()=>track.scrollWidth-innerWidth;
  const tw=gsap.to(track,{x:()=>-dist(),ease:'none',scrollTrigger:{trigger:pan,pin:true,scrub:1,start:'top top',end:()=>'+='+dist(),invalidateOnRefresh:true,anticipatePin:1}});
  track.querySelectorAll('.set').forEach(s=>{gsap.fromTo(s,{scale:.9},{scale:1,ease:'none',scrollTrigger:{trigger:s,containerAnimation:tw,start:'left right',end:'center center',scrub:true}});
   const ph=s.querySelector('.ph');ScrollTrigger.create({trigger:s,containerAnimation:tw,start:'center 60%',onEnter:()=>gloss(ph),onEnterBack:()=>gloss(ph)})})}
 function gloss(el){el&&el.animate([{transform:'translateX(-130%) skewX(-12deg)'},{transform:'translateX(130%) skewX(-12deg)'}],{duration:800,easing:'cubic-bezier(.45,0,.55,1)',pseudoElement:'::after'})}
 // ch2 finishes
 const fin=d.querySelector('.finishes');if(fin){const lays=fin.querySelectorAll('.lay'),words=fin.querySelectorAll('.fin-words span'),copy=fin.querySelectorAll('.fin-copy p'),dots=fin.querySelectorAll('.fin-dots b');
  const tl=gsap.timeline({defaults:{ease:'none'},scrollTrigger:{trigger:fin,pin:true,start:'top top',end:'+=300%',scrub:.5,snap:{snapTo:1/3,duration:.4,ease:'power1.inOut'},onUpdate:s=>{n3&&n3.set(s.progress);dots.forEach((b,i)=>gsap.set(b,{scaleX:i<=Math.round(s.progress*3)?1:0}))}}});
  for(let i=1;i<4;i++){tl.to(lays[i-1],{opacity:0,duration:.3},i-.3).to(lays[i],{opacity:1,duration:.3},i-.3).to(words[i-1],{opacity:0,y:-30,duration:.3},i-.3).fromTo(words[i],{opacity:0,y:30},{opacity:1,y:0,duration:.3},i-.3).to(copy[i-1],{opacity:0,duration:.2},i-.3).to(copy[i],{opacity:1,duration:.2},i-.15)}
  tl.fromTo(fin.querySelectorAll('.pearl'),{y:-260},{y:0,ease:'bounce.out',stagger:.08,duration:.5},1.8);
  tl.fromTo(fin.querySelector('.hl'),{x:-120},{x:420,duration:3},0);
  gsap.to(fin.querySelector('.ce-band'),{y:60,repeat:-1,yoyo:true,duration:1.6,ease:'sine.inOut'});
  let n3=null;const gl=(()=>{try{return !!d.createElement('canvas').getContext('webgl2')}catch(e){return false}})();
  if(isDesktop&&fine&&gl){const io=new IntersectionObserver(e=>{if(e[0].isIntersecting){io.disconnect();import(d.querySelector('script[src*="app.js"]').src.replace('app.js','nail3d.js')).then(m=>{const host=d.getElementById('nail');n3=m.mount(host);host.classList.add('has3d')}).catch(()=>{})}},{rootMargin:'100% 0px'});io.observe(fin)}}
 // salon blinds
 d.querySelectorAll('.blind .bands').forEach(b=>gsap.to(b.children,{scaleY:0,duration:.7,stagger:.06,ease:'power3.inOut',scrollTrigger:{trigger:b,start:'top 80%',toggleActions:'play none none none'}}));
 // book flood
 const bk=d.querySelector('.book:not(.red)');if(bk){gsap.fromTo(bk,{'--flood':0},{'--flood':1,ease:'none',scrollTrigger:{trigger:bk,start:'top bottom',end:'top 60%',scrub:true,onUpdate:s=>bk.classList.toggle('red',s.progress>.55)}})}
 // spring fade-ups
 gsap.utils.toArray('.sec-head,.card,.menu section,.look,.page-hero .wrap>*').forEach(el=>gsap.from(el,{opacity:0,y:24,duration:.6,ease:'back.out(1.2)',scrollTrigger:{trigger:el,start:'top 92%',once:true}}));
});
})();
