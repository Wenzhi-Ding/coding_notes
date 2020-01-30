
# Q59 Spiral Matrix II

https://leetcode.com/problems/spiral-matrix-ii/

## 1. Takeaways

### a. Uniqueness of List Creation

[Link1](https://stackoverflow.com/questions/13347559/create-empty-matrix-python)


```python
l1 = [[0] * 2] * 2  # This method will create a list with shared memory.
l2 = [[0 for _ in range(2)] for _ in range(2)]  # This method will create unique element.

l1[0][0] = 1
l2[0][0] = 1

l1
l2
```




    [[1, 0], [1, 0]]






    [[1, 0], [0, 0]]



## 2. My Answer

Intuitively, reach a turning point, change direction, reach a turing point, change direction...

- Runtime: 24 ms, 94.10%
- Memory Usage: 12.8 MB, 100.00%


```python
class Solution:
    def generateMatrix(self, n: int):
            matrix = [[0 for _ in range(n)] for _ in range(n)]
            idx, jdx, direction = 0, 0, 1
            right, bottom, left, upper = n - 1, n - 1, 0, 0
            for i in range(n ** 2):
                matrix[jdx][idx] = i + 1
                if (direction != 1) & ((idx, jdx) == (left, upper)):
                    direction = 1
                    left += 1
                if (direction != 2) & ((idx, jdx) == (right, upper)):
                    direction = 2
                    upper += 1
                if (direction != 3) & ((idx, jdx) == (right, bottom)):
                    direction = 3
                    right -= 1
                if (direction != 4) & ((idx, jdx) == (left, bottom)):
                    direction = 4
                    bottom -= 1
                if direction == 1:
                    idx += 1
                if direction == 2:
                    jdx += 1
                if direction == 3:
                    idx -= 1
                if direction == 4:
                    jdx -= 1
            return matrix
```


```python
s = Solution()
s.generateMatrix(3)
```




    [[1, 2, 3], [8, 9, 4], [7, 6, 5]]




```python

```
