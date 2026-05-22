class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        validRow = defaultdict(set)
        validCol = defaultdict(set)
        validSquares = defaultdict(set) # key: (r//3, c//3)

        for row in range(9):
            for col in range(9):

                val = board[row][col]

                if val == ".":
                    continue
                elif val in validRow[row] or val in validCol[col] or val in validSquares[(row//3, col//3)]:
                    return False
                else:
                    validRow[row].add(val)
                    validCol[col].add(val)
                    validSquares[(row//3, col//3)].add(val)
        
        return True
        
        # Brute force of checking row, col, square separately
        # for row in range(9):
        #     validRows = set()
        #     for col in range(9):
        #         val = board[row][col]
        #         if val != "." and val not in validRows:
        #             validRows.add(val)
        #         elif val in validRows:
        #             return False

        # for col in range(9):
        #     validCols = set()
        #     for row in range(9):
        #         val = board[row][col]
        #         if val != "." and val not in validCols:
        #             validCols.add(val)
        #         elif val in validCols:
        #             return False

        # for square in range(9):
        #     validSquares = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square//3) * 3 + i
        #             col = (square % 3) * 3 + j
        #             if board[row][col] == ".":
        #                 continue
        #             if board[row][col] in validSquares:
        #                 return False
        #             validSquares.add(board[row][col])

        # return True