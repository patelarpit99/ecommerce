from flask import current_app, render_template, make_response, session

from ecom.datastore import db,redis_store
from ecom.exceptions import ServiceUnavailableException
from ecom.models import Account
from ecom.utils import general_util

from flask import redirect, url_for
class AccountManager():
    @staticmethod
    def signup(data):
        print ("signup manager")

        account = Account()
        account.name = data.get("name")
        print (account.name)
        account.mobile = data.get("mobile")
        print (account.mobile )
        account.email = data.get("email")
        print (account.email)
        account.age = data.get("age")
        print (account.age )
        account.gender = data.get("gender")
        print (account.gender )
        account.username = data.get("username")
        print (account.username)
        account.password = data.get("psw")
        print (account.password )
        account.shipping_address = data.get("shipping_address")
        print(account.shipping_address )

        try:
            db.session.add(account)
            db.session.commit()
            print ("after commit")
        except Exception as e:
            db.session.rollback()
            print ("error")
            print (e)

            raise e
        session['name'] = account.name
        session['email'] =  account.email
        print ("reached after this")

        return redirect('/main')




    @staticmethod
    def login_form():
        print ("signup form")
        category_map =  general_util.get_category_map()
        resp = make_response(render_template('login.html',category_map=category_map))
        resp.headers['Content-type'] = 'text/html; charset=utf-8'
        return resp

    @staticmethod
    def signup_form():
        print ("signup form")
        category_map =  general_util.get_category_map()
        resp = make_response(render_template('signup.html',category_map=category_map))
        resp.headers['Content-type'] = 'text/html; charset=utf-8'
        return resp

    @staticmethod
    def login(data):
        email = data.get("email")
        password = data.get("psw")
        category_map =  general_util.get_category_map()
        print ("login manager")
        query = Account.query.filter(Account.email == email)
        account =  query.first()
        success =  1
        if not account:
            error_message = email + " is not registered with us. Please retry or signup"
            print (error_message)
            success =  0
        else:
            if account.password != password:
                error_message = "Invalid password for given email. Please retry"
                print (error_message)
                success =  0
        if success:
            print ("succcess")
            session['name'] = account.name
            session['email'] =  account.email
            resp = make_response(render_template('index.html', category_map=category_map, name= session['name']))
        else:
            resp = make_response(render_template('signup.html',category_map=category_map, error_message=error_message))

        resp.headers['Content-type'] = 'text/html; charset=utf-8'
        return resp


