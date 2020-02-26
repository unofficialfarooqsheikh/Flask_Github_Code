from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel 

class Store(Resource):


    def get(self,name):
        store = StoreModel.find_by_store_name(name)
        if store:
            return store.json()
        else:
            return {"message": f"store not found"},404

    @jwt_required()
    def post(self,name):
        if StoreModel.find_by_store_name(name):
            return {"message": f"store {name} Exists"},400
        else:
            store = StoreModel(name)
            try:
                store.add_store_to_db()
                return {"message": "store Created successfully"}
            except Exception as e:
                return {"message": f"Error with Connecting db, {e}"},500

    @jwt_required()         
    def delete(self,name):
        store = StoreModel.find_by_store_name(name)
        if store:
            store.Delete()
            return {"message": f"store {name} Deleted successfully"}
        else:
            return {"message": f"store {name} not found"},404

class StoreList(Resource):
    def get(self):
        return {"Stores": [store.json() for store in StoreModel.get_all_stores()]}
