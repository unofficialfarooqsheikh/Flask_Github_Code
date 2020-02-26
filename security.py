from werkzeug.security import safe_str_cmp
from models.user import UserModel  


def authenticate(email,password): # generates jwt toke
    user = UserModel.find_by_email(email)
    # user = user_email_mapping.get(id)
    if user and safe_str_cmp(user.password, password):
        print(user)
        return user
 
def identity(payload):  #retireves id form jwt token
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)