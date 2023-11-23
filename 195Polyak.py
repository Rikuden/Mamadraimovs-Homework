
with open("17-9.txt") as rim:
    a = [int(i) for i in rim]
n = len(a)
R2 = ""
V2 = ""
L2 = ""
for i in range(n - 2):
    R, V, L = a[i], a[i + 1], a[i + 2]
    while R > 0 and V > 0 and L > 0:
        R2 = str(R % 2) + R2
        R //= 2
        V2 = str(V % 2) + V2
        V //= 2
        L2 = str(L % 2) + L2
        L //= 2
    