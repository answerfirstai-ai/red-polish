(()=>{const d=document,H=d.documentElement,RM=H.classList.contains('rm');
const nav=d.querySelector('.nav'),mbar=d.querySelector('.mbar'),hero=d.querySelector('.hero');
const onS=()=>{const y=scrollY;nav.classList.toggle('scrolled',y>20);mbar&&mbar.classList.add('on')};addEventListener('scroll',onS,{passive:true});onS();
d.querySelectorAll('.mpanel a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
const toast=d.querySelector('.toast');let tt;function say(m){toast.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="#fff" stroke-width="2.5" d="M4 12l5 5L20 6"/></svg>'+m;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>toast.classList.remove('on'),2800)}
d.querySelectorAll('[data-look]').forEach(a=>a.addEventListener('click',()=>{try{navigator.clipboard&&navigator.clipboard.writeText(a.dataset.look).then(()=>say('Look copied. Paste it in your booking note.'),()=>{})}catch(e){}}));

if(false)d.querySelectorAll('.look .ph').forEach(p=>p.addEventListener('pointermove',e=>{const r=p.getBoundingClientRect();p.style.setProperty('--mx',e.clientX-r.left+'px');p.style.setProperty('--my',e.clientY-r.top+'px')}));
const fb=d.querySelectorAll('[data-filter]');if(fb.length)fb.forEach(b=>b.addEventListener('click',()=>{const f=b.dataset.filter;fb.forEach(x=>x.setAttribute('aria-pressed',x===b));const items=d.querySelectorAll('.look');
 const st=window.Flip&&!RM?Flip.getState(items):null;items.forEach(i=>i.classList.toggle('hide',f!=='all'&&i.dataset.f!==f));
 if(st)Flip.from(st,{duration:.5,ease:'power2.inOut',stagger:.02,absolute:true,onEnter:e=>gsap.fromTo(e,{opacity:0,scale:.94},{opacity:1,scale:1,duration:.35}),onLeave:e=>gsap.to(e,{opacity:0,duration:.25})})}));
// light sweep on rail cards as they come into view (native horizontal scroll)
const rail=null;if(rail){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting&&e.intersectionRatio>.6)e.target.classList.add('lit')}),{root:rail,threshold:[.6]});rail.querySelectorAll('.set').forEach(s=>io.observe(s))}
if(RM||!window.gsap)return;
gsap.registerPlugin(ScrollTrigger);window.Flip&&gsap.registerPlugin(Flip);
const st=d.getElementById('stage');
const mm=gsap.matchMedia();
mm.add({desk:'(min-width:821px)',mob:'(max-width:820px)',fine:'(pointer:fine)'},ctx=>{const {desk,fine}=ctx.conditions;
 if(hero){ // camera: slow push-in + light sweep. Text is never hidden.
  const seen=sessionStorage.getItem('rp-intro');const tl=gsap.timeline();
  if(!seen){tl.fromTo('.poster',{scale:1.08},{scale:1,duration:2.4,ease:'power2.out'},0).fromTo('.sweep',{xPercent:-100},{xPercent:100,duration:1.8,ease:'power2.inOut'},.4);
   const skip=()=>{tl.progress(1);['wheel','keydown','pointerdown','touchstart','scroll'].forEach(e=>removeEventListener(e,skip))};['wheel','keydown','pointerdown','touchstart','scroll'].forEach(e=>addEventListener(e,skip,{passive:true,once:true}));sessionStorage.setItem('rp-intro','1')}
  gsap.to('.poster',{scale:1.06,yPercent:4,ease:'none',scrollTrigger:{trigger:hero,start:'top top',end:'bottom top',scrub:true}});
 }
 // rack focus into their real set (scroll-linked, no pin)
 gsap.fromTo('.u-real img',{filter:'blur(12px)',scale:1.1},{filter:'blur(0px)',scale:1,ease:'none',scrollTrigger:{trigger:'.u-real',start:'top 95%',end:'top 35%',scrub:true}});
});
})();
