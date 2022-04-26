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

db.connect()
db.drop_tables([Champion])
db.create_tables([Champion])


app = Flask(__name__)


@app.route('/champion/', methods=['GET', 'POST'])
@app.route('/champion/<name>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(name=None):
  if request.method == 'GET':
    if name:
      return jsonify(model_to_dict(Champion.get(Champion.name == name)))
    else:
      champList = []
      for champ in Champion.select():
        champList.append(model_to_dict(champ))
      return jsonify(champlist)