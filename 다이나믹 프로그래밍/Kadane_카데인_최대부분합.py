import sys
rl = sys.stdin.readline


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


print(kadane(5, [1, 2, 3, 4, 5]))  # 15
print(kadane(5, [2, 1, -2, 3, -5]))  # 4
