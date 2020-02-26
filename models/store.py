from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self,name):
        self.name = name

    def json(self):
        return {"name":self.name, 'items':[item.json() for item in self.items.all()]} 
    
    @classmethod
    def find_by_store_name(cls, name):
                # using SQL Queries
                # connection = SQL()
                # with connection:
                #     cursor = connection.cursor()
                #     query = "SELECT * FROM {table} WHERE name=?".format(table='items')
                #     result = cursor.execute(query, (name,))
                #     row = result.fetchone()
                # if row:
                    # return cls(*row)
        #__________________using SQLALCHEMY_____________ #
        return StoreModel.query.filter_by(name = name).first()

    @classmethod
    def find_by_store_id(cls, id):
                # using SQL Queries
                # connection = SQL()
                # with connection:
                #     cursor = connection.cursor()
                #     query = "SELECT * FROM {table} WHERE id=?".format(table='items')
                #     result = cursor.execute(query, (id,))
                #     row = result.fetchone()
                # if row:
                #     return cls(*row)
        
        #__________________using SQLALCHEMY_____________ #
        return StoreModel.query.filter_by(id = id).first()

    @classmethod
    def get_all_stores(cls):
        print(1)
        return cls.query.all()

    def add_store_to_db(self):
        # connection = SQL()
        # with connection:
        #     print(connection.conn)
        #     cursor = connection.cursor()
        #     query = "INSERT INTO {table} VALUES(?, ?)".format(table='items')
        #     cursor.execute(query, (self.name, self.price))
        #     cursor.commit()

        #__________________using SQLALCHEMY_____________ #
        db.session.add(self) #Update and Insert: both 
        db.session.commit()

    def Delete(self):
        db.session.delete(self) #Deletes the object from db 
        db.session.commit()