# Solution 1
# Runtime: 224 ms (64.27%)
# Memory: 16.3 MB (9.68%)

def sortedSquares(nums):
    return sorted([x ** 2 for x in nums])


# Solution 2
# Runtime: 236 ms (41.54%)
# Memory: 16.3 MB (61.85%)

# def sortedSquares(nums):
#     f = 0
#     c = l = len(nums) - 1
#     results = [0] * len(nums)
#     while f <= l:
#         if nums[f] + nums[l] > 0:
#             results[c] = nums[l] ** 2
#             l -= 1
#         else:
#             results[c] = nums[f] ** 2
#             f += 1
#         c -= 1
#     return results


# nums = [-4,-1,0,3,10]
nums = [-7,-3,2,3,11]

print(sortedSquares(nums))