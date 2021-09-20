# from shop import create_app
from flask import Flask

from shop.routes import shop_bp

app = Flask(__name__)

app.register_blueprint(shop_bp)

if __name__ == '__main__':
    app.run(debug=True)