from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop import db, app, photos
from .models import Brand, Category, Addproduct
# from .forms import Addproducts
from .forms import Addproducts
import secrets
import os





@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        brand_name = request.form.get('brand')
        brand = Brand(name=brand_name)
        
        db.session.add(brand)
        flash(f'The brand {brand_name} has been added to the database', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add Brand', brands='brands')



@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        category_name = request.form.get('category')
        category = Category(name=category_name)
        
        db.session.add(category)
        flash(f'The brand {category_name} has been added to the database', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html')



@app.route('/addproducts', methods=['GET', 'POST'])
def addproducts():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount= form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        
        brand = request.form.get('brand')
        category = request.form.get('category')


        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        addpro = Addproduct(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc, brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpro)
        flash(f'The product {name} has been addedd to your database', 'success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addproducts.html', form=form,title='Add Products', brands=brands, categories=categories)




@app.route('/updateproduct/<int:id>', methods=["GET", "POST"])
def updateproduct(id):
    form = Addproducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Addproduct.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')

    if request.method == "POST":
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.brand_id = brand
        product.category_id = category
        product.stock = form.stock.data
        product.colors = form.colors.data
        product.desc = form.discription.data

        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")

            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
                
        
        db.session.commit()
        flash('Your product has been updated', 'success')

        return redirect(url_for('admin'))
        

    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.discription.data = product.desc
    
    return render_template('products/updateproduct.html', form=form, title='Update Product Page',categories=categories, brands=brands, product=product)



@app.route('/delete/<int:id>')
def delete(id):
    post = Addproduct.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin'))
