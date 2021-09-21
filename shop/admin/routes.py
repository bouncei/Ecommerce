from flask import Blueprint, render_template
shop_bp = Blueprint('shop_bp', __name__)

@shop_bp.route('/')
def home():
    return render_template('index.html')


@shop_bp.route('/register')
def register():
    return render_template('admin/register.html', title="Register user")


