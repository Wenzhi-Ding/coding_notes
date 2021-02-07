from bisect import bisect_left, bisect_right
import numpy as np


def bs_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if x <= arr[mid]: hi = mid
        else: lo = mid + 1
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

for _ in range(10000):
    arr = sorted(np.random.randint(0, 10, np.random.randint(0, 10)))
    target = np.random.randint(0, 10)
    if bs_left(arr, target) != bisect_left(arr, target): print(arr, target)
    if bs_right(arr, target) != bisect_right(arr, target): print(arr, target)
