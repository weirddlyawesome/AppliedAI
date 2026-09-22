"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        self.visited = dict()

        def dfs(curr):
            if not curr:
                return None

            if curr in self.visited:
                return self.visited[curr]

            
            root = Node(curr.val, [])
            self.visited[curr] = root

            for node in curr.neighbors:
                new_node = dfs(node)
                if new_node:
                    root.neighbors.append(new_node)

            return root

        return dfs(node)