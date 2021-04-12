from heapq import heappush, heappop
import sys

# 입력을 빠르게 받도록 stdin 활용
rl = sys.stdin.readline
# 무한 값
INF = int(1e9)


def dijkstra(si):
    """ 힙 자료구조를 활용한 다익스트라 알고리즘 O(E * logV) """
    q = []
    # 시작 노드 si 의 최단거리는 0
    dist[si] = 0
    # 시작 노드 si 를 검토할 노드 큐 q 에 추가
    heappush(q, (dist[si], si))

    # q 가 모두 소멸될 때까지 반복
    while q:
        # cd = 현재 노드까지 예상 최단거리, ci = 현재 노드 Index
        cd, ci = heappop(q)
        # 예상 최단거리 cd 가 현재 최단거리 dist[ci] 보다 길다면 무시
        if dist[ci] < cd:
            continue
        # 현재 노드 ci 와 연결된 노드의 최단 거리 갱신
        for vi, vd in G[ci]:
            # ci 와 연결된 vi 의 si 부터 vi 까지의 간선 거리 비용 nd
            # si 부터 ci 의 간선비용은 cd, vi 의 간선비용은 vd
            nd = cd + vd
            # 현재 si 부터 vi 까지 최단거리 dist[vi] 가 새로운 간선비용 nd 보다 크면 최단거리를 갱신
            if nd < dist[vi]:
                dist[vi] = nd
                # 더 짧아진 최단거리를 검토 큐 q 에 추가
                heappush(q, (dist[vi], vi))


# N = 노드 수, M = 간선 수
N, M = map(int, rl().split())
# 시작 노드 index
start_index = int(rl())
# 연결 리스트로 그래프 표현
G = [[] for _ in range(N + 1)]
for _ in range(M):
    # va = 출발 노드, vb = 도착노드, c = 간선비용
    va, vb, c = map(int, rl().split())
    # va 노드에서 vb 노드로 가는 비용이 c
    G[va].append((vb, c))

# si 시작 노드로부터의 최단거리. 'INF 무한' 으로 초기화
dist = [INF] * (N + 1)

dijkstra(start_index)

for i in range(1, N + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])

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
INFINITY
'''
