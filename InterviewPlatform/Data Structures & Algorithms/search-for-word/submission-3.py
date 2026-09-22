class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        paths = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j, k, visited):

            if k == len(word):
                return True

            if not (0 <= i < m and 0 <= j < n):
                return False

            if (i, j) in visited:
                return False

            if board[i][j] != word[k]:
                return False

            visited.add((i, j))

            for di, dj in paths:
                if dfs(i + di, j + dj, k + 1, visited):
                    return True

            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, set()):
                    return True

        return False