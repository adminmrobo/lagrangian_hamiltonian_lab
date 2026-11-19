/* 두 장의 지도 — 실험 패널 모음. 원자료 @askwhyvalley·matharium 인포그래픽을 다시 그려 손으로 움직이게 만든 것 */
(function(){
'use strict';
var NS='http://www.w3.org/2000/svg';
var C={teal:'#0f8f84',orange:'#e8731a',navy:'#1e2f6e',blue:'#2458d6',green:'#13733a',red:'#c9302c',gray:'#8a96a3',grid:'#e3e8ee',axis:'#1e2f6e',muted:'#5b6874'};
function el(tag,a,parent){var e=document.createElementNS(NS,tag);for(var k in a){if(a[k]!=null)e.setAttribute(k,a[k]);}if(parent)parent.appendChild(e);return e;}
function txt(parent,x,y,s,a){a=a||{};var t=el('text',Object.assign({x:x,y:y,'font-size':a.size||14,fill:a.fill||C.navy,'font-family':a.font||'"Cambria Math","Times New Roman",serif','font-style':a.italic===false?'normal':'italic','text-anchor':a.anchor||'start','font-weight':a.weight||'normal'},{}),parent);t.textContent=s;return t;}
function ktxt(parent,x,y,s,a){a=a||{};a.font='"IBM Plex Sans KR","Malgun Gothic","Noto Sans KR",sans-serif';a.italic=false;return txt(parent,x,y,s,a);}
function r2(v){return Math.round(v*100)/100;}
function r1(v){return Math.round(v*10)/10;}
function fmt(v,d){d=d==null?2:d;var s=(Math.round(v*Math.pow(10,d))/Math.pow(10,d)).toFixed(d);s=s.replace(/\.?0+$/,'');if(s==='-0')s='0';return s;}
function num(v){return v<0?'−'+fmt(-v):fmt(v);}
function svgOf(host,W,H){host.innerHTML='';var s=el('svg',{viewBox:'0 0 '+W+' '+H,role:'img'},host);var d=el('defs',{},s);
  ['teal','orange','navy','blue','green','red','gray'].forEach(function(c){var m=el('marker',{id:'ah-'+c+'-'+host.id,viewBox:'0 0 10 10',refX:8.5,refY:5,markerWidth:7,markerHeight:7,orient:'auto-start-reverse'},d);el('path',{d:'M0,0 L10,5 L0,10 z',fill:C[c]},m);});
  s._id=host.id;return s;}
function arrow(s,x1,y1,x2,y2,c,w){return el('line',{x1:x1,y1:y1,x2:x2,y2:y2,stroke:C[c],'stroke-width':w||3,'marker-end':'url(#ah-'+c+'-'+s._id+')'},s);}
function dash(s,x1,y1,x2,y2,c){return el('line',{x1:x1,y1:y1,x2:x2,y2:y2,stroke:C[c]||c,'stroke-width':1.6,'stroke-dasharray':'5 4'},s);}
/* 좌표평면 */
function plane(s,o){var W=o.W,H=o.H,p=o.pad||36;var sx=(W-2*p)/(o.x1-o.x0),sy=(H-2*p)/(o.y1-o.y0);
  if(o.equal){var k=Math.min(sx,sy);sx=sy=k;}
  var ox=p-o.x0*sx,oy=H-p+o.y0*sy;s._sx=sx;
  var P={X:function(x){return ox+x*sx;},Y:function(y){return oy-y*sy;},inv:function(px,py){return[(px-ox)/sx,(oy-py)/sy];},sx:sx,sy:sy};
  var g=el('g',{},s);var st=o.step||1;
  if(o.grid!==false){for(var x=Math.ceil(o.x0/st)*st;x<=o.x1+1e-9;x+=st)el('line',{x1:P.X(x),y1:P.Y(o.y0),x2:P.X(x),y2:P.Y(o.y1),stroke:C.grid},g);
  for(var y=Math.ceil(o.y0/st)*st;y<=o.y1+1e-9;y+=st)el('line',{x1:P.X(o.x0),y1:P.Y(y),x2:P.X(o.x1),y2:P.Y(y),stroke:C.grid},g);}
  var ax0=Math.max(o.x0,Math.min(0,o.x1)),ay0=Math.max(o.y0,Math.min(0,o.y1));
  if(o.ax!==undefined)ax0=o.ax;if(o.ay!==undefined)ay0=o.ay;
  el('line',{x1:P.X(o.x0),y1:P.Y(ay0),x2:P.X(o.x1)+14,y2:P.Y(ay0),stroke:C.axis,'stroke-width':2,'marker-end':'url(#ah-navy-'+s._id+')'},g);
  el('line',{x1:P.X(ax0),y1:P.Y(o.y0),x2:P.X(ax0),y2:P.Y(o.y1)-14,stroke:C.axis,'stroke-width':2,'marker-end':'url(#ah-navy-'+s._id+')'},g);
  if(/[^\x00-\x7f]/.test((o.xl||'')+(o.yl||''))){ktxt(g,P.X(o.x1)+14,P.Y(ay0)-12,o.xl,{size:13,anchor:'end'});ktxt(g,P.X(ax0)+12,P.Y(o.y1)-2,o.yl,{size:13});}else{txt(g,P.X(o.x1)+10,P.Y(ay0)+20,o.xl||'x',{size:16});txt(g,P.X(ax0)-22,P.Y(o.y1)-8,o.yl||'y',{size:16});}
  var ls=o.label||st;
  if(o.ticks!==false){for(var a=Math.ceil(o.x0/ls)*ls;a<=o.x1+1e-9;a+=ls){if(Math.abs(a-ax0)<1e-9&&!o.zeroX)continue;txt(g,P.X(a),P.Y(ay0)+18,fmt(a),{size:12.5,anchor:'middle',italic:false,fill:C.muted});}
  for(var b=Math.ceil(o.y0/ls)*ls;b<=o.y1+1e-9;b+=ls){if(Math.abs(b-ay0)<1e-9)continue;txt(g,P.X(ax0)-8,P.Y(b)+4,fmt(b),{size:12.5,anchor:'end',italic:false,fill:C.muted});}
  if(o.x0<=0&&o.y0<=0)txt(g,P.X(0)-14,P.Y(0)+18,'0',{size:12.5,italic:false,fill:C.muted});}
  return P;}
/* 끌기 */
function drag(s,node,onMove){var on=false;var host=s.parentNode;var idx=s.querySelectorAll('g.drag').length;
  node.setAttribute('tabindex','0');node.setAttribute('role','slider');node.setAttribute('aria-label','끌어서 옮기는 점 (화살표 키로도 움직입니다)');
  node.addEventListener('keydown',function(e){var k={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]}[e.key];if(!k)return;e.preventDefault();
    var c=node.querySelector('circle');var st=(s._sx||24)*(+(host.dataset.ksnap||1));host.dataset.kf=idx;onMove(+c.getAttribute('cx')+k[0]*st,+c.getAttribute('cy')+k[1]*st);});
  function pt(e){var m=s.getScreenCTM().inverse();var q=s.createSVGPoint();q.x=e.clientX;q.y=e.clientY;q=q.matrixTransform(m);return q;}
  node.classList.add('drag');
  node.addEventListener('pointerdown',function(e){on=true;node.setPointerCapture(e.pointerId);e.preventDefault();});
  node.addEventListener('pointermove',function(e){if(!on)return;var q=pt(e);onMove(q.x,q.y);});
  node.addEventListener('pointerup',function(){on=false;});node.addEventListener('pointercancel',function(){on=false;});
  if(host.dataset.kf!=null&&+host.dataset.kf===idx)node.focus({preventScroll:true});}
function handle(s,x,y,c,label){var g=el('g',{},s);el('circle',{cx:x,cy:y,r:16,fill:C[c],'fill-opacity':.14},g);el('circle',{cx:x,cy:y,r:8,fill:C[c],stroke:'#fff','stroke-width':2},g);return g;}
function dot(s,x,y,c,r){return el('circle',{cx:x,cy:y,r:r||6,fill:C[c]||c,stroke:'#fff','stroke-width':1.5},s);}
function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function snap(v,st){return Math.round(v/st)*st;}
function readout(host){var d=host.parentNode.querySelector('.readout');return d;}
function rightMark(s,x,y,ux,uy,vx,vy,k){k=k||10;el('path',{d:'M'+(x+ux*k)+','+(y+uy*k)+' L'+(x+ux*k+vx*k)+','+(y+uy*k+vy*k)+' L'+(x+vx*k)+','+(y+vy*k),fill:'none',stroke:C.orange,'stroke-width':1.5},s);}

var P={};


/* ===== 공통 도우미 (이 특집용) ===== */
function box(s,b,o){/* b={L,T,W,H}, o={x0,x1,y0,y1,xl,yl,xt,yt} */
  var X=function(x){return b.L+(x-o.x0)/(o.x1-o.x0)*b.W;},Y=function(y){return b.T+b.H-(y-o.y0)/(o.y1-o.y0)*b.H;};
  var g=el('g',{},s);
  (o.xt||[]).forEach(function(t){el('line',{x1:X(t),y1:b.T,x2:X(t),y2:b.T+b.H,stroke:C.grid},g);txt(g,X(t),b.T+b.H+17,fmt(t),{size:12,anchor:'middle',italic:false,fill:C.muted});});
  (o.yt||[]).forEach(function(t){el('line',{x1:b.L,y1:Y(t),x2:b.L+b.W,y2:Y(t),stroke:C.grid},g);txt(g,b.L-6,Y(t)+4,num(t),{size:12,anchor:'end',italic:false,fill:C.muted});});
  var ay=(o.y0<=0&&o.y1>=0)?Y(0):b.T+b.H;
  el('line',{x1:b.L,y1:ay,x2:b.L+b.W,y2:ay,stroke:C.axis,'stroke-width':1.6},g);
  el('line',{x1:b.L,y1:b.T,x2:b.L,y2:b.T+b.H,stroke:C.axis,'stroke-width':1.6},g);
  if(o.xl)ktxt(g,b.L+b.W,ay-8,o.xl,{size:13,anchor:'end',fill:C.navy});
  if(o.yl)ktxt(g,b.L+6,b.T+12,o.yl,{size:13,fill:C.navy});
  return {X:X,Y:Y};}
function curve(s,m,f,a,b,col,w,da,ylim){var d='',pen=false;for(var i=0;i<=240;i++){var x=a+(b-a)*i/240,y=f(x);
    if(!isFinite(y)||(ylim&&(y<ylim[0]||y>ylim[1]))){pen=false;continue;}d+=(pen?' L':' M')+m.X(x).toFixed(1)+','+m.Y(y).toFixed(1);pen=true;}
  return el('path',{d:d,fill:'none',stroke:C[col]||col,'stroke-width':w||2.5,'stroke-dasharray':da||null},s);}
function poly(s,m,pts,col,w,da){return el('polyline',{points:pts.map(function(q){return m.X(q[0]).toFixed(1)+','+m.Y(q[1]).toFixed(1);}).join(' '),fill:'none',stroke:C[col]||col,'stroke-width':w||2,'stroke-dasharray':da||null,'stroke-linejoin':'round'},s);}
function toggles(h,cb){var host=h.parentNode;var bs=host.querySelectorAll('.ctrl button[data-v]');bs.forEach(function(b){b.setAttribute('aria-pressed',b.classList.contains('on')?'true':'false');b.addEventListener('click',function(){bs.forEach(function(x){x.classList.toggle('on',x===b);x.setAttribute('aria-pressed',x===b?'true':'false');});cb(b.getAttribute('data-v'));});});
  var on=host.querySelector('.ctrl button.on');return on?on.getAttribute('data-v'):null;}
function inputs(h){return h.parentNode.querySelectorAll('.ctrl input');}
function bar(s,x,y0,w,hgt,col,label,val){var y=hgt>=0?y0-hgt:y0;el('rect',{x:x,y:y,width:w,height:Math.abs(hgt)||0.5,fill:C[col]||col,rx:4},s);
  ktxt(s,x+w/2,hgt>=0?y0+20:y0-8,label,{size:13,anchor:'middle'});if(val!=null)txt(s,x+w/2,(hgt>=0?y0-hgt-6:y0-hgt+16),val,{size:13,anchor:'middle',italic:false,weight:'bold',fill:C[col]||col});}

/* ===== 0편 ===== */
P.o1=function(h){var W=560,H=360,inp=inputs(h)[0],out=readout(h);
  function draw(){var x=+inp.value,s=svgOf(h,W,H),m=box(s,{L:50,T:20,W:480,H:300},{x0:-2.2,x1:2.2,y0:-0.5,y1:4.8,xt:[-2,-1,0,1,2],yt:[0,1,2,3,4],xl:'위치 w',yl:'오차'});
    curve(s,m,function(t){return t*t;},-2.2,2.2,'teal',3);var k=2*x;
    curve(s,m,function(t){return x*x+k*(t-x);},x-0.9,x+0.9,'orange',2,'6 4');
    dot(s,m.X(x),m.Y(x*x),'red',7);
    if(x!==0){var dir=k>0?-1:1;arrow(s,m.X(x),m.Y(0)+0,m.X(x+dir*0.6),m.Y(0),'navy',3);ktxt(s,m.X(x+dir*0.3),m.Y(0)+34,'내려가는 쪽',{size:12,anchor:'middle',fill:C.navy});}
    out.innerHTML='위치 '+num(x)+' · 오차 '+fmt(x*x)+' · 기울기 2×'+num(x)+' = <b>'+num(k)+'</b> → '+(k===0?'바닥입니다. 더 내려갈 곳이 없습니다.':(k>0?'오른쪽이 오르막이라 왼쪽으로 내려갑니다.':'왼쪽이 오르막이라 오른쪽으로 내려갑니다.'));}
  inp.addEventListener('input',draw);draw();};
P.o2=function(h){h.dataset.ksnap='0.5';var W=480,H=440,pt=[1.5,1],out=readout(h);
  function draw(){var s=svgOf(h,W,H),p=plane(s,{W:W,H:H,x0:-3,x1:3,y0:-3,y1:3,equal:true,label:1});
    [1,2,3].forEach(function(r){el('circle',{cx:p.X(0),cy:p.Y(0),r:r*p.sx,fill:'none',stroke:'#f2b88a','stroke-width':2},s);});
    var r=Math.hypot(pt[0],pt[1]);if(r>0.01){el('circle',{cx:p.X(0),cy:p.Y(0),r:r*p.sx,fill:'none',stroke:C.orange,'stroke-width':2.5,'stroke-dasharray':'6 4'},s);
      var g=[2*pt[0],2*pt[1]],sc=0.35;arrow(s,p.X(pt[0]),p.Y(pt[1]),p.X(pt[0]+g[0]*sc),p.Y(pt[1]+g[1]*sc),'green',3.5);
      var u=[g[0]/Math.hypot(g[0],g[1]),g[1]/Math.hypot(g[0],g[1])];rightMark(s,p.X(pt[0]),p.Y(pt[1]),u[0],-u[1],-u[1],-u[0],11);}
    var hd=handle(s,p.X(pt[0]),p.Y(pt[1]),'red');
    drag(s,hd,function(x,y){var q=p.inv(x,y);var n=[clamp(snap(q[0],.25),-2.75,2.75),clamp(snap(q[1],.25),-2.75,2.75)];if(n[0]!==pt[0]||n[1]!==pt[1]){pt=n;draw();}});
    out.innerHTML='자리 ('+num(pt[0])+', '+num(pt[1])+') · 높이 x² + y² = '+fmt(pt[0]*pt[0]+pt[1]*pt[1])+' · 오르막 화살표 (2x, 2y) = <b>('+num(2*pt[0])+', '+num(2*pt[1])+')</b> → 주황 점선(등고선)과 늘 <b>직각</b>입니다.';}
  draw();};
P.o3=function(h){var W=560,H=340,inp=inputs(h)[0],out=readout(h);
  function draw(){var a=+inp.value,s=svgOf(h,W,H),m=box(s,{L:50,T:20,W:480,H:280},{x0:-2,x1:2,y0:-0.2,y1:4.2,xt:[-2,-1,0,1,2],yt:[0,1,2,3,4],xl:'x',yl:'y'});
    curve(s,m,function(x){return x*x;},-2,2,'#8a96a3',2,'6 4',[-1,4.2]);curve(s,m,function(x){return a*x*x;},-2,2,'orange',3,null,[-1,4.2]);
    out.innerHTML='y = '+fmt(a)+'·x² · 굽음(두 번 미분) = 2 × '+fmt(a)+' = <b>'+fmt(2*a)+'</b> → '+(a>1?'회색 그릇(y = x²)보다 뾰족합니다.':(a<1?'회색 그릇보다 넓적합니다.':'회색 그릇과 같습니다.'));}
  inp.addEventListener('input',draw);draw();};

/* ===== 1번 방: 두 에너지 ===== */
P.p01=function(h){var W=560,H=330,ins=inputs(h),out=readout(h);
  function draw(){var v=+ins[0].value,hh=+ins[1].value,T=0.5*v*v,V=9.8*hh,s=svgOf(h,W,H),y0=205,k=5;
    el('line',{x1:30,y1:y0,x2:W-20,y2:y0,stroke:C.axis,'stroke-width':1.6},s);
    bar(s,60,y0,80,T*k,'teal','움직임 T',fmt(T,2));bar(s,180,y0,80,V*k,'navy','높이 V',fmt(V,2));
    bar(s,320,y0,80,(T-V)*k,'blue','T − V',num(T-V));bar(s,440,y0,80,(T+V)*k,'orange','T + V',fmt(T+V,2));
    el('line',{x1:290,y1:20,x2:290,y2:H-10,stroke:C.grid,'stroke-width':2,'stroke-dasharray':'5 5'},s);
    ktxt(s,360,24,'라그랑지안',{size:12.5,anchor:'middle',fill:C.blue});ktxt(s,480,24,'해밀토니안',{size:12.5,anchor:'middle',fill:C.orange});
    out.innerHTML='속도 '+fmt(v)+'m/s → T = ½ × 1 × '+fmt(v)+'² = <b>'+fmt(T)+'J</b> · 높이 '+fmt(hh)+'m → V = 9.8 × '+fmt(hh)+' = <b>'+fmt(V)+'J</b> · 빼면 '+num(T-V)+', 더하면 '+fmt(T+V);}
  ins.forEach(function(i){i.addEventListener('input',draw);});draw();};

/* ===== 2번 방: 작용 ===== */
P.p02=function(h){var W=640,H=320,inp=inputs(h)[0],out=readout(h);
  function S(a){return 0.5*(1+a*a/3);}
  function draw(){var a=+inp.value,s=svgOf(h,W,H);
    var m1=box(s,{L:46,T:24,W:250,H:250},{x0:0,x1:1,y0:-0.4,y1:1.5,xt:[0,0.5,1],yt:[0,0.5,1],xl:'시간',yl:'위치'});
    curve(s,m1,function(t){return t;},0,1,'#8a96a3',2,'6 4');curve(s,m1,function(t){return t+a*t*(1-t);},0,1,'teal',3.5);
    dot(s,m1.X(0),m1.Y(0),'navy',6);dot(s,m1.X(1),m1.Y(1),'navy',6);ktxt(s,m1.X(0)+8,m1.Y(0)+18,'출발',{size:12});ktxt(s,m1.X(1)-4,m1.Y(1)-10,'도착',{size:12,anchor:'end'});
    var m2=box(s,{L:376,T:24,W:240,H:250},{x0:-1.5,x1:1.5,y0:0.4,y1:0.95,xt:[-1.5,-1,-0.5,0,0.5,1,1.5],yt:[0.5,0.6,0.7,0.8,0.9],xl:'휜 정도 a',yl:'점수(작용)'});
    curve(s,m2,S,-1.5,1.5,'navy',2.5);dot(s,m2.X(a),m2.Y(S(a)),'red',7);dot(s,m2.X(0),m2.Y(0.5),'green',5);
    out.innerHTML='휜 정도 a = '+num(a)+' → 점수 ½(1 + a²/3) = <b>'+fmt(S(a),3)+'</b>'+(a===0?' — 가장 낮은 점수, 곧은 길입니다.':' · 곧은 길(0.5)보다 '+fmt(S(a)-0.5,3)+' 큽니다.');}
  inp.addEventListener('input',draw);draw();};

/* ===== 3번 방: 공 던지기 ===== */
P.p03=function(h){var W=640,H=320,inp=inputs(h)[0],out=readout(h),g=9.8;
  function S(A){return (A*A-g*A)/6;}
  function draw(){var A=+inp.value,s=svgOf(h,W,H);
    var m1=box(s,{L:46,T:24,W:250,H:250},{x0:0,x1:1,y0:0,y1:2.6,xt:[0,0.5,1],yt:[0,1,2],xl:'시간(초)',yl:'높이(m)'});
    curve(s,m1,function(t){return 4.9*t*(1-t);},0,1,'#8a96a3',2,'6 4');curve(s,m1,function(t){return A*t*(1-t);},0,1,'teal',3.5);
    dot(s,m1.X(0.5),m1.Y(A/4),'red',6);
    var m2=box(s,{L:376,T:24,W:240,H:250},{x0:0,x1:10,y0:-4.5,y1:0.8,xt:[0,2,4,6,8,10],yt:[-4,-2,0],xl:'던지는 세기 A',yl:'점수'});
    curve(s,m2,S,0,10,'navy',2.5);dot(s,m2.X(A),m2.Y(S(A)),'red',7);dot(s,m2.X(4.9),m2.Y(S(4.9)),'green',5);
    out.innerHTML='A = '+fmt(A)+' → 가장 높은 곳 '+fmt(A/4)+'m · 가속도 −2A = <b>'+num(-2*A)+'</b> · 점수 <b>'+num(S(A))+'</b>'+(Math.abs(A-4.9)<0.05?' ← 점수가 가장 낮은 길. 가속도가 중력 −9.8과 같습니다!':' (가장 낮은 점수는 A = 4.9에서 −4.0)');}
  inp.addEventListener('input',draw);draw();};

/* ===== 4번 방: 라그랑주 승수 ===== */
P.p04=function(h){var W=500,H=440,inp=inputs(h)[0],out=readout(h);
  function draw(){var th=+inp.value*Math.PI/180,x=Math.cos(th),y=Math.sin(th),f=x+y,s=svgOf(h,W,H);
    var p=plane(s,{W:W,H:H,x0:-1.7,x1:1.7,y0:-1.7,y1:1.7,equal:true,step:.5,label:1});
    el('circle',{cx:p.X(0),cy:p.Y(0),r:p.sx,fill:'none',stroke:C.red,'stroke-width':3},s);
    dash(s,p.X(f+1.7),p.Y(-1.7),p.X(f-1.7),p.Y(1.7),'#8a96a3');
    arrow(s,p.X(x),p.Y(y),p.X(x+0.5),p.Y(y+0.5),'green',3.5);txt(s,p.X(x+0.5)+4,p.Y(y+0.5)-4,'∇f',{fill:C.green});
    arrow(s,p.X(x),p.Y(y),p.X(x+0.5*x),p.Y(y+0.5*y),'red',3);txt(s,p.X(x+0.5*x)+4,p.Y(y+0.5*y)+14,'∇g',{fill:C.red});
    dot(s,p.X(x),p.Y(y),'navy',7);
    var ang=Math.abs(Math.atan2(y,x)-Math.PI/4)*180/Math.PI;if(ang>180)ang=360-ang;
    var par=ang<2.6;
    out.innerHTML='자리 ('+fmt(x)+', '+fmt(y)+') · x + y = <b>'+fmt(f,3)+'</b> · 두 화살표 사이 각도 '+fmt(ang,0)+'°'+(par?' → <span class="alert">한 줄로 섰습니다! 최댓값 √2 ≈ 1.414, λ = 1/(2x) ≈ '+fmt(1/(2*x),3)+'</span>':' → 아직 나란하지 않아 더 갈 수 있습니다.');}
  inp.addEventListener('input',draw);draw();};

/* ===== 5번 방: 지도 바꿔 그리기 ===== */
P.p05=function(h){var W=640,H=320,inp=inputs(h)[0],out=readout(h),v=2;
  function draw(){var m=+inp.value,p=m*v,s=svgOf(h,W,H);
    var m1=box(s,{L:46,T:28,W:240,H:240},{x0:-1,x1:1,y0:0,y1:7,xt:[-1,0,1],yt:[0,2,4,6],xl:'위치',yl:'속도'});
    dot(s,m1.X(0),m1.Y(v),'teal',9);ktxt(s,m1.X(0)+14,m1.Y(v)+5,'속도 2',{size:13,fill:C.teal});ktxt(s,166,20,'①편 지도 (위치·속도)',{size:13,anchor:'middle',fill:C.teal});
    var m2=box(s,{L:376,T:28,W:240,H:240},{x0:-1,x1:1,y0:0,y1:7,xt:[-1,0,1],yt:[0,2,4,6],xl:'위치',yl:'운동량'});
    dot(s,m2.X(0),m2.Y(p),'orange',9);ktxt(s,m2.X(0)+14,m2.Y(p)+5,'운동량 '+fmt(p),{size:13,fill:C.orange});ktxt(s,496,20,'②편 지도 (위치·운동량)',{size:13,anchor:'middle',fill:C.orange});
    arrow(s,300,150,360,150,'navy',2.5);ktxt(s,330,140,'바꿔 그리기',{size:11.5,anchor:'middle'});
    out.innerHTML='무게 '+fmt(m)+'kg, 속도 2m/s → 운동량 p = '+fmt(m)+' × 2 = <b>'+fmt(p)+'</b> · 움직임 에너지 p²/(2m) = '+fmt(p*p)+'/'+fmt(2*m)+' = <b>'+fmt(p*p/(2*m))+'J</b>';}
  inp.addEventListener('input',draw);draw();};

/* ===== 6번 방: 위상 공간의 그릇 ===== */
P.p06=function(h){h.dataset.ksnap='0.25';var W=480,H=440,pt=[1,0],out=readout(h);
  function draw(){var s=svgOf(h,W,H),p=plane(s,{W:W,H:H,x0:-2.6,x1:2.6,y0:-2.6,y1:2.6,equal:true,step:.5,label:1,xl:'위치 q',yl:'운동량 p'});
    [0.5,1,1.5,2,2.5].forEach(function(r){el('circle',{cx:p.X(0),cy:p.Y(0),r:r*p.sx,fill:'none',stroke:'#f2b88a','stroke-width':1.6},s);});
    var r=Math.hypot(pt[0],pt[1]);el('circle',{cx:p.X(0),cy:p.Y(0),r:r*p.sx,fill:'none',stroke:C.teal,'stroke-width':4},s);
    var hd=handle(s,p.X(pt[0]),p.Y(pt[1]),'red');
    drag(s,hd,function(x,y){var q=p.inv(x,y);var n=[clamp(snap(q[0],.25),-2.5,2.5),clamp(snap(q[1],.25),-2.5,2.5)];if(n[0]!==pt[0]||n[1]!==pt[1]){pt=n;draw();}});
    var H_=0.5*(pt[0]*pt[0]+pt[1]*pt[1]);
    out.innerHTML='출발 위치 '+num(pt[0])+', 운동량 '+num(pt[1])+' → H = ½·'+num(pt[1])+'² + ½·'+num(pt[0])+'² = <b>'+fmt(H_,3)+'</b> · 초록 원(반지름 '+fmt(r,2)+')을 따라 돕니다.';}
  draw();};

/* ===== 7번 방: 도는 화살표 ===== */
P.p07=function(h){var W=480,H=440,inp=inputs(h)[0],out=readout(h),host=h.parentNode,showG=true;
  var tb=host.querySelector('[data-toggle=grad]');tb.setAttribute('aria-pressed','true');tb.addEventListener('click',function(){showG=!showG;tb.classList.toggle('on',showG);tb.setAttribute('aria-pressed',showG?'true':'false');draw();});
  function draw(){var t=+inp.value,q=Math.cos(t),pp=-Math.sin(t),s=svgOf(h,W,H),p=plane(s,{W:W,H:H,x0:-1.7,x1:1.7,y0:-1.7,y1:1.7,equal:true,step:.5,label:1,xl:'위치 q',yl:'운동량 p'});
    for(var i=-3;i<=3;i++)for(var j=-3;j<=3;j++){var a=i*0.5,b=j*0.5;if(!a&&!b)continue;var L=0.18;el('line',{x1:p.X(a),y1:p.Y(b),x2:p.X(a+b*L),y2:p.Y(b-a*L),stroke:'#f2b88a','stroke-width':2},s);el('circle',{cx:p.X(a+b*L),cy:p.Y(b-a*L),r:2,fill:'#f2b88a'},s);}
    el('circle',{cx:p.X(0),cy:p.Y(0),r:p.sx,fill:'none',stroke:C.teal,'stroke-width':2.5,'stroke-dasharray':'6 4'},s);
    if(showG)arrow(s,p.X(q),p.Y(pp),p.X(q+0.55*q),p.Y(pp+0.55*pp),'gray',3.5);
    arrow(s,p.X(q),p.Y(pp),p.X(q+0.55*pp),p.Y(pp-0.55*q),'orange',4);
    if(showG)rightMark(s,p.X(q),p.Y(pp),q,-pp,pp,q,12);
    dot(s,p.X(q),p.Y(pp),'red',7);
    var dotp=q*pp+pp*(-q);
    out.innerHTML='시간 '+fmt(t)+' · 자리 ('+num(q)+', '+num(pp)+') · 오르막 ('+num(q)+', '+num(pp)+') · 가는 쪽 ('+num(pp)+', '+num(-q)+') · 겹침 점수 <b>'+fmt(Math.abs(dotp)<1e-9?0:dotp)+'</b> → 직각 · 에너지 '+fmt(0.5*(q*q+pp*pp))+' 그대로';}
  inp.addEventListener('input',draw);draw();};

/* ===== 8번 방: 테일러 (진자 + 원자료 ② e^x·sin x) ===== */
function fact(n){var f=1;for(var i=2;i<=n;i++)f*=i;return f;}
function taylorExp(x,d){var s=0;for(var n=0;n<=d;n++)s+=Math.pow(x,n)/fact(n);return s;}
function taylorSin(x,d){var s=0;for(var n=0;2*n+1<=d;n++)s+=Math.pow(-1,n)*Math.pow(x,2*n+1)/fact(2*n+1);return s;}
P.p08=function(h){var W=560,H=360,inp=inputs(h)[0],out=readout(h),mode;
  function draw(){var q=+inp.value,s=svgOf(h,W,H);
    if(mode==='pend'){var m=box(s,{L:50,T:20,W:480,H:300},{x0:0,x1:2.5,y0:0,y1:2.2,xt:[0,0.5,1,1.5,2,2.5],yt:[0,0.5,1,1.5,2],xl:'흔들림 q',yl:'높이 에너지'});
      curve(s,m,function(x){return 1-Math.cos(x);},0,2.5,'orange',3.5);curve(s,m,function(x){return x*x/2;},0,2.5,'teal',2.5,'7 5',[0,2.2]);
      dash(s,m.X(q),m.Y(0),m.X(q),m.Y(Math.min(2.2,q*q/2)),'#8a96a3');dot(s,m.X(q),m.Y(1-Math.cos(q)),'orange',6);if(q*q/2<=2.2)dot(s,m.X(q),m.Y(q*q/2),'teal',6);
      ktxt(s,m.X(2.45),m.Y(1-Math.cos(2.45))+18,'진자 1 − cos q',{size:12.5,anchor:'end',fill:C.orange});ktxt(s,m.X(2.0),m.Y(2.0)-8,'그릇 q²/2',{size:12.5,anchor:'end',fill:C.teal});
      var ex=1-Math.cos(q),ap=q*q/2,er=ex>0?(ap-ex)/ex*100:0;
      out.innerHTML='q = '+fmt(q)+' · 실제 '+fmt(ex,4)+' · 그릇 근사 '+fmt(ap,4)+' · 차이 <b>'+fmt(er,1)+'%</b>'+(er<3?' → 바닥 근처라 거의 같습니다.':' → 바닥에서 멀어 차이가 커집니다.');return;}
    var isE=mode==='exp',F=isE?Math.exp:Math.sin,T=isE?taylorExp:taylorSin,DS=isE?[1,2,3]:[1,3,5],cols=['blue','green','orange'];
    var LB=isE?['1차 1 + x','2차 1 + x + x²/2','3차 1 + x + x²/2 + x³/6']:['1차 x','3차 x − x³/6','5차 x − x³/6 + x⁵/120'];
    var o=isE?{x0:-2.2,x1:2.6,y0:-0.5,y1:8,xt:[-2,-1,0,1,2],yt:[0,2,4,6,8]}:{x0:-3,x1:3,y0:-2,y1:2,xt:[-3,-2,-1,0,1,2,3],yt:[-2,-1,0,1,2]};
    o.xl='x';o.yl=isE?'e^x':'sin x';var m=box(s,{L:50,T:20,W:480,H:300},o);
    DS.forEach(function(d,i){curve(s,m,function(x){return T(x,d);},o.x0,o.x1,cols[i],2.2,'7 5',[o.y0,o.y1]);});
    curve(s,m,F,o.x0,o.x1,'red',3.5,null,[o.y0,o.y1]);
    LB.forEach(function(t,i){ktxt(s,86,52+i*18,t,{size:12.5,fill:C[cols[i]]});});ktxt(s,86,52+3*18,isE?'실제 e^x':'실제 sin x',{size:12.5,fill:C.red});
    var xv=q;dash(s,m.X(xv),m.Y(Math.max(o.y0,0)),m.X(xv),m.Y(Math.min(o.y1,F(xv))),'#8a96a3');dot(s,m.X(xv),m.Y(F(xv)),'red',6);
    out.innerHTML='x = '+fmt(xv)+' · 실제 <b>'+fmt(F(xv),3)+'</b> · '+DS.map(function(d,i){return d+'차 '+fmt(T(xv,d),3);}).join(' · ')+' → 차수를 올릴수록 실제에 가까워집니다. (원자료 꼬리표의 오타를 바로잡은 식)';}
  mode=toggles(h,function(v){mode=v;draw();});inp.addEventListener('input',draw);draw();};

/* ===== 8-1번 방: 두 지도 나란히 ===== */
P.p081=function(h){var W=660,H=340,inp=inputs(h)[0],out=readout(h);
  function draw(){var t=+inp.value,q=Math.cos(t),v=-Math.sin(t),s=svgOf(h,W,H);
    var o={x0:-1.6,x1:1.6,y0:-1.6,y1:1.6,xt:[-1,0,1],yt:[-1,0,1]};
    var m1=box(s,{L:40,T:30,W:270,H:270},Object.assign({xl:'위치',yl:'속도'},o));
    [-0.6,-0.3,0.3,0.6].forEach(function(c){[1,-1].forEach(function(sg){curve(s,m1,function(x){var r=x*x+2*c;return r>=0?sg*Math.sqrt(r):NaN;},-1.6,1.6,c>0?'#9fd3cf':'#f2b88a',2,null,[-1.6,1.6]);});});
    curve(s,m1,function(x){return x;},-1.6,1.6,'#c9d2dc',1.5,'4 4');curve(s,m1,function(x){return -x;},-1.6,1.6,'#c9d2dc',1.5,'4 4');
    el('circle',{cx:m1.X(0),cy:m1.Y(0),r:m1.X(1)-m1.X(0),fill:'none',stroke:'#f2c14e','stroke-width':3},s);
    dot(s,m1.X(q),m1.Y(v),'red',7);ktxt(s,175,22,'라그랑지안 지도 — L 등고선(안장)',{size:12.5,anchor:'middle',fill:C.teal});
    var m2=box(s,{L:370,T:30,W:270,H:270},Object.assign({xl:'위치',yl:'운동량'},o));
    [0.5,1,1.5].forEach(function(r){el('circle',{cx:m2.X(0),cy:m2.Y(0),r:(m2.X(r)-m2.X(0)),fill:'none',stroke:'#f2b88a','stroke-width':2},s);});
    el('circle',{cx:m2.X(0),cy:m2.Y(0),r:m2.X(1)-m2.X(0),fill:'none',stroke:C.teal,'stroke-width':3.5},s);
    dot(s,m2.X(q),m2.Y(v),'red',7);ktxt(s,505,22,'해밀토니안 지도 — H 등고선(그릇)',{size:12.5,anchor:'middle',fill:C.orange});
    var L=0.5*v*v-0.5*q*q,Hh=0.5*v*v+0.5*q*q;
    out.innerHTML='시간 '+fmt(t)+' · 위치 <b>'+num(q)+'</b> · 속도 = 운동량 <b>'+num(v)+'</b> · L = <b>'+num(L)+'</b>(바뀜) · H = <b>'+fmt(Hh)+'</b>(그대로)';}
  inp.addEventListener('input',draw);draw();};

/* ===== 9번 방: SVM ===== */
P.p09=function(h){var W=480,H=440,out=readout(h),mode;var PTS=[[1,1,-1,0.25],[0,1,-1,0],[3,3,1,0.25],[4,4,1,0]];
  function draw(){var s=svgOf(h,W,H),p=plane(s,{W:W,H:H,x0:-0.5,x1:5,y0:-0.5,y1:5,equal:true,label:1});
    function line(c,col,da,w){var a=[c+0.5,-0.5],b=[-0.5,c+0.5];if(c+0.5>5){a=[5,c-5];b=[c-5,5];}el('line',{x1:p.X(a[0]),y1:p.Y(a[1]),x2:p.X(b[0]),y2:p.Y(b[1]),stroke:C[col]||col,'stroke-width':w,'stroke-dasharray':da||null},s);}
    if(mode==='wall'){line(2,'#8a96a3','6 4',2);line(6,'#8a96a3','6 4',2);}
    line(4,'navy',null,3);ktxt(s,p.X(4.4),p.Y(0.1),'칸막이 x + y = 4',{size:12.5,anchor:'end'});
    PTS.forEach(function(q){dot(s,p.X(q[0]),p.Y(q[1]),q[2]>0?'blue':'red',8);
      if(mode==='lam')ktxt(s,p.X(q[0])+12,p.Y(q[1])-10,'λ = '+fmt(q[3]),{size:13.5,weight:'bold',fill:q[3]>0?C.orange:C.muted});});
    if(mode==='wall'){dash(s,p.X(1),p.Y(1),p.X(3),p.Y(3),C.orange);ktxt(s,p.X(2)-8,p.Y(2)-10,'복도 폭 2.83',{size:12.5,anchor:'end',fill:C.orange});}
    out.innerHTML=mode==='lam'?'λ가 0이 아닌 점: <b>(1, 1)·(3, 3) 두 개</b>(λ = 0.25). (0, 1)·(4, 4)는 λ = 0 — 칸막이에 영향이 없습니다.':'회색 점선 = 복도의 두 벽(x + y = 2, x + y = 6). 버팀 점 (1, 1)·(3, 3)이 벽에 닿아 있고, 복도 폭은 <b>2/‖w‖ ≈ 2.83</b>입니다.';}
  mode=toggles(h,function(v){mode=v;draw();});draw();};

/* ===== 10번 방: 안전 강화학습 ===== */
P.p10=function(h){var W=600,H=330,out=readout(h),host=h.parentNode,lam,hist;
  function pol(l){return l<=0.5?10:5/l;}
  function reset(){lam=0;hist=[[0,pol(0),0]];}
  function step(){var sp=pol(lam),risk=sp*sp/10;lam=Math.max(0,lam+0.1*(risk-2.5));hist.push([hist.length,pol(lam),lam]);}
  function draw(){var s=svgOf(h,W,H),n=Math.max(30,hist.length-1),m=box(s,{L:50,T:20,W:520,H:270},{x0:0,x1:n,y0:0,y1:10.5,xt:[0,10,20,30].filter(function(x){return x<=n;}),yt:[0,2,4,6,8,10],xl:'배운 횟수',yl:'속도 / λ×5'});
    el('line',{x1:m.X(0),y1:m.Y(5),x2:m.X(n),y2:m.Y(5),stroke:C.green,'stroke-width':1.5,'stroke-dasharray':'6 4'},s);ktxt(s,m.X(n)-4,m.Y(5)-6,'안전선 속도 5 (위험 2.5)',{size:12,anchor:'end',fill:C.green});
    poly(s,m,hist.map(function(r){return[r[0],r[1]];}),'orange',3);poly(s,m,hist.map(function(r){return[r[0],r[2]*5];}),'navy',2.5);
    var last=hist[hist.length-1];dot(s,m.X(last[0]),m.Y(last[1]),'orange',6);dot(s,m.X(last[0]),m.Y(last[2]*5),'navy',6);
    ktxt(s,m.X(0)+8,m.Y(10)+16,'주황 = 속도, 남색 = λ × 5',{size:12});
    var sp=last[1];out.innerHTML=(hist.length-1)+'번 배움 · λ = <b>'+fmt(last[2],3)+'</b> · 속도 <b>'+fmt(sp)+'</b> · 위험 '+fmt(sp*sp/10)+(Math.abs(sp*sp/10-2.5)<0.02?' → <span class="alert">안전선에 딱 맞췄습니다(λ = 1).</span>':(sp*sp/10>2.5?' → 선을 넘어 λ를 올립니다.':' → 여유가 있어 λ를 조금 내립니다.'));}
  host.querySelectorAll('[data-act]').forEach(function(b){b.addEventListener('click',function(){var a=b.getAttribute('data-act');if(a==='reset')reset();else{var k=a==='ten'?10:1;for(var i=0;i<k;i++)step();}draw();});});
  reset();draw();};

/* ===== 11번 방: RLHF 거리 벌점 ===== */
P.p11=function(h){var W=560,H=320,inp=inputs(h)[0],out=readout(h),BS=[0.2,0.5,1,5];
  function draw(){var b=BS[+inp.value],e=Math.exp(1/b),pa=e/(e+1),kl=pa*Math.log(pa/0.5)+(1-pa)*Math.log((1-pa)/0.5),s=svgOf(h,W,H),y0=270,k=220;
    el('line',{x1:30,y1:y0,x2:W-20,y2:y0,stroke:C.axis,'stroke-width':1.6},s);
    bar(s,70,y0,70,0.5*k,'#9aa5b4','원래 A','0.50');bar(s,150,y0,70,pa*k,'orange','새 A',fmt(pa,3));
    bar(s,320,y0,70,0.5*k,'#9aa5b4','원래 B','0.50');bar(s,400,y0,70,(1-pa)*k,'orange','새 B',fmt(1-pa,3));
    ktxt(s,145,30,'칭찬받는 답 A (보상 1)',{size:13,anchor:'middle'});ktxt(s,395,30,'다른 답 B (보상 0)',{size:13,anchor:'middle'});
    out.innerHTML='β = '+fmt(b)+' → 답 A 확률 <b>'+fmt(pa,3)+'</b> · 원래 모델과의 거리(KL) <b>'+fmt(kl,3)+'</b>'+(b>=5?' → 벌점이 커서 원래 모델 근처에 머뭅니다.':(b<=0.2?' → 벌점이 작아 칭찬받는 답으로 쏠립니다.':''));}
  inp.addEventListener('input',draw);draw();};

/* ===== 12번 방: 모멘텀 ===== */
function runMom(beta){var x=1,y=1,vx=0,vy=0,lr=0.07,pts=[[1,1]],n=null;for(var i=1;i<400;i++){vx=beta*vx-lr*x;vy=beta*vy-lr*25*y;x+=vx;y+=vy;pts.push([x,y]);if(Math.hypot(x,y)<0.01){n=i;break;}}return{pts:pts,n:n};}
P.p12=function(h){var W=520,H=440,out=readout(h),beta;
  function draw(){var s=svgOf(h,W,H),p=plane(s,{W:W,H:H,x0:-1.3,x1:1.3,y0:-1.3,y1:1.3,equal:true,step:.5,label:.5});
    [0.05,0.2,0.5,1,2,3.5].forEach(function(c){var a=Math.sqrt(2*c),b=Math.sqrt(2*c/25);el('ellipse',{cx:p.X(0),cy:p.Y(0),rx:a*p.sx,ry:b*p.sx,fill:'none',stroke:'#f2b88a','stroke-width':1.6},s);});
    var r=runMom(+beta);poly(s,p,r.pts.map(function(q){return[q[0],q[1]];}),'navy',2);
    r.pts.forEach(function(q,i){if(i%1===0)el('circle',{cx:p.X(q[0]),cy:p.Y(q[1]),r:2.6,fill:C.navy},s);});
    dot(s,p.X(1),p.Y(1),'red',7);dot(s,p.X(0),p.Y(0),'green',6);
    out.innerHTML='β = '+beta+' → 바닥 0.01 안까지 <b>'+r.n+'걸음</b>'+(beta==='0'?' — 가파른 쪽으로 지그재그.':(beta==='0.6'?' — 기세 덕분에 가장 빠릅니다.':' — 마찰이 작아 바닥 주변을 맴돕니다.'));}
  beta=toggles(h,function(v){beta=v;draw();});draw();};

/* ===== 13번 방: 걸음법 ===== */
function orbit(kind,n,hh){var q=1,p=0,pts=[[1,0]],emax=0;for(var i=0;i<n;i++){if(kind==='euler'||kind==='plain'){var nq=q+hh*p,np=p-hh*q;q=nq;p=np;}else{p-=0.5*hh*q;q+=hh*p;p-=0.5*hh*q;}pts.push([q,p]);emax=Math.max(emax,Math.abs(0.5*(q*q+p*p)-0.5));}return{pts:pts,E:0.5*(q*q+p*p),emax:emax};}
function orbitPanel(h,labels){var W=480,H=440,out=readout(h),kind;
  function draw(){var s=svgOf(h,W,H),p=plane(s,{W:W,H:H,x0:-1.9,x1:1.9,y0:-1.9,y1:1.9,equal:true,step:.5,label:1,xl:'위치',yl:'운동량'});
    el('circle',{cx:p.X(0),cy:p.Y(0),r:p.sx,fill:'none',stroke:C.teal,'stroke-width':2,'stroke-dasharray':'6 4'},s);
    var r=orbit(kind,100,0.1);poly(s,p,r.pts,kind==='euler'||kind==='plain'?'red':'orange',2.2);dot(s,p.X(1),p.Y(0),'navy',6);
    var last=r.pts[r.pts.length-1];dot(s,p.X(last[0]),p.Y(last[1]),'red',6);
    out.innerHTML=labels(kind,r);}
  kind=toggles(h,function(v){kind=v;draw();});draw();}
P.p13=function(h){orbitPanel(h,function(k,r){return k==='euler'?'오일러 걸음 100번 → 에너지 0.5 → <b>'+fmt(r.E,2)+'</b> (약 '+fmt(r.E/0.5,1)+'배로 부풂). 원 밖으로 퍼집니다.':'리프프로그 걸음 100번 → 에너지 오차 최대 <b>'+fmt(r.emax/0.5*100,2)+'%</b>. 처음 원을 지킵니다.';});};
P.p22=function(h){orbitPanel(h,function(k,r){return k==='plain'?'에너지를 안 지키는 예측(그림 예시) → 100걸음 뒤 에너지 <b>'+fmt(r.E,2)+'</b>. 궤도가 소용돌이처럼 퍼집니다.':'에너지를 지키는 예측(그림 예시) → 에너지 오차 최대 <b>'+fmt(r.emax/0.5*100,2)+'%</b>. 궤도가 지켜집니다.';});};

/* ===== 14번 방: 역전파 ===== */
P.p14=function(h){var W=620,H=300,inp=inputs(h)[0],out=readout(h);
  function node(s,x,y,lab,val,col){el('rect',{x:x-60,y:y-34,width:120,height:68,rx:12,fill:'#fff',stroke:C[col],'stroke-width':2.5},s);ktxt(s,x,y-6,lab,{size:14,anchor:'middle',fill:C[col]});txt(s,x,y+18,val,{size:16,anchor:'middle',italic:false,weight:'bold'});}
  function draw(){var x=+inp.value,hh=2*x,y=hh*hh,ah=2*hh,ax=ah*2,s=svgOf(h,W,H);
    node(s,90,110,'입력 x',num(x),'navy');node(s,310,110,'중간 h = 2x',num(hh),'navy');node(s,530,110,'출력 y = h²',fmt(y),'navy');
    arrow(s,152,100,246,100,'navy',2.5);arrow(s,372,100,466,100,'navy',2.5);ktxt(s,200,88,'×2',{size:13,anchor:'middle'});ktxt(s,420,88,'제곱',{size:13,anchor:'middle'});
    arrow(s,466,190,372,190,'orange',3);arrow(s,246,190,152,190,'orange',3);
    ktxt(s,420,214,'그림자 가격 2h',{size:12.5,anchor:'middle',fill:C.orange});ktxt(s,200,214,'× 2',{size:12.5,anchor:'middle',fill:C.orange});
    txt(s,310,250,'a_h = '+num(ah),{size:16,anchor:'middle',italic:false,weight:'bold',fill:C.orange});txt(s,90,250,'a_x = '+num(ax),{size:16,anchor:'middle',italic:false,weight:'bold',fill:C.orange});txt(s,530,250,'시작: 1',{size:15,anchor:'middle',italic:false,fill:C.orange});
    ktxt(s,20,30,'앞으로 (계산)',{size:13,fill:C.navy});ktxt(s,20,290,'거꾸로 (그림자 가격)',{size:13,fill:C.orange});
    out.innerHTML='x = '+num(x)+' → h = '+num(hh)+' → y = '+fmt(y)+' · 거꾸로: h의 그림자 가격 <b>'+num(ah)+'</b>, x의 그림자 가격 <b>'+num(ax)+'</b> → x를 0.01 늘리면 y는 약 '+num(ax*0.01)+' 바뀝니다.';}
  inp.addEventListener('input',draw);draw();};

/* ===== 15번 방: 솔로우 황금률 ===== */
P.p15=function(h){var W=560,H=330,inp=inputs(h)[0],out=readout(h);
  function st(s_){var k=Math.pow(s_/0.1,1.5),y=Math.pow(k,1/3);return{k:k,y:y,c:(1-s_)*y};}
  function draw(){var s_=+inp.value,s=svgOf(h,W,H),m=box(s,{L:56,T:20,W:470,H:270},{x0:0,x1:0.95,y0:0,y1:1.35,xt:[0,0.2,1/3,0.6,0.8],yt:[0,0.4,0.8,1.2],xl:'저축률',yl:'정상 상태 소비'});
    curve(s,m,function(x){return st(x).c;},0.02,0.95,'teal',3);dash(s,m.X(1/3),m.Y(0),m.X(1/3),m.Y(st(1/3).c),C.orange);
    ktxt(s,m.X(1/3)+6,m.Y(st(1/3).c)-10,'황금률 1/3',{size:12.5,fill:C.orange});
    var r=st(s_);dot(s,m.X(s_),m.Y(r.c),'red',7);
    out.innerHTML='저축률 '+fmt(s_)+' → 기계 '+fmt(r.k)+' · 생산 '+fmt(r.y,3)+' · 소비 <b>'+fmt(r.c,3)+'</b>'+(Math.abs(s_-1/3)<0.006?' ← 황금률, 소비가 가장 큽니다.':' (가장 큰 소비 1.217은 저축률 1/3)');}
  inp.addEventListener('input',draw);draw();};

/* ===== 16번 방: 중첩세대 ===== */
P.p16=function(h){var W=560,H=330,inp=inputs(h)[0],out=readout(h);
  function U(c1){return Math.log(c1)+Math.log(1.5*(100-c1));}
  function draw(){var c1=+inp.value,s=svgOf(h,W,H),m=box(s,{L:56,T:20,W:470,H:270},{x0:0,x1:100,y0:5.5,y1:8.4,xt:[0,25,50,75,100],yt:[6,7,8],xl:'젊을 때 소비',yl:'만족'});
    curve(s,m,U,3,97,'teal',3,null,[5.5,8.4]);dash(s,m.X(50),m.Y(5.5),m.X(50),m.Y(U(50)),C.orange);dot(s,m.X(c1),m.Y(U(c1)),'red',7);
    out.innerHTML='젊을 때 '+fmt(c1)+' · 늙어서 '+fmt(1.5*(100-c1))+' · 만족 <b>'+fmt(U(c1),3)+'</b>'+(c1===50?' ← 가장 큼. λ = 1/50 = 0.02':' (가장 큰 만족은 50·75에서 '+fmt(U(50),3)+')');}
  inp.addEventListener('input',draw);draw();};

/* ===== 17번 방: 케이크 먹기 ===== */
P.p17=function(h){var W=560,H=330,inp=inputs(h)[0],out=readout(h);
  function draw(){var t=+inp.value,s=svgOf(h,W,H),m=box(s,{L:56,T:20,W:470,H:270},{x0:0,x1:60,y0:0,y1:105,xt:[0,20,40,60],yt:[0,25,50,75,100],xl:'햇수',yl:'남은 케이크 / 한 해 소비×10'});
    curve(s,m,function(x){return 100*Math.exp(-0.05*x);},0,60,'navy',3);curve(s,m,function(x){return 50*Math.exp(-0.05*x);},0,60,'orange',3);
    var k=100*Math.exp(-0.05*t),c=5*Math.exp(-0.05*t);dot(s,m.X(t),m.Y(k),'navy',6);dot(s,m.X(t),m.Y(10*c),'orange',6);
    ktxt(s,m.X(14),m.Y(100*Math.exp(-0.7))-8,'남은 케이크',{size:12.5,fill:C.navy});ktxt(s,m.X(8),m.Y(50*Math.exp(-0.4))+22,'한 해 소비 × 10',{size:12.5,fill:C.orange});
    out.innerHTML=t+'년째 · 남은 케이크 <b>'+fmt(k,1)+'</b> · 한 해 소비 <b>'+fmt(c,2)+'</b> · 소비/케이크 = 5% 그대로 · 그림자 가격 μ = 1/c = '+fmt(1/c,2)+'(해마다 5%씩 오름)';}
  inp.addEventListener('input',draw);draw();};

/* ===== 18번 방: q 이론 ===== */
P.p18=function(h){var W=560,H=330,inp=inputs(h)[0],out=readout(h);
  function draw(){var q=+inp.value,I=q-1,s=svgOf(h,W,H),m=box(s,{L:56,T:20,W:470,H:270},{x0:0.6,x1:1.6,y0:-0.45,y1:0.65,xt:[0.6,0.8,1,1.2,1.4,1.6],yt:[-0.4,-0.2,0,0.2,0.4,0.6],xl:'q',yl:'투자 I'});
    curve(s,m,function(x){return x-1;},0.6,1.6,'teal',3);el('line',{x1:m.X(q),y1:m.Y(0),x2:m.X(q),y2:m.Y(I),stroke:I>=0?C.blue:C.red,'stroke-width':10,'stroke-linecap':'round','stroke-opacity':.5},s);dot(s,m.X(q),m.Y(I),'red',7);
    out.innerHTML='q = '+fmt(q)+' → 투자 I = q − 1 = <b>'+num(I)+'</b> → '+(Math.abs(I)<1e-9?'그대로 둡니다.':(I>0?'기계를 더 들입니다.':'기계를 줄입니다.'))+' 설치 비용 ½·I² = '+fmt(0.5*I*I,3);}
  inp.addEventListener('input',draw);draw();};

/* ===== 19번 방: 상자 속 전자 ===== */
P.p19=function(h){var W=600,H=320,inp=inputs(h)[0],out=readout(h);
  function draw(){var n=+inp.value,s=svgOf(h,W,H);
    var m=box(s,{L:40,T:30,W:300,H:250},{x0:0,x1:1,y0:-1.2,y1:1.2,xt:[0,0.5,1],yt:[-1,0,1],xl:'상자 안 위치',yl:'파동'});
    el('line',{x1:m.X(0),y1:30,x2:m.X(0),y2:280,stroke:C.navy,'stroke-width':6},s);el('line',{x1:m.X(1),y1:30,x2:m.X(1),y2:280,stroke:C.navy,'stroke-width':6},s);
    curve(s,m,function(x){return Math.sin(n*Math.PI*x);},0,1,'orange',3.5);
    var g=box(s,{L:420,T:30,W:150,H:250},{x0:0,x1:1,y0:0,y1:6.4,yt:[0,1.5,3,4.5,6],yl:'에너지(eV)'});
    [1,2,3,4].forEach(function(k){var E_=0.376*k*k;el('line',{x1:g.X(0.1),y1:g.Y(E_),x2:g.X(0.9),y2:g.Y(E_),stroke:k===n?C.orange:'#c9d2dc','stroke-width':k===n?5:3},s);ktxt(s,g.X(0.95),g.Y(E_)+4,'n='+k,{size:12,fill:k===n?C.orange:C.muted});});
    out.innerHTML='n = '+n+' → 마디 '+(n-1)+'개 · 에너지 = 0.376 × '+n+'² = <b>'+fmt(0.376*n*n,3)+'eV</b> (1nm 상자 속 전자). 계단 사이 값은 없습니다.';}
  inp.addEventListener('input',draw);draw();};

/* ===== 20번 방: 변분 원리 ===== */
P.p20=function(h){var W=560,H=330,inp=inputs(h)[0],out=readout(h);
  function E_(a){return a/4+1/(4*a);}
  function draw(){var a=+inp.value,s=svgOf(h,W,H),m=box(s,{L:56,T:20,W:470,H:270},{x0:0,x1:3.1,y0:0.3,y1:1.45,xt:[0,1,2,3],yt:[0.5,0.75,1,1.25],xl:'파동 넓이 a',yl:'평균 에너지 ⟨H⟩'});
    el('line',{x1:m.X(0),y1:m.Y(0.5),x2:m.X(3.1),y2:m.Y(0.5),stroke:C.green,'stroke-width':2,'stroke-dasharray':'6 4'},s);ktxt(s,m.X(3.05),m.Y(0.5)+18,'진짜 바닥 0.5',{size:12.5,anchor:'end',fill:C.green});
    curve(s,m,E_,0.2,3.1,'navy',3,null,[0.3,1.45]);dot(s,m.X(a),m.Y(E_(a)),'red',7);
    out.innerHTML='a = '+fmt(a)+' → ⟨H⟩ = '+fmt(a)+'/4 + 1/(4×'+fmt(a)+') = <b>'+fmt(E_(a),3)+'</b>'+(Math.abs(a-1)<0.01?' ← 진짜 바닥과 같습니다.':' · 바닥 0.5보다 '+fmt(E_(a)-0.5,3)+' 높습니다.');}
  inp.addEventListener('input',draw);draw();};

/* ===== 21번 방: 이징 에너지 ===== */
P.p21=function(h){var W=560,H=325,out=readout(h),sel,ST=[[1,1],[1,-1],[-1,1],[-1,-1]];
  function draw(){var s=svgOf(h,W,H),y0=150,k=40;el('line',{x1:30,y1:y0,x2:W-20,y2:y0,stroke:C.axis,'stroke-width':1.6},s);
    ST.forEach(function(st,i){var E_=st[0]*st[1]+st[0];bar(s,50+i*125,y0,80,E_*k,+sel===i?'orange':'#c9d2dc','('+(st[0]>0?'+1':'−1')+', '+(st[1]>0?'+1':'−1')+')',num(E_));});
    var st=ST[+sel];[0,1].forEach(function(j){var x=200+j*160,c=st[j]>0?C.blue:C.red;el('circle',{cx:x,cy:282,r:18,fill:c,'fill-opacity':.85},s);ktxt(s,x,287,(j+1)+'번',{size:13,anchor:'middle',fill:'#fff'});});
    ktxt(s,280,314,'파랑 = +1 조, 빨강 = −1 조',{size:12.5,anchor:'middle'});
    var E_=st[0]*st[1]+st[0];out.innerHTML='배치 ('+num(st[0])+', '+num(st[1])+') → H = '+num(st[0]*st[1])+' + '+num(st[0])+' = <b>'+num(E_)+'</b>'+(E_===-2?' ← <span class="alert">가장 낮은 에너지! 이 문제의 답입니다.</span>':'');}
  sel=toggles(h,function(v){sel=v;draw();});draw();};

/* ===== 대결 ===== */
P.duel=function(h){var W=600,H=260,out=readout(h),host=h.parentNode,open={};
  var R=[['1판 · 용수철 궤적 예측','둘 다 위치 = cos t','무승부'],['2판 · 황금률(울타리 하나)','시아가 λ 한 줄로 저축률 1/3','시아 승'],['3판 · 1,000걸음 에너지 지키기','리프프로그(모아) vs 단순 오일러(시아) — 걸음법 승부','모아 승']];
  function draw(){var s=svgOf(h,W,H);R.forEach(function(r,i){var y=30+i*70;el('rect',{x:10,y:y,width:W-20,height:56,rx:12,fill:open[i+1]?'#fff':C.grid,stroke:open[i+1]?C.navy:C.grid,'stroke-width':2},s);
      ktxt(s,28,y+24,r[0],{size:14.5,weight:'bold'});ktxt(s,28,y+45,open[i+1]?r[1]:'아직 열지 않았습니다',{size:13,fill:C.muted});
      if(open[i+1])ktxt(s,W-30,y+35,r[2],{size:17,anchor:'end',weight:'bold',fill:r[2]==='시아 승'?C.teal:(r[2]==='모아 승'?C.orange:C.navy)});});
    var n=Object.keys(open).length;out.innerHTML=n<3?'연 판 '+n+'/3':'<b>1승 1패 1무 — 무승부.</b> 지도가 틀린 게 아니라 쓰임새가 다릅니다.';}
  host.querySelectorAll('[data-round]').forEach(function(b){b.setAttribute('aria-pressed','false');b.addEventListener('click',function(){open[b.getAttribute('data-round')]=1;b.classList.add('on');b.setAttribute('aria-pressed','true');draw();});});draw();};
function quiz(q){var ans=+q.getAttribute('data-ans');var fb=q.querySelector('.fb');q.querySelectorAll('button').forEach(function(b,i){b.addEventListener('click',function(){q.querySelectorAll('button').forEach(function(x){x.classList.remove('ok','no');});b.classList.add(i===ans?'ok':'no');fb.innerHTML=i===ans?'⭕ '+q.getAttribute('data-ok'):'❌ '+q.getAttribute('data-no');});});}

/* ===== 지식 색인·꾸러미 ===== */
function kg(){var raw=document.getElementById('kg-raw');var mount=document.getElementById('kg-mount');if(!raw||!mount)return;var K=JSON.parse(raw.textContent);
  mount.innerHTML='<input class="kg-search" type="search" placeholder="개념 찾기 (예: 그릇, 운동량, 그림자 가격)" aria-label="지식 색인 검색"><div class="kg-list"></div>';
  var list=mount.querySelector('.kg-list'),inp=mount.querySelector('input');
  var TY={Concept:'개념',Method:'방법',Analogy:'비유',Application:'쓰임',OpenQuestion:'열린 질문'};
  function render(){var q=inp.value.trim().toLowerCase();list.innerHTML=K.nodes.filter(function(n){return !q||(n.label.ko+' '+n.label.en+' '+(n.desc||'')).toLowerCase().indexOf(q)>=0;}).map(function(n){
    var nb=K.edges.filter(function(e){return e.s===n.id||e.o===n.id;}).map(function(e){var o=e.s===n.id?e.o:e.s;var m=K.nodes.filter(function(x){return x.id===o;})[0];return m?m.label.ko:'';}).filter(Boolean);
    return '<div class="kg-item"><span class="t">'+(TY[n.type]||n.type)+'</span><b>'+n.label.ko+'</b><span class="muted">'+n.label.en+'</span><div>'+(n.desc||'')+'</div>'+(nb.length?'<div class="muted" style="font-size:12.5px">이웃: '+nb.join(', ')+'</div>':'')+'<a href="'+(n.page?n.page+'.html':'')+n.anchor+'">설명 보러 가기 →</a></div>';}).join('');}
  inp.addEventListener('input',render);render();
  var ex=document.getElementById('export-mount');if(!ex)return;
  ex.innerHTML='<div class="exp-btns"><button class="btn" data-x="json">kg.json</button><button class="btn" data-x="ld">JSON-LD</button><button class="btn" data-x="ttl">Turtle (Protégé)</button><button class="btn" data-x="csv">CSV (Neo4j·Gephi)</button><button class="btn" data-x="bib">BibTeX</button><button class="btn" data-x="ris">RIS</button></div>';
  function dl(name,text,type){var b=new Blob([text],{type:type||'text/plain'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},500);}
  var base=K.page;var refs=JSON.parse((document.getElementById('refs-csl')||{textContent:'[]'}).textContent);
  ex.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){var x=b.getAttribute('data-x');
    if(x==='json')dl(base+'.kg.json',JSON.stringify(K,null,2),'application/json');
    if(x==='ld')dl(base+'.jsonld',document.getElementById('kg-ld').textContent,'application/ld+json');
    if(x==='ttl'){var t='@prefix lab: <urn:lab:> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n\n';
      K.nodes.forEach(function(n){t+='<urn:'+n.id+'> a lab:'+n.type+' ;\n  skos:prefLabel "'+n.label.ko+'"@ko , "'+n.label.en+'"@en ;\n  rdfs:comment "'+(n.desc||'').replace(/"/g,'\\"')+'"@ko .\n\n';});
      K.edges.forEach(function(e){t+='<urn:'+e.s+'> lab:'+e.p+' <urn:'+e.o+'> .\n';});dl(base+'.ttl',t,'text/turtle');}
    if(x==='csv'){var c='id,type,label_ko,label_en,anchor\n'+K.nodes.map(function(n){return [n.id,n.type,n.label.ko,n.label.en,(n.page||base)+'.html'+n.anchor].map(function(v){return '"'+String(v).replace(/"/g,'""')+'"';}).join(',');}).join('\n');
      c+='\n\nsource,relation,target\n'+K.edges.map(function(e){return [e.s,e.p,e.o].join(',');}).join('\n');dl(base+'.csv',c,'text/csv');}
    if(x==='bib')dl(base+'.bib',refs.map(function(r){return '@misc{'+r.id+',\n  title = {'+r.title+'},\n  author = {'+r.author[0].literal+'},\n  howpublished = {'+(r.note||'')+'},\n  note = {accessed '+r.accessed['date-parts'][0].join('-')+'}\n}';}).join('\n\n'));
    if(x==='ris')dl(base+'.ris',refs.map(function(r){return 'TY  - GEN\nTI  - '+r.title+'\nAU  - '+r.author[0].literal+'\nN1  - '+(r.note||'')+'\nER  - ';}).join('\n'));});});}

function boot(){document.querySelectorAll('[data-panel]').forEach(function(h){var k=h.getAttribute('data-panel');if(P[k])P[k](h);});
  document.querySelectorAll('.quiz').forEach(quiz);kg();
  var pr=document.getElementById('prog');if(pr)window.addEventListener('scroll',function(){var d=document.documentElement;pr.style.width=(100*d.scrollTop/Math.max(1,d.scrollHeight-d.clientHeight))+'%';},{passive:true});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
})();
