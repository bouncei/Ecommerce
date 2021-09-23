from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/hp/Documents/Python/Projects/e-commerce/myshop.db'
app.config['SECRET_KEY']= 'jdfbvgsib3e834ejdckhbd'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  


from shop.admin import routes
from shop.products import routes