from config import app

from flask import Flask
from admin.routes import admin_bp as admin_blueprint
from shop.routes import shop_bp


app.register_blueprint(admin_blueprint)
app.register_blueprint(shop_bp)

if __name__ == '__main__':
    app.run(debug=True)