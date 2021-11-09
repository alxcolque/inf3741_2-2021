from flask_login import LoginManager, login_user, logout_user, current_user
from flask import render_template, url_for, request, redirect, flash, session
from app.models.User import User
from app import db, bcrypt
class AuthController():
    def __init__(self):
        pass

    def loginGet(self):
        return render_template('auth/login.html')
    def signupGet(self):
        return render_template('auth/signup.html')
    def signup(self):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            username = request.form['username']
            password = bcrypt.generate_password_hash(request.form['password'])
            
            user = User(name=name, email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return redirect(url_for('category_router.index'))
    def login(self):
        if request.method == 'POST':
            user = User.query.filter_by(email=request.form['email']).first()
            if user:
                if bcrypt.check_password_hash(user.password, request.form['password']):
                    login_user(user)
                    return redirect(url_for("practica_router.principal"))
        
            flash("Usuario no existe, o los credenciales no son válidos.")
            return redirect(url_for('category_router.index'))
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.login'))
            
authcontroller = AuthController()
