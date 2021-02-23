# https://leetcode-cn.com/problems/grumpy-bookstore-owner/


# 滑窗
# Runtime: 296 ms (93%)

def maxSatisfied(customers, grumpy, X):

    n = len(customers)
    if X == n: return sum(customers)

    base = 0
    sum_prod = []
    for i in range(n):
        if grumpy[i]:
            sum_prod.append(customers[i])
        else:
            sum_prod.append(0)
            base += customers[i]

    window = sum(sum_prod[:X])
    ans = window
    for i in range(n - X):
        window += sum_prod[i + X] - sum_prod[i]
        ans = max(ans, window)

    return base + ans


customers = [1,0,1,2,1,1,7,5]; grumpy = [0,1,0,1,0,1,0,1]; X = 3  # 16
customers = [4,10,10]; grumpy = [1,1,0]; X = 2  # 24

print(maxSatisfied(customers, grumpy, X))