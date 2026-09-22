# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        max_dif = 0

        def find_balance(root):
            nonlocal max_dif
            if not root:
                return 0
            l = find_balance(root.left)
            r = find_balance(root.right)
            curr_diff = abs(l - r)

            if curr_diff > max_dif:
                max_dif = curr_diff


            return  1 + max(l, r)
        find_balance(root)

        return max_dif <= 1