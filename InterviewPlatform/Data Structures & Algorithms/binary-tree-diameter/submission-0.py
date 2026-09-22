# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def find_max(root):
            nonlocal max_diameter
            if not root:
                return 0

            left_res = find_max(root.left)
            right_res = find_max(root.right)

            curr_diameter = left_res + right_res
            if curr_diameter > max_diameter:
                max_diameter = curr_diameter

            return 1 + max(left_res, right_res)


        find_max(root)

        return max_diameter