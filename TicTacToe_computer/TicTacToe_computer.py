# prints the passed grid
def print_grid(grid = {}):
    empty = ' '
    for cell_no in range(1,10,3):
        print(' {} | {} | {} '.format(grid[cell_no], grid[cell_no+1], grid[cell_no+2]), end = '' )       
        print(' \t{} | {} | {} '.format(cell_no if grid[cell_no] == ' ' else empty, cell_no+1 if grid[cell_no+1] == ' ' else empty, cell_no+2 if grid[cell_no+2] == ' ' else empty))
        if(cell_no < 5):
            print(' --+---+-- \t--+---+--');

def check_winner(grid = {}):
    # row check
    if((grid[1] != ' ') and (grid[1] == grid[2]) and (grid[2] == grid[3])):
        return grid[1]

    if((grid[4] != ' ') and (grid[4] == grid[5]) and (grid[5] == grid[6])):
        return grid[4]

    if((grid[7] != ' ') and (grid[7] == grid[8]) and (grid[8] == grid[9])):
        return grid[7]
   
   # column check
    if((grid[1] != ' ') and (grid[1] == grid[4]) and (grid[4] == grid[7])):
        return grid[1]

    if((grid[2] != ' ') and (grid[2] == grid[5]) and (grid[5] == grid[8])):
        return grid[2]

    if((grid[3] != ' ') and (grid[3] == grid[6]) and (grid[6] == grid[9])):
        return grid[3]
   
   # diagonal check 
    if((grid[1] != ' ') and (grid[1] == grid[5]) and (grid[5] == grid[9])):
        return grid[1]

    if((grid[7] != ' ') and (grid[7] == grid[5]) and (grid[5] == grid[3])):
        return grid[7]

    return ' '

def check_tie(grid):
    for cell_no in range(1,10):
        if not(grid[cell_no].isalpha()):
            return False
    return True


def user_inp(grid = {}):
    while(True):
        user_move = input("\nEnter 'X' in cell (1-9) : ")

        if not(user_move.isnumeric()):
            print("Invalid Cell Input (Enter 0-9)")

        elif(int(user_move) < 1 or int(user_move) > 9):
            print("Invalid Cell Input (Enter 0-9)")

        elif(grid[int(user_move)] != ' '):
            print('Position already occupied')

        else:
            grid[int(user_move)] = 'X'
            break

def compMove(grid = {}, whos_move = 'cpu'):

    if(check_winner(grid) == 'O'):
        return [0, 1]

    if(check_winner(grid) == 'X'):
        return [0, -1]

    if(check_tie(grid)):
        return [0, 0]

    optimal_move = []

    for cell_no in range(1,10):
        if(grid[cell_no] == ' '):
            grid_cpy = grid.copy()

            if(whos_move == 'cpu'):
                grid_cpy[cell_no] = 'O'
                curr_move = compMove(grid_cpy, 'user')
                if(len(optimal_move) == 0):
                    optimal_move = [cell_no, curr_move[1]]
                elif(curr_move[1] > optimal_move[1]):
                    optimal_move = [cell_no, curr_move[1]]

            if(whos_move == 'user'):
                grid_cpy[cell_no] = 'X'
                curr_move = compMove(grid_cpy, 'cpu')
                if(len(optimal_move) == 0):
                    optimal_move = [cell_no, curr_move[1]]
                elif(curr_move[1] < optimal_move[1]):
                    optimal_move = [cell_no, curr_move[1]]

    return optimal_move


# define and initialize the tic tac toe grid to be completely empty
# this is main()
grid = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

play_game = 'y'

while(play_game == 'y'):
    
    print_grid(grid)
    user_inp(grid)
    
    if(check_winner(grid) != ' '):
        print_grid(grid)
        print('{} is the winner!'.format(check_winner(grid)))
        break
    elif(check_tie(grid)):
        print_grid(grid)
        print('Its a Tie!')
        break
    
    move_lst = compMove(grid)
    print(move_lst)
    grid[move_lst[0]] = 'O'
    
    if(check_winner(grid) != ' '):
        print_grid(grid)
        print('{} is the winner!'.format(check_winner(grid)))
        break
    elif(check_tie(grid)):
        print_grid(grid)
        print('Its a Tie!')
        break
