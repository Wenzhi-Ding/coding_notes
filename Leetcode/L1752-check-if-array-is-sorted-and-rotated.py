# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

# Runtime: 36 ms (100%)

def check(nums):
    return False if sum([nums[i] > nums[i + 1] for i in range(-1, len(nums) - 2)]) > 1 else True

# Equivalent

def check(nums):
    neg = sum([nums[i] > nums[i + 1] for i in range(-1, len(nums) - 2)])
    if neg > 1: return False
    return True

nums = [3,4,5,1,2]  # True
# nums = [2,1,3,4]  # False
# nums = [1,2,3]  # True
# nums = [1,1,1]  # True
# nums = [2,1]  # True
# nums = [6,10,6]  # True

print(check(nums))
