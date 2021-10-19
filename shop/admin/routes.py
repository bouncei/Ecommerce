
from .forms import RegistrationForm, LoginForm
from flask import render_template, session, request, url_for, flash, redirect
from shop import app, db, bcrypt
from .models import User
from shop.products.models import Addproduct, Brand, Category
import os

# @app.route('/')
# def home():
#     return render_template('admin/index.html', title='Home Page')


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    
    products = Addproduct.query.all()
    brands = Brand.query.all()
    # print(products)
    return render_template('admin/index.html', title='Admin Page', products=products, brands=brands)



@app.route('/brands')
def brands():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))

    brands = Brand.query.order_by(Brand.id.desc()).all()
    
    return render_template('admin/brand_category.html',title="Brand Page", brands=brands)


@app.route('/updatebrand/<int:id>', methods= ["GET", "POST"])
def updatebrand(id):
    if "email" not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    

    update_brand = Brand.query.get_or_404(id)
    name = update_brand.name
    brand = request.form.get('brand')

    if request.method == "POST":
        update_brand.name = brand
        
        flash(f'The brand name {name} has been updated to {update_brand.name}', 'success')
        db.session.commit()
        
        return redirect(url_for('brands'))

    return render_template('admin/updatebrand.html', title="Update Brand Page", update_brand=update_brand)


@app.route('/brands/delete/<int:id>', methods=["GET", "POST"])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    name = brand.name
    db.session.delete(brand)
    db.session.commit()

    flash(f'The brand {name} has been deleted from the database', 'success')

    return redirect(url_for('brands'))





@app.route('/categories')
def categories():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))

    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand_category.html',title="Category Page", categories=categories)


@app.route('/updatecategory/<int:id>', methods= ["GET", "POST"])
def updatecategory(id):
    update_category = Category.query.get_or_404(id)
    name = update_category.name

    category = request.form.get('category')

    if request.method == "POST":
        update_category.name = category
        
        flash(f'The category name {name} has been updated to {update_category.name}', 'success')
        db.session.commit()
        
        return redirect(url_for('categories'))

    return render_template('admin/updatebrand.html', title="Update Brand Page", update_category=update_category)


@app.route('/categories/delete/<int:id>', methods=["GET", "POST"])
def deletecat(id):
    category = Category.query.get_or_404(id)
    name = category.name
    db.session.delete(category)
    db.session.commit()

    flash(f'The category {name} has been deleted from the database', 'success')

    return redirect(url_for('categories'))







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