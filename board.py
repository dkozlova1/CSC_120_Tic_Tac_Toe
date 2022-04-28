NUM_ROWS = 3
NUM_COLS = 3

DEF INIT_BOARD():
  """
  initialize board as a list of lists
     where - means empty
  """
  
  board = [["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"]]
  return board

def display_board(board):

print("\n")
for row in range(0,NUM_ROWS):
  for col in range(0,NUM_COLS):
    if col != NUM_COLS - 1:
      print(board[row][col]+" | ",end="")
      else:
        print(board[row][col])
print("\n")
   

def is_valid_move(board,row,col):
  
  if row > NUM_ROWS or row < 1:
    return False
  elif col > NUM_COLS or col <1:
    return False
  elif board[row - 1][col - 1] != "-":
    return False
  else:
    return True
  
  def player_move(board,symbol):
    row_choice = int(input(f"Choose a row position from 1 to {NUM_ROWS}:"))
    col_choice = int(input(f"Choose a column position from 1 to {NUM_COLS}:"))
    
  while not is_valid_move(board,row_choice,col_choice):
    print("That is not a valid move choice. Try again")
    row_choice = int(input(f"Choose a row position from 1 to {NUM_ROWS}:"))
    col_choice = int(input(f"Choose a column position from 1 to {NUM_COLS}:"))
    
  board[row_choice - 1][col_choice - 1] = symbol
  
  return(board)
  
 def is_board_full(board):
  count_nonempty = 0 
  for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
      if board[row][col] != "-":
        count_nonempty += 1
  if count_nonempty == NUM_ROWS * NUM_COLS:
    return True
  else:
    return False
def is_row_won(board,row,symbol):
  for col in range(NUM_COLS):
    if board[row - 1][col] != symbol:
      return False
  return True

def is_col_won(board,col,symbol):
  for raw in range(NUM_ROWS):
    if board[row][col -1] != symbol:
      return False
  return True

def is_any_row_won(board,sybol):
  for raw in range(NUM_ROWS):
    if is_row_won(board,row,symbol):
      return True
  return False
def is_any_col_won(board,sybol):
  for col in range(NUM_COLS):
    if is_col_won(board,col,symbol):
      return True
  return False
def is_diag1_won(board,sybol):
  for raw in range(NUM_ROWS):
    col = row
    if board[row][col] != symbol:
      return False
  return True
def is_diag2_won(board,sybol):
  for col in range(NUM_COLS):
    row = NUM_ROWA - 1 - col
    if board[row][col] != symbol:
      return False
  return True

def is_won(board,symbol):
  return is_any_row_won(board,symbol) or is_any_col_won(board,symbol) or is_diag1_won(board,sybol) or is_diag2_won(board,sybol)
def play_tictactoe():
  is_game_over = False
  board = init_board9)
  current_player_symbol = "X"
  display_board(board)
  
  while not is_game_over:
    print(f"\nPlayer {current_player_symbol}'s Turn:")
    board = player_move(board,current_player_symbol)
    display_board(board)
    
    if is_won(board,current_player_symbol):
       print(f"Player {current_player_symbol} won !")
        is_game_over = True
        elis is_board_full(board):
          print(f"Game Over as a DRAW")
          is_game_over = True
        else:
          if current_player_symbol == "X":
            current_player_symbol ="O"
            else:
              current_player_symbol = "X"
   print(("Thank you for playing Tic Tac Toe")
def main():
  play_tictactoe()
  board = init_board()
  display_board(board)
  
  board = player_move(board, symbol = "X")
  display_board(board)
         
  
main()
