# https://leetcode-cn.com/problems/tree-of-coprimes/

# DFS
from math import gcd

def getCoprimes(nums, edges):

    n = len(nums)
    ans = [-1 for _ in range(n)]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in edges:
        graph[i][j] = 1
        graph[j][i] = 1

    this_node = 0
    flag = 0
    path = []
    cnt = 0

    while cnt <= len(edges):
        if not flag: path.append(this_node)
        flag = 1
        if sum(graph[this_node]):
            for k, v in enumerate(graph[this_node]):
                if v == 1:
                    next_node = k
                    graph[this_node][k] = 0
                    graph[k][this_node] = 0
                    cnt += 1
                    flag = 0
                    print(next_node)
                    for i in path[::-1]:  # 寻找该节点的最近互质祖先
                        if gcd(nums[i], nums[next_node]) == 1:
                            ans[next_node] = i
                            break
                    break
        
        if flag:  # 没找到，说明是叶子节点了
            _ = path.pop()
            if not path: break
            next_node = path[-1]

        this_node = next_node  # 更新到下一个节点
        
        
    return ans
        
            




nums = [2,3,3,2]; edges = [[0,1],[1,2],[1,3]]  # [-1,0,0,1]
nums = [5,6,10,2,3,6,15]; edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]  # [-1,0,-1,0,0,0,-1]
nums = [9,16,30,23,33,35,9,47,39,46,16,38,5,49,21,44,17,1,6,37,49,15,23,46,38,9,27,3,24,1,14,17,12,23,43,38,12,4,8,17,11,18,26,22,49,14,9]
edges = [[17,0],[30,17],[41,30],[10,30],[13,10],[7,13],[6,7],[45,10],[2,10],[14,2],[40,14],[28,40],[29,40],[8,29],[15,29],[26,15],[23,40],[19,23],[34,19],[18,23],[42,18],[5,42],[32,5],[16,32],[35,14],[25,35],[43,25],[3,43],[36,25],[38,36],[27,38],[24,36],[31,24],[11,31],[39,24],[12,39],[20,12],[22,12],[21,39],[1,21],[33,1],[37,1],[44,37],[9,44],[46,2],[4,46]]

print(getCoprimes(nums, edges))