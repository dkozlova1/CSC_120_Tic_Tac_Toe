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

def main():
  board = init_board()
  display_board(board)
  
main()
