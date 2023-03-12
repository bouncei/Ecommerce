from flask import Flask
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']= 'jdfbvgsib3e834ejdckhbd'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  


from shop.admin import routes
from shop.products import routes
from shop.carts import cart