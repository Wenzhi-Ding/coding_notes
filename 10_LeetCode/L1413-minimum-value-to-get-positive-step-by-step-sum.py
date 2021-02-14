# https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum

# Runtime: 36 ms (86%)

def minStartValue(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return max(1, -min(nums) + 1)
