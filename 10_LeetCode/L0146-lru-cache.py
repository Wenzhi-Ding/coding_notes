# https://leetcode-cn.com/problems/lru-cache/
from collections import OrderedDict

# Runtime: 136 ms (98%)

class LRUCache(OrderedDict):  # self可以继承类型

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Runtime: 98-192 ms (40-100%)

class LRUCache(dict):
    def __init__(self, capacity: int):
        self.c = capacity

    def get(self, key: int) -> int:
        if key in self:
            self[key] = self.pop(key)  # dict本身就有顺序，把原来的弹出，再创建一次，就放到末尾了
            return self[key]    
        return -1    

    def put(self, key: int, value: int) -> None:
        key in self and self.pop(key) 
        self[key] = value
        len(self) > self.c and self.pop(next(iter(self)))


# Runtime: 468 ms (10%)

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.stack = []  # 越靠后的越新
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.cache:
            self.stack.remove(key)  # 更新使用状态
            self.stack.append(key)
            return self.cache[key]
        return -1


    def put(self, key: int, value: int) -> None:
        status = self.get(key)  # 更新使用状态
        if status == -1:
            if len(self.stack) == self.capacity:  # 若满则从底部拿出
                tmp = self.stack.pop(0)
                del self.cache[tmp]
            self.stack.append(key)  # 将key放入栈顶
        self.cache[key] = value  # 更新或创建键值对
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)