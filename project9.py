from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('project9', user='lawrenceyee521', password='12345', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Champion(BaseModel):
  name = CharField()
  attribute = CharField()
  branch = CharField()

class Item(BaseModel):
  name = CharField()
  stat = CharField()

db.connect()
db.drop_tables([Champion])
db.create_tables([Champion])
db.drop_tables([Item])
db.create_tables([Item])

Champion(name="Malzahar", attribute="Arcanist", branch="Mutant").save()
Champion(name="Swain", attribute="Arcanist", branch="Hextech").save()
Champion(name="Ziggs", attribute="Arcanist", branch="Yordle").save()
Champion(name="Ahri", attribute="Arcanist", branch="Syndicate").save()
Champion(name="Viktor", attribute="Arcanist", branch="Chemtech").save()
Champion(name="Vex", attribute="Arcanist", branch="Yordle").save()
Champion(name="Malzahar", attribute="Arcanist", branch="Mutant").save()
Champion(name="Brand", attribute="Arcanist", branch="Debonair").save()
Champion(name="Orianna", attribute="Enchanter", branch="Clockwork").save()
Champion(name="Lulu", attribute="Enchanter", branch="Yordle").save()
Champion(name="Morgana", attribute="Enchanter", branch="Syndicate").save()
Champion(name="Senna", attribute="Enchanter", branch="Socialite").save()
Champion(name="Morgana", attribute="Enchanter", branch="Syndicate").save()

Item(name="Arch Angel Staff", stat="+ 25 AP every 5 seconds").save()
Item(name="Hextech Gunblade", stat="AP heal for 33% of damage dealt").save()
Item(name="Rabadon's Deathcap", stat="75 bonus AP").save()
Item(name="Jeweled Gauntlet", stat="Magic and AP can critically strike").save()
Item(name="Guinsoo's Rageblade", stat="AP attacks grant +6% bonus Attack Speed").save()
Item(name="Morello", stat="AP burns 20% of max HP").save()

app = Flask(__name__)
@app.route('/', methods=['GET'])
def welcome():
  return "Team Fight Tactics"


@app.route('/champion/', methods=['GET', 'POST'])
@app.route('/champion/<name>', methods=['GET', 'PUT', 'DELETE'])
def champs(name=None):
  if request.method == 'GET':
    if name:
      return jsonify(model_to_dict(Champion.get(Champion.name == name)))
    else:
      champList = []
      for champ in Champion.select():
        champList.append(model_to_dict(champ))
      return jsonify(champList)
  if request.method == 'POST':
    new_Champ = dict_to_model(Champion, request.get_json())
    new_Champ.save()
    return jsonify({"success": True})
  if request.method == 'DELETE':
    remove_Champ = Champion.get(Champion.name.lower() == name.lower())
    remove_Champ.delete_instance()

@app.route('/items/', methods=['GET', 'POST'])
@app.route('/items/<name>', methods=['GET', 'PUT', 'DELETE'])
def items(name=None):
  if request.method == 'GET':
    if name:
      return jsonify(model_to_dict(Item.get(Item.name.lower() == name.lower())))
    else:
      itemList = []
      for item in Item.select():
        itemList.append(model_to_dict(item))
      return jsonify(itemList)
  if request.method == 'POST':
    new_Item = dict_to_model(Item, request.get_json())
    new_Item.save()
    return jsonify({"success": True})
  if request.method == 'DELETE':
    remove_Item = Item.get(Item.name == name)
    remove_Item.delete_instance()


app.run(host="localhost", port=1234, debug=True)