# https://www.bilibili.com/video/BV1rh411f7WU/?p=1

# 基本问题：有N个盒子，有各自的长宽高，求解最高能堆多高
# 进阶问题：求解堆得最高的方法

# 列表的每一个元素即为(L, W, H)
# 假定盒子不能旋转，即L恒对L、W恒对W
boxes = [(4, 5, 3), (2, 3, 2), (3, 6, 2), (1, 5, 4), (2, 4, 1), (1, 2, 2)]
# boxes = [
#     (5, 2, 1), (2, 5, 3), (4, 5, 1),
#     (3, 4, 1), (2, 1, 2), (4, 1, 2),
#     (5, 3, 3), (4, 1, 5), (2, 2, 4)
#     ]

# 1、可视化：通过L和W可以构建出一个有向无环图，H就是边的长度，问题转化为有向无环图的最长路径
# 2、子问题及联系：到每个点的最大路径都相当于所有前一个连通节点的最大路径，加上边长

## 解法
from collections import defaultdict

# 先按面积排序，减少生成有向无环图的时间复杂度及后续索引的代码逻辑复杂度
# boxes = [x for x, _ in sorted(zip(boxes, [x[0] * x[1] for x in boxes]))]
# Note: 其实按长或宽排就够了，因为本来就不是要严格递增关系
boxes.sort(key=lambda x: x[0])

# 构建有向无环图
# Note: 这是多余的，等于是O(n^2)走了两遍

# 基本问题解法：DP求所有节点中的最大高度
def canBeStacked(top, bottom):
    return (top[0] < bottom[0]) & (top[1] < bottom[1])

max_heights = {box: box[2] for box in boxes}  # 字典比列表好，依赖index还要跨列表保持对应
for i in range(1, len(boxes)):
    box = boxes[i]
    S = [boxes[j] for j in range(i) if canBeStacked(boxes[j], box)]
    max_heights[box] = box[2] + max([max_heights[box] for box in S], default=0)

print(max_heights[max(max_heights)])

# 进阶问题解法：DP求每个节点的最大高度及前一个节点（用于打印解法）
max_heights = {box: box[2] for box in boxes}
previous_nodes = {box: box for box in boxes}
for i in range(1, len(boxes)):
    box = boxes[i]
    S = [boxes[j] for j in range(i) if canBeStacked(boxes[j], box)]
    max_heights[box] = box[2] + max([max_heights[box] for box in S], default=0)

