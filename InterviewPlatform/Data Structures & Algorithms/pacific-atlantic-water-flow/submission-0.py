class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False]*len(heights[0]) for _ in range(len(heights))]
        atlantic = [[False]*len(heights[0]) for _ in range(len(heights))]


        q_atlantic = deque()
        q_pacific = deque()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j ==0 :
                    pacific[i][j] = True
                    q_pacific.append((i, j))

                if i == len(heights) -1 or j == len(heights[0]) -1:
                    atlantic[i][j] = True
                    q_atlantic.append((i, j))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


        def bfs(q, matrix):
            

            while q:
                i, j = q.popleft()

                for x, y in directions:
                    n_i = i+x
                    n_j = j+y

                    if 0 <= n_i < len(heights) and 0 <= n_j < len(heights[0]) and not matrix[n_i][n_j] and heights[i][j] <= heights[n_i][n_j]:
                        matrix[n_i][n_j] = True
                        q.append((n_i, n_j))



        bfs(q_pacific, pacific)
        bfs(q_atlantic, atlantic)

        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])


        return res

    