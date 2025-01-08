class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {j: set() for j in range(9)}
        grids = {(i, j): set() for i in range(3) for j in range(3)}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num.isnumeric():
                    # Check row
                    if num in rows[i]:
                        return False
                    else:
                        rows[i].add(num)

                    # Check column
                    if num in cols[j]:
                        return False
                    else:
                        cols[j].add(num)

                    # Check grid
                    num_grid = (i // 3, j // 3)
                    if num in grids[num_grid]:
                        return False
                    else:
                        grids[num_grid].add(num)

        return True
