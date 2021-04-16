import sys
rl = sys.stdin.readline

# 백준 1463번 1로 만들기

N = int(rl())
DP = [0] * (10**6 + 1)

for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)

print(DP[N])

'''
[입력]
2
[출력]
1
[입력]
10
[출력]
3
'''