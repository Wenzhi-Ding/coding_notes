# https://leetcode-cn.com/problems/palindrome-partitioning

# 动态规划+递归解法
# Runtime: 85%

from functools import lru_cache

class Solution:
    @lru_cache(None)
    def partition(self, s):
        n = len(s)
        ans = []
        
        for i in range(1, n + 1):
            subs = s[:i]
            if subs == subs[::-1]:
                if i == n: ans += [[subs]]
                else: ans += [[subs] + x for x in self.partition(s[i:])]
        
        return ans


class Solution:
    def partition(self, s):
        if s == "":
            return []
        ans = [[s[0]]]
        for i in range(1, len(s)):
            curr = s[i]
            newAns = []
            for item in ans:
                newAns.append(item + [curr])
                if item[-1] == curr:
                    newAns.append(item[0:-1] + [item[-1] + curr])
                if len(item) >= 2 and item[-2] == curr:
                    newAns.append(item[0:-2] + [item[-2] + item[-1] + curr])
            ans = newAns
            print(i, s[i], ans)
        return ans
