# DP 0-1 Knapsack 배낭

def knapsack(n, capacity, w, v):
    dp = [[0] * (capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        cw, cv = w[i - 1], v[i - 1]
        for s in range(1, capacity+1):
            # i 를 선택하지 않았을 때
            no = dp[i - 1][s]
            # i 를 선택했을 때
            yes = dp[i - 1][s - cw] + cv if cw <= s else 0
            dp[i][s] = max(no, yes)

    return dp[n][capacity]