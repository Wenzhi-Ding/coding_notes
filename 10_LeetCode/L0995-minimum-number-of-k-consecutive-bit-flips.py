# https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/


# TLE --> O(NK)

def minKBitFlips(A, K):
    ans = 0
    for i in range(len(A) - K + 1):
        if A[i] == 0:
            ans += 1
            for j in range(i, i + K):  # 模拟操作太费时，应回归数学本质
                A[j] = 1 - A[j]
    return -1 if 0 in A[-K:] else ans


# Runtime: 792 ms (100%) --> O(N)
# Memory: 15.4 MB (82%) --> O(1)

def minKBitFlips(A, K):
    cur_flip, ans, len_A = 0, 0, len(A)
    for i in range(len_A):
        if i >= K and A[i - K] == 2: cur_flip -= 1  # 挪向下一位，参考K个位置以前进行调减
        
        if (A[i] + cur_flip) % 2 == 0:  # 当前位需要翻转
            if i >= len_A - K + 1: return -1
            cur_flip += 1  # 窗口中的翻转次数
            ans += 1
            A[i] = 2  # 标记该位置进行了翻转，方便K个位置以后调减cur_flip的值
            
    return ans


A = [0,1,0]; K = 1  # 2
# A = [1,1,0]; K = 2  # -1
# A = [0,0,0,1,0,1,1,0]; K = 3  # 3
# A = [0]; K = 3  # -1
# A = [0]; K = 1  # 1
# A = [0,1,1,0]; K = 3  # 2

print(minKBitFlips(A, K))