# https://leetcode-cn.com/problems/count-items-matching-a-rule/

# Runtime: 220 ms
# Memory: 20.4 MB

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        idx = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
        ans = 0
        for item in items:
            if item[idx] == ruleValue: ans += 1
        return ans

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

# items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
# ruleKey = "type"
# ruleValue = "phone"

sol = Solution()
print(sol.countMatches(items, ruleKey, ruleValue))