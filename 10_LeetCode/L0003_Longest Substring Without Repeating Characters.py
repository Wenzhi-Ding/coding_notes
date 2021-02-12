def lengthOfLongestSubstring_mine(s):
    start_pos = max_length = 0
    flag = dict(zip([x for x in range(255)], [False] * 255))
    for end_pos in range(len(s)):
        tmp_char = ord(s[end_pos])
        if flag[tmp_char]:
            flag[ord(s[start_pos])] = False
            start_pos += 1
            continue
        flag[tmp_char] = True
        max_length = max(max_length, end_pos - start_pos)
    return max_length


# 这个写的思路跟我一样，但是enumerate这个可以参考
def lengthOfLongestSubstring_sample(s):
    start = maxlen = 0
    d = {}
    for i, ch in enumerate(s):
        if ch not in d or d[ch] < start:
            maxlen = max(maxlen, i-start+1)
        else:
            start = d[ch]+1
        d[ch] = i
    return maxlen


def lengthOfLongestSubstring_fast(s):
    substring = ''
    max_length = 0
    for le in s:
        if le in substring:
            max_length = max(len(substring), max_length)
            substring = substring[substring.index(le) + 1: ]
        substring += le
    return max(len(substring), max_length)


test = ["abcabcbb", "bbbbb", "pwwkew", "", " ", "cdd"]
for test_str in test:
    print('"%s": %d' % (test_str, lengthOfLongestSubstring_fast(test_str)))
