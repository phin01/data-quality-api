from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []


class Items(Resource):
    def get(self):
        return items


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': 'item not found'}, 404

    def post(self, name):
        new_item = {'name': name, 'price': 12}
        items.append(new_item)
        return new_item, 201


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)