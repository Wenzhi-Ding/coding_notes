# https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

# 规模有点大，数字有限，考虑转字典

import collections
import math

# Runtime: 124 ms
# Memory: 20.3 MB

class Solution:
    def minOperations(self, nums1, nums2):

        diff = sum(nums2) - sum(nums1)  # 求差
        if diff < 0: nums1 = nums2 + [7 - x for x in nums1]  # 要上调nums2或下调nums1的数字
        elif diff > 0: nums1 = nums1 + [7 - x for x in nums2]  # 要下调nums2或上调nums1的数字
        else: return 0

        dct = collections.Counter(nums1)  # 统一成往上调了
        del dct[6]  # 删掉没用的
        dct = {k: dct[k] for k in sorted(dct)}  # 排个序
        diff = abs(diff)

        ans = 0
        for i in dct:
            dem = math.ceil(diff / (6 - i))  # 需要dem个数字i才能抹平diff
            if dem > dct[i]:  # 如果不够，就先扣着，接着看数字i+1
                diff -= dct[i] * (6 - i)
                ans += dct[i]
            elif dem <= dct[i]:  # 如果够了就可以退出了
                ans += dem  # 把需求数加上
                diff = 0
                break

        return -1 if diff else ans  # diff不为0表示穷尽了也抹不平，则返回-1


nums1 = [1,2,3,4,5,6]; nums2 = [1,1,2,2,2,2]  # 3
# nums1 = [1,1,1,1,1,1,1]; nums2 = [6]  # -1
# nums1 = [6,6]; nums2 = [1]  # 3
# nums1 = [5,6,4,3,1,2]; nums2 = [6,3,3,1,4,5,3,4,1,3,4]  # 4
nums1 = [5,2,1,5,2,2,2,2,4,3,3,5]; nums2 = [1,4,5,5,6,3,1,3,3]  # 1
nums1 = [6]; nums2 = [5,4,1,2,5,3,2,5,1,5,6,6,3,6,1,6]  # -1

sol = Solution()
print(sol.minOperations(nums1, nums2))