# https://leetcode-cn.com/problems/pascals-triangle-ii/

# 要求O(k)的空间复杂度

# Runtime: 36 ms (81%)
# Memory: 14.8 MB (37%)——已经是O(k)的空间复杂度了

def getRow(rowIndex: int):
    for n in range(rowIndex + 1):
        row = [row[i - 1] + row[i] if i not in [0, n] else 1 for i in range(n + 1)]  # 列表解析式意味着额外的空间开销
    return row

# for i in range(34):
#     print(getRow(i))