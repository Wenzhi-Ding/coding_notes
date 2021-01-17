# https://leetcode.com/problems/wildcard-matching/


# Runtime: 72 ms (84.42%)
# Memory: 14 MB (99.29%)

def isMatch(s, p):
    while '**' in p:  # 减少步骤
        p = p.replace('**', '*')

    s_ind = p_ind = 0  # 两个即时游标
    star_ind = s_backtrack_ind = -1  # 两个记忆游标
    
    while s_ind < len(s):
        print(f'star_ind: {star_ind}; s_backtrack_ind: {s_backtrack_ind};')
        print(p[p_ind:], s[s_ind:])

        if p_ind < len(p) and (p[p_ind] == '?' or p[p_ind] == s[s_ind]):  # 正常比较，即时游标向前移动一
            s_ind += 1
            p_ind += 1

        elif p_ind < len(p) and p[p_ind] == '*':  # 遭遇*，更新记忆游标至现在位置，s不动，p向前，恢复正常匹配
            star_ind = p_ind
            s_backtrack_ind = s_ind
            p_ind += 1 

        elif star_ind == -1:  # s已经走完，p未走完且从未遭遇*，则表明一定是不能匹配的
            return False

        else:  # 上一次*的尝试失败了，开始“吃掉”必须被*吃掉的字符（思路的核心！）
            p_ind = star_ind + 1
            s_ind = s_backtrack_ind + 1
            s_backtrack_ind = s_ind
            
    return all(c == '*' for c in p[p_ind:])  # p已匹配完，或只剩下结尾的*



# s = "aa"; p = "a"  # false
# s = "aa"; p = "*"  # true
# s = "cb"; p = "?a"  # false
# s = "adceb"; p = "*a*b"  # true
# s = "acdcb"; p = "a*c?b"  # false
# s = "a"; p = "aa"  # false
# s = "abcabczzzde"; p = "*abc???de*"  # true
# s = "hi"; p = "*?"  # true
# s = "mississippi"; p = "m*iss*"  # true
s = "mississippi"; p = "m*i?s*"  # true
# s = "aaaa"; p = "***a"  # true
# s = "c"; p = "*?*"  # true
# s = "ababbababaaaaabbababaababbaabbabababbbaaaaaaabbbaaaaabbbabbbbbabaabaabaabbabaaabaabababbaaabbaaabbabaabbbbbabbbbaabbbabbabaaaaabaaaaabaaabaaabbabbaabbbaabaaaabaabaaaaabbababaabbabbbbbaabaabaabbbbababbaab"; p = "**bb*a*b**a*a*a*aa*bb*a**aaab***bba*b*aa*aa**aa*a*abbabbbbb*abbb*ba**a*ba****a****bb******b*a*a**ab*a"  # False
# s = "ababbbaabaabaabbbaabaabaaaababaaaabbbabaabbbababbababaababbaababaaabaaaabbbbabbaaaabaaaabbaababbabaababbaaaaabaababbbbbabbaaabbabbbaaabaaaaabbabbbaabababbabbbaaabaabaabababaaabababbbbaababaabababaabba"; p = "**b**a*****abaab*abb**bb*aba***a*a*aab***b*ab*baa*b*b*a**baba****b****bb*abba*bab*****bbab*aab****bab*ba"  # True


print(isMatch(s, p))