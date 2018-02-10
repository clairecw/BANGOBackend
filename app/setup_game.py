from app import *
from app.models import *


def make_game(gameID, name):
  g = Game(id=gameID, name=name)
  db.session.add(g)
  db.session.commit()
  return "success"

def setup(gameID, data):
  g = Game.query.get(gameID)
  for id in range(len(data)):
    i = BoardItem(name=data[id]["name"], shortname=data[id]["shortname"], marked=False, diff=data[id]["diff"], game=g)
    db.session.add(i)
    db.session.commit()
  i = BoardItem(name="FREE SPACE", shortname="FREE", marked=True, diff=0, game=g)
  db.session.add(i)
  db.session.commit()
  return "success"