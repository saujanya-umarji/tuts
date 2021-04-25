from .userdataApi import UserApi, UsersApi
from .login import LoginApi , ForgotPassword , ResetPassword

def initialize_routes(api):
 api.add_resource(UserApi, '/api/v1/user')
 api.add_resource(UsersApi, '/api/v1/users/<id>')
 api.add_resource(LoginApi, '/api/v1/login')
 api.add_resource(ForgotPassword, '/api/v1/forgotpassword')
 api.add_resource(ResetPassword, '/api/v1/resetpassword')