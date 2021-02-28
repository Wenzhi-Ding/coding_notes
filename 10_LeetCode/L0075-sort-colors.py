# https://leetcode-cn.com/problems/sort-colors/


# 原地排序（常数空间）+一次遍历

# Runtime: 28 ms (99%)
# Memory: 14.9 MB (9%)

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = [0 for _ in range(2)]  # 可以不要最大数的指针，因为一定不会向前交换

        for i in range(len(nums)):  # 每一步都通过向前交换保证前面的部分是排序的
            for j in range(2):
                if nums[i] == j and idx[j] <= i:
                    if idx[j] < i: nums[idx[j]], nums[i] = nums[i], nums[idx[j]]
                    idx[j] += 1
                    for k in range(j + 1, 2): idx[k] = max(idx[k], idx[j])

        return nums


nums = [2,0,2,1,1,0]  # [0,0,1,1,2,2]
# nums = [2,0,1]  # [0,1,2]
# nums = [0]  # [0]
# nums = [1]  # [1]


s = Solution()
print(s.sortColors(nums))