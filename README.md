# 두 장의 지도 — 라그랑지안 vs 해밀토니안

공 하나의 움직임을 **빼서(T − V)** 그리면 라그랑지안, **더해서(T + V)** 그리면 해밀토니안입니다.
앞의 지도는 길 전체를 보고, 뒤의 지도는 지금 이 순간의 화살표를 봅니다. AI 모델·경제학·양자에서 두 지도가 어디에 쓰이는지 연구실 해설(비전공자판)로 봅니다.

- 공개 주소: https://adminmrobo.github.io/lagrangian_hamiltonian_lab/
- 소속: 「좌표축 위의 그릇」 시리즈 특집 ([optimization_3d_map](https://adminmrobo.github.io/optimization_3d_map/))
- 글 · 안상선 ((주)M-Robo 대표) · [저자 소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)

## 편 구성
| 파일 | 편 | 방 |
|---|---|---|
| `index.html` | 목차 · 비교 카드 한 장 | — |
| `00_orientation.html` | 0편 가방 점검 | 그릇·오르막 화살표·굽음 복습 + 퀴즈 3문항 |
| `01_lagrangian.html` | ①편 차이의 지도 — 라그랑지안 | 1 두 에너지 · 2 작용 · 3 뉴턴 법칙 · 4 라그랑주 승수 |
| `02_hamiltonian.html` | ②편 합의 지도 — 해밀토니안 | 5 지도 바꿔 그리기 · 6 위상 공간의 그릇 · 7 해밀턴 식 · 8 테일러 · 8-1 두 지도 나란히 |
| `03_ai_lagrangian.html` | ③편 AI 속의 라그랑지안 | 9 SVM 쌍대 · 10 안전 강화학습 λ · 11 RLHF 거리 벌점 |
| `04_ai_hamiltonian.html` | ④편 AI 속의 해밀토니안 | 12 모멘텀 · 13 HMC·랑주뱅·확산 · 14 역전파의 그림자 가격 |
| `05_economics.html` | ⑤편 경제학의 두 지도 | 15 솔로우 황금률 · 16 중첩세대 · 17 램지 · 18 투자 q 이론 |
| `06_quantum.html` | ⑥편 양자 (심화) | 19 연산자 · 20 변분 원리 · 21 양자 어닐링 |
| `07_duel.html` | ⑦편 대결 | 22 HNN·LNN · 대결 「같은 공, 두 지도」(무승부) · 비교 총정리 |

빠른 길: 0편 → 방 1~3 → 방 6~7 → ③·④편 → 대결.

## 연결한 도감·연구실
[머신러닝 모델 도감](https://adminmrobo.github.io/machine_learning_model_atlas/) (방 9 SVM) · [머신러닝 연구소 3D](https://adminmrobo.github.io/machine_learning_in_3d/) ·
[신경망 도감](https://adminmrobo.github.io/neural_network_atlas/0_neural_network_essence.html) (방 11 트랜스포머, 13 확산, 14·22 Neural ODE, 21 홉필드·볼츠만) · [신경망 연구소 3D](https://adminmrobo.github.io/ai_in_3d/) ·
[역전파 연구실](https://adminmrobo.github.io/backprop_lab/) (방 14) · [확률 분포 도감](https://adminmrobo.github.io/probability_distribution_dictionary/) (방 13)

## 폴더
```
assets/lab.css        낮의 연구실(흰 배경) 디자인
assets/panels.js      실험 패널 27개, 퀴즈, 지식 색인·꾸러미 (build/build.py가 만듦)
assets/fig/           비교 카드 SVG (build/make_card.py)
assets/img/           젠스파크 표지·장면 그림 자리 (docs/IMAGE_PROMPTS.md)
assets/chars/         캐릭터 표정 WebP (fruitfly-lab-expressions)
assets/og/            공유 미리보기 1200×630
build/                문구(content_a·b·c.py) → 페이지(build.py), 패널(panels_src.js), 검산(check_numbers.py), og(make_og.py)
docs/                 그림 요청 목록, 공간 좌표 해설 제작 지침서
```

다시 만들기: `python3 build/make_og.py && python3 build/build.py` · 검산: `python3 build/check_numbers.py`

## 원자료와 다르게 쓴 곳
1. @askwhyvalley 「Taylor Series」 — e^x 2차 꼬리표 "1 + x x x²/2" → 1 + x + x²/2, sin x 3차 꼬리표 "x − x²/6" → x − x³/6
2. @askwhyvalley 「The Hamiltonian Operator」 — 기호 상자 "Hamiltonion" → Hamiltonian
3. matharium 「Lagrange Multipliers」 — 예시에 λ = √2/2를 더해 적음

## 남은 일
- 표지·장면 그림 11장(젠스파크) — `docs/IMAGE_PROMPTS.md`
- 번역(언어팩), ahnboat_lab_cover_status 명부 등록, 페르소나 평가

캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다.
