# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/

from collections import Counter
from functools import lru_cache

# Runtime: 32 ms (99%)

class Solution:
    @lru_cache(None)
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = Counter(s)
        exc = [x for x in cnt if cnt[x] < k]
        if len(exc) == 0: return len(s)

        idx = [k for k, v in enumerate(s) if v in exc]
        ans = []
        
        hi = -1
        for i in range(len(idx)):
            lo, hi = hi, idx[i]
            if hi - lo >= k: ans.append(self.longestSubstring(s[lo + 1:hi], k))
        if len(s) - hi >= k: ans.append(self.longestSubstring(s[hi + 1:], k))
        
        return max(ans) if ans else 0

# Runtime: 24-44 ms (63%-100%)

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = [s]
        ans = 0
        while stack:
            cur = stack.pop()
            for c in set(cur):
                if cur.count(c) < k:
                    stack.extend([t for t in cur.split(c)])
                    break
            else:
                ans = max(ans, len(cur))
        return ans


s = "aaabb"; k = 3  # 3
s = "ababbc"; k = 2  # 5
s = "a"; k = 3  #0
s = "abcab"; k = 2  # 0
s = "bbaaacbd"; k = 3  # 3

st = Solution()
print(st.longestSubstring(s, k))