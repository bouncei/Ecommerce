# from itertools import product
from itertools import product
from .forms import RegistrationForm, LoginForm
from flask import render_template, session, request, url_for, flash, redirect
from shop import app, db, bcrypt
from .models import User
from shop.products.models import Addproduct

# @app.route('/')
# def home():
#     return render_template('admin/index.html', title='Home Page')


@app.route('/')
def admin():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    
    products = Addproduct.query.all()
    # print(products)
    return render_template('admin/index.html', title='Admin Page', products=products)

@app.route('/brands')
def brands():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))

    products = Addproduct.query.all()
    return render_template('admin/brand.html',title="Brand Page", products=products)

@app.route('/categories')
def categories():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))

    products = Addproduct.query.all()
    return render_template('admin/category.html',title="Category Page", products=products)


@app.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)   ## generate hash pasword from the registration form dataq
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data}, Thanks for registering', 'success')
        return redirect(url_for('admin'))
    return render_template('admin/register.html', form=form, title="Registration page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data}, your\'e logged in.', 'success')
            
            return redirect(request.args.get('next') or url_for('admin'))
        
        else:
            flash( 'Wrong password please try again', 'danger')

    return render_template('admin/login.html', form=form, title='Login Page')