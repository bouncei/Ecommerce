from flask import Blueprint
shop_bp = Blueprint('shop_bp', __name__)

@shop_bp.route('/')
def home():
    return "Home"


@shop_bp.route('/yes')
def yes():
    return "Yes baby"


