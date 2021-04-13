class Node:

    def __init__(self, value, left=None, right=None, height=1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height

class BTree:

    # 

    def __init__(self, root):
        if isinstance(root, Node):
            self.root = root
        elif isinstance(root, (int, float)):
            self.root = Node(root)
        self.height = 1

    def __str__(self):
        values = [self.root.value]
        queue = [self.root]
        while queue:  # 层序遍历（广度优先）
            cur_node = queue.pop(0)
            if cur_node.left:
                values.append(cur_node.left.value)
                queue.append(cur_node.left)
            if cur_node.right:
                values.append(cur_node.right.value)
                queue.append(cur_node.right)
        s = ''
        for idx, val in enumerate(values):
            if idx:
                if not (idx + 1) & idx:
                    s += '\n'
                else:
                    s += ' '
            s += f'{val}'
        return s

    def add(self, value):
        _node = Node(value)
        queue = [self.root]
        while queue:  # 层序遍历（广度优先）
            cur_node = queue.pop(0)  # 取出队列左边
            if not cur_node.left:  # 优先左节点
                cur_node.left = _node  # 放在队列右边
                _node.height = cur_node.height + 1
                self.height = max(_node.height + 1, self.height)
                return
            else:
                queue.append(cur_node.left)
            if not cur_node.right:  # 放在队列右边
                cur_node.right = _node
                _node.height = cur_node.height + 1
                self.height = max(_node.height + 1, self.height)
                return
            else:
                queue.append(cur_node.right)

    def from_list(lst):
        # 本质上是一个层序遍历
        tree = BTree(lst[0])
        for val in lst[1:]: tree.add(val)  # 待优化，这种方法太不效率了
        return tree


tree = BTree.from_list([1, 2, 3, 4, 5, 6, 7])

print(tree)
print(tree.height)