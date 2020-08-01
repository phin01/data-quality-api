from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []


class ItemList(Resource):
    def get(self):
        return {'items': items}


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'message': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'an item with name {} already exists'.format(name)}, 400

        request_data = request.get_json()
        try:
            new_item = {'name': name, 'price': request_data['price']}
            items.append(new_item)
            return new_item, 201
        except:
            return {'message': 'could not create item'}, 400


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)