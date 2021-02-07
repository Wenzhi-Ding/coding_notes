# https://leetcode.com/problems/maximum-score-from-removing-stones/


# Runtime: 36 ms (33.33%)
# Memory Usage: 14.2 MB (66.67%)

def maximumScore(a, b, c):
    a, b, c = sorted([a, b, c])
    to_alloc = a - 1  # 要分出去的部分
    b -= max(0, to_alloc - (c - b)) // 2  # 分完还剩的
    c = max(c - to_alloc, b)
    return to_alloc + min(b, c) + int(b != c)


# Runtime: 24 ms (100%)
# Memory Usage: 14.1 MB (66.67%)

def maximumScore(a, b, c):
    a, b, c = sorted([a, b, c])
    ans, b, c = b - a, a, c + a - b
    # ans: 先把最小的两个抹平
    # b: 此时等于a
    # c: 更新为抹平后剩余的c
    if a + b <= c: ans += a + b
    else: ans += a + c // 2
    return ans


a = 2; b = 4; c = 6  # 6
a = 4; b = 4; c = 6  # 7
a = 1; b = 8; c = 8  # 8
a = 1019; b = 375; c = 664  # 1029
a = 16; b = 8; c = 29  # 24

print(maximumScore(a, b, c))