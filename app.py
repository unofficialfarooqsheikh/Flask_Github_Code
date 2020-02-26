import os
from datetime import datetime, timedelta 
from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate, identity
from resources.item import Item, ItemList
from resources.user import UserManage
from resources.store import Store, StoreList


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(8) #can be used to check the secret Key
app.secret_key = app.config["SECRET_KEY"]
api = Api(app)
app.config['JWT_AUTH_URL_RULE'] = '/login'
# config JWT to expire within ? hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 1) #hours*minutes*seconds
# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://DESKTOP-IRHNO1M\SQLEXPRESS/Test DataBase?driver=SQL Server?Trusted_Connection=Yes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserManage, "/usermanage")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
