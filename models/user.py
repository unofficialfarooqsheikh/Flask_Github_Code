from sql import SQL
from db import db
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    email = db.Column(db.String(100),primary_key=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100))
    designation = db.Column(db.Integer)

    def __init__(self,email,password,username,designation):
        print("--email,password,username,designation--",email,password,username,designation)
        self.email = email
        self.password = password
        self.username = username
        self.designation = designation

    def json(self):
        return {"id":self.id,"email":self.email,"password":self.password,"username":self.username,"designation":self.designation}    
    @classmethod
    def find_by_email(cls, username):
        # conn = SQL() 
        # with conn:
        #     csr = conn.cursor()
        #     csr.execute('SELECT * FROM dbo.users WHERE email = ?',username)
        #     data=csr.fetchone()
        #     if data:
        #         user = cls(*data)
        #     else:
        #         user = None    
        #     return user
        #__________________using SQLALCHEMY_____________ #
        return cls.query.filter_by(email=username).first()

    @classmethod
    def find_by_id(cls, id):
        # conn = SQL() 
        # with conn:
        #     csr = conn.cursor()
        #     csr.execute('SELECT * FROM dbo.users WHERE id = ?',id)
        #     data=csr.fetchone()
        #     if data:
        #         user = cls(*data)
        #     else:
        #         user = None    
        #     return user
            #__________________using SQLALCHEMY_____________ #
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    def save_user_to_db(self):
        print("self.designation",self.id)
        db.session.add(self)
        db.session.commit()

    def Delete(self):
        db.session.delete(self)
        db.session.commit()
