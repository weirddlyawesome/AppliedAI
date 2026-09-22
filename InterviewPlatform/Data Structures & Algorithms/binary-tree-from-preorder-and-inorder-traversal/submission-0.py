# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.dict_inorder = {}
        for i in range(len(inorder)):
            self.dict_inorder[inorder[i]] = i
        self.pre_order = 0

        def build_tree(left, right):

            if left > right:
                return None

            value =  preorder[self.pre_order]
            mid = self.dict_inorder[value]

            root = TreeNode(value)

            self.pre_order += 1

            root.left = build_tree(left, mid-1)
            root.right = build_tree(mid+1, right)


            return root

        return build_tree(0, len(inorder) - 1)

              