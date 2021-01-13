import numpy as np

# https://bbs.nga.cn/read.php?tid=25092485
# 暴击概率：p
# 一共攻击K次，求至少暴击L次，其不存在连续M次不暴击的概率

# 动态规划求解

# 子问题
# 第k次时已经暴击l次，且此前已经连续不暴击m次的概率f(k, l, m)从k-1次如何转移过来
# f(k, l, m) = (m < M)(1 - p)f(k - 1, l, m - 1) + (m == 0)pf(k - 1, l - 1, [0, M - 1])

# 隐含边界条件
# 0 <= l <= k
# max(0, k - M * l) <= m <= min(M - 1, k - l)

### 解题部分

# K: 总攻击次数
# L: 至少暴击次数
# M: 连续未暴击小于此数
# p: 暴击概率
# k: 已攻击次数
# l: 已暴击次数
# m: 已连续未暴击次数

K, L, M, p = 23, 11, 4, 0.45

arr = np.zeros((K + 1, K + 1, M))
arr[1][1][0], arr[1][0][1] = p, 1 - p  # 临界状态

def f(k, l, m):
    '''求某种特定情况的概率'''
    if (0 <= l <= k) & (max(0, k - M * l) <= m <= min(M - 1, k - l)):  # 边界条件
        if arr[k][l][m] == 0:  # 剪枝
            if m == 0:  # 状态转移1
                for _m in range(M):  # 可以不考虑m的实际边界，直接上最大边界
                    arr[k][l][m] += f(k - 1, l - 1, _m) * p
            if 0 < m:  # 状态转移2
                arr[k][l][m] += f(k - 1, l, m - 1) * (1 - p)
    return arr[k][l][m]


result = 0
for i in range(L, K + 1):  # 加总所有暴击次数大于等于11的情况的概率
    for j in range(M):
        result += f(23, i, j)
print(result)


