# https://leetcode-cn.com/problems/container-with-most-water/

# Runtime: 62%-100%

class Solution:
    def maxArea(self, height):
        n = len(height)
        l, r = 0, n - 1
        l_val, r_val = height[l], height[r]
        
        ans = (r - l) * min(l_val, r_val)
        while l < r:
            if l_val > r_val:
                r -= 1
                r_val = height[r]
            else: 
                l += 1
                l_val = height[l]
            ans = max(ans, (r - l) * min(l_val, r_val))

        return ans

height = [1,8,6,2,5,4,8,3,7]  # 49
height = [1,1]  # 1
height = [4,3,2,1,4]  # 16
height = [1,2,1]  # 2

sol = Solution()
print(sol.maxArea(height))