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
        subcategory_product_map = general_util.subcat_product_map()

        resp = make_response(render_template('index.html', category_map=category_map, name= session.get('name'),subcategory_product_map=subcategory_product_map))
        resp.headers['Content-type'] = 'text/html; charset=utf-8'
        return resp
