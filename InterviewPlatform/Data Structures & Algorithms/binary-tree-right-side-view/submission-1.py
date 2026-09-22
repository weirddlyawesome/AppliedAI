# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       # right most element at every level
       # BFS Traversal

        if not root:
            return []

        res = []
        q = deque()

        q.append(root)

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                right_most = curr.val

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            res.append(right_most)


        return res

                




