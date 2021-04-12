# Prefix sum 누적합
# 중복해서 누적하는 부분이 없는지 확인할 것

import sys
rl = sys.stdin.readline

N = int(rl())
A = list(map(int, rl().split()))

# 누적 합
prefix_sum = [0]
for i in range(1, len(A) + 1):
    prefix_sum.append(prefix_sum[i - 1] + A[i - 1])

# 'S' 시작 번호, 'E' 끝 번호
S, E = map(int, rl().split())
print(prefix_sum[E] - prefix_sum[S - 1])

'''
[입력]
5
10 20 30 40 50
3 5
[출력]
120
'''