# https://leetcode-cn.com/problems/degree-of-an-array/

# Runtime: 60 ms (96%)

from collections import defaultdict

def findShortestSubArray(nums):

    dct = defaultdict(list)
    for key, num in enumerate(nums):
        dct[num].append(key)
    
    max_num = []
    degree = 1
    for num in dct:
        tmp_degree = len(dct[num])
        if tmp_degree == degree:
            max_num.append(num)
        elif tmp_degree > degree:
            max_num = [num]
            degree = tmp_degree
    if degree == 1: return 1  # 这个剪枝使Runtime从88%上升到96%
    
    min_len = len(nums)
    for num in max_num:
        min_len = min(min_len, max(dct[num]) - min(dct[num]) + 1)

    return min_len


nums = [1,2,2,3,1]  # 2
nums = [1,2,2,3,1,4,2]  # 6

print(findShortestSubArray(nums))