# https://leetcode-cn.com/problems/flipping-an-image/

# Runtime: 44-64 ms (45~100%)

def flipAndInvertImage(A):
    return [[1 - x for x in y][::-1] for y in A]

A = [[1,1,0],[1,0,1],[0,0,0]]
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(flipAndInvertImage(A))