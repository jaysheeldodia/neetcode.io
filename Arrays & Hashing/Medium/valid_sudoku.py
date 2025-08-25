from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}

        for i in range(9):
            rows[i] = []
            columns[i] = []
        
        # check rows and columns
        for i in range(9):
            for j in range(9):
                if board[i][j].isalnum():
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])

        for i in range(9):
            if len(rows[i]) == len(set(rows[i])) and len(columns[i]) == len(set(columns[i])):
                continue
            else:
                return False
            

        # 
        first_three = board[:3]
        second_three = board[3:6]
        last_three = board[6:]

        for k in range(0, 9, 3):
            temp = []
            for i in range(3):
                for j in range(k, k+3):
                    if first_three[i][j].isdigit():
                        temp.append(first_three[i][j])


            if len(set(temp)) != len(temp):
                return False
            

        for k in range(0, 9,3):
            temp = []
            for i in range(3):
                for j in range(k, k+3):
                    if second_three[i][j].isdigit():
                        temp.append(second_three[i][j])
            
            if len(set(temp)) != len(temp):
                return False

        for k in range(0, 9, 3):
            temp = []
            for i in range(3):
                for j in range(k, k+3):
                    if last_three[i][j].isdigit():
                        temp.append(last_three[i][j])
            
            if len(set(temp)) != len(temp):
                return False
            
        return True
    

print(Solution().isValidSudoku(board=
[[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]))
print(Solution().isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))