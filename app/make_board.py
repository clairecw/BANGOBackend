from app import *
from app.models import *
import random

def make_boardy(gameID):
  g = Game.query.get(gameID)
  list = g.boarditems[0]
  numBoardItems=len(g.boarditems)
  game = {}
  
  #GENERATE 2-D list of IDs for each board square (except 2,2)
  IDsOneD = random.sample(xrange(0,numBoardItems-1), 24)

  for i in range(5):
    row = []
    for j in range(5):
      if(i == 4 and j == 4):
        row.append({"name":"FREE SPACE", "shortname":"FREE", "diff":0, "id":numBoardItems-1})
      else:
        ite = g.boarditems[IDsOneD[i*5+j]]
        row.append({"name":ite.name, "shortname":ite.shortname, "diff":ite.diff, "id":IDsOneD[i*5 + j]})
    game["row"+str(i)] = row

  #swap free space to right space
  temp = game["row4"][4]
  game["row4"][4] = game["row2"][2]
  game["row2"][2] = temp

  return game