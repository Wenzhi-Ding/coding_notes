# https://leetcode-cn.com/problems/coin-change/

# 按背包问题做，一次只下降一个coin的值
# 按深度优先搜索做，一次尽可能高的下降，所以第一次达成目标的时候就是找到了最少组合了

# Runtime: 1268 ms (64%)
from functools import lru_cache

class Solution:
    def coinChange(self, coins, amount):

        coins = sorted(coins, key=lambda x: -x)

        @lru_cache(None)
        def recur(amount):
            if amount == 0: return 0
            if amount in coins: return 1

            ans = 10000000007
            for coin in coins:
                if amount > coin: ans = min(ans, recur(amount - coin))  
            return ans + 1

        ans = recur(amount)

        return ans if ans != 10000000008 else -1

# Runtime: 64 ms (100%)
import math

class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        coins.sort(reverse=True)     # 先给硬币排序，降序
        self.res = float("inf")      # 定义最小的使用硬币的数量为self.res

        def dfs(index,target,count):   # 定义深度优先搜索算法——>目标下降的速度更快
            coin = coins[index]
            print(f'index: {index}; coin: {coin}; target: {target}; count: {count}')
            if math.ceil(target / coin) + count >= self.res:
                return
            if target % coin == 0:
                self.res = count + target // coin
                return
            if index == n - 1:
                return
            for j in range(target // coin, -1, -1):
                dfs(index + 1,target - j * coin, count + j)

        dfs(0, amount, 0)
        return int(self.res) if self.res != float("inf") else -1


coins = [1, 2, 5]; amount = 11
# coins = [2]; amount = 3
# coins = [1]; amount = 0
# coins = [1]; amount = 1
# coins = [1]; amount = 2

s = Solution()
print(s.coinChange(coins, amount))