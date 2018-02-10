from app import db

class Game(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, index=True, nullable=False)
  boarditems = db.relationship('BoardItem', backref='game', lazy=True)

  def __repr__(self):
    return '<Name {}, ID {}>'.format(self.name, self.id) 


class BoardItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, index=True, nullable=False)
  shortname = db.Column(db.String(80), index=True, nullable=False)
  marked = db.Column(db.Boolean)
  diff = db.Column(db.Integer)
  game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

  def __repr__(self):
    return '<Name {}, Marked {}>'.format(self.name, self.marked) 

