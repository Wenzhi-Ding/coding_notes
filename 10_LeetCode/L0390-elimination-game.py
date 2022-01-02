# https://leetcode-cn.com/problems/elimination-game/

class Solution:
    def lastRemaining(self, n: int) -> int:
        le, ri, k = 1, n, 0
        n = len(range(le, ri + 1, 2 ** k))
        while n > 1:
            # 从左往右
            if k % 2 == 0:
                le += 2 ** k  # 无论如何左端都会往上移动一位
                if n % 2 == 1: ri -= 2 ** k
            # 从右往左
            else:
                ri -= 2 ** k
                if n % 2 == 1: le += 2 ** k
            k += 1
            n = len(range(le, ri + 1, 2 ** k))
        
        return le


# 进一步简化了
class Solution:
    def lastRemaining(self, n: int) -> int:
        remain, flag, res, step = n, True, 1, 1
        while remain > 1:
            if flag or remain % 2 == 1:  # 当 从左往右 或 为奇数长度，左端点右移——其实只需要关注左端点即可
                res += step
            flag = not flag
            step *= 2
            remain //= 2
        return res