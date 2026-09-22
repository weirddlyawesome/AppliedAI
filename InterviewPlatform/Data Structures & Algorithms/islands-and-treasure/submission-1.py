class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        grid = grid
        rows = len(grid)
        columns = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()

            for x, y in directions:
                n_r = i +x
                n_c = j +y

                if (0 <= n_r < rows and 0 <= n_c < columns) and grid[n_r][n_c] == 2147483647:
                    grid[n_r][n_c] = grid[i][j] + 1
                    queue.append((n_r, n_c))




        

        

        

    

    
        