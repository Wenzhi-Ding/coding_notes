# https://leetcode.com/problems/largest-merge-of-two-strings/

# 迅速解决的关键在于想明白：不是比较下一个字符的大小（只能得到局部最优），而是比较剩余字符串的大小（得到全局最优）

# Runtime: 100 ms
# Memory Usage: 14.7 MB

def largestMerge(word1, word2):
    merge = ''
    pt1, pt2 = 0, 0
    while (pt1 < len(word1)) & (pt2 < len(word2)):
        if word1[pt1:] > word2[pt2:]:
            merge += word1[pt1]
            pt1 += 1
        else:
            merge += word2[pt2]
            pt2 += 1
    return merge + word1[pt1:] + word2[pt2:]


# 利用list.pop的特性将上面代码压缩

# Runtime: 124 ms
# Memory Usage: 14.7 MB

def largestMerge(word1, word2):
    A = list(word1)
    B = list(word2)
    return "".join([max(A, B).pop(0) for _ in A + B])


word1 = "cabaa"; word2 = "bcaaa"; ans = "cbcabaaaaa"
# word1 = "abcabc"; word2 = "abdcaba"; ans = "abdcabcabcaba"
# word1 = "uuurruuuruuuuuuuuruuuuu"; word2 = "urrrurrrrrrrruurrrurrrurrrrruu"; ans = "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"
# word1 = "nnnnpnnennenpnnnnneenpnn"; word2 = "nnnennnnnnpnnennnnennnnee"; ans = "nnnnpnnnnnennnnnnpnnennnnennnnennenpnnnnneenpnnee"


a = largestMerge(word1, word2)
print(a)
print(ans)
print(a == ans)