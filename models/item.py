from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #stores.id is the table name
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.id = None
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name":self.name, "price":self.price, "store_id": self.store_id}
    
    @classmethod
    def find_by_item_name(cls, name):
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
        return ItemModel.query.filter_by(name = name).first()

    @classmethod
    def find_by_item_id(cls, id):
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
        return ItemModel.query.filter_by(id = id).first()

    @classmethod
    def get_all_items(cls):
        return cls.query.all()

    def save_to_db(self):
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