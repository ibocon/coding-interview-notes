

def rotate90(m):
    """ 행렬 m 을 시계방향으로 90 도 회전시킨다. """
    return list(map(list, zip(*m[::-1])))


print(rotate90([[1, 2], [3, 4]]))  # [[3, 1], [4, 2]]
