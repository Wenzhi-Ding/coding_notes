# https://leetcode-cn.com/problems/tree-of-coprimes/

# Runtime: 1204 ms (86%)
# Memory: 67 MB (99%)

# DFS
from math import gcd
from collections import defaultdict

def getCoprimes(nums, edges):

    ans = [-1 for _ in range(len(nums))]
    stack = defaultdict(list)  # 存储路径上每个值的深度，最后取互质数的最大深度即可
    coprime_map = {key: [x for x in range(1, 51) if gcd(x, key) == 1] for key in range(1, 51)}  # 预计算，省很多时间
    
    # 图有两种选择：
    # 1. 节点*节点: 1/0
    # 2. 节点: [节点]
    # 本题节点量10^5，如果按方式1则要造一个10^10元素的大矩阵，遍历起来极慢
    graph = defaultdict(set)
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)

    this_node, path = 0, [0]  # 初始状态
    stack[nums[0]].append(0)
    cnt, e = 0, len(edges)  # BFS计数

    while cnt < e:  # 遍历直到所有边都完成
        if graph[this_node]:  # 找到一条可行边
            k = graph[this_node].pop()
            graph[k].remove(this_node)
            cnt += 1

            _ans = -1  # 寻找该节点的最近互质祖先
            coprimes = coprime_map[nums[k]]  # 遍历预计算好的所有互质数
            for coprime in coprimes:
                tmp = stack[coprime]
                if tmp: _ans = max(_ans, tmp[-1])  # 取每个互质数的栈顶
            if _ans != -1: ans[k] = path[_ans]

            path.append(k)  # 更新路径和栈
            stack[nums[k]].append(len(path) - 1)
        else:  # 触及叶子节点，退回父节点
            pop_k = path.pop()  # 路径退栈
            _ = stack[nums[pop_k]].pop()  # 坐标退栈
            k = path[-1]  # 更新栈顶
            
        this_node = k  # 更新到下一个节点
        
    return ans
        
        

nums = [2,3,3,2]; edges = [[0,1],[1,2],[1,3]]  # [-1,0,0,1]
nums = [5,6,10,2,3,6,15]; edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]  # [-1,0,-1,0,0,0,-1]

print(getCoprimes(nums, edges))


# print(cnt, path)
# print('stack:', {key: stack[key] for key in stack if stack[key]})
# print('graph:', {key: graph[key] for key in graph if graph[key]})
# print('ans:', ans)
# print()