# 核心思想是压缩，将共同边数的点收进counter去算，先不考虑减边算出一份边的个数（因为无边的点占据了大多数），再逐个减边，获得了不同边数的counter后，就由大到小累加，二分查找给出结果，超边界的即无结果

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        p_c = [0] * (n+1) # point count
        e_c = defaultdict(int) # edge count
        
        for a,b in edges:
            p_c[a] += 1
            p_c[b] += 1
            if a<b:
                e_c[(a,b)] += 1
            else:
                e_c[(b,a)] += 1
        
        d_c = defaultdict(int) # degree count
        for i in range(1,n+1):
            d_c[p_c[i]] += 1

        cnt_amt = defaultdict(int) # amount of same cnt on pairs
        d_key = list(d_c.keys()) # degree key
        l_d = len(d_key)
        for i in range(l_d):
            d1 = d_key[i]
            cnt_amt[d1*2] += d_c[d1] * (d_c[d1]-1) // 2
            for j in range(i+1, l_d):
                d2 = d_key[j]
                cnt_amt[d1+d2] += d_c[d1] * d_c[d2]
        
        for (u,v), z in e_c.items(): # amount of cnt adjustment
            s = p_c[u] + p_c[v]
            t = s - z
            cnt_amt[s] -= 1
            cnt_amt[t] += 1
        
        cnt_keys = sorted(cnt_amt.keys(), key=lambda x: -x) # accumulate amount of cnt by descending order
        res = defaultdict(int)
        tmp = 0
        for key in cnt_keys:
            if cnt_amt[key]:
                tmp += cnt_amt[key]
                res[key] = tmp

        res_keys = sorted(res.keys()) # bisection search 
        for i, q in enumerate(queries):
            local = bisect.bisect(res_keys, q)
            try:
                queries[i] = res[res_keys[local]]
            except:
                queries[i] = 0
        
        return queries