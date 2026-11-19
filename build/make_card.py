import math
W,H=1080,1350
TEAL='#1f8a8a'; TEAL_L='#e6f4f3'; OR='#e07a2e'; OR_L='#fdf0e6'; NAVY='#1e2f4f'; GRAY='#5b6576'
FONT="'Noto Sans CJK KR','Noto Sans KR',sans-serif"
o=[]
def t(x,y,s,size=22,fill=NAVY,w=400,anchor='start',style=''):
    o.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{w}" text-anchor="{anchor}" {style}>{s}</text>')
def lerp(c1,c2,a):
    a=max(0,min(1,a));h=lambda c:[int(c[i:i+2],16) for i in (1,3,5)]
    r=[round(x+(y-x)*a) for x,y in zip(h(c1),h(c2))];return '#%02x%02x%02x'%tuple(r)

def proj(u,v,z,cx,cy,k=95,kz=95):
    x=cx+(u-v)*math.cos(math.radians(30))*k
    y=cy+(u+v)*math.sin(math.radians(30))*k - z*kz
    return x,y

def surface(f,cx,cy,lo,hi,col_lo,col_hi,zmin,zmax,polar=False,n=14):
    quads=[]
    for i in range(n):
        for j in range(n):
            if polar:
                r0=1.35*i/n; r1=1.35*(i+1)/n; a0=2*math.pi*j/n*1.0; a1=2*math.pi*(j+1)/n
                pts=[(r0*math.cos(a0),r0*math.sin(a0)),(r1*math.cos(a0),r1*math.sin(a0)),(r1*math.cos(a1),r1*math.sin(a1)),(r0*math.cos(a1),r0*math.sin(a1))]
            else:
                u0=lo+(hi-lo)*i/n; u1=lo+(hi-lo)*(i+1)/n; v0=lo+(hi-lo)*j/n; v1=lo+(hi-lo)*(j+1)/n
                pts=[(u0,v0),(u1,v0),(u1,v1),(u0,v1)]
            zs=[f(u,v) for u,v in pts]; zc=sum(zs)/4
            depth=sum(u+v for u,v in pts)/4 - zc*0.01
            quads.append((depth,pts,zs,zc))
    quads.sort(key=lambda q:q[0])
    for d,pts,zs,zc in quads:
        P=' '.join('%.1f,%.1f'%proj(u,v,z,cx,cy) for (u,v),z in zip(pts,zs))
        c=lerp(col_lo,col_hi,(zc-zmin)/(zmax-zmin))
        o.append(f'<polygon points="{P}" fill="{c}" fill-opacity="0.92" stroke="#ffffff" stroke-width="0.8"/>')

def axes(cx,cy,lu,lv,lz):
    for (a,b,c),lab,dx,dy in [((1.75,0,0),lu,8,22),((0,1.75,0),lv,-10,22),((0,0,1.25),lz,6,-6)]:
        x0,y0=proj(0,0,0,cx,cy); x1,y1=proj(a,b,c,cx,cy)
        o.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{NAVY}" stroke-width="2" marker-end="url(#ah)"/>')
        t(x1+dx,y1+dy,lab,19,NAVY,600,'middle')

def curve(f,pts_uv,cx,cy,color,w=4,dash=''):
    P=' '.join('%.1f,%.1f'%proj(u,v,f(u,v),cx,cy) for u,v in pts_uv)
    o.append(f'<polyline points="{P}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" {dash}/>')
def dot(f,u,v,cx,cy,color):
    x,y=proj(u,v,f(u,v),cx,cy); o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="#fff" stroke="{color}" stroke-width="4"/>');return x,y

L=lambda q,qd:0.5*qd*qd-0.5*q*q
Hf=lambda q,p:0.5*p*p+0.5*q*q
o.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
o.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1e2f4f"/></marker>'
         f'<marker id="ao" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{OR}"/></marker>'
         f'<marker id="at" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{TEAL}"/></marker></defs>')
o.append(f'<g font-family="{FONT}">')
# title
t(W/2,72,'라그랑지안 vs 해밀토니안',50,NAVY,800,'middle')
t(W/2,114,'같은 용수철의 흔들림을 그린 <tspan fill="'+TEAL+'" font-weight="700">두 장의 지도</tspan>',25,GRAY,500,'middle')
# column headers
for x,c,cl,name,sub in [(30,TEAL,TEAL_L,'라그랑지안 지도','길 전체에 점수를 매긴다'),(555,OR,OR_L,'해밀토니안 지도','지금 이 순간의 화살표를 본다')]:
    o.append(f'<rect x="{x}" y="140" width="495" height="430" rx="18" fill="{cl}"/>')
    o.append(f'<rect x="{x}" y="140" width="495" height="58" rx="18" fill="{c}"/><rect x="{x}" y="175" width="495" height="23" fill="{c}"/>')
    t(x+24,179,name,27,'#fff',800); t(x+471,179,sub,18,'#fff',500,'end')
# 3D left saddle
cxL,cyL=277,385
surface(L,cxL,cyL,-1.3,1.3,'#9fd3cf','#0e5e5e',-0.85,0.85)
th=[2*math.pi*i/120 for i in range(121)]
curve(L,[(math.cos(a),-math.sin(a)) for a in th],cxL,cyL,'#f2c14e',4)
axes(cxL,cyL,'위치','속도','L')
x,y=dot(L,1,0,cxL,cyL,'#c0392b'); t(x-14,y+6,'출발: 위치 1, 속도 0',16,NAVY,700,'end','stroke="#fff" stroke-width="5" paint-order="stroke"')
t(277,540,'L의 모양 = <tspan font-weight="800">안장</tspan> (한쪽은 오르막, 한쪽은 내리막)',19,NAVY,500,'middle')
# 3D right bowl
cxR,cyR=802,410
surface(Hf,cxR,cyR,0,0,'#fde0c8','#c4561a',0,0.95,polar=True)
curve(Hf,[(math.cos(a),math.sin(a)) for a in th],cxR,cyR,TEAL,5)
axes(cxR,cyR,'위치','운동량','H')
x,y=dot(Hf,1,0,cxR,cyR,'#c0392b'); t(x+14,y+6,'출발',16,NAVY,700)
t(802,540,'H의 모양 = <tspan font-weight="800">그릇</tspan> · 점은 높이 0.5의 둘레를 돈다',19,NAVY,500,'middle')
# legend curve
t(277,566,'노란 선: 실제로 움직인 길이 안장 위에 그린 자취',15,GRAY,400,'middle')
t(802,566,'초록 원: 에너지가 같은 높이 = 한 바퀴가 한 번 흔들림',15,GRAY,400,'middle')

# row 2 idea
y0=595
for x,c,cl,head,body in [(30,TEAL,TEAL_L,'L = 움직임 에너지 − 높이 에너지','빼서 본다 (T − V)'),(555,OR,OR_L,'H = 움직임 에너지 + 높이 에너지','더해서 본다 (T + V)')]:
    o.append(f'<rect x="{x}" y="{y0}" width="495" height="96" rx="14" fill="#fff" stroke="{c}" stroke-width="2.5"/>')
    t(x+247,y0+42,head,23,c,800,'middle'); t(x+247,y0+76,body,19,GRAY,500,'middle')
# bridge
o.append(f'<rect x="380" y="{y0+100}" width="320" height="44" rx="22" fill="{NAVY}"/>')
t(540,y0+129,'⇄ 지도 바꿔 그리기: 속도 축 → 운동량 축',16,'#fff',600,'middle')
t(540,y0+165,'운동량 = 무게 × 속도 (이 용수철은 무게 1이라 같은 숫자)',16,GRAY,400,'middle')

# row 3 how it sees
y1=785
for x,c in [(30,TEAL),(555,OR)]:
    o.append(f'<rect x="{x}" y="{y1}" width="495" height="235" rx="14" fill="#fff" stroke="#d9dee6" stroke-width="2"/>')
t(54,y1+38,'어떻게 답을 찾나',21,TEAL,800)
t(579,y1+38,'어떻게 답을 찾나',21,OR,800)
# left: paths A->B
ax,ay,bx,by=100,y1+175,280,y1+175
for k,dash,col,wid in [(-55,'stroke-dasharray="7 6"','#9aa5b4',2.5),(0,'',TEAL,4.5)]:
    o.append(f'<path d="M{ax},{ay} Q{(ax+bx)/2},{ay+2*k} {bx},{by}" fill="none" stroke="{col}" stroke-width="{wid}" {dash}/>')
for (px,py),lab,dx,an in [((ax,ay),'출발',-12,'end'),((bx,by),'도착',12,'start')]:
    o.append(f'<circle cx="{px}" cy="{py}" r="7" fill="{NAVY}"/>'); t(px+dx,py+5,lab,15,NAVY,600,an)
t(190,y1+108,'휜 길: 점수 0.67',15,GRAY,500,'middle')
t(190,y1+203,'곧은 길: 점수 0.50 (진짜 길)',15,TEAL,800,'middle')
for i,s in enumerate(['길마다 점수를 매겨 보면','진짜 길은 살짝 비틀어도','점수가 거의 변하지 않는','길이다.']):
    t(330,y1+90+i*30,s,17,NAVY,500)
t(54,y1+64,'같은 출발·도착, 휜 정도만 다른 두 길',14,GRAY)
# right: contour + arrows
ccx,ccy=655,y1+148
for r in (26,48,70):
    o.append(f'<circle cx="{ccx}" cy="{ccy}" r="{r}" fill="none" stroke="#f2b88a" stroke-width="2"/>')
px,py=ccx+48,ccy
o.append(f'<line x1="{px}" y1="{py}" x2="{px+40}" y2="{py}" stroke="#9aa5b4" stroke-width="3" marker-end="url(#ah)"/>')
t(px+20,py-12,'오르막',14,GRAY,600,'middle')
o.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+50}" stroke="{OR}" stroke-width="4.5" marker-end="url(#ao)"/>')
t(px+8,py+66,'가는 쪽',14,OR,700)
o.append(f'<circle cx="{px}" cy="{py}" r="6" fill="{NAVY}"/>')
for i,s in enumerate(['지금 자리에서 화살표가','오르막과 직각이라','내려가지도 오르지도 않고','둘레를 계속 돈다.']):
    t(790,y1+90+i*30,s,17,NAVY,500)
t(579,y1+64,'둥근 선 = 에너지가 같은 높이(등고선)',14,GRAY)

# same answer band
y2=1040
o.append(f'<rect x="30" y="{y2}" width="1020" height="70" rx="14" fill="#eef1f6"/>')
t(540,y2+31,'두 지도, <tspan font-weight="800">같은 답</tspan>: 위치가 1 → 0 → −1 → 0 → 1로 흔들리고',20,NAVY,500,'middle')
t(540,y2+58,'에너지는 처음 0.5 그대로 (빼서 보든 더해서 보든 움직임은 하나)',18,GRAY,400,'middle')

# uses
y3=1128
for x,c,cl,head,items in [(30,TEAL,TEAL_L,'이럴 때 편하다',['울타리(예산·조건)가 있는 최적화','좌표를 바꿔도 식이 그대로','AI: 라그랑주 승수 · 조건 있는 학습']),
                          (555,OR,OR_L,'이럴 때 편하다',['오래 돌리는 시뮬레이션','에너지를 지키며 계산하기','AI: 모멘텀 학습 · HMC 표본 뽑기'])]:
    o.append(f'<rect x="{x}" y="{y3}" width="495" height="140" rx="14" fill="{cl}"/>')
    t(x+24,y3+34,head,20,c,800)
    for i,s in enumerate(items): t(x+30,y3+66+i*28,'• '+s,17,NAVY,500)
# footer
t(540,1296,'같은 이름의 가족: 최적화의 라그랑지안(목표 − λ×조건)도 "규칙을 한 점수표에 넣고 멈추는 점을 찾는다"',15,NAVY,500,'middle')
t(540,1322,'안장은 L 값의 모양이고, 최소·멈춤은 길 전체 점수의 이야기 · 형식 참고 matharium · 글 안상선 ((주)M-Robo 대표)',13,GRAY,400,'middle')
o.append('</g>')
open('/home/claude/card/lagrangian_vs_hamiltonian_card.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'+''.join(o)+'</svg>')
