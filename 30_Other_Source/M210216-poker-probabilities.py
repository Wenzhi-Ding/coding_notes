import numpy as np
from collections import Counter
from scipy.special import comb

# 52张牌中取出5张牌，包含至少两对的可能性（只有AA才算一对，AAA不算一对，AAAA不算两对）
# 即牌型是AABBC

N = 1000000

# 扑克牌是不放回抽样，所以不能直接简单的用union distribution的randint，而是用choice
# 且设置replace=False
deck = []
for x in range(1, 14):
    deck.extend([x] * 4)
arr = [np.random.choice(deck, size=5, replace=False) for _ in range(N)]

def hit(nums):
    tmp = Counter(nums)
    cnt = 0
    for key in tmp:
        if tmp[key] == 2: cnt += 1
    return cnt >= 2


arr2 = [hit(nums) for nums in arr]
print(sum(arr2) / N)
# for key, val in enumerate(arr2):
#     if val: print(arr[key])

# 解析解参考
print(comb(13, 2) * comb(11, 1) * comb(4, 2) * comb(4, 2) * comb(4, 1) / comb(52, 5))