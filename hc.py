import copy
import random

# Thinking of the first dimension as Rows, second as Columns
def randomize_queens(board):
    for i in range(N):
        random_column = random.randint(0,N-1)
        board[i][random_column] = 1

# Returns how many pairs of Queens are attacking each other
# Each Row has only one Queen, thus starting at the first row the function checks
# Only downwards so there's no duplicates
# Stacked(3+) Queen pairs are counted
def attacking_obj(board):
    attacking = 0
    for row in range(N):
        for column in range(N):
            if(board[row][column] == 1):
                #checking downwards vertically
                for q_row in range(row+1, N):
                    if(board[q_row][column] == 1):
                        attacking += 1
                #checking downwards diagonally leftwise
                for i,j in zip(range(row+1, N),
                               range(column-1, -1, -1)):
                    # print("Current value: %d" %(board[i][j]))
                    if(board[i][j] == 1):
                        attacking +=1
                #checking downwards diagonally rightwise
                for i,j in zip(range(row+1, N),
                               range(column+1, N)):
                    if(board[i][j] == 1):
                        attacking +=1

    return attacking


def choose_neighbour(board):
    board_temp = copy.deepcopy(board)

    row_temp = attacking_obj(board)
    previous_temp = row_temp

    while(attacking_obj(board) > 0):
        if(row_temp == previous_temp):
            random_row = random.randint(0, N-1)
            random_column = random.randint(0, N-1)
            if(board[random_row][random_column] != 1):
                board[random_row][random_column] = 1
                for i in range(0,N):
                    if(i != random_column):
                        board[random_row][i] = 0


            a = random.randint(1, 1000)
            if(a == 5):
                for i in range(0, N):
                    rand = random.randint(0,N-1)
                    board[i][rand] = 1
                    for j in range(0,N):
                        if(board[i][j] == 1 and j != rand):
                            board[i][j] = 0



        # print("Row temp is: %d previous_temp is: %d" %(row_temp, previous_temp))
        for i in range(0,N):
            row_index = -1

            for j in range(0,N):
                if(board_temp[i][j] != 1):
                    board_temp[i][j] = 1
                    # Removing the other Queen in the row
                    for k in range(0,N):
                        if(k != j):
                            board_temp[i][k] = 0
                            # print_board(board_temp)
                            # a = input("...")
                            if(attacking_obj(board_temp) < row_temp):
                                row_temp = attacking_obj(board_temp)
                                board = copy.deepcopy(board_temp)
                                # print_board(board)
                                # a = input("...")


        previous_temp = row_temp

    return board

def print_board(board):
    for i in range(N):
        print(board[i])

# run
N = int(input("Enter the Number of Queens: "))

print("Initialising for a  %d x %d chessboard..." %(N, N))
main_board = [[0]*N for i in range(N)] # Creates a NxN matrix with every value being 0
randomize_queens(main_board)

print("Printing initial randomized state: ")
print_board(main_board)

print("Current number of pairs of Queens attacking each other: %d" %(attacking_obj(main_board)))
print("Calculating solution")
main_board = choose_neighbour(main_board)
print_board(main_board) 
