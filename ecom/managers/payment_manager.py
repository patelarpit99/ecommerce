from flask import current_app, render_template, make_response, session

from ecom.datastore import db,redis_store
from ecom.exceptions import ServiceUnavailableException
from ecom.models import Item, Cart, Account
import json
import razorpay
from ecom.utils import general_util

class PaymentManager():
    @staticmethod
    def pay():
        category_map =  general_util.get_category_map()
        print ("payment manager pay")
        if 'email' in session:
            query = Account.query.filter(Account.email == session['email'])
            account =  query.first()
            query = Cart.query.filter_by(account_id=account.id, active=True)
            cart =  query.first()
            print (cart.items)
            value = 0
            for item in cart.items:
                value += item.price
            amount =  int(value*100)
            print ("checcccc")
            print (amount)
            resp = make_response(render_template('payment.html',name=account.name,email=account.email,contact=account.mobile,amount=amount, category_map=category_map))
            resp.headers['Content-type'] = 'text/html; charset=utf-8'
            return resp
        else:

            status_message = "SignUp or Login to continue shopping"
            resp = make_response(render_template('signup.html',category_map=category_map, status_message=status_message))
            resp.headers['Content-type'] = 'text/html; charset=utf-8'
            return resp



    @staticmethod
    def charge(data):
        category_map =  general_util.get_category_map()
        print ("payment manager charge")
        print (data)
        client = razorpay.Client(auth=(current_app.config.get('RAZORPAY_KEY'), current_app.config.get('RAZORPAY_SECRET')))
        client.set_app_details({"title" : "mmmkart", "version" : "1.0"})
        #data = {"amount": 1000, "currency": "INR", "receipt": "654", "payment_capture": 1}
        #client.order.create(data=data)
        query = Account.query.filter(Account.email == session['email'])
        account =  query.first()
        query = Cart.query.filter_by(account_id=account.id, active=True)
        cart =  query.first()
        print (cart.items)
        value = 0
        for item in cart.items:
            value += item.price
        amount =  int(value*100)
        payment_id = data['razorpay_payment_id']
        resp  = client.payment.capture(payment_id, amount)
        print (resp)
        print (resp['status'])
        if resp["status"] == "captured":
            print ("sycccecece")
            cart.active = False
            try:
                print ("inserrr")
                db.session.add(cart)
                db.session.commit()
            except Exception as e:
                print (e)
                db.session.rollback()

            message = "Congratulations !!! Your payment is successful"
            resp = make_response(render_template('paymentresponse.html',message=message,success=1,category_map=category_map,name=session.get('name')))
            resp.headers['Content-type'] = 'text/html; charset=utf-8'
            return resp
        else:
            print ("fsasasas")
            message = "Oops !!! Your payment got declined. Please retry payment"
            resp = make_response(render_template('paymentresponse.html',message=message,category_map=category_map,name=session.get('name')))
            resp.headers['Content-type'] = 'text/html; charset=utf-8'
            return resp

