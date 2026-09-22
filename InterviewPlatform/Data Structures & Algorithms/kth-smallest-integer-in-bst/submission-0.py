# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder_traversal(curr, k):
            nonlocal arr

            if not curr:
                return

            inorder_traversal(curr.left, k)
            arr.append(curr.val)
            inorder_traversal(curr.right, k)

            


        inorder_traversal(root, k)
        return arr[k-1]
