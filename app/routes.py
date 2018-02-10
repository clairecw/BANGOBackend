from app import app, models, db, setup_game
from app.models import *
from app.setup_game import *
from app.update_board import *
from flask import jsonify, abort, request
from app.make_board import *
from app.check_win import *
games = []

@app.route('/')
@app.route('/index')
def index():
  return "Hello, World!"
@app.route('/getnextgameid', methods=['GET'])
def get_id():
  NoneType = type(None)
  for i in range(1, 100):
    if(type(Game.query.get(i)) == NoneType):
      return str(i)
  return '-1'

@app.route('/getboard', methods=['GET'])
def get_tasks():
  #TODO add getBoard fun
  return jsonify({'tasks': tasks})

@app.route('/postgame', methods=['POST'])
def create_game():
  data = request.get_json()
  return jsonify(make_game(data["id"], data["name"]))

@app.route('/postitems', methods=['POST'])
def add_board_list():
  data = request.get_json()
  return jsonify(setup(data["gameID"], data["items"]))

@app.route('/getboard', methods=['POST', 'GET'])
def get_board():
  data = request.get_json()
  gameID = data["gameID"]
  return jsonify(make_boardy(gameID))

#Next assumes you just flip the marked variable at the item id
@app.route('/updateitem', methods=['POST'])
def update_item():
  data = request.get_json()
  return jsonify(update_boardy(data["gameID"], data["itemID"]))

@app.route('/bango', methods=['POST', 'GET'])
def bango():
  data = request.get_json()
  return jsonify(check_bango(data["gameID"], data["board"]))





@app.route('/testget', methods=['POST', 'GET'])
def testjson():
  #data = request.get_json()
  Board = [
    [
      {
        "name":"Fed eats it",
        "shortname":"FeddyWap",
        "diff":0,
        "id":1
      },
      {
        "name":"Fed eats itasdfassf",
        "shortname":"FeddyWasdfap",
        "diff":0,
        "id":2
      }
    ],
    [
      {
      "name":"Fed eats itasdf",
        "shortname":"FeddyWasdfapsfsd",
        "diff":0,
        "id":3
      },
      {
        "name":"Fed eats sfsfit",
        "shortname":"FeddyfasdfsdWap",
        "diff":0,
        "id":4
      }
    ]
  ]
  return jsonify(Board)