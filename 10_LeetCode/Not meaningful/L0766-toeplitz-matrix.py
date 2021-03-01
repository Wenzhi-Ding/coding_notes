# https://leetcode-cn.com/problems/toeplitz-matrix/

# Runtime: 40 ms (87%)
# Memory: 14.7 MB (56%)

def isToeplitzMatrix(matrix):

    m, n = len(matrix), len(matrix[0])
    for j in range(-m, n):
        num = -1
        for i in range(m):
            if 0 <= i + j < n:
                tmp = matrix[i][i + j]
                if num == -1: num = tmp
                elif num != tmp: return False
    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]  # True
matrix = [[1,2],[2,2]]  # False
matrix = [[1]]  # True
matrix = [[11,74,0,93],[40,11,74,7]]  # False

print(isToeplitzMatrix(matrix))