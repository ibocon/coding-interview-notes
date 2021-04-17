# DP(Dynamic Programming) 다이나믹 프로그래밍
# LCS(Longest Common Subsequence) 가장 길게 공통되는 부분 수열

import sys
rl = sys.stdin.readline


def lcs(s1, s2):

    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 == 0 or len_s2 == 0:
        return 0

    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    for i in range(1, len_s1+1):
        for j in range(1, len_s2+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len_s1][len_s2]


S1 = rl().rstrip()
S2 = rl().rstrip()

print(lcs(S1, S2))

'''
[입력]
ACAYKP
CAPCAK
[출력]
4
'''