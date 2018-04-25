from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []
class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        data = request.get_json()
        print(data)
        item = {'name': name, 'price': 17.00}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')  #127.0.0.1:5000/item/pen
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)