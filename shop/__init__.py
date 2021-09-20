from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from .routes import shop_bp

db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)

#     app.config['SECRET_KEY'] = 'joshua inyang'

#     db.init_app(app)


#     app.register_blueprint(shop_bp)




#     return app 