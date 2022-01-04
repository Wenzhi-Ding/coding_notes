# https://leetcode-cn.com/problems/cat-and-mouse/solution/mao-he-lao-shu-by-leetcode-solution-444x/

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        n = len(graph)
        dp = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]  # 3维数组：鼠位置-猫位置-轮次

        # 边界条件
        def getResult(mouse: int, cat: int, turns: int) -> int:
            if turns == n * 2:  # 达到2n轮次说明必和，原因见题解
                return DRAW

            # 检查是否已搜索过
            res = dp[mouse][cat][turns]
            if res != -1:
                return res

            if mouse == 0:  # 若鼠在0位置（洞里），则鼠胜
                res = MOUSE_WIN
            elif cat == mouse:  # 若猫在鼠位置，则猫胜
                res = CAT_WIN
            else:  # 若非结束条件，则进入搜索
                res = getNextResult(mouse, cat, turns)

            dp[mouse][cat][turns] = res  # 记录搜索结果
            return res

        # 状态转移
        def getNextResult(mouse: int, cat: int, turns: int) -> int:
            curMove = mouse if turns % 2 == 0 else cat
            defaultRes = MOUSE_WIN if curMove != mouse else CAT_WIN  # 默认设为必输状态
            res = defaultRes
            for next in graph[curMove]:  # 遍历可以走的节点
                # 猫不可能进0位置（洞）
                if curMove == cat and next == 0:
                    continue

                # 设置新状态
                nextMouse = next if curMove == mouse else mouse
                nextCat = next if curMove == cat else cat

                # 根据新状态判定是否符合边界条件
                nextRes = getResult(nextMouse, nextCat, turns + 1)

                # 博弈：判断是否结束搜索
                if nextRes != defaultRes:  # 如果不是必输，则更新结果——必输是最差策略，任何比它好的结果都应该覆盖它
                    res = nextRes
                    if res != DRAW:  # 新搜出来的结果既不是必输，也不是必和，所以是必胜，那么已经是最优策略，不必再搜索了
                        break
            return res

        return getResult(1, 2, 0)