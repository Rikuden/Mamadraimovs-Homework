with open("17-243.txt") as Rikuden:
    a = [int(i) for i in Rikuden]
n = len(a)
srav = 0
cnt = 0
minn = 10000000
for i in range(n):
    if (n == 1) and (a[i] % 151 == 0):
        srav = a[n]
    if (n != 1) and (a[i] > a[i - 1]) and (n % 151 == 0):
        srav = a[n]
flagr = 0
flagv = 0
for i in range(n - 1):
    v, r = a[i], a[i - 1]
    while v > 0:
        if v % 16 == 3:
            flagv = 1
        v //= 16
    while r > 0:
        if r % 16 == 3:
            flagr = 1
        r //= 16
for i in range(n - 1):
    r, v = a[i], a[i + 1]
    if ((r > srav) or(v > srav)) and(flagr == 1 or flagv == 1):
        cnt += 1
        minn = min(minn, r + v)
print(cnt, minn)