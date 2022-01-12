# https://leetcode-cn.com/problems/increasing-triplet-subsequence

# 贪心：

# first维护的是在已遍历过的序列中，能够达到1递增长度的最小数字
# 这样一来，后面任何比first大的数字都至少能够达到2递增长度

# second维护的是在已遍历过的序列中，能够达到2递增长度的最小数字
# 这样一来，后面任何比second大的数字都至少能够达到3递增长度

# 同理该问题还可以延伸至N递增长度，维护一个N长度的列表即可

def increasingTriplet(nums) -> bool:
    first, second = float('inf'), float('inf')
    for num in nums:
        if num > second: return True
        if num > first: second = num
        else: first = num
    return False