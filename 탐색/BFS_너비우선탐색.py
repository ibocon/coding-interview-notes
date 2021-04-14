from collections import deque
import sys
rl = sys.stdin.readline


def bfs(n, m, v, x, y):
    """ 너비우선탐색 """
    global dx, dy

    # 순차적으로 방문하는 리스트
    # BFS 의 핵심. 큐로 순차 방문.
    q = deque([(x, y)])
    v[x][y] = True

    total = 0
    while q:
        cx, cy = q.popleft()

        # 아파트가 아니라면 무시
        if m[cx-1][cy-1] == 0:
            continue

        total += 1

        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if 0 < nx <= n and 0 < ny <= n:
                # 순환되지 않도록 방문 여부 확인 후 탐색
                if m[nx-1][ny-1] == 1 and not v[nx][ny]:
                    q.append((nx, ny))
                    v[nx][ny] = True

    return total


# 'N' 단지 크기
N = int(rl())
# 'M' 단지
M = []
for _ in range(N):
    M.append(list(map(int, rl().rstrip())))

# 'V' 방문 여부 저장 리스트
V = [[False] * (N + 1) for _ in range(N + 1)]

# 'dx' 'dy' 방향 LTRB
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

towns = []
for i in range(1, N+1):
    for j in range(1, N+1):
        # 방문한 아파트는 무시
        if V[i][j]:
            continue

        if M[i-1][j-1] == 1:
            towns.append(bfs(N, M, V, i, j))

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