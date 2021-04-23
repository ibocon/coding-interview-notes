from heapq import heappush, heappop
import sys

# 입력을 빠르게 받도록 stdin 활용
rl = sys.stdin.readline
# 무한 값
INF = int(1e9)


def dijkstra(n, g, si):
    """ 힙 자료구조를 활용한 다익스트라 알고리즘 O(E * logV) """
    dist = [INF] * (n + 1)
    # 시작 노드 si 의 최단거리는 0
    dist[si] = 0

    q = []
    # 검토할 노드 큐 q 에 시작 노드 si 를 추가
    heappush(q, (dist[si], si))

    # 검토할 노드가 모두 소멸될 때까지 반복
    while q:
        # 'cd' si 부터 ci 까지 예상 최단거리, 'ci' 검토할 노드 번호
        cd, ci = heappop(q)
        # 예상 최단거리 cd 가 현재 최단거리 dist[ci] 보다 길다면 무시
        if dist[ci] < cd:
            continue
        # 검토하는 노드 ci 와 연결된 노드의 최단 거리 갱신
        for vd, vi in g[ci]:
            # ci 와 연결된 vi 검토
            # si 부터 vi 까지의 간선 거리 비용 'nd' = si 부터 ci 의 간선비용 'cd' + vi 의 간선비용 'vd'
            nd = cd + vd
            # 새로운 최단거리 'nd' 가 현재 최단거리 'dist[vi]' 보다 작으면 새로운 최단거리 'nd' 로 갱신
            if nd < dist[vi]:
                dist[vi] = nd
                # 최단거리가 갱신되었으므로, 노드 vi 를 q 에 추가
                heappush(q, (dist[vi], vi))

    return dist

# 'N' 노드 수, 'M' 간선 수
N, M = map(int, rl().split())
# 'start_index' 시작 노드 번호
start_index = int(rl())
# 연결 리스트로 그래프 표현
G = [[] for _ in range(N + 1)]
for _ in range(M):
    # 'va' 출발 노드, 'vb' 도착노드, 'c' 간선비용
    va, vb, c = map(int, rl().split())
    # 'va' 에서 'vb' 로 가는 비용 'c'
    G[va].append((c, vb))

# 'dist' 시작 노드 start_index 부터 각 노드까지의 최단거리 리스트
# dist 를 'INF 무한' 으로 초기화

# 다익스트라 알고리즘으로 dist 계산 갱신
D = dijkstra(N, G, start_index)

for i in range(1, N + 1):
    if D[i] == INF:
        print("INF")
    else:
        print(D[i])

'''
[입력]
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
[출력]
0
2
3
7
INF
'''
