def check_row(arr):
    result = 0
    n = len(arr)
    myset = set()

    for i in arr:
        if i == ".":
            continue
        result ^= int(i)
        myset.add(int(i))
    
    for j in myset:
        result ^= j
    
    return result

def check_column(index, arr):
    result = 0
    n = len(arr)
    myset = set()

    for i in range(len(arr)):
        if arr[i][index] == ".":
            continue
        result ^= int(arr[i][index])
        myset.add(int(arr[i][index]))

    for j in myset:
        result ^= j
    
    return result

def check_box(board):
    row = 0
    col = 0
    result = 0
    for R in range(0, 9, 3):
        for C in range(0, 9, 3):
            myset = set()
            for i in range(3):
                for j in range(3):
                    if board[R+i][C+j] == ".":
                        continue
                    result ^= int(board[R+i][C+j])
                    myset.add(int(board[R+i][C+j]))

            for j in myset:
                result ^= j

            if result != 0:
                return result

    return result



    

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # This solution is wrong because xor is not good at finding multiple duplicates
        for index in range(len(board)):
            if check_row(board[index]) != 0:
                return False
            if check_column(index, board) != 0:
                return False

        if check_box(board) != 0:
            return False
        
        return True