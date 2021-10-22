from flask import request, render_template, redirect, session, current_app, flash
from shop import db, app
from shop.products.models import Addproduct


def MagerDict(dict1, dict2):
    if isinstance(dict, list) and isinstance(dict2, list):
        return dict1 + dict2
    
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict.items() + list(dict2.items())))
    return False

@app.route('/addcart', methods=['POST'])
def add_cart():
    try:
        product_id = request.get('product_id')
        product_quantity = request.get('quantity')
        product_color = request.get('color')

        product = Addproduct.query.filter_by(id=product_id).first()
        if product_id and product_quantity and product_color and request.method == "POST":
            dicItems = {product_id: {'name': product.name, 'price': product.price,
            'discount': product.discount, 'color': product_color, 'quantity': product_quantity, 'image': product.image_1}}

            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])

                if product_id in session['Shoppingcart']:
                    print('This product is aldredy in cart')
                    flash('This product is aldredy in cart', 'error')
                else:
                    session['Shoppingcart'] = MagerDict(session['Shoppingcart'], dicItems)
                    flash(f"{product.name} has succesfully been added to cart", 'success')
                    return redirect(request.referrer)

            else:
                session['Shoppingcart'] = dicItems
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)