# https://leetcode-cn.com/problems/first-common-ancestor-lcci/

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归，写起来特别简单，本质上也是深度优先搜索
# 速度与非递归的DFS是一样的，空间上差不少
# https://leetcode-cn.com/problems/first-common-ancestor-lcci/solution/di-gui-jie-fa-python-3-c-by-z1m/

# 子问题：给定任意一个节点root，p、q在左支还是右支
# 模式一：root就是p、q之一，另一个也在root下，那root就是最近共同祖先
# 模式二：一左一右，那root就是最近共同祖先
# 模式三：某一边没有，那么就去另一边的子节点作为root继续搜
# 每次子问题需要返回的状态：该节点下是否有p、q之一
# 何时可以确定返回：
#     root=p或root=q或p、q分别在root左右，则可以返回root给上一层
#     p和q不存在于root（包括本节点），则返回None给上一层

# 简而言之，就是通过递归的方式保存了父节点的信息
# 然后将有效的父节点逐层上传，直到汇合
# 最后一起传到最外层的出口
# （跟我自己想的通过列表存路径是等价的，但这个太简洁了）

# Runtime: 72 ms (92%)
# Memory: 25.4 MB (75%)

def lowestCommonAncestor(root, p, q):
    if not root or p == root or q == root: return root  # 这里的not root保证了最后找不到的时候能返回None
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right: return root
    return left if left else right
    # 这个else right保证了查不到的时候，能最终返回None
    # 也可以严格的写成，if right: return right; return None


# 深度优先遍历，每次找到其中一点都保存其路径（即当时的队列）
# 最后取两条路径最后一个交点

# Runtime: 76 ms (83%)
# Memory: 18.5 MB (99%)

def lowestCommonAncestor(root, p, q):
    queue = [root]
    visited = []
    p_path, q_path = [], []
    while queue and not (p_path and q_path):  # 这里用空判断比用列表长度积判断要快
        node = queue[-1]

        if not p_path and node.val == p.val: 
            p_path = queue[:]
        if not q_path and node.val == q.val:
            q_path = queue[:]

        if node.left and node.left not in visited:
            queue.append(node.left)
            continue
        if node.right and node.right not in visited:
            queue.append(node.right)
            continue

        if node == queue[-1] or not (node.right or node.left):
            visited.append(queue.pop())
    
    for i in range(min(len(p_path), len(q_path))):
        if p_path[i] != q_path[i]: return p_path[i - 1]
    return p_path[i]
