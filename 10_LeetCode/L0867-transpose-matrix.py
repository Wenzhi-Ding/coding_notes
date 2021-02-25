# https://leetcode-cn.com/problems/transpose-matrix/

# Runtime: 40 ms (99%)
# Memory: 15.3 MB (51%)

def transpose(matrix):
    n, m = len(matrix), len(matrix[0])
    new_matrix = [[None for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            new_matrix[i][j] = matrix[j][i]

    return new_matrix


# 妙啊（慢不少，但短）
def transpose(matrix):
    return list(zip(*matrix))  # *用来unpack这个matrix变成n个m长度的列表，zip之后就成了m个n长度的元组


matrix = [[1,2,3],[4,5,6],[7,8,9]]  # [[1,4,7],[2,5,8],[3,6,9]]
# matrix = [[1,2,3],[4,5,6]]  # [[1,4],[2,5],[3,6]]


print(transpose(matrix))