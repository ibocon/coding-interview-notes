# KMP 문자열 탐색
# O(N * M) N = 문자열 길이, M = 패턴 길이

def long_prefix_suffix(pattern):
    """ KMP 의 핵심 함수로 prefix 와 suffix 를 파악 """
    length = len(pattern)
    lps = [0] * length

    lps[0] = 0 # lps[0] 은 prefix 나 suffix 가 없으므로, 언제나 0

    i = 1
    last_length = 0

    while i < length:
        if pattern[i] == pattern[last_length]:
            last_length += 1
            lps[i] = last_length
            i += 1
        else:
            if last_length != 0:
                last_length = lps[last_length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp(pattern, text):
    result = []

    m = len(pattern)
    n = len(text)

    if n < m:  # pattern 이 text 보다 길 경우
        return result

    lps = long_prefix_suffix(pattern)

    j = 0   # pattern 인덱스
    i = 0  # text 인덱스
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  # 패턴을 발견했을 경우
            result.append(i-j+1)
            j = lps[j - 1]

        # 패턴을 발견하지 못했을 경우
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

TEXT = "adsgwadsxdsgwadsgz"
PATTERN = "dsgwadsgz"
print(kmp(PATTERN, TEXT))  # [10]

TEXT = "aa"
PATTERN = "a"
print(kmp(PATTERN, TEXT))  # [1, 2]

TEXT = "aba"
PATTERN = "a"
print(kmp(PATTERN, TEXT))  # [1, 3]

TEXT = "ABC ABCDAB ABCDABCDABDE"
PATTERN = "ABCDABD"
print(kmp(PATTERN, TEXT))  # [16]

TEXT = "ab  ab"
PATTERN = "  "
print(kmp(PATTERN, TEXT))  # [3]