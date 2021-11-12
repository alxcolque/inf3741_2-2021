from flask import Blueprint
from app.controllers.AuthController import authcontroller
from flask_login import login_required

auth_router = Blueprint('auth_router', __name__)

@auth_router.route('/signup',methods=['GET'])
def signup():
    return authcontroller.signupGet()

@auth_router.route('/login',methods=['POST','GET'])
def login():
    return authcontroller.login()

@auth_router.route('/register',methods=['POST'])
def register():
    return authcontroller.register()

@auth_router.route('/logout', methods=["GET","POST"])
@login_required
def logout():
    return authcontroller.logout()
