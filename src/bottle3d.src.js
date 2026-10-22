import {WebGLRenderer,Scene,PerspectiveCamera,Mesh,Group,MeshPhysicalMaterial,CylinderGeometry,SphereGeometry,ConeGeometry,PMREMGenerator,Color,ACESFilmicToneMapping,EquirectangularReflectionMapping,SRGBColorSpace,DirectionalLight,PlaneGeometry,MeshBasicMaterial,AdditiveBlending,CanvasTexture} from 'three';
import {RGBELoader} from 'three/examples/jsm/loaders/RGBELoader.js';
export async function mount(host,hdr,opt={}){
  const r=new WebGLRenderer({antialias:true,alpha:false,preserveDrawingBuffer:true,powerPreference:'low-power'});
  r.setPixelRatio(opt.w?1:Math.min(devicePixelRatio,1.5));r.toneMapping=ACESFilmicToneMapping;r.toneMappingExposure=1.1;r.outputColorSpace=SRGBColorSpace;
  const sc=new Scene();sc.background=new Color('#100205');const cam=new PerspectiveCamera(26,1,.1,60);cam.position.set(0,.6,13);
  const tex=await new RGBELoader().loadAsync(hdr);tex.mapping=EquirectangularReflectionMapping;
  const pm=new PMREMGenerator(r);sc.environment=pm.fromEquirectangular(tex).texture;tex.dispose();
  const red=new Color('#B5121B');
  const glass=new MeshPhysicalMaterial({color:'#ffffff',transmission:1,thickness:.6,ior:1.5,roughness:.02,metalness:0,clearcoat:1,envMapIntensity:1,attenuationColor:new Color('#ffd6da'),attenuationDistance:4,transparent:true});
  const liquid=new MeshPhysicalMaterial({color:'#c0121c',roughness:.08,clearcoat:1,clearcoatRoughness:.02,sheen:.3,sheenColor:new Color('#ff3b45')});
  const chrome=new MeshPhysicalMaterial({color:'#f2f3f5',metalness:1,roughness:.05,envMapIntensity:1.3});
  const lacq=new MeshPhysicalMaterial({color:red,roughness:.15,clearcoat:1,clearcoatRoughness:.03});
  const bead=new MeshPhysicalMaterial({color:'#c4141e',roughness:.02,clearcoat:1,clearcoatRoughness:0,specularIntensity:1,sheen:.4,sheenColor:new Color('#ff6b73')});
  const B=new Group();sc.add(B);
  const body=new Mesh(new CylinderGeometry(1.25,1.1,2.1,10,1),glass);B.add(body);
  const liq=new Mesh(new CylinderGeometry(1.1,.97,1.95,10,1),liquid);liq.position.y=-.02;B.add(liq);
  const shoulder=new Mesh(new CylinderGeometry(.5,1.25,.35,10,1),glass);shoulder.position.y=1.22;B.add(shoulder);
  const neck=new Mesh(new CylinderGeometry(.42,.45,.35,32),glass);neck.position.y=1.55;B.add(neck);
  const cap=new Group();const capM=new Mesh(new CylinderGeometry(.56,.56,1.45,48),chrome);capM.position.y=.72;cap.add(capM);cap.position.y=1.62;B.add(cap);
  const brush=new Group();const stem=new Mesh(new CylinderGeometry(.06,.06,1.6,16),lacq);stem.position.y=-.8;const bris=new Mesh(new ConeGeometry(.13,.75,32),lacq);bris.rotation.x=Math.PI;bris.position.y=-1.95;
  const bd=new Mesh(new SphereGeometry(.17,32,24),bead);bd.position.y=-2.4;brush.add(stem,bris,bd);cap.add(brush);
  // light sweep: soft additive card moving behind the glass
  const cv=document.createElement('canvas');cv.width=64;cv.height=4;const cx=cv.getContext('2d');const gr=cx.createLinearGradient(0,0,64,0);gr.addColorStop(0,'rgba(255,255,255,0)');gr.addColorStop(.5,'rgba(255,240,240,1)');gr.addColorStop(1,'rgba(255,255,255,0)');cx.fillStyle=gr;cx.fillRect(0,0,64,4);
  const sweep=new Mesh(new PlaneGeometry(1.2,7),new MeshBasicMaterial({map:new CanvasTexture(cv),transparent:true,opacity:.16,blending:AdditiveBlending,depthWrite:false}));sweep.position.z=-1.6;sweep.rotation.z=-.25;sc.add(sweep);
  const floor=new Mesh(new PlaneGeometry(60,60),new MeshBasicMaterial({color:'#100205'}));floor.rotation.x=-Math.PI/2;sc.add(floor);
  const gc=document.createElement('canvas');gc.width=gc.height=128;const gx=gc.getContext('2d');const rg=gx.createRadialGradient(64,64,0,64,64,64);rg.addColorStop(0,'rgba(255,30,45,.9)');rg.addColorStop(.4,'rgba(181,18,27,.35)');rg.addColorStop(1,'rgba(0,0,0,0)');gx.fillStyle=rg;gx.fillRect(0,0,128,128);
  const glow=new Mesh(new PlaneGeometry(5,2.6),new MeshBasicMaterial({map:new CanvasTexture(gc),transparent:true,blending:AdditiveBlending,depthWrite:false}));glow.rotation.x=-Math.PI/2;sc.add(glow);
  const shc=document.createElement('canvas');shc.width=shc.height=64;const sx=shc.getContext('2d');const sg=sx.createRadialGradient(32,32,0,32,32,32);sg.addColorStop(0,'rgba(0,0,0,.85)');sg.addColorStop(1,'rgba(0,0,0,0)');sx.fillStyle=sg;sx.fillRect(0,0,64,64);
  const shadow=new Mesh(new PlaneGeometry(3.4,1.6),new MeshBasicMaterial({map:new CanvasTexture(shc),transparent:true,depthWrite:false}));shadow.rotation.x=-Math.PI/2;sc.add(shadow);
  const key=new DirectionalLight('#ffffff',1.2);key.position.set(-3,4,5);sc.add(key);
  let BX=2.4,BY=-.9,CZ=13;function comp(a){if(a>1.1){BX=Math.min(3.2,1.2*a);BY=-.9;CZ=13}else{BX=0;BY=1.3;CZ=25}floor.position.y=BY-1.06;glow.position.set(BX+.9,BY-1.05,.6);shadow.position.set(BX,BY-1.045,0)}
  let prog=0,shown=0,vis=true,raf,mx=0,my=0,tx=0,ty=0;const t0=performance.now();
  function size(){const b=host.getBoundingClientRect();const W=opt.w||b.width,Hh=opt.h||b.height;r.setSize(W,Hh,false);cam.aspect=W/Hh;cam.updateProjectionMatrix();comp(cam.aspect);}
  host.appendChild(r.domElement);size();
  function pose(p,t){ // p: 0 closed .. 1 uncapped with bead
    const a=Math.min(1,p/.4),b=Math.max(0,Math.min(1,(p-.35)/.45));
    cap.rotation.y=-a*Math.PI*3;cap.position.y=1.62+a*.3+b*2.4;brush.visible=p>.4;bd.scale.setScalar(.15+1.1*Math.max(0,(p-.55)/.45));
    B.rotation.y=t*(Math.PI*2/40)+tx;B.rotation.x=ty;B.position.set(BX,BY,0);
    const fy=BY+1.62+.3+.2*b;cam.position.set(BX*b*.6,.6+(BY+.9)*.4+b*(fy-.2),CZ-b*(CZ-7.5));cam.lookAt(BX*b,.3+(BY+.9)*.5+b*(fy-.3),0);
    sweep.position.x=BX+((t%7)/7)*7-3.5;}
  if(opt.still!=null){pose(opt.still,opt.t!=null?opt.t:opt.still*6);r.render(sc,cam);return r.domElement}
  addEventListener('resize',size);
  if(matchMedia('(pointer:fine)').matches)addEventListener('pointermove',e=>{mx=(e.clientX/innerWidth-.5)*.17;my=(e.clientY/innerHeight-.5)*.09},{passive:true});
  new IntersectionObserver(e=>{vis=e[0].isIntersecting;if(vis)loop();}).observe(host);
  function loop(){cancelAnimationFrame(raf);if(!vis)return;shown+=(prog-shown)*.12;tx+=(mx-tx)*.06;ty+=(my-ty)*.06;pose(shown,(performance.now()-t0)/1000);r.render(sc,cam);raf=requestAnimationFrame(loop);}
  loop();return {set(v){prog=v}};
}
