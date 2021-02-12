# https://leetcode-cn.com/problems/minimize-deviation-in-array/


# Runtime: 304 ms (94%)

def minimumDeviation(nums):
    nums = [num * 2 if num % 2 == 1 else num for num in list(set(nums))]
    _min = min(nums)
    for key, num in enumerate(nums):
        while num % 2 == 0 and num // 2 > _min: num //= 2
        nums[key] = num

    ans = max(nums) - _min
    while True:
        _max = max(nums)
        ans = min(ans, _max - _min)
        if _max % 2 == 1: return ans
        nums[nums.index(_max)] //= 2
        _min = min(_min, _max // 2)


# Runtime: 192 ms (100%)

from heapq import heapify, heapreplace
def minimumDeviation(nums):
    heapify(nums)
    # 对最小数乘2，并维持堆结构。直到最小数为偶数
    while nums[0] % 2 == 1:  # 可用位运算nums[0] & 1
        heapreplace(nums, nums[0] * 2)  # 可用位运算nums[0] << 1: 
    
    # 下面思路都一样，但是用堆结构减少了每次取max和找max的坐标的开销
    down = nums[0]
    nums = [-x for x in nums]  # 最小堆转为最大堆，大数排前面
    heapify(nums)
    res = -nums[0] - down
    while nums[0] % 2 == 0:
        down = min(down, -nums[0] // 2)
        heapreplace(nums, nums[0] // 2)
        res = min(res, -nums[0] - down)
    return res

nums = [1,2,3,4]  # 1
nums = [4,1,5,20,3]  # 3
nums = [2,10,8]  # 3
nums = [2,4,8]  # 0
nums = [2,10,8,9]  # 7
# nums = [3,5,6]  # 1
# nums = [10,12]  # 1
# nums = [1,1,1]  # 0
# nums = [1024,1024,1025]  # 1
# nums = [10,4,3]  # 2

print(minimumDeviation(nums))