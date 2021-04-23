import sys
rl = sys.stdin.readline
INF = int(1e9)

def bellman_ford(v, e, s):
    """ 벨만 포드 알고리즘 함수 """
    dist = [INF] * (v+1)
    dist[s] = 0

    is_edge_relaxed = True
    for vi in range(1, v+1):
        if not is_edge_relaxed:
            break

        is_edge_relaxed = False
        for ec, es, ee in e:
            if dist[es] + ec < dist[ee]:
                dist[ee] = dist[es] + ec
                is_edge_relaxed = True

    is_edge_relaxed = True
    for vi in range(1, v+1):
        if not is_edge_relaxed:
            break
        is_edge_relaxed = False
        for ec, es, ee in e:
            if dist[es] + ec < dist[ee]:
                dist[ee] = -INF
                is_edge_relaxed = True

    return dist[1:]


V = 9
E = [
    (1, 1, 2), (1, 2, 3), (1, 3, 5), (-3, 5, 4), (1, 4, 3),
    (4, 2, 6), (4, 2, 7), (5, 6, 7), (4, 7, 8), (3, 6, 8)]
S = 1

result = bellman_ford(V, E, S)
for r in result:
    if r == -INF:
        print("-INF")
    elif r == INF:
        print("INF")
    else:
        print(r)

'''
[출력]
0
1
-INF
-INF
-INF
5
5
8
INF
'''