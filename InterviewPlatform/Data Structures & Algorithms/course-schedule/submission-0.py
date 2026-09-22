class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0]*numCourses

        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegrees[course] += 1

        q = deque()

        finish = 0
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        
        while q:
            node = q.popleft()
            finish += 1

            for i in adj[node]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    q.append(i)


        return finish == numCourses


            




        



            