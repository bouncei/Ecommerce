from os import name
from flask import redirect, render_template, url_for, flash, request, session
from shop import db, app
from .models import Brand, Category





@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == 'POST':
        brand_name = request.form.get('brand')
        brand = Brand(name=brand_name)
        
        db.session.add(brand)
        flash(f'The brand {brand_name} has been added to the database', 'success')
        # db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add Brand', brands='brands')



@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == 'POST':
        category_name = request.form.get('category')
        category = Category(name=category_name)
        
        db.session.add(category)
        flash(f'The brand {category_name} has been added to the database', 'success')
        # db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html')