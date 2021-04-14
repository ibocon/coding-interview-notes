import sys
rl = sys.stdin.readline

N = int(rl())
M = int(rl())
INF = int(1e9)
m = [[INF] * (N+1) for _ in range(N+1)]
for t in range(1, N+1):
    m[t][t] = 0

for _ in range(M):
    a, b, c = map(int, rl().split())
    m[a][b] = min(m[a][b], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            m[i][j] = min(m[i][j], m[i][k] + m[k][j])

for x in range(1, N+1):
    for y in range(1, N+1):
        if m[x][y] == INF:
            print(0, end=" ")
        else:
            print(m[x][y], end=" ")
    print()
