from flask import Blueprint
from app.controllers.CategoryController import categorycontroller
from flask_login import login_required

category_router = Blueprint('category_router', __name__)

@login_required
@category_router.route('/categories',methods=['GET'])
def index():
    return categorycontroller.index()

@login_required
@category_router.route('/categories/create',methods=['GET'])
def create():
    return categorycontroller.create()

@login_required
@category_router.route('/categories/store',methods=['POST'])
def store():
    return categorycontroller.store()

@login_required
@category_router.route('/categories/<int:id>/delete',methods=['GET'])
def delete(id):
    return categorycontroller.delete(id)

@login_required
@category_router.route('/categories/<int:id>/edit',methods=['GET'])
def edit(id):
    return categorycontroller.edit(id)

@login_required
@category_router.route('/categories/<int:id>/update',methods=['POST'])
def update(id):
    return categorycontroller.update(id)