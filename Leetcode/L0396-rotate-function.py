# https://leetcode.com/problems/rotate-function/

# 除了从算法的角度规划问题，更要从数学的角度简化问题

# Runtime: 68 ms (99.77%)
# Memory: 15.7 MB (87.41%)
def maxRotateFunction(A):
    s = max_s = sum(k * v for k, v in enumerate(A))
    lst_sum = sum(A)
    for i in range(1, len(A)):
        s += lst_sum - len(A) * A[-i]
        if s > max_s: max_s = s
    return max_s

A = [4, 3, 2, 6]
A = [-2147483648,-2147483648]

r = maxRotateFunction(A)
print(r)