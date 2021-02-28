# https://leetcode-cn.com/problems/monotonic-array/

# Runtime: 468 ms (99%)
# Memory: 20.8 MB (73%)

class Solution:
    def isMonotonic(self, A):
        l = len(A)
        if l <= 2: return True

        inc = 1 if A[0] <= A[1] else 0
        dec = 1 if A[0] >= A[1] else 0
        
        num = A[1]
        for i in range(2, l):
            tmp = A[i]
            if inc and tmp < num: inc = 0
            if dec and tmp > num: dec = 0
            if inc == 0 and dec == 0: return False
            num = tmp
        
        return True

# Runtime: 456-480 ms (93-100%)
# Memory: 20.9 MB (51%)

class Solution:
    def isMonotonic(self, A):
        B = sorted(A)
        return (A == B or A == B[::-1])


A = [1,2,2,3]
A = [6,5,4,4]
A = [1,3,2]
A = [1,2,4,5]
A = [1,1,1]

sol = Solution()
print(sol.isMonotonic(A))