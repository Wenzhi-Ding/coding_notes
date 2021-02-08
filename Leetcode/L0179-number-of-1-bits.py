# https://leetcode.com/problems/number-of-1-bits

# Runtime: 32 ms (76%)

def hammingWeight(n):
    return sum([int(x) for x in bin(n)[2:]])


# Runtime: 24 ms (97.31%)

def hammingWeight(n):
    return bin(n).count('1')


# 位运算解法
# 首先明确在二进制中：100 - 1 = 011
# 所以只要保证后面全是0，我们就可以方便的通过
# n和n-1的位运算逐个把最后一个1翻转为0
# 当数字为0时，表明已经全部翻转完
# 注：本题不考虑负数

# Runtime: 24 ms (97.31%)

def hammingWeight(n):
    ans = 0
    while n != 0:
        n &= n - 1
        ans += 1
    return ans


n = 11  # 3
n = 128  # 1
n = 4294967293  # 31
n = 0  # 0

print(hammingWeight(n))