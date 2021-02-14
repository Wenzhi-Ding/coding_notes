from functools import lru_cache

def countHomogenous(s):

    @lru_cache
    def comb(n):
        if n == 0: return 0
        if n == 1: return 1
        return comb(n - 1) + n

    tmp_len = 1
    ans = 0
    tmp_c = s[0]
    for k, c in enumerate(s[1:]):
        if c == tmp_c: 
            tmp_len += 1
        else:
            ans += comb(tmp_len)
            tmp_c = c
            tmp_len = 1
    ans += comb(tmp_len)
    
    return ans % 1000000007

s = "abbcccaa"
s = "xy"
s = "x"
s = "zzzzz"

print(countHomogenous(s))