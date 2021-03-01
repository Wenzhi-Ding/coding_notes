# https://leetcode-cn.com/problems/max-consecutive-ones/

# Runtime: 360 ms (93%)

def findMaxConsecutiveOnes(nums):
    ans, tmp = 0, 0
    for i in nums:
        if i == 1: tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    return max(ans, tmp)


nums = [1,1,0,1,1,1]
nums = [0]
# nums = [1]

print(findMaxConsecutiveOnes(nums))
