# https://leetcode-cn.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:

        N = len(arr)

        inds = defaultdict(set)
        for v, k in enumerate(arr):
            inds[k].add(v)

        min_step = [N + 1] * N
        min_step[0] = 0
        queue = deque([0])
        visited = set([0])

        while min_step[-1] == N + 1:
            i = queue.popleft()
            s = min_step[i]

            for j in inds[arr[i]]:
                if i != j and j not in visited:
                    min_step[j] = s + 1
                    queue.append(j)
                    visited.add(j)
            del inds[arr[i]]  # 关键一步

            if i + 1 <= N - 1 and i + 1 not in visited:
                min_step[i + 1] = s + 1
                queue.append(i + 1)
                visited.add(i + 1)

            if i - 1 >= 0 and i - 1 not in visited:
                min_step[i - 1] = s + 1
                queue.append(i - 1)
                visited.add(i - 1)

        return min_step[-1]