from flask import current_app, render_template, make_response

from ecom.datastore import db,redis_store
from ecom.exceptions import ServiceUnavailableException
from ecom.models import Product, ProductSubcategory


class ProductManager():
    @staticmethod
    def load_all(subcategory_id):
        print ("product manager")
        query = Product.query.filter(Product.product_subcategory_id == subcategory_id)
        products =  query.all()
        print ("products")
        print (products)
        display_products = []
        for product in products:
            display_products.append({'id': product.id, 'name':product.name,'description':product.description,'price':product.price,
                'available_item_count':product.available_item_count,'image':product.image})
        print ("display_products")
        print (display_products)

        category_map = eval(redis_store.get('category_map'))
        resp = make_response(render_template('subcategory.html', products=display_products, category_map=category_map ))
        resp.headers['Content-type'] = 'text/html; charset=utf-8'
        return resp
