# Count sort 계수 정렬
# O(n + k), k = 최대값
# K 가 10,000,000 이하여야 사용할 수 있다.

def counting(array, max_value):
    """ Counting sort 계수 정렬 """
    answer = []

    # 값이 나타난 회수를 기록하는 리스트
    count = [0] * (max_value + 1)
    for a in array:
        count[a] += 1

    for i in range(len(count)):
        for _ in range(count[i]):
            # 최소값부터 시작해서 값이 나타난 횟수만큼 추가
            answer.append(i)

    return answer


data = [8, 5, 4, 3, 7, 2, 3]
result = counting(data, max(data))
for k in result:
    print(k, end=" ")
# 2 3 3 4 5 7 8
