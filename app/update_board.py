from app import *
from app.models import *

def update_boardy(gameID, itemID):
  g = Game.query.get(gameID)
  numItems = len(g.boarditems)
  if itemID > numItems:
    return "failure"
  item = g.boarditems[itemID]
  item.marked = not item.marked
  db.session.commit()
  return "success "+str(item.marked)