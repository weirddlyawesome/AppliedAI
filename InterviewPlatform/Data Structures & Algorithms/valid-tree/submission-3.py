class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False


        adj_list = defaultdict(list)

        visited = set()

        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)

        def dfs(node, parent):
            visited.add(node)
            if len(visited) == n:
                return True

            for nei in adj_list[node]:

                if nei == parent:
                    continue
                
                if nei != parent and nei in visited:
                    return False

                if not dfs(nei, node):
                    return False

             



            return True


        if not dfs(0, -1):
            return False

        return len(visited) == n

                

                


        