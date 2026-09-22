class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        res = []
        while q:
            prev = q.popleft()
            finish += 1
            res.append(prev)

            for node in adj[prev]:
                indegree[node] -= 1

                if indegree[node] == 0:
                    q.append(node)

        if finish == numCourses:
            return res
        
        return []