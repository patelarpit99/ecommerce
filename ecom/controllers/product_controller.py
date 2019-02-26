from ecom.controllers import BaseController
from ecom.managers import ProductManager
from flask import request


class ProductController(BaseController):
    def get(self):
    	subcategory_id = request.args.get("subcategory")
    	print ("product controller")
    	print (subcategory_id)
    	resp = ProductManager.load_all(subcategory_id)
    	return resp