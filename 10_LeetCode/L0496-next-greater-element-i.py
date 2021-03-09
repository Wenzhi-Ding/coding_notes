# https://leetcode-cn.com/problems/next-greater-element-i/submissions/

# Runtime: 99%

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        nxt, stack = {}, []
        for num in nums2:
            while stack and num > stack[-1]: nxt[stack.pop()] = num
            stack.append(num)
        return [nxt[i] if i in nxt else -1 for i in nums1]