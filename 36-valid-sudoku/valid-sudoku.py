class Solution:

    def isValidTracker(self, tracker: List[List[int]]) -> bool:

        for row in tracker:
            for col in row:
                if col > 1:
                    return False
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row_tracker = [[0 for _ in range(n)] for _ in range(n)]
        col_tracker = [[0 for _ in range(n)] for _ in range(n)]
        box_tracker = [[0 for _ in range(n)] for _ in range(n)]
        
        # for rows
        for i in range(n):
            for val in board[i]:
                if val != ".":
                    row_tracker[i][ord(val)-ord('0')-1] += 1
        
        # for cols
        for i in range(n):
            for j in range(n):
                val = board[j][i]
                if val != ".":
                    col_tracker[i][ord(val)-ord('0')-1] += 1

        # for boxes
        for b in range(n):
            row = (b // 3) * 3
            col = (b % 3) * 3
            for i in range(row, row+3):
                for j in range(col, col+3):
                    val = board[i][j]
                    if val != ".":
                        box_tracker[b][ord(val)-ord('0')-1] += 1
        
        return self.isValidTracker(row_tracker) and self.isValidTracker(col_tracker) and self.isValidTracker(box_tracker) 

        
        