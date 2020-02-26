from sql import SQL,SqlDatatoJson
from models.user import UserModel
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class UserManage(Resource): 

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email",required =True, help =" Error in the data received make sure 'key = email and value = string'" )
        parser.add_argument("username",required =True, help =" Error in the data received make sure 'key = username and value = string'" )
        parser.add_argument("password",required =True, help =" Error in the data received make sure 'key = password and value = string'" )
        parser.add_argument("designation",required =True, help ="Error in the data received make sure 'key = designation and value = int'" )
        data = parser.parse_args()
        print("POST data",data)
        if (UserModel.find_by_email(data["email"])):
            return {"message":"user already exists"}, 400
        else:
           user= UserModel(**data)
        # conn = SQL() 
        # with conn:
        #     csr = conn.cursor()
        #     try:
        #         csr.execute("INSERT INTO dbo.users VALUES (?, ?, ?, ?)",(data["email"],data["password"],data["username"],int(data["designation"])))
        #         csr.commit()
        #         return {"message": "user Successfully entered"}
        #     except:
        #         return {"message":"error in connection to db"}
        #     finally:
        #         print("Done")
            #__________________using SQLALCHEMY_____________ #
        try:
            user.save_user_to_db()
            return {"message": "user Successfully entered"}
        except Exception as e:
            return {"message":f"Unable to connect to DB &,{e}"}, 404

    @jwt_required()
    def get(self):
        # conn = SQL()
        # with conn:
        #     csr = conn.cursor()
        #     tablename='users'
        #     csr.execute(f"SELECT * FROM dbo.{tablename}")
        #     data = csr.fetchall()
        #     query = ("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{}'").format(tablename)
        #     csr.execute(query)
        #     columnData = csr.fetchall()
        #     # Feed the data to the funtion
        #     output=SqlDatatoJson(data,columnData)
        # return {"data":output}
            #__________________using SQLALCHEMY_____________ #
        try:
            users = UserModel.get_all_users() 
        except Excpetion as e:
            return{"message":e}
        return {"users":list(map(lambda x : x.json(), users))}

    @jwt_required()
    def delete(self):
        parser= reqparse.RequestParser()
        parser.add_argument("email",required=True,help="Error in the data received make sure 'key = email'")
        data = parser.parse_args()
        user= UserModel.find_by_email(data["email"])
        if(user):
            # print("if")
            # conn = SQL()
            # tablename= 'users'
            # with conn:
            #     csr = conn.cursor()
            #     try:
            #         query = ("DELETE FROM {} WHERE email= ?").format(tablename)
            #         csr.execute(query,name)
            #         csr.commit()
            #         return ({"message":"successfully deleted"} ,200)
            #     except:
            #         return {"message":"Unable to connect to DB"}, 404

                        #__________________using SQLALCHEMY_____________ #
            try:
                user.Delete()
                return ({"message":"successfully deleted"} ,200)
            except:
                return {"message":"Unable to connect to DB"}, 404
        else:
            return ({"message":"user not found"},400)
    
    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email",required =True, help =" Error in the data received make sure 'key = email and value = string'" )
        parser.add_argument("username",required =True, help =" Error in the data received make sure 'key = username and value = string'" )
        parser.add_argument("password",required =True, help =" Error in the data received make sure 'key = password and value = string'" )
        parser.add_argument("designation",required =True, type=int, help ="Error in the data received make sure 'key = designation and value = int'" )
        data = parser.parse_args()
        if(data):
            # print("if")
            # conn = SQL()
            # tablename= 'users'
            # with conn:
            #     csr = conn.cursor()
            #     try:
            #         query = ("UPDATE {} SET password = ?, username = ?, designation = ? WHERE id =?").format(tablename)
            #         csr.execute(query,data['password'],data['username'],int(data['designation']),int(olddata.id))
            #         csr.commit()
            #         return ({"message":"successfully Updated"} ,200)
            #     except Exception as e:
            #         return {"message":"Unable to connect to DB"}, 404
                        #__________________using SQLALCHEMY_____________ #
            try:
                user = UserModel.find_by_email(data["email"])
                if user is None:
                    user = UserModel(**data)
                else:
                    user.username = data["username"]
                    user.password = data["password"]
                    user.designation = data["designation"]
                user.save_user_to_db()
                return ({"message":"successfully Updated"} ,200)
            except Exception as e:
                return {"message":f"Unable to connect to DB &,{e}"}, 404
        else:
            print("else")
            return ({"message":"user not found"},400)
