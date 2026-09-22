class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])


        # row_num = index//#cols
        # col_num = index % #cols


        #index = cols*row_num + col_num

        l = 0
        r = rows * cols - 1

        while l <= r:
            mid = (l+r)//2
            row_num = mid // cols
            col_num = mid % cols

            curr = matrix[row_num][col_num]

            if curr == target:
                return True
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1


        return False
        