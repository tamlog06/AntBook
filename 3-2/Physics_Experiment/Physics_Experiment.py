from decimal import Decimal, ROUND_HALF_UP
N = int(input())
H = int(input())
R = int(input())
T = int(input())
g = 10

def calc(T):
    if T < 0:
        return H

    t = Decimal(pow(2*H/g, 0.5))
    k = T//t
    if k % 2 == 0:
        return Decimal(H - g*pow(T - k*t, 2)/2)
    else:
        return Decimal(H - g*pow(k*t+t-T, 2)/2)

y = []
for i in range(N):
    y.append(calc(T-i))

y.sort()
for i in range(N):
    y[i] = y[i] + Decimal(2*R*i/100)
    y[i] = y[i].quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

print(*y)


