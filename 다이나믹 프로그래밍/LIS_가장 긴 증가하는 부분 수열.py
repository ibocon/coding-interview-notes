# DP(Dynamic Programming) 다이나믹 프로그래밍
# LIS(Longest Increasing Subsequence) 가장 긴 증가하는 부분 수열

def lis(n, a):
    # 1로 DP 테이블 초기화
    dp = [1] * n

    for i in range(1, n):
        # 0 부터 i - 1 까지 길이 갱신
        for j in range(0, i):
            # 모든 0 <= j < i 에 대하여,
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

N = 6
A = [10, 20, 10, 30, 20, 50]
print(max(lis(N, A)))  # 4

def lnds(n, a):
    """Longest Non-Decreasing Subsequence 가장 긴 감소하지 않는 부분 수열 """
    # 1로 DP 테이블 초기화
    dp = [1] * n

    for i in range(1, n):
        # 0 부터 i - 1 까지 길이 갱신
        for j in range(0, i):
            # 모든 0 <= j < i 에 대하여,
            if a[j] <= a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

N = 6
A = [10, 20, 10, 10, 20, 50]
print(max(lnds(N, A)))  # 5
