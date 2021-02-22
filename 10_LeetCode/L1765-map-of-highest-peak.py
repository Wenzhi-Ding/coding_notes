# https://leetcode-cn.com/contest/biweekly-contest-46/problems/map-of-highest-peak/

# Runtime: 924 ms (100%)

def highestPeak(isWater):

    queue = []
    m = len(isWater)
    n = len(isWater[0])
    res = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1: queue.append((i, j))

    height = 0

    while queue:
        height += 1
        sub_queue = queue
        queue = []
        for i, j in sub_queue:
            if i > 0 and isWater[i - 1][j] == 0:
                res[i - 1][j] = height
                isWater[i - 1][j] = 1
                queue.append((i - 1, j))
            if i < m - 1 and isWater[i + 1][j] == 0:
                res[i + 1][j] = height
                isWater[i + 1][j] = 1
                queue.append((i + 1, j))
            if j > 0 and isWater[i][j - 1] == 0:
                res[i][j - 1] = height
                isWater[i][j - 1] = 1
                queue.append((i, j - 1))
            if j < n - 1 and isWater[i][j + 1] == 0:
                res[i][j + 1] = height
                isWater[i][j + 1] = 1
                queue.append((i, j + 1))

    return res

isWater = [[0,1],[0,0]]  # [[1,0],[2,1]]
isWater = [[0,0,1],[1,0,0],[0,0,0]]  # [[1,1,0],[0,1,1],[1,2,2]]
isWater = [[0,0],[1,1],[1,0]]

print(highestPeak(isWater))