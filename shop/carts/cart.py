import re
from flask import request, render_template, redirect, session, current_app
from shop import db, app

@app.route('/addcart', methods=['POST'])
def add_cat():
    pass