# https://leetcode-cn.com/problems/escape-a-large-maze

from collections import deque

def isEscapePossible(blocked, source, target):

    FOUND, OPEN_LOOP = True, True

    N = len(blocked)
    if N <= 1: return True

    LIMIT = N * (N - 1) / 2
    LB, UB = 0, 10 ** 6 - 1

    # 哈希化：因为要反复在这里面查找，同时这些点又具有不变的属性，所以肯定是全部哈希化，能大幅提高效率
    blocked = set(tuple(pos) for pos in blocked)
    source, target = tuple(source), tuple(target)

    flags = []

    for _source, _target in [[source, target], [target, source]]:  # 正反进行两次搜索
        # 设立搜索目标
        visited, queue = set([_source]), deque([_source])

        # BFS核心代码
        while queue:
            i, j = queue.popleft()  # 用deque的好处是只需要维护一个queue即可BFS；用set则需要两个queue实现BFS，单个set则适合DFS
            for _i, _j in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if (LB <= _i <= UB) & (LB <= _j <= UB) & ((_i, _j) not in blocked) & ((_i, _j) not in visited):
                    if (_i, _j) == _target: return FOUND
                    visited.add((_i, _j))
                    queue.append((_i, _j))

            # 剪枝：blocked的数量少，决定了可以从“blocked能围的最大面积”的角度剪枝
            if len(visited) > LIMIT:
                flags.append(OPEN_LOOP)
                break

    return (sum(flags) == 2)


test_cases = [
    [[[0,1],[1,0]], [0,0], [0,2]],
    [[], [0,0], [999999,999999]],
    [
        [[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]],
        [655988,180910],
        [267728,840949]
    ],
    [
        [[0,3],[1,0],[1,1],[1,2],[1,3]],
        [0,0],
        [0,2]
    ]
]

for blocked, source, target in test_cases:
    print(isEscapePossible(blocked, source, target))