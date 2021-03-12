# https://leetcode-cn.com/problems/longest-nice-substring/

# Runtime: 44 ms (99%)

def longestNiceSubstring(s):

    substrs = [s]
    nice_substrs = []

    while substrs:
        tmp_s = substrs.pop(0)
        if len(tmp_s) <= 1: continue
        ex_chars = set([])

        for char in set(tmp_s):
            if char.upper() not in tmp_s or char.lower() not in tmp_s: ex_chars.add(char)
        
        if len(ex_chars) == 0:
            nice_substrs.append(tmp_s)
            continue
        
        i = 0
        for j in range(len(tmp_s)):
            if tmp_s[j] in ex_chars:
                substrs.append(tmp_s[i:j])
                i = j + 1
        substrs.append(tmp_s[i:])

    if not nice_substrs: return ""
    lens = [len(x) for x in nice_substrs]
    nice_substrs = [x for x in nice_substrs if len(x) == max(lens)]
    source = [s.index(x) for x in nice_substrs]

    return nice_substrs[source.index(min(source))]


s = "YazaAay"  # "aAa"
s = "Bb"  # "Bb"
s = "c"  # ""
s = "dDzeE"  # "dD"
s = "qQUjJ"
s = "wWOExoVhvXebB"


print(longestNiceSubstring(s))