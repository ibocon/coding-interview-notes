def binary_search(a, t, lo=0, hi=None):
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] == t:
            return mid

        if t < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return None


def bisect_left(a, t, lo=0, hi=None):
    """
    cpython/biselct.py 의 bisect_left 함수
    찾는 값 t 의 번호를 반환한다.
    """
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if t <= a[mid]:
            # 찾는 값 t 보다 비교 값 a[min] 이 크거나 같으면 hi 를 낮춘다.
            hi = mid
        else:
            # 찾는 값 t 보다 비교 값 a[min] 이 작으면 lo 를 높인다.
            lo = mid + 1

    return lo


def bisect_right(a, t, lo=0, hi=None):
    """
    cpython/biselct.py 의 bisect_right 함수
    찾는 값 t 의 바로 다음 번호를 반환한다.
    """
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if t < a[mid]:
            # 찾는 값 t 보다 비교 값 a[min] 이 크면 hi 를 낮춘다.
            hi = mid
        else:
            # 찾는 값 t 보다 비교 값 a[min] 이 작거나 같은면 lo 를 높인다.
            lo = mid + 1

    return lo


def binary_count(a, t, lo=0, hi=None):
    right = bisect_right(a, t, lo, hi)
    left = bisect_left(a, t, lo, hi)

    return right - left


# 테스트
N = 10
A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

T = 13
print(binary_search(A, T, 0, N))  # 6
print(bisect_left(A, T, 0, N))  # 6
print(bisect_right(A, T, 0, N))  # 7
print()
T = 20
print(binary_search(A, T, 0, N))  # None
print(bisect_left(A, T, 0, N))  # 10
print(bisect_right(A, T, 0, N))  # 10
print()
N = 8
A = [1, 2, 2, 3, 3, 3, 4, 4]
print(binary_count(A, 1, 0, N))  # 1
print(binary_count(A, 2, 0, N))  # 2
print(binary_count(A, 3, 0, N))  # 3
print(binary_count(A, 4, 0, N))  # 2
print(binary_count(A, 5, 0, N))  # 0
