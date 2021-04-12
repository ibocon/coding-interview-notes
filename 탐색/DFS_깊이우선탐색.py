import sys
rl = sys.stdin.readline


def dfs(n, m, v, x, y):
    """ 깊이우선탐색 """
    global dx, dy

    # 방문처리
    V[x][y] = True
    total = 1
    # DFS 의 핵심. 재귀 함수로 방문.
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 < nx <= n and 0 < ny <= n:
            # 순환되지 않도록 방문 여부 확인 후 탐색
            if M[nx-1][ny-1] == 1 and not v[nx][ny]:
                total += dfs(n, m, v, nx, ny)

    return total


# 'N' 단지 크기
N = int(rl())
# 'M' 단지
M = []
for _ in range(N):
    M.append(list(map(int, rl().rstrip())))

# 'V' 방문 여부 저장 리스트
V = [[False] * (N+1) for _ in range(N+1)]

# 'dx' 'dy' 방향 LTRB
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

towns = []
for i in range(1, N+1):
    for j in range(1, N+1):
        # 아파트면서 방문하지 않았다면 단지를 형성하는 DFS 깊이우선탐색 수행
        if M[i-1][j-1] == 1 and not V[i][j]:
            towns.append(dfs(N, M, V, i, j))

# 단지 출력
print(len(towns))
for t in sorted(towns):
    print(t)

# 백준 2667 단지번호붙이기
'''
[입력]
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
[출력]
3
7
8
9
'''