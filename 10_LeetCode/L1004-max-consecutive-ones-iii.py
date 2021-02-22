# https://leetcode-cn.com/problems/max-consecutive-ones-iii/

# Runtime: 580 ms (95-100%)

def longestOnes(A, K):
    zeros = [key for key, var in enumerate(A) if var == 0]
    if K >= len(zeros): return len(A)  # 表示全部可以翻

    max_len = max(zeros[K], len(A) - zeros[-K - 1] - 1)
    for pos in range(1, len(zeros) - K):
        max_len = max(max_len, zeros[pos + K] - zeros[pos - 1] - 1)

    return max_len


# 更直观的滑窗思路
# Runtime: 596 ms (90-100%)

def longestOnes(A, K):
    left, right, count = 0, 0, 0
    for right in range(len(A)):
        if A[right] == 0:
            count += 1
        if count > K:
            if A[left] == 0:  # 这个left的设置很聪明
                count -= 1
            left += 1
        print(left, right)
    return right - left + 1

A = [1,1,1,0,0,0,1,1,1,1,0]; K = 2  # 6
# A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; K = 3  # 10
# A = [1,1,1,0,0,0,1,1,0,0,0]; K = 0

print(longestOnes(A, K))