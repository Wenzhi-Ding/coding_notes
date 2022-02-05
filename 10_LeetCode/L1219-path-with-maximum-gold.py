# https://leetcode-cn.com/problems/path-with-maximum-gold

def getMaximumGold(grid):
    M = len(grid)
    N = len(grid[0])
    ans = 0

    def helper(i, j, gold):
        # 走过该节点，更新目前累计的最大gold，并与全局最大做比较
        rec = grid[i][j]
        gold += rec
        nonlocal ans
        ans = max(ans, gold)

        # 注意此处直接将原始的grid[i][j]置0了
        # 回溯中自动代入grid拷贝，而不是引用，所以可以通过这样的方式记录已经走过的路径
        grid[i][j] = 0
        for a, b in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            if 0 <= i + a < M and 0 <= j + b < N and grid[i + a][j + b] != 0:
                helper(i + a, j + b, gold)
        grid[i][j] = rec  # 需要在回溯完该节点所有路径后，复原grid[i][j]，以供后续其他起点使用

    for i in range(M):
        for j in range(N):
            if grid[i][j] != 0:
                # 剪枝：任意点的出入度有0、1、2、3、4五种，其中3和4的出入度都肯定不会是最优的起点，所以可以略过
                deg = 0
                for a, b in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    if 0 <= i + a < M and 0 <= j + b < N and grid[i + a][j + b] != 0:
                        deg += 1
                if deg > 2: continue

                # 回溯
                helper(i, j, 0)

    return ans


tc = [
    [[0,6,0],[5,8,7],[0,9,0]]
    , [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    , [[5,3,36,26,27],[11,31,23,30,4],[5,7,21,38,10],[39,30,10,17,13],[16,0,0,26,1],[25,0,10,0,0]]
]

for c in tc:
    print(getMaximumGold(c))