# Author: Wenzhi Ding
# Create at: July 6, 2020

# Problem:
# https://leetcode.com/problems/climbing-stairs/

import numpy as np

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Author: Wenzhi Ding

        Runtime: 24ms (92.37%)
        Memory: 13.6MB (94.78%)
        '''
        def dp(n):
            if n - 2 not in mem:
                mem[n - 2] = dp(n - 2)
            if n - 1 not in mem:
                mem[n - 1] = dp(n - 1)
            return mem[n - 1] + mem[n - 2]

        mem = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13, 38: 63_245_986}
        # mem = {0: 1, 1: 1}  # This is enough. But more is better lol :)
        # If n-1 and n-2 all in memory, will not further trigger recursive.
        if n in mem:
            # Still need a exit condition when input is 1.
            return mem[n]
        return dp(n)
        
s = Solution()
cases = [
    1,
    2,
    3,
    4,
    5,
    38
]

for case in cases:
    print(case)
    ans = s.climbStairs(case)
    print(ans)
    # print(ans)