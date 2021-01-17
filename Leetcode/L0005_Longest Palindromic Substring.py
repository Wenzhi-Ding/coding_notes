def longestPalindrome_fast(s):  ## 92ms
    start_odd, max_odd = 0, 1
    start_even, max_even = 0, 0
    
    for i in range(len(s)):
        if i - max_odd - 1 >= 0 and s[i - max_odd - 1:i + 1] == s[i - max_odd - 1:i + 1][::-1]:  # Python有字符串倒转和比较的功能，就不要自己一个个字符的去比了，显然慢得多
            start_odd = i - max_odd - 1
            max_odd += 2  # max的设计实现了有效的剪枝，在后面的遍历中，短于max的字符串都不看了
        if i - max_even - 1 >= 0 and s[i - max_even - 1:i + 1] == s[i - max_even - 1:i + 1][::-1]:
            start_even = i - max_even - 1
            max_even += 2

    return s[start_even:start_even + max_even] if max_odd < max_even else s[start_odd:start_odd + max_odd]
        


def longestPalindrome_mine(s):  # 162ms，未剪枝前1776ms
    result = ""
    center = 0
    while center < len(s):
        start = round(center - len(result) // 2 + 0.1)  # 0.1是为了避开Python3中round(0.5)=0的问题
        end = int(center + len(result) // 2)
        while (0 <= start) and (end < len(s)):
            if s[start:end + 1] == s[start:end + 1][::-1]:
                if end - start + 1 > len(result):
                    result = s[start:end + 1]
                start -= 1
                end += 1
            else:
                break
        center += 0.5
    return result


## Test Unit
args_lst = [
            "babad",
            "cbbd",
            "a",
            "",
            "aaaa",
            "ccc"
            ]
for arg in args_lst:
    print(arg, longestPalindrome_mine(arg))