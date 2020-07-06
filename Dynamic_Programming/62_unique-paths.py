# Author: Wenzhi Ding
# Create at: July 6, 2020

# Problem:
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Author: Wenzhi Ding

        Runtime: 36ms (35.73%)
        Memory: 14.1MB (5.12%)
        '''

        mem = [[0] * m for _ in range(n)]
        mem[0][0] = 1

        def dp(j, k):
            if not j + k: return 1

            if k:
                if mem[j][k - 1]: a = mem[j][k - 1]
                else: a = mem[j][k - 1] = dp(j, k - 1)
            else: a = 0
            if j:
                if mem[j - 1][k]: b = mem[j - 1][k] 
                else: b = mem[j - 1][k] = dp(j - 1, k)
            else: b = 0
            return int(a + b)

        return dp(n - 1, m - 1)
        
s = Solution()
cases = [
    (3, 2),
    (7, 3),
    (1, 1)
]

for case in cases:
    print(case)
    ans = s.uniquePaths(case[0], case[1])
    print(ans)
    # print(ans)