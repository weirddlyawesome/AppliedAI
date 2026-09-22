class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        res = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j]:
                    res = max(res, self.find_area(i, j))
        
        return res


    def find_area(self, i, j):
        area = 0
        if not self.is_valid(i, j) or self.grid[i][j] == 0:
            return area

        self.grid[i][j] = 0
        area += 1

        for x, y in self.directions:
            area += self.find_area(i +x, y +j)

        return area

    
    def is_valid(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            return True

        return False
    