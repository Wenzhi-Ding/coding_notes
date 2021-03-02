# https://leetcode-cn.com/problems/counting-bits/

# 要求：
# 1. 时间O(n)
# 2. 空间O(n)
# 3. 不使用内置（最好是C++实现）

# 思路
# 偶数+1到奇数，1的数量一定是+1
# 此外，1的数量上，偶数=偶数/2

# Runtime: 72 ms (84%)
# Memory: 21.2 MB (41%)

class Solution:
    def countBits(self, num: int):
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i // 2] + (i % 2))
        return ans


num = 2  # [0,1,1]
num = 5  # [0,1,1,2,1,2]

sol = Solution()
print(sol.countBits(num))
