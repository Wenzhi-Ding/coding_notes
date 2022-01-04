# https://leetcode-cn.com/problems/cat-and-mouse/solution/mao-he-lao-shu-by-leetcode-solution-444x/

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]

        def getResult(mouse: int, cat: int, turns: int) -> int:
            if turns == n * 2:
                return DRAW
            res = dp[mouse][cat][turns]
            if res != -1:
                return res
            if mouse == 0:
                res = MOUSE_WIN
            elif cat == mouse:
                res = CAT_WIN
            else:
                res = getNextResult(mouse, cat, turns)
            dp[mouse][cat][turns] = res
            return res

        def getNextResult(mouse: int, cat: int, turns: int) -> int:
            curMove = mouse if turns % 2 == 0 else cat
            defaultRes = MOUSE_WIN if curMove != mouse else CAT_WIN
            res = defaultRes
            for next in graph[curMove]:
                if curMove == cat and next == 0:
                    continue
                nextMouse = next if curMove == mouse else mouse
                nextCat = next if curMove == cat else cat
                nextRes = getResult(nextMouse, nextCat, turns + 1)
                if nextRes != defaultRes:
                    res = nextRes
                    if res != DRAW:
                        break
            return res

        return getResult(1, 2, 0)