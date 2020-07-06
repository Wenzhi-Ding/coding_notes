# Author: Wenzhi Ding
# Create at: July 6, 2020

# Problem:
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        '''
        Author: Wenzhi Ding

        Runtime: 528ms (6.16%)---Fast answer are using 1 to add. Not generalized answer.
        Memory: 14.2MB (5.08%)
        '''

        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        mem = [[0] * n for _ in range(m)]
        mem[0][0] = 1

        if obstacleGrid[0][0] | obstacleGrid[m - 1][n - 1]:
            return 0

        def dp(j, k):
            if not j + k: return 1

            if (k != 0) & (obstacleGrid[j][k - 1] == 0):  # x-axis
                if mem[j][k - 1]: a = mem[j][k - 1]
                else: a = mem[j][k - 1] = dp(j, k - 1)
            else: a = 0
            if (j != 0) & (obstacleGrid[j - 1][k] == 0):  # y-axis
                if mem[j - 1][k]: b = mem[j - 1][k] 
                else: b = mem[j - 1][k] = dp(j - 1, k)
            else: b = 0
            # print(mem)
            return int(a + b)

        return dp(m - 1, n - 1)
        
s = Solution()
cases = [
    [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ],
    # [[1]],
    # [[0,0],[1,1],[0,0]]
]

for case in cases:
    print(case)
    ans = s.uniquePathsWithObstacles(case)
    print(ans)
    # print(ans)