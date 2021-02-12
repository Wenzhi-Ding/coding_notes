# https://leetcode.com/problems/two-city-scheduling/

# Runtime: 40 ms (69.31%)
# Exactly the same as 20 ms (100%) solution

def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    return sum([costs[i][0] + costs[-i - 1][1] for i in range(len(costs) // 2)])


costs = [[10,20],[30,200],[400,50],[30,20]]  # 110
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]  # 1859
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]  # 3086

print(twoCitySchedCost(costs))