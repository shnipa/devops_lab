K = list(map(int, input().split()))
V = list(map(int, input().split()))
c = {}

for n in range(len(K)):
    if n < len(V):
        c[K[n]] = V[n]
    else:
        c[K[n]] = "None"
print(c)
