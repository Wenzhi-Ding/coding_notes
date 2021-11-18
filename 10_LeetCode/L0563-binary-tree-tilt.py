# https://leetcode-cn.com/problems/binary-tree-tilt/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.res = 0

        def helper(node):
            if not node:
                return 0

            l_sum = helper(node.left)
            r_sum = helper(node.right)

            # Postorder traversal
            self.res += abs(r_sum - l_sum)  
            return l_sum + r_sum + node.val

        helper(root)

        return self.res

