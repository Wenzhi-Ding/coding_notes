# Coding Notes

分享我的代码练习（主要是为了方便自己以后参考），以下只列举一些个人觉得比较好的。

[ToC]

1. 数组/矩阵 Array/Matrix
	- [M210116 Monte Carlo](./30_Other_Source/M210116_Monte_Carlo.py)：通过矩阵运算极大的加速大规模的模拟。
1. 深度优先搜索 Depth-First-Search
	- [LI0408 First Common Ancestor](./10_LeetCode/LI0408-first-common-ancestor-lcci.py)：用递归写DFS的简洁性（5行 vs. 30行）。
1. 动态规划 Dynamic Programming
	- [M210114 Complicate Probability](./30_Other_Source/M210114_Complicate_Probability.py)：三维的动态规划，计算复杂的概率问题。
	- [M210122 Chocolate Game](./20_Tutorial/USC_DSO570_Chocolate_Game): 二维动态规划，模拟机票、酒店的最优定价模型，计算最大期望收益。
	- [L0638 Shopping Offers](./10_LeetCode/L0638-shopping-offers.py)：1）用`lru_cache`的装饰器来简化DP的编写；2）更重要的是体现了合理剪枝的威力。
1. 回溯法 Backtracking
	- [L0044 Wildcard Matching](./10_LeetCode/L0044_wildcard-matching.py)：体现了回溯法在正确的剪枝思路下的简洁和效率。
1. 堆 Heap
	- [L0703 Kth Largest Element in a Stream](./10_LeetCode/L0703-kth-largest-element-in-a-stream.py)：一道基础的堆队列题目。
	- [L1675 Minimize Deviation in Array](./10_LeetCode/L1675-minimize-deviation-in-array.py) ：1）体现了复杂问题的优化首先应从数学本质的角度思考；2）体现了堆队列处理最大最小值问题的时间效率性。
1. 线性规划 Linear Programming
    - [M210211 Filatoi Riuniti](./20_Tutorial/USC_DSO570_Filatoi_Riuniti)：线性规划及其敏感性分析的经典例题。
1. 算法复现 Algorithm Replication
	- [M210207 Bisect](./00_Algorithm/M210207_bisect.py): 二分查找，复现Python自带的`bisect.bisect_left`和`bisect.bisect_right`。
1. 数据结构复现 Data Structure Replication
    - 堆队列[TBD]
    - 生成器[TBD]
    - 二叉树[TBD]