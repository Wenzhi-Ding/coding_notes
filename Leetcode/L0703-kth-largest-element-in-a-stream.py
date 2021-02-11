# https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

from heapq import heapify, heappushpop, nlargest, heappush

# Runtime: 68-80 ms (97%-100%) 

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        nums = nlargest(self.k, nums)
        heapify(nums)
        self.nums = nums

    def add(self, val):
        if len(self.nums) < self.k: heappush(self.nums, val)
        elif val > self.nums[0]: heappushpop(self.nums, val)
        return self.nums[0]

# keys = ["KthLargest", "add", "add", "add", "add", "add"]
# param = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# keys = ["KthLargest","add","add","add","add","add"]
# param = [[1,[]],[-3],[-2],[-4],[0],[4]]

keys = ["KthLargest","add","add","add","add","add"]
param = [[3,[5,-1]],[2],[1],[-1],[3],[4]]

for key, var in enumerate(keys):
    if var != 'add':
        k, nums = param[key]
        obj = KthLargest(k, nums)
    else:
        ans = obj.add(param[key][0])
        print(ans)