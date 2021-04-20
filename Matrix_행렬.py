

def rotate90(m):
    """ 행렬 m 을 시계방향으로 90 도 회전시킨다. """
    return list(map(list, zip(*m[::-1])))

a = [0, 1, 2, 3, 4, 5]
start = 2
stop = 4
step = -1
print(a[start:stop])    # [2, 3]                [start, stop)
print(a[start:])        # [2, 3, 4, 5]          [start,
print(a[:stop])         # [0, 1, 2, 3]          stop)
print()
print(a[:])             # [0, 1, 2, 3, 4, 5]    all
print(a[-1])            # 5                     last
print(a[-2:])           # [4, 5]                last 2
print(a[:-2])           # [0, 1, 2, 3]          all - last 2
print()
print(a[::-1])          # [5, 4, 3, 2, 1, 0]    reverse
print(a[1::-1])         # [1, 0]                first 2 reverse
print(a[:-3:-1])        # [5, 4]                last 2 reverse
print(a[-3::-1])        # [3, 2, 1, 0]          all - last 2 reverse
print()
print(rotate90([[1, 2], [3, 4]]))  # [[3, 1], [4, 2]]
