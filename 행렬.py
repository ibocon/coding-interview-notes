

def rotate90(m):
    """ 행렬 m 을 시계방향으로 90 도 회전시킨다. """
    return zip(*m[::-1])
