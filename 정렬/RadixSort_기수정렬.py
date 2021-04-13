# Radix Sort 기수 정렬
# Radix sort in Python

# 자릿수 정렬을 위해 Count sort 계수 정렬을 활용
def counting(array, place):
    size = len(array)
    output = [0] * size
    # 자릿수 0 - 9 까지
    count = [0] * 10

    # 목표 자릿수 카운팅
    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1

    # 누적 값으로 변경
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]


def radix(array):
    """ Radix sort 기수정렬 """
    # 최대 값
    max_value = max(array)
    # 1의 자리부터 정렬
    place = 1
    while max_value // place > 0:
        counting(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radix(data)
for d in data:
    print(d, end=" ")
# 1 23 45 121 432 564 788
