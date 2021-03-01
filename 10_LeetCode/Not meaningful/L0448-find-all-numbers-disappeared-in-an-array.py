# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

# 要求不使用额外空间、时间复杂度为O(n)

# Runtime: 312-356 ms (95-100%)
# Memory: 25.4 MB (9%)——用了额外空间

def findDisappearedNumbers(nums):
    return list(set(range(1, len(nums) + 1)) - set(nums))


# 通过引入负数符号这一额外信息，在同一个空间里表示两组信息
# 存在的数字，对应的坐标会被翻转为负，最后把那些还是正数的坐标号返回即可

# Runtime: 568 ms (5%)
# Memory: 20.8 MB (98-100%)

def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] > 0: nums[abs(nums[i]) - 1] *= -1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < 0: del nums[i]
        else: nums[i] = i + 1
    return nums


# Runtime: 396 ms (69%)
# Memory: 22.5 MB (65%)

def findDisappearedNumbers(nums):
    for num in nums:  # 这部分等价于上面解法的第一部分（各方面都等价）
        nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
    return [idx + 1 for idx, num in enumerate(nums) if num > 0]  # 这里用列表解析式显著减少了用时，但用了额外的空间


nums = [4,3,2,7,8,2,3,1]  # [5,6]

print(findDisappearedNumbers(nums))