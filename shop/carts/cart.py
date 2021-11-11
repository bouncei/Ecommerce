import re
from flask import request, render_template, redirect, session, current_app, flash
from shop import db, app
from shop.products.models import Addproduct


def MagerDict(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))

    return False

@app.route('/addcart', methods=["POST"])
def add_cart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')

        print(quantity,colors)

        product = Addproduct.query.filter_by(id=product_id).first()
        string_product_price = str(product.price)
        
        if quantity and colors and product_id and request.method == "POST":
            dicItems = {product_id: {'name': product.name, 'price': string_product_price,
            'discount': product.discount, 'colors': colors, 'quantity': quantity, 'image': product.image_1}}

            # print(dicItems)

            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])

                if product_id in session['Shoppingcart']:
                    # print('This product is already in cart')
                    flash('This product is already in cart', 'error')
                else:
                    session['Shoppingcart'] = MagerDict(session['Shoppingcart'], dicItems)
                    flash(f"{product.name} has succesfully been added to cart", 'success')
                    return redirect(request.referrer)

            else:
                print("nothing Here Boss")
                session['Shoppingcart'] = dicItems
                return redirect(request.referrer)



            # if 'Shoppingcaart' not in session:
                
            #     session['Shoppingcart'] = dicItems
            #     return redirect(request.referrer)


            # else:
            #     print(session['Shoppingcart'])

            #     if product_id in session['Shoppingcart']:
            #         print("This product is already in cart")
            #         # flash("", "success")

            #     else:
            #         session['Shoppingcart'] = MagerDict(session['Shoppingcart'], dicItems)
            #         flash(f"{product.name} has succesfully been added to cart", 'success')
            #         return redirect(request.referrer)


    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)