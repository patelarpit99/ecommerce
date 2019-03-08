from flask import current_app, render_template, make_response, session, redirect, request

from ecom.datastore import db,redis_store
from ecom.exceptions import ServiceUnavailableException
from ecom.models import Item, Cart, Account, Product
from ecom.utils import general_util

class CartManager():
    @staticmethod
    def add_to_cart(product_id):
        category_map =  general_util.get_category_map()
        print ("cart manager add")
        print (product_id)
        query = Product.query.filter(Product.id == product_id)
        product =  query.first()
        print (product.price)

        if 'email' in session:
            #logged in user case
            query = Account.query.filter(Account.email == session['email'])
            account =  query.first()
            print (account.id)

            ####
            cart = Cart.query.filter_by(account_id=account.id, active=True).first()
            if not cart:
                cart = Cart()
            cart.account_id = account.id
            item = Item()
            item.cart = cart
            item.product_id = product_id
            item.quantity = 1
            item.price = product.price
            try:
                print ("inserrr")
                db.session.add(cart)
                db.session.add(item)
                db.session.commit()
            except Exception as e:
                print (e)
                db.session.rollback()
        else:
            if 'cart' in session:
                cart = session['cart']
                item = {"product":{"name": product.name, "description": product.description,"price":product.price,
                       "image":product.image, "id":product.id}, "quantity": 1,"price":product.price}
                cart.append(item)
                session['cart'] =  cart

            else:
                cart = []
                item = {"product":{"name": product.name, "description": product.description,"price":product.price,
                       "image":product.image, "id": product.id}, "quantity": 1,"price":product.price}
                cart.append(item)
                session['cart'] =  cart


        return redirect('/get_cart_items')



        ######

    @staticmethod
    def get_cart_items():
        category_map =  general_util.get_category_map()
        if 'email' in session:
            print (session['email'])
            query = Account.query.filter(Account.email == session['email'])
            account =  query.first()

            query = Cart.query.filter_by(account_id=account.id, active=True)
            cart =  query.first()
            if cart:
                value = 0
                for item in cart.items:
                    value += item.price

                resp = make_response(render_template('cart.html', items=cart.items, total=value,category_map=category_map, name=session.get('name')))
                resp.headers['Content-type'] = 'text/html; charset=utf-8'
                return resp
            else:
                resp = make_response(render_template('cart.html', items=[], total=0,category_map=category_map, name=session.get('name')))
                resp.headers['Content-type'] = 'text/html; charset=utf-8'
                return resp
        else:
            if 'cart' in session:
                cart =  session['cart']
                value = 0
                for item in cart:
                    value += item['price']
            else:
                cart = []
                value = 0
            resp = make_response(render_template('cart.html', items=cart, total=value,category_map=category_map, name=session.get('name')))
            resp.headers['Content-type'] = 'text/html; charset=utf-8'
            return resp


    @staticmethod
    def remove_from_cart(item_id):
        print ("remove from cart")
        print (item_id)
        query = Account.query.filter(Account.email == session['email'])
        account =  query.first()
        query = Cart.query.filter_by(account_id=account.id, active=True)
        cart =  query.first()
        for item in cart.items:
            if item.id == item_id:
                db.session.delete(item)
                db.session.commit()
        return {"status":"success"}

