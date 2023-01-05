# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

# 一般实现：通过创建专门的节点类来实现

# Runtime: 208 ms (24%)
# Memory: 32.9 MB (16%)
from collections import defaultdict


class Node:

    def __init__(self):
        self.child = defaultdict(int)
        self.is_end = False  # 用来标识树的结尾

    def get(self, char):
        return self.child[char]  # 返回某个节点

    def put(self, char):
        self.child[char] = Node()  # 在对应位置创建一个节点
        return self.child[char]

# 对应的Trie实现省略


# 高效实现：字典直接作为Node

# Runtime: 92-144 ms (55-100%)
# Memory: 27.8 MB (43%)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}  # 创建空的根节点

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pt = self.root
        for c in word:
            if not c in pt: pt[c] = {}  # 若不存在则建节点
            pt = pt[c]
        pt['#'] = '#'  # 用这个来标识结尾

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pt = self.root
        for c in word:
            if not c in pt: return False
            pt = pt[c]
        return '#' in pt  # 这里是search和startsWith的唯一差异

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pt = self.root
        for c in prefix:
            if not c in pt: return False
            pt = pt[c]
        return True


# Your Trie object will be instantiated and called as such:
word = 'abc'
obj = Trie()
obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
print(obj.search('abc'), obj.search('ab'), obj.search('abcd'))
print(obj.startsWith('abc'), obj.startsWith('ab'), obj.startsWith('abcd'))