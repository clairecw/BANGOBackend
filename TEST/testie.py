def check_win(trueBoard):
  #Need to check columns and rows
  stuff = [[True, True, True, True, True], 
           [True, True, True, True, True],
           [True, True]]

  for i in range(5):
    for j in range(5):
      if(i==j):
        stuff[2][0] = stuff[2][0] and trueBoard[i][j]
      if(i == 4-j)
      stuff[0][i] = stuff[0][i] and trueBoard[i][j]
      stuff[1][j] = stuff[1][j] and trueBoard[i][j]
  return True in stuff
