# https://leetcode-cn.com/problems/as-far-from-land-as-possible/

# Runtime: 256 ms (92%)

def maxDistance(grid):
    N, lands = len(grid), []
    for i in range(N):
        for j in range(N):
            if grid[i][j]: lands.append((i, j))
    if len(lands) == 0 or len(lands) == N * N: return -1

    # 层序遍历——BFS
    cur_layer_queue, nxt_layer_queue = lands, []  # 对重复值不敏感的/序列不够长的，不用HashSet可能会快一些（比如重复值会迅速被剪枝剪掉）
    layer = 0  # 从陆地出发，所以初始距离是 (=-1 + 1)

    while True:
        for cur_i, cur_j in cur_layer_queue:
            for tmp_i, tmp_j in [(cur_i + 1, cur_j), (cur_i - 1, cur_j), (cur_i, cur_j + 1), (cur_i, cur_j - 1)]:
                if tmp_i < 0 or tmp_i >= N or tmp_j < 0 or tmp_j >= N: continue
                if grid[tmp_i][tmp_j] == 0:
                    nxt_layer_queue.append((tmp_i, tmp_j))  # 将周围未遍历海洋网格加入队列
                    grid[tmp_i][tmp_j] = layer + 1  # 被放入队列就算是被走到了，更新数值防止重复走到
        if nxt_layer_queue:
            layer += 1  # 层序遍历完一层，层数+1
            cur_layer_queue, nxt_layer_queue = nxt_layer_queue, []
        else: return layer  # 出口
    

grid = [[1,0,1],[0,0,0],[1,0,1]]  # 2
grid = [[1,0,0],[0,0,0],[0,0,0]]  # 4
grid = [[1,0,0],[0,0,0],[0,1,0]]  # 2
grid = [[1,0,0,1],[0,0,0,0],[0,1,0,0],[0,0,0,0]]  # 3
# grid = [[0, 0], [0, 0]]

print(maxDistance(grid))