# https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

# Runtime: 252 ms (99%)

def hasAllCodes(s, k):
    target = 2 ** k  # 要把这个运算移出来存着，放在循环里会算很多遍，就很慢

    if len(s) < target + k - 1: return False  # 剪枝

    tmp = s[:k]
    res = set([tmp])
    for i in s[k:]:
        tmp = tmp[1:] + i
        res.add(tmp)
        if len(res) == target: return True
    return False
