# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.util(root)

        return root
        
    def util(self, curr):
        if curr is None:
            return 

        t = curr.left
        curr.left = curr.right
        curr.right = t

        self.util(curr.left)
        self.util(curr.right)

        