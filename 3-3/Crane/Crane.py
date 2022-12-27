from math import sin, cos, pi
import sys
sys.setrecursionlimit(1000000)

ST_SIZE = 1 << 15 - 1

# 入力
N, C = map(int,input().split())
L = list(map(int,input().split()))
S = list(map(int,input().split()))
A = list(map(int,input().split()))

# セグメント木のデータ
vx = [0.0] * ST_SIZE    #各節点のベクトル
vy = [0.0] * ST_SIZE
ang = [0.0] * ST_SIZE

# 角度の変化を調べるため、現在の角度を保存しておく
prv = [0.0] * N

# セグメント木を初期化する
# kは接点の番号、l, rはその節点が[l, r)に対応づいていることを表す
def init(k, l, r):
    ang[k] = vx[k] = 0.0
    if r - l == 1:
        # 葉
        vy[k] = L[l]
    else:
        # 葉でない節点
        chL = k * 2 + 1
        chR = k * 2 + 2
        init(chL, l, (l + r) // 2)
        init(chR, (l + r) // 2, r)
        vy[k] = vy[chL] + vy[chR]

# 場所sの角度がaだけ変更になった
# vは節点の番号、l, rはその節点が[l, r)に対応づいていることを表す
def change(s, a, v, l, r):
    if s <= l:
        return
    elif s < r:
        chL = v * 2 + 1
        chR = v * 2 + 2
        m = (l + r) // 2
        change(s, a, chL, l, m)
        change(s, a, chR, m, r)
        if s <= m:
            ang[v] += a
        
        s = sin(ang[v])
        c = cos(ang[v])
        vx[v] = vx[chL] + (c * vx[chR] - s * vy[chR])
        vy[v] = vy[chL] + (s * vx[chR] + c * vy[chR])

# 初期化
init(0, 0, N)
for i in range(1, N):
    prv[i] = pi

# 各クエリを処理
for i in range(C):
    s = S[i]
    a = A[i] / 360.0 * 2 * pi    # ラジアンに直す
    
    change(s, a - prv[s], 0, 0, N)
    prv[s] = a
    
    print("%.2f %.2f" % (vx[0], vy[0]))
