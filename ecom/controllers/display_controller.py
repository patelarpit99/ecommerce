from ecom.controllers import BaseController
from ecom.managers import DisplayManager


class DisplayController(BaseController):
    def get(self):
    	print ("display controller")
    	resp = DisplayManager.display()
    	return resp
