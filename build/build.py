# -*- coding: utf-8 -*-
"""두 장의 지도 — 라그랑지안 vs 해밀토니안. python3 build/build.py 로 index·00~07 페이지와 assets/panels.js를 다시 만든다."""
import json, os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_a import ROOMS_A, ROOMS_B
from content_b import ROOMS_C, ROOMS_D, ML_ATLAS, ML_3D, NN_ATLAS0, NN_ATLAS1, NN_ATLAS2, NN_3D, BACKPROP
from content_c import ROOMS_E, ROOMS_F, ROOMS_G
from easy_extra import SAY, DOC, AI, SYM

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = "v1.4"
DATE = "2026-11-19"
SITE = "https://adminmrobo.github.io/lagrangian_hamiltonian_lab/"
REPO = "https://github.com/adminmrobo/lagrangian_hamiltonian_lab"
AUTHOR_URL = "https://adminmrobo.github.io/who_am_i/who_am_i.html"
BOWL = "https://adminmrobo.github.io/optimization_3d_map/"
NABLA = "https://github.com/adminmrobo/vector_calculus_lab"
E = html.escape

CH = {
 "sia": ("시아", "sia", "인턴(No.005) · 직관파. 라그랑지안 팀 — 길 전체를 본다"),
 "moa": ("모아", "moa", "인턴(No.006) · 꼼꼼파. 해밀토니안 팀 — 지금 이 순간의 화살표를 본다"),
 "doctor": ("박사", "doctor", "두 지도를 그린 사람. 방마다 \"AI에서는\"을 정리한다"),
 "haru": ("조수 하루", "haru", "수식 상자 담당. 어려운 식을 대신 묻고 숫자로 풀어 본다. 대결 심판"),
 "fruitfly": ("초파리 연구원", "fruitfly", "의심 담당. \"이걸 눌러 봐\"로 실험 패널을 권한다"),
 "jupanbot": ("주판봇", "jupanbot", "성급한 확신으로 흔한 오해를 대표한다"),
}
COLV = {"doctor": "doc", "haru": "asst", "fruitfly": "fly", "jupanbot": "robo", "sia": "sia", "moa": "moa"}

def face(k, e="e13", cls=""):
    n, f, _ = CH[k]
    return f'<img src="assets/chars/{f}_{e}.webp" alt="{E(n)}" width="96" height="96" loading="lazy"{(" class=%s" % cls) if cls else ""}>'

# ------------------------------------------------------------- 편 정의
PARTS = [
 dict(key="00", fn="00_orientation.html", n="0편 · 오리엔테이션", title="가방 점검", rooms=[],
      card="그릇·오르막 화살표·굽음을 실험 3개로 복습합니다. 건너뛰어도 됩니다.", face=("doctor","e08")),
 dict(key="01", fn="01_lagrangian.html", n="①편 · 방 1~4", title="차이의 지도 — 라그랑지안", rooms=ROOMS_A,
      card="T − V로 길 전체에 점수를 매기고, 점수가 멈추는 길을 고릅니다. 울타리(라그랑주 승수)까지.", face=("sia","e01"),
      lead="움직임 에너지에서 높이 에너지를 <b>빼서</b> 길 전체에 점수를 매깁니다. 점수가 멈추는 길이 자연이 고르는 길입니다.",
      three=("에너지를 빼서(T − V) 길 전체에 점수를 매기는 법과, 울타리 조건을 점수표에 넣는 법을 배웁니다.",
             "법칙을 직접 짜지 않고 점수 규칙만 정하면 답이 나온다는 생각이 최적화·머신러닝과 같습니다.",
             "예산·안전선 같은 조건을 지키며 가장 좋은 답을 고르는 일에 바로 쓰입니다."),
      intro=[("doctor","e08","오늘은 공 하나의 움직임을 지도 두 장에 그린다. 첫 장은 빼기의 지도다."),("sia","e19","저는 이쪽 팀이에요. 길 전체를 한눈에 보는 거 좋아요!"),("jupanbot","e16","빼기든 더하기든 그게 그거 아닌가요?")]),
 dict(key="02", fn="02_hamiltonian.html", n="②편 · 방 5~8-1", title="합의 지도 — 해밀토니안", rooms=ROOMS_B,
      card="위치·운동량 지도 위에 T + V 그릇을 세우고, 둘레를 도는 화살표를 봅니다. 두 지도 나란히까지.", face=("moa","e16"),
      lead="속도 축을 운동량 축으로 바꾸고 에너지를 <b>더하면</b> 그릇이 생깁니다. 공은 그 그릇의 둘레를 돕니다.",
      three=("위치·운동량 지도 위에 에너지(T + V) 그릇을 세우고, 지금 이 순간의 화살표를 읽습니다.",
             "에너지가 지켜지는 계산, 모멘텀 학습, 표본 뽑기, 양자역학이 모두 이 지도 위에서 돌아갑니다.",
             "오래 돌리는 시뮬레이션이 왜 틀어지는지, 학습이 왜 맴도는지 설명할 수 있습니다."),
      intro=[("doctor","e07","둘째 장은 더하기의 지도다. 축 하나를 바꿔 그린다."),("moa","e16","제 팀이에요. 지금 이 순간 어디로 가는지가 중요하죠."),("sia","e09","제 지도랑 정말 같은 움직임이 나와요?")]),
 dict(key="03", fn="03_ai_lagrangian.html", n="③편 · 방 9~11", title="AI 속의 라그랑지안 — 울타리 있는 학습", rooms=ROOMS_C,
      card="SVM의 쌍대, 안전 강화학습의 λ, 언어모델 미세조정의 거리 벌점.", face=("sia","e19"),
      lead="조건을 지키며 배우는 모델은 모두 라그랑주 승수를 씁니다. 머신러닝 도감·신경망 도감과 이어 봅니다.",
      three=("SVM, 안전 강화학습, 언어모델 미세조정이 조건(울타리)을 λ로 다루는 방법을 봅니다.",
             "\"정확도만\"이 아니라 \"안전선·원래 모델과의 거리\"까지 지키는 학습이 늘고 있습니다.",
             "벌점 계수를 얼마로 둘지, 왜 학습 중에 바꾸는지 판단할 수 있습니다."),
      intro=[("doctor","e08","라그랑지안이 실제 모델 안에서 일하는 곳을 보자. 셋 다 울타리가 있다."),("sia","e19","라그랑지안 팀 출동이에요!"),("jupanbot","e16","울타리는 그냥 마지막에 잘라내면 되잖아요!")]),
 dict(key="04", fn="04_ai_hamiltonian.html", n="④편 · 방 12~14", title="AI 속의 해밀토니안 — 움직이는 학습", rooms=ROOMS_D,
      card="모멘텀 경사 하강, HMC에서 확산 모델까지, 역전파의 그림자 가격.", face=("moa","e10"),
      lead="기세(운동량)를 가진 학습, 에너지를 지키는 표본 뽑기, 거꾸로 흐르는 그림자 가격. 해밀토니안의 지도로 읽습니다.",
      three=("모멘텀 학습, HMC·확산 모델의 표본 뽑기, 역전파를 해밀토니안의 지도로 봅니다.",
             "딥러닝 학습과 그림 생성 모델의 핵심 계산이 이 지도 위에 있습니다.",
             "모멘텀 값, 걸음법(적분 방법)을 왜 그렇게 고르는지 이해합니다."),
      intro=[("doctor","e07","이번엔 움직이며 배우는 모델이다. 해밀토니안의 공이 그대로 들어 있다."),("moa","e10","해밀토니안 팀 차례예요!"),("jupanbot","e16","신경망에 물리가 왜 나와요?")]),
 dict(key="05", fn="05_economics.html", n="⑤편 · 방 15~18", title="경제학의 두 지도 — 한 장면 vs 끝없는 시간", rooms=ROOMS_E,
      card="솔로우 황금률·중첩세대(라그랑지안), 램지·투자 q 이론(해밀토니안).", face=("doctor","e08"),
      lead="한 장면·두 기간의 선택은 라그랑지안, 끝없이 이어지는 시간의 선택은 해밀토니안. 거시경제학 안에서도 두 지도가 나뉩니다.",
      three=("거시경제학의 성장·저축·투자 모형이 두 지도 중 어느 쪽으로 풀리는지 봅니다.",
             "λ(한 장면의 그림자 가격)와 μ·q(시간 위의 그림자 가격)가 AI의 그림자 가격과 같은 자리입니다.",
             "저축률·투자 판단을 그림자 가격으로 설명할 수 있습니다."),
      intro=[("doctor","e08","경제학도 같은 두 지도를 쓴다. 시점이 몇 개냐가 갈림길이다."),("sia","e01","한 장면이면 제 팀이죠?"),("moa","e09","끝없는 시간이면 제 팀이고요.")]),
 dict(key="06", fn="06_quantum.html", n="⑥편 · 방 19~21 (심화)", title="양자의 해밀토니안 — 연산자에서 최적화까지", rooms=ROOMS_F,
      card="연산자가 된 해밀토니안, 변분 원리, 양자 어닐링. 심화 편이라 교양 수업에서는 건너뛰어도 됩니다.", face=("haru","e09"),
      lead="해밀토니안이 가장 깊이 쓰이는 곳입니다. 심화 편이라 건너뛰어도 대결을 따라올 수 있습니다.",
      three=("양자 세계에서 해밀토니안이 \"정해진 에너지 계단\"을 만들고, 최적화 문제를 푸는 데 쓰이는 모습을 봅니다.",
             "양자 컴퓨터의 최적화(VQE·양자 어닐링)가 손실 줄이기와 같은 모양입니다.",
             "조합 최적화 문제를 \"에너지 바닥 찾기\"로 바꿔 보는 눈이 생깁니다."),
      intro=[("doctor","e08","심화 편이다. 해밀토니안이 숫자에서 연산자로 바뀐다."),("haru","e04","수식이 제일 많은 편이죠? 제가 대신 물어볼게요."),("moa","e16","해밀토니안 팀의 마지막 무대네요.")]),
 dict(key="07", fn="07_duel.html", n="⑦편 · 방 22 + 대결", title="같은 공, 두 지도 — 대결", rooms=ROOMS_G,
      card="두 지도를 배우는 신경망(HNN·LNN), 시아 vs 모아 세 판, 비교 카드로 정리.", face=("haru","e10"),
      lead="두 지도를 배우는 신경망을 보고, 시아(라그랑지안 팀)와 모아(해밀토니안 팀)가 세 판을 겨룹니다.",
      three=("HNN·LNN을 보고, 같은 문제를 두 지도로 풀어 겨룹니다.",
             "어느 지도가 \"더 낫다\"가 아니라 \"어디에 쓰나\"를 판단하는 눈이 결론입니다.",
             "문제를 만나면 조건이 중심인지(라그랑지안), 시간 흐름이 중심인지(해밀토니안)부터 봅니다."),
      intro=[("doctor","e08","마지막이다. 두 지도를 신경망이 배우는 방을 지나면 대결이다."),("sia","e19","드디어 대결이에요!"),("moa","e10","지는 쪽이 비교 카드 정리하기예요.")]),
]
ALL_ROOMS = [r for p in PARTS for r in p["rooms"]]
for p in PARTS:
    for r in p["rooms"]:
        r["page"] = p["fn"]

ABBR = [("라그랑지안 L", "움직임 에너지 − 높이 에너지(T − V). 최적화에서는 목표 − λ × 조건"),
        ("해밀토니안 H", "움직임 에너지 + 높이 에너지(T + V)"),
        ("작용 S", "길 위의 L을 모두 더한 점수"),
        ("λ(람다), 라그랑주 승수", "조건 하나의 값(그림자 가격)"),
        ("운동량 p", "질량 × 속도 (질량 = 물체가 가진 양, kg)"),
        ("위상 공간", "위치·운동량 두 축으로 된 지도"),
        ("르장드르 변환", "속도 축을 운동량 축으로 바꿔 그리는 식(H = p·v − L)"),
        ("공동상태변수 μ·q", "시간 위의 그림자 가격"),
        ("SVM·RLHF·HMC", "서포트 벡터 머신 · 사람 피드백 강화학습 · 해밀토니안 몬테카를로"),
        ("HNN·LNN", "해밀토니안 신경망 · 라그랑지안 신경망"),
        ("KL", "두 확률이 다른 정도. 거리처럼 쓰지만 방향이 있어 대칭은 아님"),
        ("기호 읽기", "각 방의 조수 상자 아래 「기호 읽기」에 그 방에 나온 기호의 읽는 법과 뜻이 있습니다. 예: ∂ 라운드 디(편미분), ∫ 인티그럴(모두 더하기), ∇ 나블라(오르막 화살표), λ 람다(그림자 가격)")]

def head(title, desc, og, path):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:type" content="article"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE}assets/og/{og}"><meta property="og:url" content="{SITE}{path}"><meta name="twitter:card" content="summary_large_image">
<meta name="author" content="안상선">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/lab.css">
</head>
<body>
<div id="prog"></div>
"""

def nav(links):
    a = "".join(f'<a href="{h}">{E(t)}</a>' for h, t in links)
    return f'<nav class="top"><div class="row"><a class="logo" href="index.html">두 장의 <i>지도</i></a><div class="links">{a}</div></div></nav>\n'

def cover(key, cap, cast):
    img = os.path.join(ROOT, "assets", "img", f"cover_{key}.webp")
    if os.path.exists(img):
        return f'<div class="cover"><div class="frame"><img class="art" src="assets/img/cover_{key}.webp" alt="{E(cap)}" width="1600" height="900"><span class="cap">{E(cap)}</span></div></div>\n'
    imgs = "".join(face(k, e, "s" if i in (0, len(cast) - 1) and len(cast) > 3 else "") for i, (k, e) in enumerate(cast))
    # 대체 표지: 왼쪽 안장 등고선(쌍곡선), 오른쪽 그릇 등고선(원)
    sad = "".join(f'<path d="M{430-60*k},{120} Q430,{450-0} {430-60*k},{780}" fill="none" stroke="#9fd3cf" stroke-width="3"/><path d="M{430+60*k},{120} Q430,450 {430+60*k},{780}" fill="none" stroke="#9fd3cf" stroke-width="3"/>' for k in (1, 2, 3, 4))
    bowl = "".join(f'<circle cx="1170" cy="450" r="{r}" fill="none" stroke="#f2b88a" stroke-width="3"/>' for r in (70, 140, 210, 280))
    deco = (sad + bowl + '<circle cx="1170" cy="450" r="140" fill="none" stroke="#0f8f84" stroke-width="7"/>'
            '<line x1="800" y1="60" x2="800" y2="840" stroke="#d5dbe2" stroke-width="3" stroke-dasharray="12 10"/>'
            '<text x="430" y="80" font-size="44" text-anchor="middle" fill="#0f8f84" font-weight="700" font-family="sans-serif">T − V</text>'
            '<text x="1170" y="80" font-size="44" text-anchor="middle" fill="#e8731a" font-weight="700" font-family="sans-serif">T + V</text>')
    return f"""<div class="cover"><div class="frame"><svg class="grid" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{deco}</svg>
<span class="cap">{E(cap)}</span><span class="badge">표지 그림 준비 중</span><div class="cast">{imgs}</div></div></div>\n"""

def three(what, why, work):
    dl = "".join(f"<dt>{E(a)}</dt><dd>{E(b)}</dd>" for a, b in ABBR)
    return f"""<div class="three"><h2>처음 오신 분께 — 이 페이지를 3줄로</h2><ul>
<li><b>무엇을</b>: {what}</li><li><b>왜 중요한가</b>: {why}</li><li><b>업무에서는</b>: {work}</li></ul>
<p>코드·수식을 몰라도 됩니다. 식은 조수 상자 안에만 있습니다.</p>
<details class="abbr"><summary>원어·약어 풀이 (펼치기)</summary><dl>{dl}</dl></details></div>\n"""

def talk(lines):
    out = []
    for k, e, t in lines:
        side = " r" if k == "moa" else ""
        out.append(f'<div class="line{side}">{face(k, e)}<div class="bub"><b style="color:var(--c-{COLV[k]})">{E(CH[k][0])}</b>{E(t)}</div></div>')
    return '<div class="talk">' + "".join(out) + "</div>"

def cast_section():
    items = "".join(f'<div class="who">{face(k, "e01" if k in ("sia","moa") else "e13")}<b>{E(CH[k][0])}</b><span>{E(CH[k][2])}</span></div>' for k in CH)
    return f'<section id="cast"><div class="wrap"><h2>등장인물</h2><p class="muted">본문에서는 시아·모아를 이름으로 부릅니다. 방청객 X1~X3은 이번 특집에서는 쉽니다.</p><div class="cast-grid">{items}</div></div></section>\n'

def quiz(q, opts, ans, ok, no):
    b = "".join(f'<button type="button">{E(o)}</button>' for o in opts)
    return f'<div class="quiz" data-ans="{ans}" data-ok="{E(ok)}" data-no="{E(no)}"><div class="qq">확인 퀴즈 — {E(q)}</div><div class="opts">{b}</div><div class="fb" aria-live="polite"></div></div>'

def panel_html(key, title, note, ctrl):
    return (f'<div class="panel"><div class="ph"><b>{E(title)}</b><small>{E(note)}</small></div>'
            f'<div id="pp-{key}" data-panel="{key}"></div><div class="ctrl">{ctrl}</div><div class="readout" aria-live="polite"></div></div>')

def scene(name, alt):
    if os.path.exists(os.path.join(ROOT, "assets", "img", name + ".webp")):
        return f'<figure class="fig scene"><img src="assets/img/{name}.webp" alt="{E(alt)}" width="1200" height="800" loading="lazy"></figure>'
    return ""

def compare_fig(cap="비교 카드 — 같은 용수철을 그린 두 장의 지도"):
    return (f'<figure class="fig"><img src="assets/fig/compare_card.svg" alt="라그랑지안 vs 해밀토니안 비교 카드" width="1080" height="1350" loading="lazy">'
            f'<figcaption>{E(cap)} · 형식 참고 matharium 「Lagrange Multipliers」 · 내용은 이 페이지에서 새로 씀</figcaption></figure>')

def room(r):
    labels = ["문제", "앞 방의 한계", "해법"]
    why = "".join(f"<li><b>{labels[i]}</b> — {E(x)}</li>" for i, x in enumerate(r["why"]))
    pcs = "".join(f"<tr><td class='m'>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in r["pieces"])
    tries = "".join(f"<li>{E(t)}</li>" for t in r["tries"])
    solve = "".join(f"<p>{E(s)}</p>" for s in r["solve"])
    code = ""
    if r.get("code"):
        code = f'<details class="code"><summary>파이썬 코드로 보면 (몰라도 됩니다)</summary><pre><code>{E(r["code"][0])}</code></pre><p>{E(r["code"][1])}</p></details>'
    links = ""
    if r.get("links"):
        links = '<div class="seealso"><b>이어서 보기</b> ' + " · ".join(f'<a href="{h}">{E(t)}</a>' for h, t in r["links"]) + "</div>"
    p = r["panel"]
    fig = compare_fig() if r["id"] == "r08b" else ""
    say = f'<p class="saywords"><b>말로 먼저</b> — {E(SAY[r["id"]])}</p>' if r["id"] in SAY else ""
    blob = " ".join(a + " " + b for a, b in r["pieces"]) + " " + " ".join(r["tries"])
    syms = [f"<span><b>{E(k)}</b> {E(v)}</span>" for k, v in SYM if k in blob]
    symread = f'<div class="symread"><b>기호 읽기</b>{"".join(syms)}</div>' if syms else ""
    tl = list(r["talk"])
    if r["id"] in DOC:
        if tl and tl[0][0] == "doctor":
            tl[0] = ("doctor", tl[0][1], DOC[r["id"]] + " " + tl[0][2])
        else:
            tl.insert(0, ("doctor", "e08", DOC[r["id"]]))
    aibox = ""
    if r["id"] in AI:
        a1, a2, a3 = AI[r["id"]]
        aibox = f'<div class="box aicheck"><h4>AI 판단 코너 — 그대로 믿어도 될까?</h4><p><b>AI의 답</b> {E(a1)}</p><p><b>확인할 질문</b> {E(a2)}</p><details><summary>확인 결과 보기</summary><p>{E(a3)}</p></details></div>' 
    q = r["quiz"]
    return f"""<section class="room" id="{r['id']}"><div class="wrap">
<div class="roomno">{r['no']}번 방</div>
<h2>{E(r['title'])}</h2><p class="muted">{E(r['sub'])}</p>
<div class="tags"><span class="tag src">{E(r['src'])}</span><span class="tag how">{E(r['how'])}</span><span class="tag day">{E(r['day'])}</span></div>
<div class="duo">
<div class="box why"><h4>왜 이 방법을 쓰나</h4><ol>{why}</ol><div class="easy"><b>쉽게 말하면</b> — {E(r['easy'])}</div></div>
<div class="box mathbox"><h4>수학 수식을 어려워하는 조수가 대신 물어봅니다</h4>
<div class="q">{face('haru','e04')}<div><b>조수</b> {E(r['haru_q'])}</div></div>
{say}
<p><b>학교 수학으로 보면</b> — {E(r['school'])}</p>
<div class="try"><b>숫자로 한 번 해 보기</b><ol class="steps">{tries}</ol></div>
<details class="formula"><summary>식으로 보면 (몰라도 됩니다) — 식 조각 {len(r['pieces'])}개와 기호 읽기</summary>
<table><thead><tr><th>식 조각</th><th>뜻</th></tr></thead><tbody>{pcs}</tbody></table>
{symread}</details>
<div class="q">{face('haru','e16')}<div><b>조수</b> {E(r['haru_c'])}</div></div></div>
</div>
<div class="pair"><div class="box"><h4>일상으로 치면</h4><p>{E(r['daily'])}</p></div><div class="box ml"><h4>AI에서는</h4><p>{E(r['ml'])}</p>{links}</div></div>
{fig}
{talk(tl)}
{panel_html(p['key'], f"실험 패널 {r['no']}", p['note'], p['ctrl'])}
<div class="solve"><h4>풀이</h4>{solve}</div>
{aibox}
<div class="limit"><b>이 방의 한계</b> — {E(r['limit'])}</div>
{code}
{quiz(q[0], q[1], q[2], q[3], q[4])}
</div></section>
"""

# ------------------------------------------------------------- 지식 색인
EN = {"r01": "Kinetic and potential energy", "r02": "Action (path score)", "r03": "Euler–Lagrange equation and Newton's law", "r04": "Lagrange multipliers",
      "r05": "Legendre transform: velocity to momentum", "r06": "Phase-space bowl (Hamiltonian)", "r07": "Hamilton's equations", "r08": "Taylor series: every minimum is a spring",
      "r08b": "Lagrangian vs Hamiltonian side by side", "r09": "SVM dual problem", "r10": "Lagrangian safe reinforcement learning", "r11": "KL-regularized RLHF",
      "r12": "Momentum gradient descent", "r13": "HMC, Langevin and diffusion sampling", "r14": "Backpropagation as costate (adjoint)", "r15": "Solow golden rule",
      "r16": "Overlapping generations (Diamond)", "r17": "Ramsey model and current-value Hamiltonian", "r18": "Tobin's q theory of investment", "r19": "Hamiltonian operator and energy levels",
      "r20": "Variational principle and VQE", "r21": "Quantum annealing and Ising Hamiltonian", "r22": "Hamiltonian and Lagrangian neural networks"}
TYPE_OF = {9: "Application", 10: "Application", 11: "Application", 12: "Application", 13: "Application", 14: "Application",
           15: "Application", 16: "Application", 17: "Application", 18: "Application", 21: "Application", 22: "Application"}
def kg_block(pagekey, rooms):
    nodes = []
    for r in rooms:
        t = TYPE_OF.get(r["no"], "Concept") if isinstance(r["no"], int) else "Concept"
        nodes.append(dict(id="lab:room/" + r["id"], type=t, label=dict(ko=r["title"], en=EN.get(r["id"], r["id"])), anchor="#" + r["id"],
                          desc=r["sub"], page=r["page"][:-5], source="lab:work/lagrangian_hamiltonian_lab"))
    nodes.append(dict(id="lab:concept/lagrangian", type="Concept", label=dict(ko="라그랑지안(T − V)", en="Lagrangian"), anchor="#r02", desc="길 전체에 점수를 매기는 지도", page="01_lagrangian", source="lab:work/lagrangian_hamiltonian_lab"))
    nodes.append(dict(id="lab:concept/hamiltonian", type="Concept", label=dict(ko="해밀토니안(T + V)", en="Hamiltonian"), anchor="#r06", desc="지금 이 순간의 화살표를 보는 지도", page="02_hamiltonian", source="lab:work/lagrangian_hamiltonian_lab"))
    ids = [n["id"] for n in nodes if n["id"].startswith("lab:room/")]
    edges = [dict(s=ids[i], p="motivates", o=ids[i + 1]) for i in range(len(ids) - 1)]
    L = {"r02","r03","r04","r09","r10","r11","r15","r16"}; Hs = {"r06","r07","r12","r13","r14","r17","r18","r19","r20","r21"}
    for n in nodes:
        rid = n["id"].split("/")[-1]
        if rid in L: edges.append(dict(s="lab:concept/lagrangian", p="usedIn", o=n["id"]))
        if rid in Hs: edges.append(dict(s="lab:concept/hamiltonian", p="usedIn", o=n["id"]))
    edges.append(dict(s="lab:concept/lagrangian", p="relatedTo", o="lab:concept/hamiltonian"))
    raw = dict(version="1.3", page=pagekey, series="두 장의 지도", nodes=nodes, edges=edges)
    ld = {"@context": {"@vocab": "urn:lab:", "skos": "http://www.w3.org/2004/02/skos/core#", "schema": "https://schema.org/"},
          "@graph": [{"@id": "urn:" + n["id"], "@type": n["type"], "skos:prefLabel": [{"@value": n["label"]["ko"], "@language": "ko"}, {"@value": n["label"]["en"], "@language": "en"}],
                      "skos:definition": n["desc"], "schema:url": SITE + n["page"] + ".html" + n["anchor"]} for n in nodes]}
    refs = [dict(id="askwhyvalley_hamiltonian", type="graphic", title="The Hamiltonian Operator (infographic)", author=[dict(literal="@askwhyvalley")], accessed={"date-parts": [[2026, 11, 19]]}, note="사용자 제공 이미지. 다시 그려 실험 패널로 바꿈"),
            dict(id="askwhyvalley_taylor", type="graphic", title="Taylor Series (infographic)", author=[dict(literal="@askwhyvalley")], accessed={"date-parts": [[2026, 11, 19]]}),
            dict(id="matharium_lagrange", type="graphic", title="Lagrange Multipliers (infographic)", author=[dict(literal="matharium")], accessed={"date-parts": [[2026, 11, 19]]}),
            dict(id="greydanus2019", type="paper-conference", title="Hamiltonian Neural Networks", author=[dict(family="Greydanus"), dict(family="Dzamba"), dict(family="Yosinski")], issued={"date-parts": [[2019]]}, **{"container-title": "NeurIPS"}),
            dict(id="cranmer2020", type="article", title="Lagrangian Neural Networks", author=[dict(family="Cranmer")], issued={"date-parts": [[2020]]}),
            dict(id="chen2018", type="paper-conference", title="Neural Ordinary Differential Equations", author=[dict(family="Chen")], issued={"date-parts": [[2018]]}, **{"container-title": "NeurIPS"}),
            dict(id="su2014", type="paper-conference", title="A Differential Equation for Modeling Nesterov's Accelerated Gradient Method", author=[dict(family="Su"), dict(family="Boyd"), dict(family="Candès")], issued={"date-parts": [[2014]]}),
            dict(id="ramsauer2020", type="article", title="Hopfield Networks is All You Need", author=[dict(family="Ramsauer")], issued={"date-parts": [[2020]]}),
            dict(id="romer_am", type="book", title="Advanced Macroeconomics", author=[dict(family="Romer", given="David")], publisher="McGraw-Hill")]
    meta = dict(title=pagekey, series="두 장의 지도", creator=[dict(name="안상선", role="author", affiliation="(주)M-Robo")], date=DATE, version=VER, license="캐릭터·그림 무단 사용 금지")
    J = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    return f"""<section id="kg"><div class="wrap"><h2>지식 색인 — 이 페이지에서 찾아보기</h2>
<p class="muted">이 페이지에 나온 방과 개념을 모았습니다. 검색하고, "설명 보러 가기"로 본문에 돌아갑니다.</p><div id="kg-mount"></div></div></section>
<section id="export"><div class="wrap"><h2>온톨로지·서지 꾸러미 — 이 페이지의 지식을 가져가기</h2>
<p class="muted">지식 색인을 출처와 함께 파일로 내려받습니다. Zotero(BibTeX·RIS), Protégé(Turtle), Neo4j·Gephi(CSV), 여러 페이지 합치기(kg.json)에 씁니다.</p><div id="export-mount"></div></div></section>
<script type="application/json" id="kg-raw">{J(raw)}</script>
<script type="application/ld+json" id="kg-ld">{J(ld)}</script>
<script type="application/json" id="refs-csl">{J(refs)}</script>
<script type="application/json" id="page-meta">{J(meta)}</script>
"""

def footer():
    links = " · ".join(f'<a href="{p["fn"]}">{E(p["n"].split(" · ")[0])}</a>' for p in PARTS)
    return f"""<footer><div class="wrap">
<h3>출처</h3>
<div class="tbl"><table><thead><tr><th>#</th><th>자료</th><th>이 페이지에서 쓴 곳</th></tr></thead><tbody>
<tr><td>[1]</td><td>@askwhyvalley, 인포그래픽 「The Hamiltonian Operator」 (사용자 제공 이미지, 2026-11-19 확인)</td><td>방 5~7, 19~20. 식을 다시 써서 실험 패널로 바꿈. 이미지는 붙여 넣지 않음</td></tr>
<tr><td>[2]</td><td>@askwhyvalley, 인포그래픽 「Taylor Series」 (사용자 제공 이미지)</td><td>방 8</td></tr>
<tr><td>[3]</td><td>matharium, 인포그래픽 「Lagrange Multipliers」 (사용자 제공 이미지)</td><td>방 4, 비교 카드의 형식</td></tr>
<tr><td>[4]</td><td>Greydanus 외(2019) 「Hamiltonian Neural Networks」, Cranmer 외(2020) 「Lagrangian Neural Networks」, Chen 외(2018) 「Neural Ordinary Differential Equations」, Su·Boyd·Candès(2014), Ramsauer 외(2020) 「Hopfield Networks is All You Need」</td><td>방 12·14·21·22에서 이름·연도·한 줄 사실만 소개</td></tr>
<tr><td>[5]</td><td>D. Romer, 「Advanced Macroeconomics」 — 램지·중첩세대·투자 장의 풀이 방식</td><td>방 15~18에서 풀이 방식 소개(주장하지 않음)</td></tr>
</tbody></table></div>
<h3>원자료와 다르게 쓴 곳</h3>
<p>원자료 ② e^x 예시의 2차 꼬리표 \"1 + x x x²/2\"를 이 페이지에서는 1 + x + x²/2로, sin x 예시의 3차 꼬리표 \"x − x²/6\"을 x − x³/6으로 바꿉니다. 원자료 ① 기호 상자의 \"Hamiltonion\"은 Hamiltonian으로 고칩니다. 원자료 ③ 예시에는 λ 값이 빠져 있어 λ = √2/2를 더해 적습니다.</p>
<h3>예시값·설명용 숫자</h3>
<p>배달 로봇의 속도·위험, 답 A·B의 확률, SVM의 점 4개, 임금·이자·케이크·저축률 수치는 설명을 위해 만든 예시값입니다. 모든 \"숫자로 한 번 해 보기\"는 build/check_numbers.py로 검산했습니다.</p>
<p>캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다. 캐릭터 그림: fruitfly-lab-expressions.</p>
<p>글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p>
<p><a href="index.html">목차</a> · {links} · <a href="{REPO}">저장소</a></p>
</div></footer>
<script src="assets/panels.js"></script>
</body></html>
"""

def ladder():
    cells = "".join(f'<a href="{r["page"]}#{r["id"]}"><b>{r["no"]}번 방</b>{E(r["title"])}</a>' for r in ALL_ROOMS)
    return '<div class="ladder">' + cells + "</div>"

def part_cards():
    out = []
    for p in PARTS:
        out.append(f'<a class="card" href="{p["fn"]}">{face(*p["face"])}<span class="n">{E(p["n"])}</span><h3>{E(p["title"])}</h3><p>{E(p["card"])}</p></a>')
    return '<div class="cards">' + "".join(out) + "</div>"

# ------------------------------------------------------------- index
def build_index():
    t = "두 장의 지도 — 라그랑지안 vs 해밀토니안"
    d = "같은 움직임을 빼서(T − V) 그리면 라그랑지안, 더해서(T + V) 그리면 해밀토니안. AI 모델·경제학·양자까지 두 지도의 쓰임을 연구실 해설로 봅니다."
    s = head(t, d, "og_index.jpg", "index.html")
    s += nav([("#parts", "편 목록"), ("#class", "수업에 쓰실 때"), ("#card", "한 장으로 보기"), ("#map", "큰 그림"), ("#cast", "등장인물"), ("#source", "원자료")])
    s += cover("index", "책상 위에 펼친 지도 두 장", [("sia","e19"),("doctor","e08"),("moa","e16"),("haru","e01")])
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">좌표축 위의 그릇 · 특집</span>
<h1>두 장의 지도<br><span style="font-size:.55em;color:var(--muted)">라그랑지안 vs 해밀토니안</span></h1>
<p class="lead">공 하나의 움직임을 <b>빼서(T − V)</b> 그리면 라그랑지안, <b>더해서(T + V)</b> 그리면 해밀토니안입니다. 앞의 지도는 길 전체를 보고, 뒤의 지도는 지금 이 순간의 화살표를 봅니다. 모델 학습, 경제의 선택, 양자 컴퓨터의 최적화가 모두 이 두 지도 위에서 움직입니다.</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section><div class="wrap">{three("움직이는 것의 에너지를 \"빼서\" 그리는 지도와 \"더해서\" 그리는 지도를 비교합니다.", "울타리(조건) 있는 학습은 앞의 지도, 움직이며 배우는 학습·표본 뽑기는 뒤의 지도가 강합니다.", "예산 안의 최적 배분, 안전선 지키며 학습하기, 모멘텀 값 고르기에 바로 쓰입니다.")}</div></section>
<section id="parts"><div class="wrap"><h2>편 목록</h2>
<p class="muted">빠른 길: 0편 → 방 1~3 → 방 6~7 → ③·④편(AI) → 대결. 양자 편(⑥)은 심화라 건너뛰어도 됩니다.</p>
{part_cards()}</div></section>
<section id="class"><div class="wrap"><h2>수업에 쓰실 때</h2>
<div class="tbl"><table><thead><tr><th>차시(90분)</th><th>편</th><th>꼭 할 실험</th></tr></thead><tbody>
<tr><td>1차시</td><td>0편 · ①편 · ②편</td><td>방 3 공 던지기, 방 7 도는 화살표, 방 8-1 두 지도 나란히</td></tr>
<tr><td>2차시</td><td>③편 · ④편 (AI)</td><td>방 10 안전선 λ, 방 12 모멘텀 세 버튼, 방 13 걸음법</td></tr>
<tr><td>3차시</td><td>⑤편 · ⑦편 대결</td><td>방 15 황금률, 방 17 케이크, 대결 세 판 + 비교 총정리</td></tr>
</tbody></table></div>
<p class="muted">⑥편 양자는 자습·심화용입니다. 시간이 모자라면 빠른 길(0편 → 방 1~3 → 방 6~7 → ③·④편 → 대결)만으로도 결론까지 갑니다. 모든 퀴즈는 페이지 안에서 바로 채점되고 저장하지 않습니다.</p></div></section>
<section id="card"><div class="wrap"><h2>한 장으로 먼저 보기</h2>
<p class="muted">같은 용수철이 왼쪽 지도에서는 안장, 오른쪽 지도에서는 그릇이 됩니다. 자세한 설명은 <a href="02_hamiltonian.html#r08b">8-1번 방</a>에 있습니다.</p>
{compare_fig()}</div></section>
<section id="map"><div class="wrap"><h2>큰 그림 — 앞 방의 한계가 다음 방의 이유</h2>{ladder()}</div></section>
{cast_section()}
<section id="source"><div class="wrap"><h2>원자료와 이 해설</h2>
<p>원자료는 인포그래픽 세 장입니다. @askwhyvalley의 「The Hamiltonian Operator」·「Taylor Series」, matharium의 「Lagrange Multipliers」입니다. 식을 다시 쓰고 직접 움직이는 실험 패널로 바꿨습니다.</p>
<p>AI 쪽은 이 시리즈의 도감과 이어집니다: <a href="{ML_ATLAS}">머신러닝 모델 도감</a> · <a href="{ML_3D}">머신러닝 연구소(3D)</a> · <a href="{NN_ATLAS0}">신경망 도감</a> · <a href="{NN_3D}">신경망 연구소(3D)</a> · <a href="{BACKPROP}">역전파 연구실</a></p>
<p>좌표축 위의 그릇 시리즈를 먼저 보면 좋습니다: <a href="{BOWL}">좌표축 위의 그릇 — 3D 지도로 본 모델 최적화</a> · ∇ 특별편 <a href="{NABLA}">vector_calculus_lab</a></p></div></section>
"""
    s += kg_block("index", ALL_ROOMS)
    s += footer()
    open(os.path.join(ROOT, "index.html"), "w").write(s)

# ------------------------------------------------------------- 0편
def build_orient():
    p = PARTS[0]
    t = "두 장의 지도 0편 — 가방 점검 (오리엔테이션)"
    d = "그릇·오르막 화살표·굽음을 실험 3개로 짧게 복습합니다. 건너뛰어도 됩니다."
    s = head(t, d, "og_00.jpg", p["fn"])
    s += nav([("#bag1", "그릇과 기울기"), ("#bag2", "오르막 화살표"), ("#bag3", "굽음"), ("#check", "확인"), ("01_lagrangian.html", "①편으로")])
    s += cover("00", "연구실 책상 · 가방 점검", [("sia","e13"),("doctor","e08"),("moa","e09")])
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">0편 · 오리엔테이션</span><h1>가방 점검</h1>
<p class="lead">지도를 펼치기 전, 박사가 시아·모아의 가방을 엽니다. 꺼낸 물건은 세 개 — 모두 그릇 시리즈에서 쓴 것입니다.</p>
<p>좌표축 위의 그릇 시리즈를 먼저 보고 오시면 좋습니다. 처음이라면 이 쪽만 읽어도 따라올 수 있습니다.</p>
<a class="skip" href="01_lagrangian.html#r01">건너뛰고 바로 1번 방으로 →</a>
<p class="byline" style="margin-top:12px">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section><div class="wrap">{talk([("doctor","e08","지도 두 장을 펼치기 전에 가방부터 보자. 그릇, 화살표, 그리고 굽음."),("sia","e01","그릇 시리즈에서 본 것들이네요!"),("moa","e09","그걸로 물리랑 AI를 다 설명할 수 있어요?"),("doctor","e16","충분하다. 하나씩 꺼내 보자.")])}</div></section>
"""
    bags = [
     ("bag1", "가방 속 ① 그릇과 기울기", ["오차 그릇 y = x² 위의 점마다 기울기(미분)가 있습니다.", "기울기가 양수면 오른쪽이 오르막, 음수면 왼쪽이 오르막입니다.", "경사 하강은 기울기 반대쪽으로 한 걸음씩 내려갑니다."],
      "o1", "점의 위치 x를 바꿔 보세요", '<label>x <input type="range" min="-2" max="2" step="0.25" value="1" aria-label="위치"></label>', f'<a href="{BOWL}first_step_1.html">최적화 첫걸음 — 미분 좋아하세요</a>'),
     ("bag2", "가방 속 ② 등고선과 오르막 화살표", ["높이가 같은 곳을 이은 선이 등고선입니다.", "오르막 화살표(그래디언트)는 늘 등고선과 직각입니다.", "7번 방의 \"직각으로 도는 화살표\"가 여기서 나옵니다."],
      "o2", "점을 끌어 보세요", "", f'<a href="{BOWL}3_arrow_field.html">좌표축 위의 그릇 3편 — 화살표 밭</a>'),
     ("bag3", "가방 속 ③ 바닥의 굽음", ["같은 그릇이라도 바닥이 뾰족하거나 넓적할 수 있습니다.", "굽음은 두 번 미분한 값(헤시안)으로 잽니다. y = a·x²이면 2a입니다.", "8번 방 테일러 급수의 \"2번째 항\"이 바로 이 굽음입니다."],
      "o3", "굽음 a를 바꿔 보세요", '<label>a <input type="range" min="0.25" max="2" step="0.25" value="1" aria-label="굽음"></label>', f'<a href="{BOWL}1_math_map.html">좌표축 위의 그릇 1편 — 수학 편</a>'),
    ]
    for bid, title, lines, key, note, ctrl, link in bags:
        li = "".join(f"<li>{E(x)}</li>" for x in lines)
        s += f"""<section class="room" id="{bid}"><div class="wrap"><h2>{E(title)}</h2>
<div class="box"><h4>요약 3줄</h4><ol>{li}</ol></div>
{panel_html(key, "실험", note, ctrl)}
<p class="muted">더 보기: {link}</p></div></section>
"""
    qs = [("y = x²에서 x = 1일 때 기울기는?", ["1", "2", "0"], 1, "2x = 2입니다.", "실험 ①에서 x = 1로 놓아 보세요."),
          ("오르막 화살표와 등고선의 각도는?", ["나란하다", "직각이다", "45도"], 1, "늘 직각입니다.", "실험 ②에서 점을 옮겨 보세요."),
          ("y = 2x²의 굽음(두 번 미분)은?", ["2", "4", "1"], 1, "2a = 4입니다.", "y = a·x²이면 굽음은 2a입니다.")]
    qh = "".join(quiz(q[0], q[1], q[2], q[3], q[4]) for q in qs)
    s += f"""<section id="check"><div class="wrap"><h2>가방 확인 퀴즈 3문항</h2>{qh}
<p id="gate" class="readout">세 문제를 모두 맞히면 1번 방 문이 열립니다.</p>
<div class="next"><span></span><a href="01_lagrangian.html#r01">①편 1번 방으로 →</a></div></div></section>
<script>(function(){{var g=document.getElementById('gate');var qs=document.querySelectorAll('#check .quiz');function chk(){{var n=0;qs.forEach(function(q){{if(q.querySelector('button.ok'))n++;}});if(n===qs.length){{g.innerHTML='<span class=\\"alert\\">🔓 1번 방 문이 열렸습니다!</span> <a href=\\"01_lagrangian.html#r01\\">들어가기 →</a>';}}else{{g.textContent='맞힌 문제 '+n+'/'+qs.length+' — 세 문제를 모두 맞히면 1번 방 문이 열립니다.';}}}}qs.forEach(function(q){{q.addEventListener('click',function(){{setTimeout(chk,0);}});}});}})();</script>
"""
    s += kg_block("00_orientation", [])
    s += footer()
    open(os.path.join(ROOT, p["fn"]), "w").write(s)

# ------------------------------------------------------------- 대결
def duel_section():
    return f"""<section class="room" id="duel"><div class="wrap"><div class="roomno">대결</div><h2>같은 공, 두 지도</h2>
<p class="muted">심판: 조수 하루 · 시아(라그랑지안 팀) vs 모아(해밀토니안 팀) · 세 판</p>
{scene("duel", "대결 장면 — 시아와 모아, 심판 하루")}
{talk([("haru","e07","세 판입니다! 같은 문제를 각자의 지도로 풀어 주세요."),
       ("sia","e19","길 전체를 보는 제 지도가 이길 거예요!"),
       ("moa","e10","지금 이 순간을 보는 제 지도도 만만치 않아요."),
       ("jupanbot","e16","더하기가 빼기보다 크니까 해밀토니안이 무조건 이기죠!"),
       ("fruitfly","e09","정말? 한 판씩 열어 봐.")])}
{panel_html("duel", "대결 패널", "판을 차례로 열어 보세요", '<button type="button" data-round="1">1판 열기</button><button type="button" data-round="2">2판 열기</button><button type="button" data-round="3">3판 열기</button>')}
<div class="solve"><h4>심판 판정</h4>
<p>1판 용수철 궤적 예측: 시아는 점수가 멈추는 길(3번 방), 모아는 해밀턴 화살표(7번 방)로 풀었습니다. 둘 다 위치 = cos t로 같은 답입니다. 무승부.</p>
<p>2판 황금률(15번 방): \"소비 + 유지비 = 생산\" 울타리 하나에 λ만 붙이면 끝납니다. 시아가 한 줄로 저축률 1/3을 냈습니다. 시아 승.</p>
<p>3판 1,000걸음 시뮬레이션에서 에너지 지키기(13번 방): 모아는 해밀턴 식을 리프프로그로 걸어 에너지를 지켰고, 시아는 같은 걸음 수를 단순 오일러 계산으로 걸어 에너지가 크게 불었습니다. 모아 승.</p>
<p class="hint">📝 심판 덧붙임 — 3판의 차이는 지도 탓이 아니라 걸음법 탓입니다. 라그랑지안 쪽에도 에너지를 잘 지키는 걸음법(변분 적분법)이 있습니다. 이번 판은 "오일러 vs 리프프로그" 승부였습니다.</p></div>
{talk([("haru","e10","판정! 1승 1패 1무, 무승부입니다."),("doctor","e16","지도가 틀린 게 아니라 쓰임새가 다르다. 조건이 중심이면 라그랑지안, 시간 흐름이 중심이면 해밀토니안."),("sia","e01","다음엔 문제부터 보고 지도를 고를게요."),("moa","e16","저도요. 둘 다 들고 다녀야겠어요."),("jupanbot","e14","더하기가 무조건 이기는 게 아니었군요…")])}
</div></section>
"""

COMPARE_ROWS = [("식", "T − V (차이)", "T + V (합)"), ("쓰는 축", "위치·속도", "위치·운동량"), ("보는 방식", "길 전체의 점수(작용)", "지금 이 순간의 화살표"),
 ("식 모양", "2차 미분방정식 n개", "1차 미분방정식 2n개"), ("잘하는 일", "조건 넣기, 좌표 바꾸기, 대칭 찾기", "에너지 지키기, 긴 시뮬레이션, 양자역학"),
 ("머신러닝", "SVM 쌍대, 안전 강화학습의 λ, RLHF 거리 벌점, LNN", "모멘텀, HMC·확산 모델, 역전파의 그림자 가격, HNN"),
 ("경제학", "솔로우 황금률·중첩세대, λ", "램지·투자 q 이론, μ·q"), ("양자", "경로적분(파인먼) — 모든 길의 작용을 더한다", "연산자·변분 원리·양자 어닐링")]

def summary_section():
    rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in COMPARE_ROWS)
    return f"""<section id="sum"><div class="wrap"><h2>비교 총정리</h2>
<div class="tbl"><table><thead><tr><th></th><th style="color:var(--teal)">라그랑지안 (시아 팀)</th><th style="color:var(--orange)">해밀토니안 (모아 팀)</th></tr></thead><tbody>{rows}</tbody></table></div>
{compare_fig("아웃트로 — 두 지도를 한 장에")}</div></section>
<section id="outro"><div class="wrap"><h2>아웃트로</h2>
{scene("outro", "아웃트로 — 두 지도를 함께 든 시아와 모아")}
{talk([("doctor","e08","두 지도는 같은 세상을 그린다. 문제에 맞는 지도를 고르는 게 실력이다."),("haru","e16","오늘 숫자는 전부 검산 완료입니다!"),("sia","e19","그릇 시리즈로 돌아가면 이제 그릇이 다르게 보일 것 같아요."),("moa","e16","다음 특집도 기대할게요.")])}
<div class="next"><a href="index.html">목차로</a><a href="{BOWL}">좌표축 위의 그릇으로 →</a></div></div></section>
"""

def build_part(i):
    p = PARTS[i]
    rooms = p["rooms"]
    t = f"두 장의 지도 {p['n'].split(' · ')[0]} — {p['title']}"
    d = p["three"][0]
    s = head(t, d, f"og_{p['key']}.jpg", p["fn"])
    navl = [(f"#{r['id']}", f"{r['no']}번 방") for r in rooms]
    if p["key"] == "07": navl += [("#duel", "대결"), ("#sum", "총정리")]
    s += nav(navl)
    s += cover(p["key"], f"{p['n']}", [p["face"], ("doctor","e08"), ("haru","e09")])
    s += f"""<header class="hero"><div class="wrap"><span class="kicker">{E(p['n'])}</span><h1>{E(p['title'])}</h1><p class="lead">{p['lead']}</p>
<p class="byline">글 · 안상선 ((주)M-Robo 대표) · <a href="{AUTHOR_URL}">저자 소개</a> · {DATE} · {VER}</p></div></header>
<section><div class="wrap">{three(*p['three'])}</div></section>
<section><div class="wrap">{talk(p['intro'])}</div></section>
"""
    if i == 1:
        s += cast_section()
        s += '<section><div class="wrap"><p class="muted">아직 준비가 안 됐다면 <a href="00_orientation.html">0편 가방 점검</a>을 먼저 보세요(3분).</p></div></section>'
    for r in rooms:
        s += room(r)
    if p["key"] == "07":
        s += duel_section() + summary_section()
    else:
        prev = PARTS[i - 1]; nxt = PARTS[i + 1]
        s += f'<section><div class="wrap"><div class="next"><a href="{prev["fn"]}">← {E(prev["n"].split(" · ")[0])}</a><a href="{nxt["fn"]}">{E(nxt["n"].split(" · ")[0])} {E(nxt["title"])} →</a></div></div></section>'
    s += kg_block(p["fn"][:-5], rooms)
    s += footer()
    open(os.path.join(ROOT, p["fn"]), "w").write(s)

def build_js():
    b = os.path.dirname(os.path.abspath(__file__))
    js = open(os.path.join(b, "js_head.js")).read() + open(os.path.join(b, "panels_src.js")).read() + open(os.path.join(b, "js_tail.js")).read()
    js = js.replace("자와 각도기의 방 — 실험 패널 모음. 원자료 @eeanimation 「EUCLIDEAN SPACE 01~10」의 차트를 다시 그려 손으로 움직이게 만든 것",
                    "두 장의 지도 — 실험 패널 모음. 원자료 @askwhyvalley·matharium 인포그래픽을 다시 그려 손으로 움직이게 만든 것")
    js = js.replace("['teal','orange','navy','blue','green','red'].forEach", "['teal','orange','navy','blue','green','red','gray'].forEach")
    js = js.replace("red:'#c9302c',", "red:'#c9302c',gray:'#8a96a3',", 1)
    js = js.replace("개념 찾기 (예: 거리, 그림자, 칸막이)", "개념 찾기 (예: 그릇, 운동량, 그림자 가격)")
    open(os.path.join(ROOT, "assets", "panels.js"), "w").write(js)

if __name__ == "__main__":
    build_js(); build_index(); build_orient()
    for i in range(1, len(PARTS)): build_part(i)
    print("built", len(ALL_ROOMS), "rooms")
