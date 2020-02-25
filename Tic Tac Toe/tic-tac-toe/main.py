from tic_tac_toe import TicTacToeGame

def play():
  game = TicTacToeGame()

  while not game.isgameover:
    game.play()
    game.print()
    game.is_over()

  game.print_result()

if __name__ == "__main__":
  play()
