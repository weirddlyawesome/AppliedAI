class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        que = deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    que.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        res = 0

        while que:
            flag = False

            n = len(que)

            for _ in range(n):
                i, j = que.popleft()

                for x, y in directions:
                    n_r = i + x
                    n_c = j + y

                    if (0 <= n_r < rows and
                        0 <= n_c < cols and
                        grid[n_r][n_c] == 1):

                        grid[n_r][n_c] = 2
                        fresh -= 1
                        flag = True

                        que.append((n_r, n_c))

            if flag:
                res += 1

        return res if fresh == 0 else -1