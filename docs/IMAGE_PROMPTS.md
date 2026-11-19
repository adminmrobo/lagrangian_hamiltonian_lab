# Genspark 그림 지시문 — 두 장의 지도 (픽셀풍, v2)

> v1(2026-11-19)은 "cute anime style"로 써서 시리즈 화풍 지침(16비트 RPG 픽셀풍)을 어겼습니다. v2에서 바로잡습니다.
> 지금 저장소에 들어 있는 그림 11장(v1로 받은 것)은 v2로 다시 받아 같은 이름으로 덮어씁니다.

## 공통 규칙 (최적화 첫걸음 지시문과 같은 규칙)
- **참고 이미지:** fruitfly-lab-expressions의 캐릭터 그림만 첨부합니다(꾸러미 `ref/`). v1 그림은 참고로 올리지 않습니다(애니풍이 옮겨 붙음).
- **화풍:** 참고 그림과 똑같이 — 참고 그림이 없으면 16비트 RPG 픽셀 아트, 굵은 어두운 외곽선, 2~3단 음영, 작은 하이라이트. 밝은 낮 연구실, 흰 벽.
- **글자 금지:** 그림 안에 글자·숫자·기호를 넣지 않습니다("T − V", "T + V"도 넣지 않음). 지도 이름·편 이름은 HTML이 얹습니다.
- **안전 영역:** 얼굴·손은 가운데(좌우 12%, 위 10%, 아래 18% 여백) 안. 왼쪽 아래 모서리는 비워 둡니다(표지 꼬리표 자리).
- **색:** 라그랑지안 쪽 틸(#0f8f84), 해밀토니안 쪽 주황(#e8731a), 남색 포인트.
- **파일:** 표지 16:9(1600×900), 장면 3:2(1200×800), WebP → `assets/img/`에 같은 이름으로 → `python3 build/make_og.py && python3 build/build.py`.

## 캐릭터 묘사 줄 (프롬프트의 대문자 이름 자리에 그대로 넣음)
- SIA: `a calm girl intern with long straight jet-black hair, charcoal-black maid dress with large gray bow`
- MOA: `a gentle girl intern with long ash-beige wavy hair, white frilled maid headband, camel cardigan`
- DOCTOR: `chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie`
- HARU: `girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie`
- FLY: `anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings`
- BOT: `boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads`

## 공통 머리말 (모든 프롬프트 맨 앞)
```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight, clean white walls, teal (#0f8f84) and orange (#e8731a) accents with small navy details.
```
## 공통 꼬리말 (모든 프롬프트 맨 끝)
```
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain and bright.
No text, no letters, no numbers, no symbols, no logos, no school uniform, no weapons, no real brands.
```

| 순서 | 저장 이름 | 쓰는 곳 | 비율 | 요청 회차 |
|---|---|---|---|---|
| 1 | cover_index.webp | 목차 | 16:9 | 1회차(단독, 화풍 확인) |
| 2~4 | cover_00·01·02.webp | 0편·①편·②편 | 16:9 | 2회차 |
| 5~7 | cover_03·04·05.webp | ③편·④편·⑤편 | 16:9 | 3회차 |
| 8~9 | cover_06·07.webp | ⑥편·⑦편 | 16:9 | 4회차 |
| 10~11 | duel.webp · outro.webp | 대결·아웃트로 | 3:2 | 5회차 |

---

## 1. cover_index — 목차
대체 글: 탁자 위에 펼친 안장 지도와 그릇 지도 앞의 시아·모아·박사
```
Scene: on a wooden lab table two maps lie unfolded side by side. Left map (teal): a saddle-shaped terrain with hyperbola contour lines. Right map (orange): a bowl-shaped terrain with circular contour lines. Above the right map floats a translucent 3D bowl; a small ball rolls around it along a glowing teal ring at constant height.
Left: SIA, standing by the left map, pointing at it with confidence.
Right: MOA, standing by the right map, holding a notebook, smiling.
Center back: DOCTOR, looking down at both maps.
Mood: friendly rivalry, curious.
```

## 2. cover_00 — 0편 가방 점검
대체 글: 박사가 연 가방에서 그릇·화살표·휜 자가 나오는 장면
```
Scene: DOCTOR opens two small backpacks on a white lab table; out come a small glass bowl, a green arrow-shaped pointer, and a bendable ruler curved into a U shape.
Left: SIA, smiling. Right: MOA, curious face, leaning in.
Mood: calm checklist before a trip.
```

## 3. cover_01 — ①편 차이의 지도(라그랑지안)
대체 글: 여러 길 중 하나만 빛나는 바닥 격자와 공을 던지는 시아
```
Scene: a large floor grid in a white lab. Several dotted paths connect a start dot and an end dot; one smooth teal path glows brighter than the others. A red circle-shaped fence lies on the floor; at one point on it two arrows line up in the same direction.
Center: SIA tosses a ball upward and watches its arc.
Back right: BOT, holding an abacus, confidently pointing at a wrong dotted path.
Mood: discovery.
```

## 4. cover_02 — ②편 합의 지도(해밀토니안)
대체 글: 그릇 옆면을 도는 공과 이를 가리키는 모아
```
Scene: a large translucent orange bowl stands on two floor axes. A ball rolls around the bowl's side at a constant height along a glowing teal ring; small orange arrows are tangent to the ring.
Right: MOA points at the ring, pleased.
Left: SIA looks surprised that the ball does not fall to the bottom.
Mood: surprise, wonder.
```

## 5. cover_03 — ③편 AI 속의 라그랑지안
대체 글: 가드레일 길을 달리는 배달 로봇과 다이얼을 돌리는 시아
```
Scene: a small delivery robot drives along a winding road with a teal guardrail inside the lab. On a control panel, one big dial with no markings. In the background a whiteboard shows red dots and blue dots separated by a straight line with a wide empty corridor between them.
Front: SIA turns the dial with a confident look.
Side: BOT, waving the robot to go faster.
Mood: careful but bold.
```

## 6. cover_04 — ④편 AI 속의 해밀토니안
대체 글: 그릇 골짜기를 나선으로 내려가는 썰매와 꽃이 드러나는 화면
```
Scene: a sled slides down an elongated orange bowl-shaped valley, leaving a smooth spiral track toward the bottom. On a side screen, noisy static gradually turns into a clear picture of a flower. Above, three small boxes linked by thin orange arrows flowing backward.
On the sled: MOA, happy.
Watching: DOCTOR, explaining with one finger raised.
Mood: speed and control.
```

## 7. cover_05 — ⑤편 경제학
대체 글: 저금통·공장 모형·작아지는 케이크 조각 앞의 연구실 식구들
```
Scene: on a lab table: a piggy bank, a small factory diorama with machines, and a round cake cut into slices that get smaller from left to right. On a chalkboard: a simple curve with one peak.
DOCTOR explains with a pointer. SIA holds the piggy bank. MOA counts the cake slices.
Mood: thoughtful, everyday.
```

## 8. cover_06 — ⑥편 양자(심화)
대체 글: 빛나는 상자 속 물결과 에너지 계단을 살피는 하루
```
Scene: a glowing glass box with a standing wave inside; beside it a staircase of four energy steps; two small spheres, one blue and one red.
HARU holds a magnifying glass over the box. MOA looks amazed.
Mood: mysterious, calm.
```

## 9. cover_07 — ⑦편 대결
대체 글: 틸 지도와 주황 지도를 든 시아·모아, 가운데 심판 하루
```
Scene: a white lab arena with a referee stand. A scoreboard with three empty rows hangs above.
Left: SIA holds a teal map. Right: MOA holds an orange map. They face each other with friendly rivalry.
Center: HARU as referee with a whistle.
Corner: BOT, cheering with its abacus.
Mood: friendly match.
```

## 10. duel — 대결 장면 (3:2, 무승부) — 머리말 첫 줄을 "Scene illustration, 3:2."로 바꿈
대체 글: 악수하며 웃는 시아·모아와 무승부를 알리는 하루
```
Scene: the scoreboard now shows three rows marked with simple shapes only: an equal-sign-like tie mark, a teal check, an orange check.
SIA and MOA shake hands and laugh. HARU raises both hands to signal a draw. BOT looks puzzled in the corner. FLY peeks from behind, nodding.
```

## 11. outro — 아웃트로 (3:2) — 머리말 첫 줄을 "Scene illustration, 3:2."로 바꿈
대체 글: 두 지도를 겹쳐 들고 복도를 걷는 시아·모아
```
Scene: SIA and MOA walk together down a bright white corridor, each holding one map (teal and orange); the two maps overlap slightly in the middle into one picture of a bowl and a saddle.
DOCTOR waves from behind. Warm, hopeful, lots of white space.
```

## 받은 뒤 확인
- [ ] 픽셀풍(굵은 외곽선·2~3단 음영)인지, 애니풍이 섞이지 않았는지
- [ ] 그림 안에 글자·숫자가 없는지 (있으면 "remove all text, keep everything else")
- [ ] 시아(검은 머리·검은 메이드복)·모아(베이지 머리·카멜 카디건)·하루(분홍 머리 두 갈래 번)가 바뀌지 않았는지
- [ ] duel·outro는 두 인턴이 함께 웃는 표정(무승부)
