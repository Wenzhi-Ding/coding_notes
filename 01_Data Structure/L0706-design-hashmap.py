# https://leetcode-cn.com/problems/design-hashmap/

# 使用的哈希函数：mod
# 每个数字取余得到k，加入快表第k位中的列表（慢表）
# 对这个列表再做普通的查询
# 所以时间复杂度是O(m)，m是慢表的大小，只要除数够大，这个也是接近常数时间的
# 性能已经接近内置的HashSet了

# 比起HashSet，加多一个栈用来存值，就形成了键值对

# Runtime: 100%
# Memory: 87%

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 1000
        self.bucket = [[] for _ in range(self.mod)]
        self.values = [[] for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = key % self.mod
        if key not in self.bucket[k]:
            self.bucket[k].append(key)
            self.values[k].append(value)
        if key in self.bucket[k]:
            idx = self.bucket[k].index(key)
            self.values[k][idx] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = key % self.mod
        if key in self.bucket[k]:
            return self.values[k][self.bucket[k].index(key)]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k = key % self.mod
        if key in self.bucket[k]:
            idx = self.bucket[k].index(key)
            self.values[k].pop(idx)
            self.bucket[k].pop(idx)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)