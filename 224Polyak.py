with open("17-4.txt") as rome:
    a = [int(i) for i in rome]
n = len(a)
cnt = 0
k = 0
flag1 = 0
flag2 = 0
minn = 10000000
for i in range(n):
    k += a[i]
sredn = k / n
for i in range(n - 1):
    r, v = a[i], a[i + 1]
    while r > 0:
        if r % 10:
            flag1 = 1
        r //= 10
    while v > 0:
        if r % 10:
            flag2 = 1
        v //= 10
for i in range(n - 1):
    r, v = a[i], a[i + 1]
    if ((r < sredn) or(v < sredn)) and ((flag1 == 0) or (flag2 == 0)):
        cnt += 1
        minn = min(minn, r + v)
print(cnt, minn)