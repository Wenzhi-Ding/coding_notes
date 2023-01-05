# Coding Notes

分享我的代码练习（主要是为了方便自己以后参考），以下只列举一些个人觉得比较好的题目，会不定期增删。

## 算法 Algorithm
1. 深度优先搜索 Depth-First-Search
	- [LI0408 First Common Ancestor](./10_LeetCode/LI0408-first-common-ancestor-lcci.py)：用递归写 DFS 的简洁性。
	- [L0322 Coin Change](./10_LeetCode/L0322-coin-change.py)：同样是动态规划，要因地制宜的考虑状态转移的方式。DFS 可以更快的接近目标。
	- [L0563 Binary Tree Tilt](./10_LeetCode/L0563-binary-tree-tilt.py)：后序遍历。
1. 广度优先搜索 Breadth-First-Search
    - [L1162 As Far from Land as Possible](./10_LeetCode/L1162-as-far-from-land-as-possible.py)：一个层序遍历的样例。
    - [L1036 Escape a Large Maze](./10_LeetCode/L1036-escape-a-large-maze.py)：层序遍历+找短板剪枝。
    - [L1345 Jump Game IV](./10_LeetCode/L1345-jump-game-iv.py)：遍历后不需要再遍历的备选项及时删掉，可能可以把时间复杂度降低一个幂次。
    - [L2045 Second Minimum Time to Reach Destination](./10_LeetCode/L2045-second-minimum-time-to-reach-destination.py)：改变 BFS 的记忆方式，可以实现同时检索最短路径、次短路径以至第N短路径。
1. 动态规划 Dynamic Programming
	- [M210114 Complicate Probability](./30_Other_Source/M210114_Complicate_Probability.py)：三维的动态规划，计算复杂的概率问题。
	- [M210122 Chocolate Game](./20_Tutorial/USC_DSO570_Analytics_Edge/Chocolate_Game): 二维动态规划，模拟机票、酒店的最优定价模型，计算最大期望收益。
	- [L0638 Shopping Offers](./10_LeetCode/L0638-shopping-offers.py)：1）用 `cache` 的装饰器来简化 DP 的编写；2）更重要的是体现了合理剪枝的威力。
	- [L0132 Palindrome Partitioning II](./10_LeetCode/L0132-palindrome-partitioning-ii.py)：两次动态规划，第一次用来做预处理。
	- [L1815 Maximum Number of Groups Getting Fresh Donuts](./10_LeetCode/L1815-maximum-number-of-groups-getting-fresh-donuts.py)：状态压缩的动态规划（DFS、位运算、状态压缩）。
	- [L1994 The Number of Good Subsets](./10_LeetCode/L1994-the-number-of-good-subsets.py)：位运算、状态压缩动态规划、大整数。
1. 回溯法 Backtracking
	- [L0044 Wildcard Matching](./10_LeetCode/L0044_wildcard-matching.py)：体现了回溯法在正确的剪枝思路下的简洁和效率。
	- [L0115 Distinct Subsequences](./10_LeetCode/L0115-distinct-subsequences.py)：优化递归的效率可以从转成循环+数组开始考虑。
	- [L1219 Path with Maximum Gold](./10_LeetCode/L1219-path-with-maximum-gold.py)：回溯的时候调用变量是拷贝而非引用，可以利用这一特性巧妙地记录回溯路径（此外此题还有关于搜索路径的剪枝）。
1. 线性规划 Linear Programming
    - [M210211 Filatoi Riuniti](./20_Tutorial/USC_DSO570_Analytics_Edge/Filatoi_Riuniti)：线性规划及敏感性分析的经典例题。
1. 二分查找 Binary Search
    - [L1760 Minimum Limit of Balls in a Bag](./10_LeetCode/L1760-minimum-limit-of-balls-in-a-bag.py)：二分查找的实际应用。查找的逻辑不一定是简单的数值比较。只要有目标函数、序列有单调性，都可以二分查找（其他相关：[L0354](./10_LeetCode/L0354-russian-doll-envelopes.py)）。
1. 滑窗 Sliding Window
    - [L0995 Minimum Number of K Consecutive Bit Flips](./10_LeetCode/L0995-minimum-number-of-k-consecutive-bit-flips.py)：数组长度 N，窗口长度 K。纯模拟操作 O(NK)，优化成滑窗则变为 O(N)。
1. 双指针 Two Pointers
    - [L0011 Container with Most Water](./10_LeetCode/L0011-container-with-most-water.py)：双指针重要的是想清楚指针移动的规则，有时并不会很直观，需要一点推导。


## 数据结构 Data Structure
1. 数组/矩阵 Array/Matrix
	- [M210116 Monte Carlo](./30_Other_Source/M210116_Monte_Carlo.py)：通过矩阵运算极大的加速大规模模拟（要求运算逻辑可向量化）。
	- [L1774 Closest Dessert Cost](./10_LeetCode/L1774-closest-dessert-cost.py)：快速且占用小地枚举所有子集。
	- [L0303 Range Sum Query Immutable](./10_LeetCode/L0303-range-sum-query-immutable.py)：通过对数组的预处理（前缀和）来简化需要大量重复的调用。
    - [L0304](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)：二维前缀和。
1. 链表 ListNode
1. 并查集 UnionFindSet
    - [L1971 Find if Path Exists in Graph](https://leetcode.cn/problems/find-if-path-exists-in-graph/description/)：并查集的基本思想是构建/压缩树，使得只需检查两个节点是否在一个树中，就可以判断两点是否连通。
1. 图 Graph
	
	- [L1761 Minimum Degree of a Connected Trio in a Graph](./10_LeetCode/L1761-minimum-degree-of-a-connected-trio-in-a-graph.py)：1）用矩阵存储图的信息可能可以高效（但要看情况，反例见[L1766](./10_LeetCode/L1766-tree-of-coprimes.py)）；2）一个好用的排序+剪枝的思路和写法。
1. 堆 Heap
	- [L0703 Kth Largest Element in a Stream](./10_LeetCode/L0703-kth-largest-element-in-a-stream.py)：一道基础的堆队列题目。
	- [L1675 Minimize Deviation in Array](./10_LeetCode/L1675-minimize-deviation-in-array.py) ：1）体现了复杂问题的优化首先应从数学本质的角度思考；2）体现了堆队列处理最大最小值问题的时间效率性。
	- [L1792 Maximum Average Pass Ratio](./10_LeetCode/L1792-maximum-average-pass-ratio.py)：Python 内置的 `heapq.heapify` 可以直接用于多维数组，按数组的第一个元素排序。所以可以轻松维护 `[sort_key, value1, value2...]` 这样的结构，能够完成更复杂的任务。
        - [L1801](./10_LeetCode/L1801-number-of-orders-in-the-backlog.py)类似，在仅需要按顺序索引，不需要按键值索引时，可以直接维护一个堆，而不需要另外再维护一个字典。
1. 栈 Stack
    - [L1766 Tree of Coprimes](./10_LeetCode/L1766-tree-of-coprimes.py)：1）栈 + DFS 的样例，也涉及了树的存储问题；2）重要思路：根据数据量选择突破口。
    - [L1776 Car Fleet II](./10_LeetCode/L1776-car-fleet-ii.py)：一个单调栈的好例子，为以下问题提供了参考：1）什么时候可以用栈？2）怎么从问题中提炼出栈的维护规则？3）栈在 Python 中的正确使用姿势。（其他相关：[L0496](./10_LeetCode/L0496-next-greater-element-i.py)）
    - [L0224 Basic Calculator](./10_LeetCode/L0224-basic-calculator.py)：用栈以更高的效率实现等价于递归的操作（而且写起来比递归简单）。
    - [L1996 The Number of Weak Characters in the Game](./10_LeetCode/1996-the-number-of-weak-characters-in-the-game.py)：列表套列表 + 单调栈 + 空间复杂度优化。
    - [L0146 LRU Cache](./01_Data_Structure/L0146-lru-cache.py)：LRU 缓存机制可以视为一种特殊的栈。
1. 字典树 Trie
    - [L0208 Implement Trie Prefix Tree](./01_Data_Structure/L0208-implement-trie-prefix-tree.py)：前缀字典树的基础实现。
    - [L1803 Count Pairs with XOR in a Range](https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/description/)：字典树思想解决计算问题。
1. 哈希表 HashMap
    - [L0705 Design HashSet](./01_Data_Structure/L0705-design-hashset.py)：哈希集的基本实现。
    - [L0706 Design HashMap](./01_Data_Structure/L0706-design-hashmap.py)：哈希表的基本实现。

## 数学 Math
1. 抽样 Sampling
     - [M210216 Poker Probabilities](./30_Other_Source/M210216-poker-probabilities.py)：在做模拟的时候要关注概率分布及动态变化。扑克牌的玩法中多数为不放回抽样，如果直接用均匀分布或正态分布去模拟，就会算出错误的结果。
2. 非线性规划 Non-linear Programming
   - [M210223 Portfolio Management](./30_Other_Source/M210223-portfolio-management.py)：用 `scipy.optimize` 模块求解非线性的规划问题。需要考虑可行边界。
3. 离散规划 Discrete Optimization
   - [M210323 Dellmar Supply Chain](./20_Tutorial/USC_DSO570_Analytics_Edge/Dellmar)：将逻辑运算（非线性的）转为线性问题的范式，从而能够使用线性规划。
   - [M210410 Discrete Optimization Assignment](./20_Tutorial/USC_DSO570_Analytics_Edge/Discrete_Optimization)：非线性约束转换为线性约束，其实就是把边界画出来，用直线去拼出这个边界。通常需要涉及创建一些中间的线性变量。
     - 此外，只要不涉及决策变量，都可以先做一些预处理。恰当的预处理可以显著减小后面约束的复杂度。
4. 因数 Divisor
   - [L1819 Number of Different Subsequences GCDs](./10_LeetCode/L1819-number-of-different-subsequences-gcds.py)：一个数组可以表示 `nums[i] = gcd * rel_prime[i]`，`gcd` 是数组 `nums` 的最大公约数，`rel_prime` 是一个最大公约数为1的数组。
5. 等差数列
   - [L0390 Elimination Game](./10_LeetCode/L0390-elimination-game.py)：数学的角度思考问题，并不一定是解析解，也可以是数学简化问题（抽象）+模拟的思路。
6. 博弈问题
   - [L0390 Cat and Mouse](./10_LeetCode/L0913-cat-and-mouse.py)：动态规划解决博弈问题，清晰的逻辑思考是关键，准确全面的识别出边界状态和结束条件。
   - [L2029 Stone Game IX](./10_LeetCode/L2029-stone-game-ix.py)：博弈问题往往可以通过归纳变成极其简单的问题。虽然实际情况是复杂的，但规则是简单的，所以往往可以将实际情况化简讨论。
7. 贪心
   - [L0334 Increasing Triplet Subsequence](./10_LeetCode/L0334-increasing-triplet-subsequence.py)：贪心算法的一个迷你样例。
8. 概率
   - [M220325 Conditional Distribution](./30_Other_Source/M220325-conditional-distribution.ipynb)：可视化的呈现条件期望和条件方差的影响。

## 数据处理

- 用 Pandas 构建平衡的面板：[M210712-balanced-panel](./30_Other_Source/M210712-balanced-panel.py)
- 用 Pandas 构建不平衡的面板：[M220806-unbalanced-panel](./30_Other_Source/M220806-unbalanced-panel.py)
- 在 Pandas 中将列表元素分配至多列（[Link](https://stackoverflow.com/a/69148256/8352445)）
- 在 Pandas 选择多个范围的列（[Link](https://stackoverflow.com/a/72584885/8352445)）
- 滚动匹配序列特征：[M211123-rolling-match-pattern](./30_Other_Source/M211123-rolling-match-pattern.py)
- Numpy 加速运算：[M220411_accelerate_numpy](./20_Tutorial/M220411_accelerate_numpy.ipynb)
- 迭代替换字符串：[M220814_finditer](./30_Other_Source/M220814_finditer.py)
- 异步：[M220827_asyncio](./20_Tutorial/M220827_asyncio.py)

## 其他参考

- 拉不拉东算法与数据结构全教程（[Link](https://labuladong.github.io/algo/)）