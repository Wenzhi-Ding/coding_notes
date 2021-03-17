# https://leetcode-cn.com/problems/design-hashset/

# 使用的哈希函数：mod
# 每个数字取余得到k，加入快表第k位中的列表（慢表）
# 对这个列表再做普通的查询
# 所以时间复杂度是O(m)，m是慢表的大小，只要除数够大，这个也是接近常数时间的
# 性能已经接近内置的HashSet了

class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 1000
        self.bucket = [[] for _ in range(self.mod)]

    def add(self, key: int) -> None:
        k = key % self.mod
        if key not in self.bucket[k]:
            self.bucket[k].append(key)

    def remove(self, key: int) -> None:
        k = key % self.mod
        if key in self.bucket[k]:
            self.bucket[k].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        k = key % self.mod
        return key in self.bucket[k]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)