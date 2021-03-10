# https://stackoverflow.com/questions/66545873/getting-several-list-of-possibilities-based-on-two-list/66547124#66547124

def find_comb(demands:list, entry:list):
    
    # Exit for dynamic programming
    if len(entry) == 1:
        if not demands: return [[[None]]]
        elif sum(demands) < entry[-1]: return [[demands]]
        else: return [-1]  # Not fulfill
    
    # Get all possible combinations for the entry[0]
    combs = [[0]]
    for d in demands:
        combs += [c + [d] for c in combs if sum(c) + d <= entry[0]]

    # Update [0] to [None] according to your request
    combs = [[x for x in c if x] if c != [0] else [None] for c in combs]

    # Get combinations
    ans = []
    for c in combs:
        res_demands = [d for d in demands if d not in c]
        for n in find_comb(res_demands, entry[1:]):  # Dynamic programming here
            if n == -1: continue
            if not n: n = [[None]] 
            ans.append([c] + [k for k in n])

    return ans

# [7, 9, 1]
# [5, 19]

for a in find_comb([4, 3, 8], [5, 19]):
    print(a)

# def clean_ans(rows):
#     return [[x if len(x) > 1 else x[0] for x in row] for row in rows]

# print(clean_ans(find_comb(demands=[4, 3, 8], entry=[5, 19])))

