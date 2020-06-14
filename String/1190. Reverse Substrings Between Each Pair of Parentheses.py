# Author: Wenzhi Ding
# Create at: June 14, 2020

# Problem:
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        '''
        Author: Wenzhi Ding

        Runtime: 44ms
        Memory: 13.9MB
        '''
        rp = s.find(')')
        while rp > 0:
            lp = len(s[:rp]) - s[:rp][::-1].find('(')
            # Should search '(' in s[:rp] instead of s
            # Relevant test case: "ta()usw((((a))))"
            tmp = s[lp:rp][::-1]
            s = s[:lp - 1] + tmp + s[rp + 1:]
            rp = s.find(')')
        return s

    def reverseParentheses2(self, s: str) -> str:
        '''
        Author: PR511
        Link: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/681582/Python-easy-and-simple-99-efficient
        
        Runtime: 36ms
        Memory: 13.8MB
        '''
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                # Everytime meets ')', make sure content after previou '(' are reversed
                st = ""
                while stack[-1] != '(':
                    st += stack[-1][::-1]
                    # Reverse last element in stack and add to st
                    stack.pop()  # Delete last element in stack
                stack.pop()  # Delete '('
                stack.append(st)  # Put reversed string to the last of stack
        return ''.join(stack)


s = Solution()
cases = {
    "(abcd)": "dcba",
    "(u(love)i)": "iloveu",
    "(ed(et(oc))el)": "leetcode",
    "a(bcdefghijkl(mno)p)q": "apmnolkjihgfedcbq",
    "ta()usw((((a))))": "tauswa"
}

for case in cases:
    print(case)
    ans = s.reverseParentheses2(case)
    print(ans == cases[case], ans)
    # print(ans)