from app import db

class Game(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, index=True, unique=True, nullable=False)
  boarditems = db.relationship('BoardItem', backref='game', lazy=True)

  def __repr__(self):
    return '<Name {}, Marked {}>'.format(self.name, self.marked) 


class BoardItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, index=True, unique=True, nullable=False)
  shortname = db.Column(db.String(80), index=True, unique=True, nullable=False)
  marked = db.Column(db.Boolean)
  game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

  def __repr__(self):
    return '<Name {}, Marked {}>'.format(self.name, self.marked) 

