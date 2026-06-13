class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row
        for i in range(len(board[0])):
            visited = []
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in visited:
                    return False
                else:
                    visited.append(board[i][j])
        
        #col
        for i in range(len(board)):
            visited = []
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in visited:
                    return False
                else:
                    visited.append(board[j][i])
                    
        #grids

        myLst = [[0,1,2], [3,4,5], [6,7,8]]

        for LstInd1 in range(3):
            for LstInd2 in range(3):
                visited = []
                for i in range(3):
                    for j in range(3):
                        if board[myLst[LstInd1][i]][myLst[LstInd2][j]] == ".":
                            continue
                        elif board[myLst[LstInd1][i]][myLst[LstInd2][j]] in visited:
                            return False
                        else:
                            visited.append(board[myLst[LstInd1][i]][myLst[LstInd2][j]])
        return True



        