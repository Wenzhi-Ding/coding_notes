# https://leetcode-cn.com/problems/string-to-integer-atoi/

# Runtime: 36 ms (96%)

def myAtoi(s):
    s = s.lstrip()
    if not s: return 0

    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    if not s: return 0

    pos = -1
    for k, d in enumerate(s):
        if pos == -1:
            if d.isdigit(): pos = k
            else: return 0
        elif not d.isdigit():
            ans = sign * int(s[pos:k])
            break
    else:
        ans =  sign * int(s[pos:])

    return max(min(ans, 2147483647), -2147483648)  # 不要写2 ** 31，浪费好多时间

s = '42'
s = "   -42"
# s = "-91283472332"
# s = "words and 987"
# s = "4193 with words"
s = "  -4193 with words"
# s = "+-12"
# s = "-+12"
# s = ""

print(myAtoi(s))