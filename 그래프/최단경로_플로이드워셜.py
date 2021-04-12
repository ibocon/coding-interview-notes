
import sys
rl = sys.stdin.readline
INF = int(1e9)

# 'N' 노드 수, 'M' 간선 수
N, M = map(int, rl().split())
G = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신과의 거리는 0 으로 초기화
for a in range(1, N+1):
    G[a][a] = 0

for _ in range(M):
    # 'vs' 출발 노드, 've' 도착 노드, 'c' 간선 비용
    vs, ve, c = map(int, rl().split())
    G[vs][ve] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 점화식
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for x in range(1, N+1):
    for y in range(1, N+1):
        if G[x][y] == INF:
            print("INF", end=" ")
        else:
            print(G[x][y], end=" ")
    print()
'''
[입력]
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
[출력]
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''