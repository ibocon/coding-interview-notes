import sys
rl = sys.stdin.readline


def find(p, v):
    """ 부모노드 리스트 P 에서 노드 v 의 부모를 재귀 탐색 """
    if p[v] != v:
        p[v] = find(p, p[v])
    return p[v]


def union(p, va, vb):
    """ va 와 vb 의 루트 노드를 동일하게 만들어, 같은 집합이 되도록 결합 """
    pa = find(p, va)
    pb = find(p, vb)
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

for _ in range(E):
    # 모든 간선에 대해 union 연산 수행
    vs, ve = map(int, rl().split())
    union(P, vs, ve)

for x in range(1, V+1):
    # 노드가 속한 집합 출력
    print(P[x], end=' ')

'''
[입력]
6 4
1 4
2 3
2 4
5 6
[출력]
1 1 2 1 5 5
'''