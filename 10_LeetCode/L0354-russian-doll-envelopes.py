# https://leetcode-cn.com/problems/russian-doll-envelopes/

# Runtime: 52% -> O(n^2)

class Solution:
    def maxEnvelopes(self, envelopes):
        
        if not envelopes: return 0

        envelopes.sort(key=lambda x: x[0])

        n = len(envelopes)

        max_num = [1 for _ in range(n)]
        for i in range(1, n):
            w1, h1 = envelopes[i]
            tmp = 0
            for j in range(i - 1, -1, -1):
                w0, h0 = envelopes[j]
                _max_num = max_num[j]
                if _max_num > tmp and h0 < h1 and w0 < w1: tmp = _max_num
            max_num[i] = 1 + tmp

        return max(max_num)

import bisect

# Runtime: 66-100% -> O(n log n)

class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # 高度从大到小排，保证了

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
            print(f)
        
        return len(f)


envelopes = [[5,4],[6,4],[6,7],[2,3]]  # 3
envelopes = [[5,4],[6,4],[6,7],[2,3],[1,2]]  # 4
envelopes = [[10,8],[1,12],[6,15],[2,18]]  # 2
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]  # 4
# envelopes = [[1,1],[1,1],[1,1]]  # 1
envelopes = [[1,1],[1,2],[1,3]]  # 1

sol = Solution()
print(sol.maxEnvelopes(envelopes))