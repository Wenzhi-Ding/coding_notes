# https://leetcode-cn.com/problems/power-of-two/

# 位运算
# Runtime: 36 ms (89%)
def isPowerOfTwo(n):
    return n > 0 and (bin(n).count('1') == 1)

# Runtime: 40 ms (70%)
def isPowerOfTwo(n):
    return n > 0 and not (n & (n - 1))
    # 2^n是100..
    # 2^n-1是11..
    # “与”运算后，应该为0


# 普通解法
# Runtime: 36 ms (88%)
def isPowerOfTwo(n):
    if n <= 0: return False 
    while n % 2 == 0: n /= 2
    return n == 1
