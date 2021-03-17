# https://leetcode-cn.com/problems/maximum-average-pass-ratio/

from heapq import heapify, heappop, heappush

class Solution:
    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        margin = [(-(b - a) / (b * (b + 1)), a, b) for a, b in classes]

        heapify(margin)

        for _ in range(extraStudents):
            _, a, b = heappop(margin)
            a, b = a + 1, b + 1
            heappush(margin, (-(b - a) / (b * (b + 1)), a, b))

        return sum([a / b for _, a, b in margin]) / len(classes)
