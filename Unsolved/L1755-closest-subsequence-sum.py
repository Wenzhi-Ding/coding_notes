# https://leetcode.com/problems/closest-subsequence-sum/

import itertools
from bisect import bisect_left

# 如果直接遍历所有子集的和，时间复杂度是O(2^n)

# 分治：将集合分成两个子集，分别求这两个子集的所有子集的和，得到A和B
# 二分查找：对A排序，从B中查找最接近目标的组合
# 这样就保证了能够遍历任意组合。本质上是节约了重复的遍历
# 时间复杂度是O(n*2^(n/2))

# Runtime: 3812 ms (14%)

def minAbsDifference(nums, goal):

    nums_left = nums[:len(nums) // 2]
    nums_right = nums[len(nums) // 2:]

    # def powerset(nums):
    #     return itertools.chain.from_iterable(itertools.combinations(nums, r) for r in range(len(nums) + 1))
    # sums_left, sums_right = sorted(list(set(sum(x) for x in powerset(nums_left)))), set(sum(x) for x in powerset(nums_right))

    def powerset(nums):  # 
        ans = {0}
        for x in nums: ans |= {x + y for y in ans}  # 通过迭代操作一个不断更新的对象，实现“所有子集和”
        return ans
    sums_left, sums_right = sorted(list(powerset(nums_left))), powerset(nums_right)

    print(len(sums_left), len(sums_right))

    def bs_left(arr, x):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if x <= arr[mid]: hi = mid
            else: lo = mid + 1
        return lo
    
    ans = float('inf')
    for x in sums_right:
        k = bs_left(sums_left, goal - x)  # 还是有效率问题，3812 ms (14%)
        # k = bisect_left(sums_left, goal - x)  # 1104 ms (28.57%)
        if k < len(sums_left): ans = min(ans, abs(goal - sums_left[k] - x))
        if k > 0: ans = min(ans, abs(goal - sums_left[k - 1] - x))
    
    return ans

# Runtime: 44 ms
# 尚未理解原理
def minAbsDifference(nums, goal):
    n = len(nums)
    nums.sort(key=lambda x: -abs(x))
    neg = [0 for _ in range(n+1)]
    pos = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        if nums[i] < 0:
            neg[i] = neg[i+1] + nums[i]
            pos[i] = pos[i+1]
        else:
            pos[i] = pos[i+1] + nums[i]
            neg[i] = neg[i+1]
    ans = abs(goal)
    s = set([0])
    print(nums, neg, pos)

    def check(a, b):
        if b < goal - ans or goal + ans < a:
            return False
        return True

    for i in range(n):
        sl = [x for x in s if check(x+neg[i], x+pos[i])]
        if len(sl) == 0:
            break
        s = set(sl)
        for x in sl:
            y = x + nums[i]
            if abs(y - goal) < ans:
                ans = abs(y - goal)
            if ans == 0:
                return 0
            s.add(y)
    return ans

nums = [5,-7,3,5]; goal = 6; ans = 0
# nums = [7,-9,15,-2]; goal = -5; ans = 1
# nums = [1,2,3]; goal = -7; ans = 7
# nums = [1556913,-259675,-7667451,-4380629,-4643857,-1436369,7695949,-4357992,-842512,-118463]; goal = -9681425; ans = 10327
# nums = [6099,-2975,6343,2048,9628,5418,-2082,1088,-4228,9848,-4063,9023,4782,7523,-5104,-8095,6513,682,7317,-5575,-3015,333,6178,5741,814,-6121,-5809,-5409,-1597,-2627,-7116,7656,-8361,8450,-4362,-6195]; goal = 849461796; ans = 849356312
# nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; goal = 1000000000; ans = 1000000000
# nums = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]; goal = 20; ans = 2
# nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,-1,-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024,-2048,-4096,-8192,-16384,-32768,-65536,-131072,-262144,-524288]; goal = 1048574; ans = 0

a = minAbsDifference(nums, goal)
print(a, a == ans)
# print(sum(nums))