from collections import deque
import sys
rl = sys.stdin.readline


def topology():
    r = []
    q = deque()

    for i in range(1, N+1):
        if ID[i] == 0:
            q.append(i)

    while q:
        cv = q.popleft()
        r.append(cv)

        for nv in G[cv]:
            ID[nv] -= 1
            if ID[nv] == 0:
                q.append(nv)

    return r


N, M = map(int, rl().split())
ID = [0] * (N+1)
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, rl().split())
    G[a].append(b)
    ID[b] += 1

answer = topology()
for k in answer:
    print(k, end=" ")

