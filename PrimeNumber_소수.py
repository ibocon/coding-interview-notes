import math


def is_prime_number(x):
    """ 소수 판별 함수 """
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(is_prime_number(54))  # False
print(is_prime_number(787))  # True


# 에라토스테네스의 체
# 1,000,000 <= N
def sieve(n):
    # 에라토스테네스의 체 초기화
    # n 까지 모두 소수인 것으로 초기화
    s = [True] * (n+1)
    # 0 과 1 은 소수가 아님
    s[0] = s[1] = False

    # n의 최대 약수인 n 의 제곱근까지만 검토
    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        # i가 소수인 경우
        if s[i]:
            # i이후 i의 배수들은 소수가 아님
            j = 2
            while i * j <= n:
                s[i * j] = False
                j += 1

    # 소수 목록 산출
    return [i for i in range(2, n+1) if s[i]]


for p in sieve(35):
    print(p, end=" ")
# [2, 3, 5, 7, 11, 13, 19, 23, 29, 31]
