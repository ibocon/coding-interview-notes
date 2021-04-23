import sys
rl = sys.stdin.readline
INF = int(1e9)

def max_contiguous_subarray_sum(n, a):
    dp = [-INF] * n
    dp[0] = a[0]

    for i in range(1, len(a)):
        dp[i] = max(dp[i-1] + a[i], a[i])

    return max(dp)


def kadane(n, a):
    p_sum = [0] * n
    p_sum[0] = a[0]

    for k in range(1, n):
        p_sum[k] = p_sum[k-1] + a[k]

    max_sum, min_sum = 0, 0

    for i in range(n):
        max_sum = max(max_sum, p_sum[i] - min_sum)
        min_sum = min(max_sum, min_sum)

    return max_sum

print(max_contiguous_subarray_sum(5, [1, 2, 3, 4, 5]))  # 15
print(max_contiguous_subarray_sum(5, [2, 1, -2, 3, -5]))  # 4
print()
print(kadane(5, [1, 2, 3, 4, 5]))  # 15
print(kadane(5, [2, 1, -2, 3, -5]))  # 4
