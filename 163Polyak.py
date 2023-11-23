with open("17-3.txt") as kim:
    a = [int(i) for i in kim]
n = len(a)
res = 0
cnt = 0
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    x1 = x % 2
    y1 = y % 2
    if (x1 > y1) and (x % 11 == 0) and (y % 4 == 0):
        cnt += 1
        res = max(res, (x + y))
    if(x1 < y1) and(y % 11 == 0) and (x % 4 == 0):
        cnt += 1
        res = max(res,(x + y))
print(cnt, res)