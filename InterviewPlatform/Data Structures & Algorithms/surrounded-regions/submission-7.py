class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        rows = len(board)
        cols = len(board[0])

        captured = [[True]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j ==0 or i == rows - 1 or j == cols -1:
                    if board[i][j] == "O":
                        q.append((i, j))
                        captured[i][j] = False


        while q:

            i, j = q.popleft()

            for x, y in directions:
                n_i = i +x
                n_j = j +y

                if 0 <= n_i < rows and 0 <= n_j < cols and board[n_i][n_j] == 'O' and captured[n_i][n_j] == True:
                    captured[n_i][n_j] = False
                    q.append((n_i, n_j))


        for i in range(rows):
            for j in range(cols):
                if captured[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'




        

        