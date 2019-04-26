# class Nqueen():
#     def __init__(self,r,c):
#         self.board = [0]*r
#         for i in range(r):
#             self.board[i] = [0]*c
#         self.r = r
#         self.c = c
#
#     def ans(self):
#
#         def nq_recur(r,c):
#             if any(self.board[r]):
#                 nq_recur(r+1,c)
#             elif any([self.board[i][c] for i in range(self.r)]):
#                 nq_recur(r, c+1)
#             any([self.board[i][j]] for i in range(self.r) for j in range(self.c)):
#                 nq_recur(r+1,c)
#             if any([self.board[i][j-i]] for i in range(self.r) for j in range(self.c)):
#                 nq_recur(r+1,c)
#
# nq = Nqueen(4,4)
#
# print(nq.ans())



# Python program to solve N Queen
# Problem using backtracking

global N
N = 4

def printSolution(board):
    for i in range(N):
        print (board[i])

# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens

def isSafe(board, row, col):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i,j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True
def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    global solutions
    saved_board = board[:][:]
    solutions.append(saved_board)


def solveNQUtil(board, col):
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):

        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # add solution
            if col == N-1:
                add_solution(board)
                board[i][col] = 0
                return
            # recur to place rest of the queens
            if solveNQUtil(board, col+1) == True:
                return True

            # If placing queen in board[i][col]
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this colum col then return false
    return False

# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one of the
# feasible solutions.
def solveNQ():
    board = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False

    # printSolution(board)
    print(solutions)
    return True
solutions = []
# driver program to test above function
solveNQ()

# This code is contributed by Divyanshu Mehta
