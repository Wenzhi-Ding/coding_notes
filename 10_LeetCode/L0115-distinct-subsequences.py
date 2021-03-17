# https://leetcode-cn.com/problems/distinct-subsequences/

# 递归的优化：转为循环+数组

from functools import lru_cache

# Runtime: 5%

class Solution:
    @lru_cache(None)
    def numDistinct(self, s: str, t: str) -> int:

        if not t: return 1

        t0 = t[0]
        cnt = 0
        ls, lt = len(s), len(t)
        for k, c in enumerate(s):
            if k + lt <= ls and t0 == c: cnt += self.numDistinct(s[k + 1:], t[1:])

        return cnt

# Runtime: 100%

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        a = [0] * lt + [1]
        for i in range(ls):
            for j in range(lt - 1, -1, -1):
                if s[i] == t[j]:
                    a[j] += a[j - 1]
        return a[lt - 1]
