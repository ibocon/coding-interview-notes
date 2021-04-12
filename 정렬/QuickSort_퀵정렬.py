# Hoare partition 호어 분할 방식 (투포인터)
# 최악 O(n^2) 평균 O(n * log(n))
def quick(array, start, end):
    """ Quick sort 퀵 정렬 """
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 첫번째 원소를 피벗으로 선택
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # left 에서 피벗보다 큰 값을 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # right 에서 피벗보다 작은 값을 찾을 때까지 반복
        while start < right and array[pivot] <= array[right]:
            right -= 1

        if left > right:  # left 와 right 이 엇갈렸다면, 작은 값과 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # left 와 right 이 엇갈리지 않았다면, 작은 값과 큰 값을 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 피벗 왼쪽과 오른쪽으로 나눠 재귀 호출하여 정렬
    quick(array, start, right - 1)
    quick(array, right + 1, end)


def p_quick(array):
    """ Python 스타일의 퀵 정렬 """
    # array 가 하나 이하의 원소만 담고 있다면,
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [k for k in tail if k <= pivot]
    right = [k for k in tail if pivot < k]

    return p_quick(left) + [pivot] + p_quick(right)


n = 5
data = [8, 5, 4, 7, 2]
quick(data, 0, n - 1)
for x in data:
    print(x, end=" ")
# 2 4 5 7 8
print()
data2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
data2 = p_quick(data2)
for y in data2:
    print(y, end=" ")
# 0 1 2 3 4 5 6 7 8 9
