# https://leetcode-cn.com/problems/basic-calculator

# Runtime: 100%

class Solution:
    def calculate(self, s: str) -> int:
        stack = [[0, 1]]
        num, sign = 0, 1
        
        for c in s:
            if c == ' ': continue
            elif c == '+':
                stack[-1][0] += sign * num
                num, sign = 0, 1
            elif c == '-':
                stack[-1][0] += sign * num
                num, sign = 0, -1
            elif c == '(':
                stack.append([0, sign])
                num, sign = 0, 1
            elif c == ')':
                stack[-1][0] += sign * num
                num, sign = 0, 1
                this_group = stack.pop()
                stack[-1][0] += this_group[1] * this_group[0]
            else: num = num * 10 + int(c)
                
        return stack[-1][0] + sign * num