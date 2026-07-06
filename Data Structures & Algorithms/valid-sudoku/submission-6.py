class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidArr(arr: List[str]) -> bool:
            seen = set()

            for num in arr:
                if num == ".":
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)

            return True

        colArr = []
        
        for i in range(9):
            col = []
            for arr in board:
                col.append(arr[i])

            colArr.append(col)

        subBoard = []

        for i in range(3):
            for j in range(3):
                sub = []

                for row in range(i*3, i*3 + 3):
                    for col in range(j*3, j*3 + 3):
                        sub.append(board[row][col])

                subBoard.append(sub)

        for row in board:
            if not isValidArr(row):
                return False

        for col in colArr:
            if not isValidArr(col):
                return False

        for sub in subBoard:
            if not isValidArr(sub):
                return False

        return True