# https://leetcode-cn.com/problems/minimum-limit-of-balls-in-a-bag

# Runtime: 1488 ms (100%)

def minimumSize(nums, maxOperations):
    hi, lo = max(nums), 0
    while hi > lo:
        mid = (hi + lo) // 2
        if mid == 0: return 1
        ops = sum([(n - 0.1) // mid for n in nums])
        if ops > maxOperations:
            lo = mid + 1
        else:
            hi = mid
    return hi


nums = [9]; maxOperations = 2  # 3
# nums = [2,4,8,2]; maxOperations = 4  # 2
# nums = [7,17]; maxOperations = 2  # 7
nums = [1]; maxOperations = 10  # 1


print(minimumSize(nums, maxOperations))