with open("17-1.txt") as Romania:
    a = [int(i) for i in Romania]
n = len(a)
k = 0
maxx = 0
cnt = 0
for i in range(n):
    k += a[i]
sredn = k / n
for i in range(n - 2):
    r, v, L = a[i], a[i + 1], a[i + 2]
    if(((r < sredn or v < sredn) and L < sredn) or ((r < sredn or L < sredn) and v < sredn) or ((L < sredn or v < sredn) and r < sredn)) and((r % 100 == 14) or (v % 100 == 14) or(L % 100 == 14)):
        cnt += 1
        maxx = max(maxx, (r + v + L))
print(cnt, maxx)