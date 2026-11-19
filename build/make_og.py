# -*- coding: utf-8 -*-
"""공유 미리보기(og:image) 1200×630 — 표지 그림이 들어오기 전 임시판. assets/img/cover_*.webp가 있으면 그것을 잘라 쓴다."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def font(sz): return ImageFont.truetype(F, sz, index=1)
ITEMS = [('index', '두 장의 지도', '라그랑지안 vs 해밀토니안', ['sia_e19', 'moa_e16']),
         ('00', '0편 · 가방 점검', '그릇 · 오르막 화살표 · 굽음', ['sia_e13', 'moa_e09']),
         ('01', '①편 · 차이의 지도', '라그랑지안 T − V · 작용 · 라그랑주 승수', ['sia_e01', 'jupanbot_e16']),
         ('02', '②편 · 합의 지도', '해밀토니안 T + V · 위상 공간의 그릇', ['moa_e16', 'sia_e09']),
         ('03', '③편 · AI 속의 라그랑지안', 'SVM 쌍대 · 안전 강화학습 · RLHF', ['sia_e19', 'jupanbot_e16']),
         ('04', '④편 · AI 속의 해밀토니안', '모멘텀 · HMC·확산 · 역전파', ['moa_e10', 'jupanbot_e16']),
         ('05', '⑤편 · 경제학의 두 지도', '솔로우 · 중첩세대 · 램지 · q 이론', ['sia_e01', 'moa_e09']),
         ('06', '⑥편 · 양자의 해밀토니안', '연산자 · 변분 원리 · 양자 어닐링', ['moa_e16', 'sia_e09']),
         ('07', '⑦편 · 같은 공, 두 지도', 'HNN·LNN · 대결 · 비교 총정리', ['sia_e19', 'moa_e10'])]
for key, t, sub, ch in ITEMS:
    W, H = 1200, 630
    cov = os.path.join(ROOT, 'assets/img', f'cover_{key}.webp')
    if os.path.exists(cov):
        c = Image.open(cov).convert('RGB'); r = max(W / c.width, H / c.height)
        c = c.resize((int(c.width * r) + 1, int(c.height * r) + 1)); x = (c.width - W) // 2; y = (c.height - H) // 2
        c.crop((x, y, x + W, y + H)).save(os.path.join(ROOT, 'assets/og', f'og_{key}.jpg'), quality=82); continue
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    for k in range(1, 5):
        d.arc([300 - 60 * k, 315 - 60 * k, 300 + 60 * k, 315 + 60 * k], 0, 360, fill='#f6d2b3', width=3)
    for k in range(1, 5):
        d.arc([900 - 60 * k, 315 - 60 * k, 900 + 60 * k, 315 + 60 * k], 0, 360, fill='#f2b88a', width=3)
    d.ellipse([900 - 120, 315 - 120, 900 + 120, 315 + 120], outline='#0f8f84', width=7)
    d.text((300, 40), 'T − V', font=font(40), fill='#0f8f84', anchor='mt'); d.text((900, 40), 'T + V', font=font(40), fill='#e8731a', anchor='mt')
    d.rounded_rectangle([80, 120, 760, 340], radius=18, fill='white', outline='#d5dbe2', width=2)
    d.text((110, 145), t, font=font(48), fill='#16212b'); d.text((110, 222), sub, font=font(27), fill='#0f8f84')
    d.text((110, 282), '좌표축 위의 그릇 · 특집 · 글 안상선', font=font(22), fill='#5b6874')
    for i, c in enumerate(ch):
        cim = Image.open(os.path.join(ROOT, f'assets/chars/{c}.webp')).convert('RGBA').resize((230, 230), Image.LANCZOS)
        im.paste(cim, (700 + i * 240, 380), cim)
    im.save(os.path.join(ROOT, 'assets/og', f'og_{key}.jpg'), quality=82)
print('og done')
