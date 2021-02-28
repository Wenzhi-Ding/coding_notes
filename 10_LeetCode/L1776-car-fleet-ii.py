# https://leetcode-cn.com/problems/car-fleet-ii/

# Python中用列表做栈，官方推荐的使用是将尾部视作栈顶，如此
# stack.pop() = list.pop()
# stack.push() = list.append()
# stack.top() = list[-1]

# 本题的关键在于想明白两点
# 1、追到后，后车等于消失（再也与计算无关了）
# 2、追到后，前车还是按原来的状态继续行进
# 所以可以用栈，只用考虑追右边的车。右边的车只有三种状态：追不到、追到前消失和追到
# 追不到：清空栈，本车就是新的栈顶
# 追到前消失：退栈，追更前面一辆车
# 追到：直接计算追车时间，本车推入栈顶

# Runtime: 644 ms
# Memory: 45.6 MB

class Solution:
    def getCollisionTimes(self, cars):
        
        l = len(cars)
        ans = [None for _ in range(l)]
        stack = []

        for i in range(l - 1, -1, -1):
            print(i)
            print(stack, ans)
            while stack:
                if cars[stack[-1]][1] >= cars[i][1]: stack.pop() # 速度比前车慢，等它消失去撞它前面的，先将它从队列中弹出
                else:  # 速度比前车快，去撞前车
                    if ans[stack[-1]] < 0: break  # -1说明它已经确定了不会消失，那肯定能撞到
                    d = ans[stack[-1]] * (cars[i][1] - cars[stack[-1]][1])  # 这里说明了前车会消失，要计算一下消失前能否撞上
                    if d > cars[stack[-1]][0] - cars[i][0]: break  # 这说明能追上
                    else: stack.pop()  # 追不上，改追它前面的车
                print(stack, ans)
            if not stack: ans[i] = -1  # 栈空了，说明前面没有可追的车
            else:
                ans[i] = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])
            stack.append(i)  # 该车已经计算完毕，放入栈顶计算后车
      
        return ans

cars = [[1,2],[2,1],[4,3],[7,2]]  # [1.00000,-1.00000,3.00000,-1.00000]
cars = [[3,4],[5,4],[6,3],[9,1]]  # [2.00000,1.00000,1.50000,-1.00000]

sol = Solution()
print(sol.getCollisionTimes(cars))