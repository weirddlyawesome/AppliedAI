class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.steps = [(0,1), (1, 0), (-1, 0), (0,-1)]
        self.rows = len(self.grid)
        self.columns = len(self.grid[0])
        
        res = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == "1":
                    res += 1
                    self.visitnmark(i, j)

        return res

    def visitnmark(self, i, j):
        if not self.isvalid(i, j) or self.grid[i][j] == "0":
            return 

        self.grid[i][j] = "0"

        for x, y in self.steps:
            self.visitnmark(i+x, j+y)

        return

    def isvalid(self, i, j):
        if 0<= i < self.rows and 0 <= j < self.columns:
            return True

        return False