# 그림 요청 목록 — 두 장의 지도 (젠스파크용, 만드는 순서대로)

공통
- 흰 배경(낮의 연구실). 강조색: 틸 #0f8f84(라그랑지안·시아 팀) · 주황 #e8731a(해밀토니안·모아 팀) · 남색 #1e2f6e.
- 캐릭터는 fruitfly-lab-expressions 기본 그림(시아·모아·박사·조수 하루·초파리 연구원·주판봇)을 참고 그림으로 함께 올린다.
- 목차 표지(1번)를 먼저 받아 그림체를 확인한 뒤, 나머지를 요청할 때 1번 그림을 참고 그림으로 함께 올린다.
- 그림 안에 글자는 "T − V", "T + V" 외에는 넣지 않는다(제목은 페이지가 얹는다).

저장 규칙
- 표지 1600×900(16:9), 장면 1200×800(3:2), WebP, 한 장 250KB 안팎.
- `assets/img/`에 아래 이름으로 넣고 `python3 build/make_og.py && python3 build/build.py`를 돌리면 표지·공유 미리보기가 자동으로 바뀝니다.

| 순서 | 저장 이름 | 쓰는 곳 | 비율 | 요청 묶음 |
|---|---|---|---|---|
| 1 | cover_index.webp | 목차 표지 | 16:9 | 1회차 (단독) |
| 2 | cover_00.webp | 0편 가방 점검 | 16:9 | 2회차 |
| 3 | cover_01.webp | ①편 라그랑지안 | 16:9 | 2회차 |
| 4 | cover_02.webp | ②편 해밀토니안 | 16:9 | 2회차 |
| 5 | cover_03.webp | ③편 AI 속의 라그랑지안 | 16:9 | 3회차 |
| 6 | cover_04.webp | ④편 AI 속의 해밀토니안 | 16:9 | 3회차 |
| 7 | cover_05.webp | ⑤편 경제학 | 16:9 | 3회차 |
| 8 | cover_06.webp | ⑥편 양자 | 16:9 | 4회차 |
| 9 | cover_07.webp | ⑦편 대결 | 16:9 | 4회차 |
| 10 | duel.webp | 대결 장면(무승부) | 3:2 | 5회차 |
| 11 | outro.webp | 아웃트로 | 3:2 | 5회차 |

---

## 1. 목차 표지 — cover_index.webp
> Bright daytime research lab, white background dominant. On a wooden desk lie two unfolded maps side by side: the left map in teal shows a saddle-shaped terrain with hyperbola contour lines and the label "T − V"; the right map in orange shows a bowl-shaped terrain with circular contour lines and the label "T + V". Above the right map floats a translucent 3D bowl with a glowing teal circular orbit around it and a small ball on the orbit. The black-haired intern in a maid-style lab outfit stands by the left map pointing at it with confidence; the beige-haired intern stands by the right map holding a notebook, smiling. A doctor in a white lab coat with glasses watches from behind. Cute anime style matching the reference character sheet, soft teal, orange and navy accents, generous empty space on the upper right for title text. 16:9.

## 2. 0편 표지 — cover_00.webp
> White lab table, the doctor opens two backpacks; out come a small glass bowl, a green arrow-shaped pointer, and a bendable ruler curved into a U shape. The black-haired intern smiles, the beige-haired intern looks curious. Same style as the index cover, white background, 16:9.

## 3. ①편 표지 — cover_01.webp
> White lab room with a large floor grid. Several dotted paths connect a start point and an end point; one smooth teal path glows brighter than the others with a small score badge. The black-haired intern tosses a ball upward and watches its arc. A red circle-shaped fence on the floor with two arrows lined up in parallel at one point. Minimal, lots of white space, teal accent, 16:9.

## 4. ②편 표지 — cover_02.webp
> White lab room, a large translucent orange bowl standing on two floor axes (position and momentum). A ball rolls around the bowl's side at a constant height along a glowing teal ring, small orange arrows tangent to the ring. The beige-haired intern points at the ring, the black-haired intern looks surprised that the ball does not fall to the bottom. Minimal, orange accent, 16:9.

## 5. ③편 표지 — cover_03.webp
> White lab room, a teal fence (guardrail) along a winding road; a small delivery robot drives along the road below a speed sign, a dial labeled "λ" on a control panel. In the background, a whiteboard with red and blue dots separated by a straight line and a wide corridor. The black-haired intern turns the λ dial with a confident look. Teal accent, minimal, 16:9.

## 6. ④편 표지 — cover_04.webp
> White lab room, a sled sliding down an elongated orange bowl-shaped valley leaving a smooth spiral track toward the bottom; on a side screen, noisy static gradually turning into a clear picture of a flower. Thin orange arrows flow backward along a chain of three boxes. The beige-haired intern rides the sled happily. Orange accent, minimal, 16:9.

## 7. ⑤편 표지 — cover_05.webp
> White lab desk with a piggy bank, a small factory model with machines, and a round cake cut into slices of decreasing size from left to right. A simple curve with a peak drawn on a chalkboard. The doctor explains with a pointer, the black-haired intern holds the piggy bank, the beige-haired intern counts cake slices. Teal and orange accents, minimal, 16:9.

## 8. ⑥편 표지 — cover_06.webp
> White lab room, a glowing box with a standing sine wave inside, an energy staircase of four steps beside it, and two small spheres colored blue and red labeled only by color. The assistant (as in the reference sheet) holds a magnifying glass, the beige-haired intern looks amazed. Navy and orange accents, minimal, 16:9.

## 9. ⑦편 표지 — cover_07.webp
> White lab arena with a referee stand; the black-haired intern holding a teal map on the left, the beige-haired intern holding an orange map on the right, facing each other with friendly rivalry. The assistant stands at the center as referee with a whistle. A scoreboard with three empty rows above them. Teal vs orange split composition, 16:9.

## 10. 대결 장면 — duel.webp (결과: 무승부)
> The scoreboard now shows three rows: a tie mark, a teal check, an orange check. The black-haired intern and the beige-haired intern shake hands and laugh; the assistant raises both hands to signal a draw. The abacus robot looks puzzled in the corner. White background, 3:2.

## 11. 아웃트로 — outro.webp
> The two interns walk together down a bright white corridor, each holding one map (teal and orange), the maps overlapping slightly in the middle to form a single picture of a bowl and a saddle. The doctor waves from behind. Warm, hopeful, lots of white space, 3:2.

---

## 저장 이름 체크리스트
- [ ] cover_index.webp
- [ ] cover_00.webp · cover_01.webp · cover_02.webp
- [ ] cover_03.webp · cover_04.webp · cover_05.webp
- [ ] cover_06.webp · cover_07.webp
- [ ] duel.webp · outro.webp

표정 확인: 대결은 무승부라 duel·outro 모두 두 인턴이 함께 웃는 표정이어야 합니다. 틀리면 기존 그림 + 표정 그림을 첨부해 "표정만 편집"으로 다시 요청합니다.
