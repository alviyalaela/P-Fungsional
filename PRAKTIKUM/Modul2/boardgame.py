import random

def create_board(width, default_char='-'):
    board = [[default_char for _ in range(width)] for _ in range(width)]
    return board

def generate_random_position(width):
    while True:
        row = random.randint(0, width - 1)
        col = random.randint(0, width - 1)
        yield (row, col)

def place_piece(board, row, col, piece_char):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        board[row][col] = piece_char
    else:
        print("This position is outside of the board.")

def print_board(board):
    for row in board:
        print(' '.join(row))

def move_piece(board, position, move_direction):
    row, col = position
    new_row, new_col = row, col

    if move_direction == 'w' and row > 0 and board[row - 1][col] != '#':
        new_row = row - 1
    elif move_direction == 's' and row < len(board) - 1 and board[row + 1][col] != '#':
        new_row = row + 1
    elif move_direction == 'a' and col > 0 and board[row][col - 1] != '#':
        new_col = col - 1
    elif move_direction == 'd' and col < len(board[0]) - 1 and board[row][col + 1] != '#':
        new_col = col + 1

    if (new_row, new_col) != (row, col):
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
        return new_row, new_col
    else:
        return row, col

def main():
    
    count = 0
    width = int(input("Enter the board game's width: "))
    board = create_board(width)
    
    position_generator = generate_random_position(width)
    start_row, start_col = next(position_generator)
    goal_row, goal_col = next(position_generator)
    place_piece(board, start_row, start_col, 'A')
    place_piece(board, goal_row, goal_col, 'O')
    print_board(board)
    

    while True:
        choose = input(str("Do you want to restart the game? (Y/N)"))
        if choose == "y":
            place_piece(board, start_row, start_col, '-')
            place_piece(board, goal_row, goal_col, '-')
            start_row, start_col = next(position_generator)
            goal_row, goal_col = next(position_generator)
            place_piece(board, start_row, start_col, 'A')
            place_piece(board, goal_row, goal_col, 'O')
            print_board(board)   
            count += 1
        else:
            break

        if count == 3:
            print("You can't restart the game more than thrice")
            break

    while True:
        move_direction = input("Enter your move direction (w/a/s/d) or 'q' to quit the game: ").lower()

        if move_direction == 'q':
            print("You're quit.")
            break

        if move_direction not in ['w', 'a', 's', 'd']:
            print("You lost")
            continue
        

        start_row, start_col = move_piece(board, (start_row, start_col), move_direction)
        print_board(board)

        if (start_row, start_col) == (goal_row, goal_col):
            print("Congratulations! You win!")
            break

if __name__ == "__main__":
    main()

