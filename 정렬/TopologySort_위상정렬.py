# Topology sort 위상정렬
# 순서가 정해져 있는 일련의 작업을 수행할 순서로 정렬

# 1. 진입차수가 0 인 노드를 큐에 추가
# 2. 큐에서 노드를 꺼내, 노드에서 출발하는 간선 제거
# 3. 새롭게 진입차수가 0 인 노드를 큐에 추가

# * 모든 원소 방문 전, 큐가 비면 사이클 존재
# * 큐에 노드 개수 2 이상 추가 시, 경우의 수 발생

from collections import deque
import sys
rl = sys.stdin.readline


def topology():
    """ Topology sort 위상 정렬 함수 """
    r = []
    q = deque()

    # 1. 진입차수가 0 인 노드를 큐에 추가
    for i in range(1, V+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 진입차수가 0 인 노드 추출
        cv = q.popleft()
        r.append(cv)

        for nv in G[cv]:
            # 노드 cv 에서 출발하는 간선 제거
            in_degree[nv] -= 1
            if in_degree[nv] == 0:
                q.append(nv)

    return r


# 'V' 노드 수, 'E' 간선 수
V, E = map(int, rl().split())
# 모든 노드의 진입 차수를 0 으로 초기화
in_degree = [0] * (V+1)
# 그래프 초기화
G = [[] for _ in range(V+1)]

# 간선 정보 처리
for _ in range(E):
    vs, ve = map(int, rl().split())
    G[vs].append(ve)
    # vs 에서 ve 로 간선이 추가되어, ve 의 진입차수 증가
    in_degree[ve] += 1

answer = topology()
for a in answer:
    print(a, end=' ')

'''
[입력]
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
[출력]
1 2 5 3 6 4 7
'''