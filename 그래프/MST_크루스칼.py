import sys
rl = sys.stdin.readline


def find(p, v):
    """ 부모노드 리스트 P 에서 노드 v 의 부모를 재귀 탐색 """
    if p[v] != v:
        p[v] = find(p, p[v])
    return p[v]


def union(p, vs, ve):
    """ va 와 vb 의 루트 노드를 동일하게 만들어, 같은 집합이 되도록 결합 """
    pa = find(p, vs)
    pb = find(p, ve)
    if pa < pb:
        p[pb] = pa
    else:
        p[pa] = pb


# 'V' 노드 수, 'E' 간선 수
V, E = map(int, rl().split())
# 'P' 노드 간 집합 관계를 표현한 부모 리스트
P = [0] * (V+1)
# 모든 노드의 부모를 자신으로 초기화. 즉 V 수만큼의 집합 생성
for k in range(1, V+1):
    P[k] = k

edges = []
for _ in range(E):
    # 노드 va 부터 노드 vb 까지 간선 비용 c
    va, vb, c = map(int, rl().split())
    # 간선 리스트 edges 에 입력된 간선 추가
    # c 를 0 번에 배치하여 정렬에 활용
    edges.append((c, va, vb))

# edges 를 간선비용 오름차순으로 정렬 O(NlogN)
# 최소 비용 간선이 0 번에 위치
edges.sort()

# 최소 신장 트리를 구성하는 간선 리스트
mst = []
# 최소 신장 트리 전체 간선 비용
total_cost = 0

# 순환이 발생하지 않으면서 비용이 최소인 간선부터 선택
# 'c' 간선 비용, 'vs' 출발 노드, 've' 도착 노드
for c, v_start, v_end in edges:
    # vs 와 ve 의 부모가 같으면 같은 집합에 속한다는 뜻이며 이미 연결되었다는 의미
    # 따라서 현재 간선을 추가하면 이미 연결된 vs와 ve 를 다시 연결하므로 순환 발생
    if find(P, v_start) != find(P, v_end):
        # vs 와 ve 를 같은 집합에 결합시켜 연결
        union(P, v_start, v_end)
        mst.append((v_start, v_end))
        total_cost += c

print(total_cost)

'''
[입력]
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
[출력]
159
'''