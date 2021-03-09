# https://leetcode-cn.com/problems/count-pairs-of-nodes/

import bisect
from collections import Counter

class Solution:
    def countPairs(self, n: int, edges, queries):
        deg = [0] * n
        for x, y in edges:
            deg[x - 1] += 1
            deg[y - 1] += 1
        
        wtf = Counter()
        for x, y in edges:
            wtf[(min(x, y), max(x, y))] += 1
        
        print(wtf)
            
        s = sorted(deg)
        
        ans = list()
        for q in queries:
            tot = 0
            for x in range(n):
                it = bisect.bisect_left(s, q - deg[x] + 1)
                tot += n - it
                if deg[x] + deg[x] > q:
                    tot -= 1
            print(tot)
            for (x, y), z in wtf.items():
                if deg[x - 1] + deg[y - 1] > q and deg[x - 1] + deg[y - 1] - z <= q:
                    tot -= 2
            ans.append(tot // 2)
        
        return ans