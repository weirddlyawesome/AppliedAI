# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        list_nodes = self.util_nodes(root, subRoot)
        if not list_nodes:
            return False

        for node in list_nodes:
            if self.same_tree(node, subRoot):
                return True

        return False

    def same_tree(self, root, subroot):
        if not subroot and not root:
            return True

        if not subroot or not root:
            return False

        return root.val == subroot.val and self.same_tree(root.left, subroot.left) and self.same_tree(root.right, subroot.right)

        

    def util_nodes(self, root, subRoot):
        res = []

        def find_nodes(curr, subRoot):
            if not curr:
                return 
            nonlocal res

            if curr.val == subRoot.val:
                res.append(curr)

            find_nodes(curr.left, subRoot)
            find_nodes(curr.right, subRoot)

            return 


        find_nodes(root, subRoot)

        return res    