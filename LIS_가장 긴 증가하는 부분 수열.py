# DP(Dynamic Programming) 다이나믹 프로그래밍
# LIS(Longest Increasing Subsequence) 가장 긴 증가하는 부분 수열

import sys
rl = sys.stdin.readline

# 'N' 배열 길이
N = int(rl())
# 'A' 배열
A = list(map(int, rl().split()))

# 1로 DP 테이블 초기화
dp = [1] * N

for i in range(1, N):
    # 0 부터 i - 1 까지 길이 갱신
    for j in range(0, i):
        # 모든 0 <= j < i 에 대하여,
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

'''
[입력]
6
10 20 10 30 20 50
[출력]
4
'''