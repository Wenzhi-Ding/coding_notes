# https://bbs.nga.cn/read.php?tid=25092485

# 用矩阵来实现快速模拟复杂逻辑

### 问题1
# 暴击概率：p
# 一共攻击K次，求至少暴击L次且不存在连续M次不暴击的概率

import numpy as np

N = 10000000
series = (np.random.rand(N, 23) <= 0.45).astype(np.uint8)

total_ch_le_11 = np.sum(series, axis=1) >= 11
no_4_ng = np.logical_not(np.any((series[:, :-3] + series[:,1:-2] + series[:,2:-1] + series[:,3:]) == 0, axis=1))
whole_good = np.logical_and(total_ch_le_11, no_4_ng)
print(np.sum(whole_good.astype(np.float64)) / N)


### 问题2
# 暴击概率：p
# 一共攻击K次，求任一连续的M次攻击中都至少暴击L次的概率

N = 1000000
K, M, L, p = 11, 7, 3, 0.45
hits = (np.random.rand(N, K) <= p).astype(int)

hit_counts = hits[:, :1 - M] + hits[:, M - 1:]
for m in range(1, M - 1):
    hit_counts += hits[:, m:1 - M + m]
all_meet = np.all(hit_counts >= L, axis=1)
any_meet = np.any(hit_counts >= L, axis=1)
print(np.sum(all_meet) / N)  # np.sum比原生的sum快很多
print(np.sum(any_meet) / N)