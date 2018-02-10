from app import *
from app.models import *

def check_bango(gameID, board):
  g = Game.query.get(gameID)
  items = g.boarditems

  clientBoard = []
  serverBoard = []
  trueBoard = []
  for i in range(5):
    clientBoard.append([])
    serverBoard.append([])
    trueBoard.append([])
    for j in range(5):
      clientBoard[i].append(False)
      serverBoard[i].append(False)
      trueBoard[i].append(False)


  for i in range(5):
    for j in range(5):
      clientBoard[i][j] = board[i][j]["marked"]
      serverBoard[i][j] = items[board[i][j]["id"]].marked
      trueBoard[i][j] = serverBoard[i][j] and clientBoard[i][j]

  check_win(trueBoard)


def check_win(trueBoard):
  #Need to check columns and rows
  stuff = [[True, True, True, True, True], 
           [True, True, True, True, True],
           [True, True]]

  for i in range(5):
    for j in range(5):
      if(i==j):
        stuff[2][0] = stuff[2][0] and trueBoard[i][j]
      if(i == 4-j):
        stuff[2][1] = stuff[2][1] and trueBoard[i][j]
      stuff[0][i] = stuff[0][i] and trueBoard[i][j]
      stuff[1][j] = stuff[1][j] and trueBoard[i][j]
  return True in stuff