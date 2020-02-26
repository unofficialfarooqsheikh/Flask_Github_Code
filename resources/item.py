from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sql import SQL
from models.item import ItemModel 
class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):
        item = ItemModel.find_by_item_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_item_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}
        data = Item.parser.parse_args()
        item = ItemModel(name,data["price"],data['store_id'])
        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"An error occurred inserting the item.,{e}"}
        return item.json()

    @jwt_required()
    def delete(self, name):
        # connection = SQL()
        # with connection:
        #     cursor = connection.cursor()
        #     query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        #     cursor.execute(query, (name,))
        #     cursor.commit()
        # return {'message': 'Item deleted'}
        # __________using SQL Alchemy______________
        item = ItemModel.find_by_item_name(name)
        if item:
            item.Delete()
        return {'message': 'Item deleted'}
        
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_item_name(name)
        if item is None:
            item = ItemModel(name,data["price"],data['store_id'])
        else:
            item.price = data["price"] 
            item.store_id = data['store_id']
        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"An error occurred inserting the item. {e}"}
        finally:
            return item.json()


class ItemList(Resource):
    
    def get(self):
        # connection = SQL()
        # with connection:
        #     cursor = connection.cursor()
        #     query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        #     result = cursor.execute(query)
        #     items = []
        #     for row in result:
        #         items.append({"id":row[0],'name': row[1], 'price': row[2]})
        # return {'items': items}
        items = ItemModel.get_all_items()
        return {"items": list(map(lambda x: x.json(), items))}