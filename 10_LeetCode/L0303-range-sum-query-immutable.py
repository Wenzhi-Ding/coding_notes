# https://leetcode-cn.com/problems/range-sum-query-immutable/

# Runtime: 64 ms (91%)
# Memory: 18 MB (42%)

class NumArray:

    def __init__(self, nums):
        self.tmp = [0]
        for i in range(len(nums)):
            self.tmp.append(self.tmp[-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.tmp[j + 1] - self.tmp[i]
        # 如果直接sum(nums[i:j + 1])，运行时间是1000ms左右