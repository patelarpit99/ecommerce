from flask import current_app, render_template, make_response, session

from ecom.datastore import db,redis_store
from ecom.exceptions import ServiceUnavailableException
from ecom.models import ProductCategory, ProductSubcategory
from ecom.utils import general_util


class DisplayManager():
    @staticmethod
    def display():
        print ("display manager")
        category_map =  general_util.get_category_map()
        if  'name' in session:
            print ("dddchurraaa")
            print (session['name'])
            resp = make_response(render_template('index.html', category_map=category_map, name= session['name']))
        else:
            resp = make_response(render_template('index.html', category_map=category_map))
        resp.headers['Content-type'] = 'text/html; charset=utf-8'
        return resp
