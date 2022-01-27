# https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/
# 我的题解：https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/solution/python-dan-diao-zhan-jian-ji-yi-dong-shi-heva/

from collections import defaultdict

# 解法1：需要维护一个字典，占用空间很大
def numberOfWeakCharacters(properties):

    p = defaultdict(list)
    for a, b in properties:
        p[a].append(b)
    k = sorted(list(p.keys()))

    res = 0
    m = max(p[k.pop()])
    while k:
        _ms = p[k.pop()]
        _m_max = 0

        for _m in _ms:
            if m > _m: res += 1
            _m_max = max(_m_max, _m)

        m = max(m, _m_max)

    return res


# 时间(92%)空间(100%)双优
def numberOfWeakCharacters(properties):
    properties.sort()

    res = 0
    max_a, max_b = cur_a, cur_b = properties.pop()
    while properties:
        _a, _b = properties.pop()
        if cur_a != _a:  # 当a切换
            max_b, cur_b = max(max_b, cur_b), _b  # 更新全局最大b，并缓存当前a对应的局部最大b
            cur_a = _a  # 缓存当前a

        if max_b > _b and max_a > _a: res += 1
    
    return res


ps = [
    [[5,5],[6,3],[3,6]],
    [[2,2],[3,3]],
    [[1,5],[10,4],[4,3]],
    [[1,5], [1,4]],
    [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]],
    [[10,1],[5,1],[7,10],[4,1],[5,9],[6,9],[7,2],[1,10]]
]

for p in ps:
    print(numberOfWeakCharacters(p))