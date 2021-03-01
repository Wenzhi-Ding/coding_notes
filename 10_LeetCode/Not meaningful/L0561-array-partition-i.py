# https://leetcode-cn.com/problems/array-partition-i/

# Runtime: 84 ms (55%)

def arrayPairSum(nums):
    nums = sorted(nums)
    return sum([x for i, x in enumerate(nums) if i % 2 == 0])


# Runtime: 72 ms (93%)

def arrayPairSum(nums):
    return sum(sorted(nums)[::2])


nums = [1,4,3,2]
nums = [6,2,6,5,1,2]
nums = [1, 1]

print(arrayPairSum(nums))