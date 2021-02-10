# https://leetcode-cn.com/problems/permutation-in-string/

from collections import Counter, defaultdict

# Runtime: 64 ms (95%)
def checkInclusion(s1, s2):
    s1c = Counter(s1)
    s2c = Counter(s2[:len(s1)])  # 还可以通过只关注s1中的字母来减少哈希表的更新次数，不过已经够快了，懒得优化了
    for i in range(len(s2) - len(s1)):
        if s1c == s2c: return True
        s2c[s2[i]] -= 1
        if s2c[s2[i]] == 0: del s2c[s2[i]]  # 可以这样删除字典中的某个键
        c = s2[i+len(s1)]
        s2c[c] += 1  # Counter类通过定义__missing__默认返回0来保证不会产生KeyError
    return s1c == s2c

# 字符串长度至少为1，不用考虑空字符串的情况

s1 = "ab"; s2 = "eidbaooo"; ans = True
# s1 = "ab"; s2 = "eidboaoo"; ans = False
# s1 = "abc"; s2 = "bbbca"; ans = True
# s1 = "ab"; s2 = "a"; ans = False  # 初始化字典时考虑s1短于s2的情况

print(checkInclusion(s1, s2) == ans)

