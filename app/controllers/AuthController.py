from app import db, bcrypt, app
from flask_login import LoginManager, login_user, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash, session
from app.models.User import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_router.login"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class AuthController():
    def __init__(self):
        pass

    
    def signupGet(self):
        return render_template('auth/signup.html')
    def login(self):
        if request.method == 'POST':
            user = User.query.filter_by(email=request.form['email']).first()
            if user:
                if bcrypt.check_password_hash(user.password, request.form['password']):
                    login_user(user)
                    return redirect(url_for("main_router.main"))
        
            flash("Usuario no existe, o los credenciales no son válidos.")
            return redirect(url_for('auth_router.login'))
        return render_template('auth/login.html')
    def register(self):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            username = request.form['username']
            password = bcrypt.generate_password_hash(request.form['password'])
            
            user = User(name=name, email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return redirect(url_for("main_router.main"))
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.login'))

    

authcontroller = AuthController()
