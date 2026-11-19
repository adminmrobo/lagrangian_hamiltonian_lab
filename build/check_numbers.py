# -*- coding: utf-8 -*-
"""'숫자로 한 번 해 보기'·퀴즈·대결 숫자 검산. 하나라도 틀리면 AssertionError."""
from math import sqrt, cos, sin, exp, log, isclose, hypot, pi
ok = lambda a, b, t=0.01: isclose(a, b, abs_tol=t)
# 1 두 에너지
assert 0.5*1*2**2 == 2 and ok(1*9.8*1, 9.8) and 0.5*4**2 == 8
# 2 작용 = ½(1 + a²/3): 수치 적분으로 확인
def action(a, n=20000):
    s = 0
    for i in range(n):
        t = (i+.5)/n; v = 1 + a*(1-2*t); s += 0.5*v*v/n
    return s
assert ok(action(0), 0.5, 1e-6) and ok(action(1), 0.6667, 1e-3)
# 3 던진 공: S(A) = A²/6 − gA/6, 최소 A = g/2
g = 9.8
def S3(A, n=20000):
    s = 0
    for i in range(n):
        t = (i+.5)/n; v = A*(1-2*t); x = A*t*(1-t); s += (0.5*v*v - g*x)/n
    return s
assert ok(S3(4.9), (4.9**2 - g*4.9)/6, 1e-4) and ok(S3(4.9), -4.0, 0.01) and ok(4.9/4, 1.23, 0.01) and ok(-2*4.9, -9.8)
# 4 라그랑주 승수
x = 1/sqrt(2); assert ok(x, 0.707) and ok(2*x, 1.414) and ok(1/(2*x), 0.707)
# 5 운동량
assert 1*2 == 2 and 2**2/2 == 2 and 2*2 == 4 and 4**2/4 == 4 and 2*3 == 6
# 6 위상 그릇
assert 0.5*0 + 0.5*1 == 0.5 and 0.5*4 == 2
# 7 직각
assert 1*0 + 0*(-1) == 0 and ok(2*pi, 6.28)
# 8 테일러
assert ok(1-cos(.5), 0.1224, 1e-4) and ok((0.125-(1-cos(.5)))/(1-cos(.5))*100, 2.1, 0.05)
# 8-1
q, v = cos(1), -sin(1)
assert ok(q, 0.54) and ok(v, -0.84) and ok(0.5*(q*q+v*v), 0.5) and ok(0.5*v*v-0.5*q*q, 0.21)
# 9 SVM
w, b = (0.5, 0.5), -2
for (px, py), y in [((1, 1), -1), ((3, 3), 1)]: assert ok(y*(w[0]*px+w[1]*py+b), 1)
for (px, py), y in [((0, 1), -1), ((4, 4), 1)]: assert y*(w[0]*px+w[1]*py+b) > 1
lam = 0.25; assert ok(lam*(3-1), w[0]) and ok(2/hypot(*w), 2.83) and ok(hypot(2, 2), 2.83)
# 10 안전 강화학습
lam = 0; hist = []
for t in range(60):
    s = 10 if lam <= 0.5 else 5/lam; risk = s*s/10; lam = max(0, lam + 0.1*(risk-2.5)); hist.append((s, risk, lam))
assert ok(hist[0][2], 0.75) and ok(hist[1][0], 6.67) and ok(hist[1][1], 4.44) and ok(hist[1][2], 0.944, 0.001)
assert ok(hist[19][2], 1.0, 0.001) and ok(5/1, 5) and ok(5/3, 1.67)
# 11 RLHF
def pa(bt): e = exp(1/bt); return e/(e+1)
def kl(bt): p = pa(bt); return p*log(p/.5)+(1-p)*log((1-p)/.5)
assert ok(pa(5), 0.55) and ok(kl(5), 0.005, 0.001) and ok(pa(1), 0.73) and ok(kl(1), 0.11) and ok(pa(.2), 0.99) and ok(kl(.2), 0.65)
# 12 모멘텀
def run(beta, lr=0.07):
    x = y = 1.0; vx = vy = 0
    for i in range(1, 400):
        vx = beta*vx - lr*x; vy = beta*vy - lr*25*y; x += vx; y += vy
        if hypot(x, y) < 0.01: return i
assert run(0) == 64 and run(0.6) == 19 and run(0.9) == 85
# 13 걸음법
q, p = 1.0, 0.0
for _ in range(100): q, p = q + .1*p, p - .1*q
assert ok(0.5*(q*q+p*p), 1.35) and ok((q*q+p*p), 2.7, 0.01)
q, p, em = 1.0, 0.0, 0
for _ in range(100):
    p -= .05*q; q += .1*p; p -= .05*q; em = max(em, abs(0.5*(q*q+p*p)-0.5))
assert em/0.5 < 0.0026
# 14 역전파
x = 1; h = 2*x; y = h*h; ah = 2*h; ax = ah*2
assert (h, y, ah, ax) == (2, 4, 4, 8)
# 15 황금률
def st(s): k = (s/0.1)**1.5; yy = k**(1/3); return k, yy, (1-s)*yy
assert ok(st(.2)[0], 2.83) and ok(st(.2)[2], 1.131, 1e-3) and ok(st(1/3)[0], 6.09) and ok(st(1/3)[2], 1.217, 1e-3) and ok(st(.5)[0], 11.18) and ok(st(.5)[2], 1.118, 1e-3)
assert max(st(i/1000)[2] for i in range(10, 950)) <= st(1/3)[2] + 1e-9
# 16 중첩세대
U = lambda c: log(c)+log(1.5*(100-c))
assert max(range(1, 100), key=U) == 50 and 50*1.5 == 75 and ok(1/50, 0.02)
# 17 케이크·램지
assert ok(0.05*100, 5)
k = (1/3/0.12)**1.5; assert ok(k, 4.63) and ok(k**(1/3)-0.1*k, 1.204, 1e-3)
# 18 q 이론
assert ok(1.2-1, 0.2) and ok(0.8-1, -0.2)
# 19 상자 속 전자
hP, me, L = 6.62607e-34, 9.10938e-31, 1e-9
E1 = hP**2/(8*me*L*L)/1.602177e-19
assert ok(E1, 0.376, 0.001) and ok(4*E1, 1.50) and ok(9*E1, 3.38)
# 20 변분 원리
E = lambda a: a/4 + 1/(4*a)
assert ok(E(2), 0.625) and ok(E(1), 0.5) and ok(E(.5), 0.625) and min(E(i/100) for i in range(20, 300)) >= 0.5 - 1e-12
# 21 이징
Hs = {(s1, s2): s1*s2+s1 for s1 in (1, -1) for s2 in (1, -1)}
assert Hs == {(1, 1): 2, (1, -1): 0, (-1, 1): -2, (-1, -1): 0}
# 0편
assert 2*1 == 2 and 2*2 == 4
print("all numbers ok")
