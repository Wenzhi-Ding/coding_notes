# Coding Notes

分享我的代码练习（主要是为了方便自己以后参考），以下只列举一些个人觉得比较好的题目，会不定期增删。

## 算法 Algorithm
1. 深度优先搜索 Depth-First-Search
	- [LI0408 First Common Ancestor](./10_LeetCode/LI0408-first-common-ancestor-lcci.py)：用递归写DFS的简洁性（5行 vs. 30行）。
	- [L0322 Coin Change](./10_LeetCode/L0322-coin-change.py)：同样是动态规划，要因地制宜的考虑状态转移的方式。DFS可以更快的接近目标。
1. 广度优先搜索 Breadth-First-Search
    - [L1162 As Far from Land as Possible](./10_LeetCode/L1162-as-far-from-land-as-possible.py)：一个BFS（层序遍历）的样例。
1. 动态规划 Dynamic Programming
	- [M210114 Complicate Probability](./30_Other_Source/M210114_Complicate_Probability.py)：三维的动态规划，计算复杂的概率问题。
	- [M210122 Chocolate Game](./20_Tutorial/USC_DSO570_Analytics_Edge/Chocolate_Game): 二维动态规划，模拟机票、酒店的最优定价模型，计算最大期望收益。
	- [L0638 Shopping Offers](./10_LeetCode/L0638-shopping-offers.py)：1）用`lru_cache`的装饰器来简化DP的编写；2）更重要的是体现了合理剪枝的威力。
1. 回溯法 Backtracking
	- [L0044 Wildcard Matching](./10_LeetCode/L0044_wildcard-matching.py)：体现了回溯法在正确的剪枝思路下的简洁和效率。
1. 线性规划 Linear Programming
    - [M210211 Filatoi Riuniti](./20_Tutorial/USC_DSO570_Analytics_Edge/Filatoi_Riuniti)：线性规划及其敏感性分析的经典例题。
1. 非线性规划 Non-linear Programming
    - [M210227 Endurance Investor](./20_Tutorial/USC_DSO570_Analytics_Edge/Endurance_Investor)：需要考虑可行边界的问题。
1. 二分查找 Binary Search
	- [M210207 Bisect](./00_Algorithm/M210207_bisect.py)：复现Python自带的`bisect.bisect_left`和`bisect.bisect_right`。
	- [L1760 Minimum Limit of Balls in a Bag](./10_LeetCode/L1760-minimum-limit-of-balls-in-a-bag.py)：二分查找的实际应用。查找的逻辑不一定是简单的数值比较。只要有目标函数、序列有单调性，都可以二分查找。（其他相关：[L0354](./10_LeetCode/L0354-russian-doll-envelopes.py)）
1. 滑窗 Sliding Window
    - [L0995 Minimum Number of K Consecutive Bit Flips](./10_LeetCode/L0995-minimum-number-of-k-consecutive-bit-flips.py)：数组长度N，窗口长度K。纯模拟操作O(NK)，优化成滑窗则变为O(N)。
1. 双指针 Two Pointers
    - [L0011 Container with Most Water](./10_LeetCode/L0011-container-with-most-water.py)：双指针重要的是想清楚指针移动的规则，有时并不会很直观，需要一点推导。


## 数据结构 Data Structure
1. 数组/矩阵 Array/Matrix
	- [M210116 Monte Carlo](./30_Other_Source/M210116_Monte_Carlo.py)：通过矩阵运算极大的加速大规模模拟（要求运算逻辑可向量化）。
	- [L1774 Closest Dessert Cost.](./10_LeetCode/L1774-closest-dessert-cost.py)：快速且占用小地枚举所有子集。
	- [L0303 Range Sum Query Immutable](./10_LeetCode/L0303-range-sum-query-immutable.py)：通过对数组的预处理（前缀和）来简化需要大量重复的调用。（二维前缀和：[L0304](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)）
	
1. 图 Graph
	- [L1761 Minimum Degree of a Connected Trio in a Graph](./10_LeetCode/L1761-minimum-degree-of-a-connected-trio-in-a-graph.py)：1）用矩阵存储图的信息可能可以高效（但要看情况，反例见[L1766](./10_LeetCode/L1766-tree-of-coprimes.py)）；2）一个好用的排序+剪枝的思路和写法。
	
1. 堆 Heap
	- [L0703 Kth Largest Element in a Stream](./10_LeetCode/L0703-kth-largest-element-in-a-stream.py)：一道基础的堆队列题目。
	- [L1675 Minimize Deviation in Array](./10_LeetCode/L1675-minimize-deviation-in-array.py) ：1）体现了复杂问题的优化首先应从数学本质的角度思考；2）体现了堆队列处理最大最小值问题的时间效率性。
	
1. 栈 Stack
    - [L1766 Tree of Coprimes](./10_LeetCode/L1766-tree-of-coprimes.py)：1）栈+DFS的样例，也涉及了树的存储问题；2）重要思路：根据数据量选择突破口。
    - [L1776 Car Fleet II](./10_LeetCode/L1776-car-fleet-ii.py)：一个单调栈的好例子，为以下问题提供了参考：1）什么时候可以用栈？2）怎么从问题中提炼出栈的维护规则？3）栈在Python中的正确使用姿势。（其他相关：[L0496](./10_LeetCode/L0496-next-greater-element-i.py)）
    - [L0224 Basic Calculator](./10_LeetCode/L0224-basic-calculator.py)：用栈以更高的效率实现等价于递归的操作（而且写起来比递归简单）。

1. 字典树 Trie
    - [L0208 Implement Trie Prefix Tree](./10_LeetCode/L0208-implement-trie-prefix-tree.py)：前缀字典树的基础实现。
    - [L0472 Concatenated Words](L0472-concatenated-words.py)：还没学会。

1. 数据结构复现 Data Structure Replication
    - 堆队列[TBD]
    - 生成器[TBD]
    - 二叉树[TBD]
    - 栈[TBD]
    - 双向链表
      - LRU Cache：一种带有清退机制的缓存结构。
        - O(1)时间基本实现（[L0146 LRU Cache](./10_LeetCode/L0146-lru-cache.py)）[TBD]
        - 装饰器实现[TBD]。
    - 集合 Collections
      - HashSet：简单实现（[L0705](./10_LeetCode/L0705-design-hashset.py)）
      - OrderedDict[TBD]
      - DefaultDict[TBD]

## 数学 Math
1. 抽样 Sampling
	- [M210216 Poker Probabilities](./30_Other_Source/M210216-poker-probabilities.py)：在做模拟的时候要关注概率分布及动态变化。扑克牌的玩法中多数为不放回抽样，如果直接用均匀分布或正态分布去模拟，就会算出错误的结果。
