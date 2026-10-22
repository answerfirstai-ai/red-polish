(()=>{const d=document,H=d.documentElement,RM=H.classList.contains('rm');
const nav=d.querySelector('.nav'),mbar=d.querySelector('.mbar'),hero=d.querySelector('.hero');
const onS=()=>{const y=scrollY;nav.classList.toggle('scrolled',y>20);mbar&&mbar.classList.toggle('on',y>(hero?hero.offsetHeight-80:300))};addEventListener('scroll',onS,{passive:true});onS();
d.querySelectorAll('.mpanel a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
const toast=d.querySelector('.toast');let tt;function say(m){toast.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="#fff" stroke-width="2.5" d="M4 12l5 5L20 6"/></svg>'+m;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>toast.classList.remove('on'),2800)}
d.querySelectorAll('[data-look]').forEach(a=>a.addEventListener('click',()=>{try{navigator.clipboard&&navigator.clipboard.writeText(a.dataset.look).then(()=>say('Look copied. Paste it in your booking note.'),()=>{})}catch(e){}}));
d.querySelectorAll('.btn').forEach(b=>b.addEventListener('pointerdown',()=>{b.classList.remove('zip');void b.offsetWidth;b.classList.add('zip')}));
if(matchMedia('(pointer:fine)').matches&&!RM)d.querySelectorAll('.look .ph').forEach(p=>p.addEventListener('pointermove',e=>{const r=p.getBoundingClientRect();p.style.setProperty('--mx',e.clientX-r.left+'px');p.style.setProperty('--my',e.clientY-r.top+'px')}));
const fb=d.querySelectorAll('[data-filter]');if(fb.length)fb.forEach(b=>b.addEventListener('click',()=>{const f=b.dataset.filter;fb.forEach(x=>x.setAttribute('aria-pressed',x===b));const items=d.querySelectorAll('.look');
 const st=window.Flip&&!RM?Flip.getState(items):null;items.forEach(i=>i.classList.toggle('hide',f!=='all'&&i.dataset.f!==f));
 if(st)Flip.from(st,{duration:.5,ease:'power2.inOut',stagger:.02,absolute:true,onEnter:e=>gsap.fromTo(e,{opacity:0,scale:.94},{opacity:1,scale:1,duration:.35}),onLeave:e=>gsap.to(e,{opacity:0,duration:.25})})}));
// light sweep on rail cards as they come into view (native horizontal scroll)
const rail=d.querySelector('.rail');if(rail&&!RM){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting&&e.intersectionRatio>.6)e.target.classList.add('lit')}),{root:rail,threshold:[.6]});rail.querySelectorAll('.set').forEach(s=>io.observe(s))}
if(RM||!window.gsap)return;
gsap.registerPlugin(ScrollTrigger);window.Flip&&gsap.registerPlugin(Flip);
const st=d.getElementById('stage');
const mm=gsap.matchMedia();
mm.add({desk:'(min-width:821px)',mob:'(max-width:820px)',fine:'(pointer:fine)'},ctx=>{const {desk,fine}=ctx.conditions;
 if(hero){ // camera: slow push-in + light sweep. Text is never hidden.
  gsap.fromTo('.poster',{scale:1.1},{scale:1,duration:2.8,ease:'power2.out'});
  gsap.fromTo('.sweep',{xPercent:-100},{xPercent:100,duration:2.2,ease:'power2.inOut',delay:.6,repeat:-1,repeatDelay:7});
  let ctl=null,prog=0;const pt=ScrollTrigger.create({trigger:hero,start:'top top',end:'bottom top',scrub:true,onUpdate:s=>{prog=s.progress;ctl&&ctl(prog)}});
  gsap.to('.hero-inner',{yPercent:-12,ease:'none',scrollTrigger:{trigger:hero,start:'top top',end:'bottom top',scrub:true}});
  const gl=(()=>{try{return !!d.createElement('canvas').getContext('webgl2')}catch(e){return false}})();
  const base=d.querySelector('script[src*="app.js"]').src.replace('js/app.js','');
  const go=()=>{if(desk&&fine&&gl){import(base+'js/bottle3d.js').then(m=>m.mount(st,base+'img/studio-256.hdr')).then(b=>{ctl=v=>b.set(v);b.set(prog);st.classList.add('on');hero.classList.add('live')}).catch(()=>{})}
   else{ // mobile: pre-rendered PBR sequence scrubbed by scroll
    const im=st.querySelector('.seq'),N=24,ext=d.createElement('canvas').toDataURL('image/avif').indexOf('avif')>0?'avif':'webp',fr=[];
    let ok=0;for(let i=0;i<N;i++){const x=new Image();x.decoding='async';x.onload=()=>{if(++ok===N){im.hidden=false;st.classList.add('on');hero.classList.add('live');ctl(prog)}};x.src=base+'seq/b'+String(i).padStart(2,'0')+'.'+ext;fr.push(x.src)}
    let last=-1;ctl=v=>{const k=Math.round(v*(N-1));if(k!==last){last=k;im.src=fr[k]}}}};
  ('requestIdleCallback' in window)?requestIdleCallback(go,{timeout:2500}):setTimeout(go,1200);
 }
 // rack focus into their real set (scroll-linked, no pin)
 gsap.fromTo('.u-real img',{filter:'blur(12px)',scale:1.1},{filter:'blur(0px)',scale:1,ease:'none',scrollTrigger:{trigger:'.u-real',start:'top 95%',end:'top 35%',scrub:true}});
 gsap.fromTo('.u-macro img',{scale:1.15},{scale:1,ease:'none',scrollTrigger:{trigger:'.u-macro',start:'top bottom',end:'bottom top',scrub:true}});
 // layered parallax backgrounds
 [['.mat',14],['.kt',18],['.book-bg',16],['.brushband img',30]].forEach(([s,a])=>d.querySelectorAll(s).forEach(el=>gsap.fromTo(el,{yPercent:-a/2},{yPercent:a/2,ease:'none',scrollTrigger:{trigger:el.parentElement,start:'top bottom',end:'bottom top',scrub:true}})));
 gsap.fromTo('.s-photo img',{scale:1.12},{scale:1,ease:'none',scrollTrigger:{trigger:'.s-photo',start:'top bottom',end:'center 40%',scrub:true}});
 if(desk)gsap.fromTo('.rail',{x:60},{x:0,ease:'none',scrollTrigger:{trigger:'.rail',start:'top bottom',end:'top 40%',scrub:true}});
});
})();
