# https://leetcode-cn.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

# 要点：
# 1、问题本质：无论是三角形、四边形还是单纯的边，目标值都是点的度数加和
# 2、问题转化：1) 算出点的度数；2) 找到连通的三点
# 3、数据结构：需要尽可能减少索引的次数，用矩阵表示图的连通性
# 4、遍历剪枝：任意一点，若其所在三角形已经都遍历过了，那之后就不用再遍历这个点了
#    （时间复杂度从O(N^3)下降到约1/3）
# 5、进阶剪枝：1) 三角形 = 三个点 = 一条边 + 一个点；2) 存在某个成分的度数大于当前最优目标值时，
#    整体也一定不会小于当前最优值，如果从小到大排序，则可以避免后面所有遍历
#    （遍历次数下降到原来的1%）


# Runtime: 4552 ms

def minTrioDegree(n, edges):
    tmp = [[0] * (n + 1) for _ in range(n + 1)]  # 开个n+1的二维矩阵，每个维度的第一个元素记录度数，其他维度表示连通
    for edge in edges:
        x, y = edge
        tmp[x][0] += 1
        tmp[y][0] += 1
        tmp[x][y] += 1
        tmp[y][x] += 1
    ans = n * 3
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if tmp[i][j] > 0:
                for k in range(j + 1, n + 1):  # 虽然最高需要循环1000多万次，但只要后面的索引不耗时，其实暴力枚举并不慢
                    if tmp[i][k] > 0 and tmp[j][k] > 0:
                        ans = min(ans, tmp[i][0] + tmp[j][0] + tmp[k][0] - 6)
                        if ans <= 0: return 0
    return ans if ans < n * 3 else -1


# Runtime: 264 ms (100%)

from collections import defaultdict

def minTrioDegree(n, edges):
    graph = defaultdict(set)
    for x, y in edges:
        graph[x].add(y)  # graph[x]存储了所有跟x连通的节点
        graph[y].add(x)
    nodes = sorted([[len(graph[x]), x] for x in graph])  # nds的每个元素是[点的度数, 点的连通集]
    edges = sorted([[len(graph[x]) + len(graph[y]), x, y] for x, y in edges])  # nnds的每个元素是[边的总度数, 节点1连通集, 节点2连通集]
    ans = n * 3 + 1
    for ed, x, y in edges:
        if ed >= ans: break  # 边的度数已经大于目前最小返回值了，结束遍历。因为是排过序的，后面只会比前面更大
        for nd, z in nodes:
            if ed + nd >= ans:  break  # 同上
            if z in graph[x] and z in graph[y]:
                ans = min(ans, ed + nd)
                break
    return ans - 6 if ans < n * 3 + 1 else -1


n = 6; edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
n = 7; edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
n = 3; edges = [[3,2],[2,1]]

print(minTrioDegree(n, edges))