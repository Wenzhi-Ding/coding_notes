# https://leetcode-cn.com/problems/form-array-by-concatenating-subarrays-of-another-array/

# Runtime: 44 ms (84%)

def canChoose(groups, nums):
    
    for i in range(len(groups)):
        group = groups[i]
        while nums:
            num = group[0]
            if num in nums: nums_idx = nums.index(num)
            else: return False
            nums = nums[nums_idx:]
            for k, v in enumerate(group):
                if k >= len(nums): return False
                if v != nums[k]:
                    nums = nums[1:]
                    break
            else:
                nums = nums[k + 1:]
                break
        if i < len(groups) - 1 and len(nums) == 0: return False

    return True

groups = [[1,-1,-1],[3,-2,0]]; nums = [1,-1,0,1,-1,-1,3,-2,0]  # True
groups = [[10,-2],[1,2,3,4]]; nums = [1,2,3,4,10,-2]  # False
groups = [[1,2,3],[3,4]]; nums = [7,7,1,2,3,4,7,7]  # False

print(canChoose(groups, nums))