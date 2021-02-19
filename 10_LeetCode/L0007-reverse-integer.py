# https://leetcode-cn.com/problems/reverse-integer/

# Runtime: 24 ms (100%)

def reverse(x):
    ans = int(str(abs(x))[::-1])
    if x < 0: ans *= -1
    return ans if -2147483648 <= ans <= 2147483647 else 0

x = 123
x = -123
# x = 120
# x = 0

print(reverse(x))