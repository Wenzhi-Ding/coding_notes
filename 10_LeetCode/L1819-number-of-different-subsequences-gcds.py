# https://leetcode-cn.com/problems/number-of-different-subsequences-gcds/

from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums) -> int:
        nums = set(nums)
        n = max(nums)  # 数组大小的上限
        
        ans = 0
        for i in range(1, n + 1):  # 遍历所有候选公约数
            cur = -1

            # 检查该数是否能由数组中的子数组公约而成
            for j in range(i, n + 1, i):
                # 这里的step=i很重要，只遍历包含该约数的元素
                if j not in nums: continue
                if cur < 0:
                    cur = j // i  
                    # cur为j的“剩余因子”
                    # 只要保证该剩余因子与剩余遍历的某个“剩余因子”互质，就说明这是一个可实现的最大公约数
                    # 注意此处由于step=i的存在，其实是一定能整除的
                    # 之所以专门整除是为了满足gcd的输入条件
                else:
                    cur = gcd(cur, j // i)
                    # 更新“剩余因子”
                    # 若互质，则找到了目标组合，即cur被更新为1
                    # 若不互质，现有组合产生一个更新的“剩余因子”，并寻找与之互质的“剩余因子”
                if cur == 1:
                    ans += 1
                    break
        return ans


    def countDifferentSubsequenceGCDs2(self, nums) -> int:
        nums, n, ans = set(nums), max(nums), 0
        for i in range(1, n + 1):  # 简短写法
            if gcd(*[x for x in range(i, n + 1, i) if x in nums]) == i: ans += 1
        return ans

    def countDifferentSubsequenceGCDs3(self, nums) -> int:
        nums, n = set(nums), max(nums)  # 终极简短写法
        return sum([gcd(*[x for x in range(i, n + 1, i) if x in nums]) == i for i in range(1, n + 1)])


nums = [6,10,3]
nums = [5,15,40,5,6]

s = Solution()
print(s.countDifferentSubsequenceGCDs(nums))