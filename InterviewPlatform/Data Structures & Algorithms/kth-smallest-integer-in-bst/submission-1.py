# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.answer = None

        def inorder_traversal(curr):
            if not curr:
                return

            inorder_traversal(curr.left)
            self.k -= 1
            if not self.k:
                self.answer = curr.val
                return



            inorder_traversal(curr.right)

            


        inorder_traversal(root)
        return self.answer
