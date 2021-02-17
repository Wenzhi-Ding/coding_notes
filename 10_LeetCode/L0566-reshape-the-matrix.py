# https://leetcode-cn.com/problems/reshape-the-matrix/

# Runtime: 112 ms (59%)

def matrixReshape(nums, r, c):
    if len(nums) * len(nums[0]) != r * c: return nums
    res, cnt, this_row = [], 0, []
    for row in nums:
        for col in row:
            this_row.append(col)
            cnt += 1
            if cnt == c:
                res.append(this_row)
                cnt, this_row = 0, []
    return res


# Runtime: 100 ms (96%)

def matrixReshape(nums, r, c):
    if len(nums) * len(nums[0]) != r * c: return nums
    one_dim = []
    for row in nums:
        one_dim.extend(row)
    return [one_dim[i: i + c] for i in range(0, len(one_dim), c)]

nums = [[1,2], [3,4]]; r = 1; c = 4
# nums = [[1,2], [3,4]]; r = 2; c = 4
# nums = [[1,2], [3,4]]; r = 2; c = 2

print(matrixReshape(nums, r, c))