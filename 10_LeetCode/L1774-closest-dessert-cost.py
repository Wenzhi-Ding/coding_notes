# https://leetcode-cn.com/problems/closest-dessert-cost/

# 问题的规模很小，直接穷举吧
import bisect

# Runtime: 72 ms
# Memory: 22.2 MB

class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):

        # 穷举
        toppingSum = set([0])
        for i in toppingCosts * 2:  # 快速求排列组合
            toppingSum |= set([s + i for s in toppingSum])
        toppingSum = sorted(list(toppingSum))
        l = len(toppingSum)

        # 二分查找
        ans = 1000000007
        for c in baseCosts:
            i = bisect.bisect_right(toppingSum, target - c)
            if i > 0 and abs(c + toppingSum[i - 1] - target) < abs(ans - target): ans = c + toppingSum[i - 1]
            if i < l and abs(c + toppingSum[i] - target) < abs(ans - target): ans = c + toppingSum[i]
        return ans


        








baseCosts = [1,7]; toppingCosts = [3,4]; target = 10  # 10
# baseCosts = [2,3]; toppingCosts = [4,5,100]; target = 18  # 17
# baseCosts = [3,10]; toppingCosts = [2,5]; target = 9  # 8
# baseCosts = [10]; toppingCosts = [1]; target = 1  # 10
# baseCosts = [3]; toppingCosts = [3]; target = 9  # 9

sol = Solution()
print(sol.closestCost(baseCosts, toppingCosts, target))