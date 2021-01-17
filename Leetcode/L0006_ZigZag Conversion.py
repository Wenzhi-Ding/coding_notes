def convert(s, numRows):
    if numRows == 1:
        return s
    index = []
    for row in range(1, numRows + 1):
        index_1 = [row + x * 2 * (numRows - 1) - 1 for x in range(len(s) // numRows + 1)]
        index_2 = [row - 2 * (row - 1) + x * 2 * (numRows - 1) - 1 for x in range(len(s) // numRows + 1)]
        index_tmp = [num for num in sorted(list(set(index_1 + index_2))) if num >= 0 and num < len(s)]
        index += index_tmp
    return "".join([s[num] for num in index])

def convert_fast(s, numRows):
    if len(s) < numRows or numRows == 1:
        return s
    
    row = 0
    step = 1
    L = [''] * numRows
    for x in s:  # 跳出锯齿的形状看问题，把锯齿拍扁了，其实就是一个上下移动游标的过程
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        L[row] += x
        row = row + step
    return ''.join(L)

## Test Unit
args_lst = [
            ("PAYPALISHIRING", 3),
            ("PAYPALISHIRING", 4),
            ("A", 3),
            ("AB", 1)
            ]
for arg in args_lst:
    print(arg, convert(arg[0], arg[1]))


# 5
# 1       9
# 2     8 10
# 3   7   11
# 4 6     12
# 5       13


# 4

# 1     7
# 2   6 8
# 3 5   9
# 4     10

# 3

# 1   5
# 2 4 6
# 3   7

# 2
# 1 3
# 2 4