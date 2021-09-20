from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    render_template('index.html')