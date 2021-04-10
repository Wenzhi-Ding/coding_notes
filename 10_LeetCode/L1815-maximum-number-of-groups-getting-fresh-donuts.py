# https://leetcode-cn.com/problems/maximum-number-of-groups-getting-fresh-donuts/

from functools import cache

class Solution:
    def maxHappyGroups(self, batchSize, groups):
        @cache
        def dfs(cur, rest):
            print(cur, rest)
            res = 0
            for i in range(1, batchSize):
                print(i, rest // (31 ** i) % 31)
                if rest // (31 ** i) % 31 > 0:  # 条件表示的含义是：余数i在列表中存在，不能等于0
                    res = max(res, (cur == 0) + dfs((cur + i) % batchSize, rest - 31 ** i))
                    # cur == 0表示当前又发现了一个组合满足条件
                    # dfs((cur + i) % batchSize, rest - 31 ** i)表示继续在剩下的元素中找满足条件的组合
                    # (cur + i) % batchSize按余数cur + i在剩余列表里面搜索组合数量
                    # rest - 31 ** i表示将当前元素从列表中拿出，即该数字表示了状态压缩后的剩余列表
            return res
        dfs.cache_clear()
        rest = [0] * batchSize
        for each in groups:
            rest[each % batchSize] += 1
            # rest[i]表示数组中除batchSize与i的数字有多少个
            # rest[0]则表示一开始就已经可以除尽的那些数
        return rest[0] + dfs(0, sum(rest[i] * 31 ** i for i in range(1, batchSize)))
        # 用31进制进行状态压缩（因为groups最大为30个元素）
        # 这里将该列表组装为31进制数存储：sum(rest[i] * 31 ** i for i in range(1, batchSize))
        

batchSize = 3; groups = [1,2,3,4,5,6]
# batchSize = 4; groups = [1,3,2,5,2,2,1,6]

s = Solution()
print(s.maxHappyGroups(batchSize, groups))