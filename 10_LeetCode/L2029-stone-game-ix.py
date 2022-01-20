# https://leetcode-cn.com/problems/stone-game-ix/

from collections import Counter

def stoneGameIX(stones):

    stones = Counter([x % 3 for x in stones])

    if stones[0] % 2 == 0:
        return stones[1] > 0 and stones[2] > 0

    return abs(stones[1] - stones[2]) > 2