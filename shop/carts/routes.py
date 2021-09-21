from flask import Blueprint
carts_bp = Blueprint('carts_bp', __name__)

@carts_bp.route('/cart')
def cart():
    return "Cart"




