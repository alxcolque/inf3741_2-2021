from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        user = {'name': 'Carlos'}
        return render_template('index.html', usuario=user)
        """ from app.models.User import User
        users = User.query.all()
        return render_template('materias/index.html', users=users) """

maincontroller = MainController()
