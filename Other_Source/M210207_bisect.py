from bisect import bisect_left, bisect_right
import numpy as np

# 经验：不要用递归做，时间和空间开销都大
# 而且需要引入额外参数来返回坐标，写起来麻烦
# 用两个游标即可表示所有状态

def bs_left(arr, x):
    lo, hi = 0, len(arr)  # 从两端开始
    while lo < hi:
        mid = (lo + hi) // 2
        if x <= arr[mid]: hi = mid
        else: lo = mid + 1  # 不要漏+1
    return lo


def bs_right(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < arr[mid]: hi = mid
        else: lo = mid + 1
    return lo

# arr = [1, 1, 2, 3, 3, 5, 5, 6, 9]
# arr = []
# target = 5

# print(bs_left(arr, target), bisect_left(arr, target))
# print(bs_right(arr, target), bisect_right(arr, target))

# 测试与Python原生实现的一致性
for _ in range(10000):
    arr = sorted(np.random.randint(0, 10, np.random.randint(0, 10)))
    target = np.random.randint(0, 10)
    if bs_left(arr, target) != bisect_left(arr, target): print(arr, target)
    if bs_right(arr, target) != bisect_right(arr, target): print(arr, target)
