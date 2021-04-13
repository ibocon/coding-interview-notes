n = 5  # 'N' 데이터의 개수
m = 5  # 'M' 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# 'start' 포인터 이동
for start in range(n):
    # 'end' 포인터 이동
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 만약 합이 동일하면 카운트
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
