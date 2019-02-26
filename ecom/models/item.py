from ecom.datastore import db
from ecom.models import Base
from ecom.models.custom_datatypes import UUID


class Item(Base):
    __tablename__ = 'items'
    product_id = db.Column(
        UUID, db.ForeignKey('products.id'), nullable=False)
    product = db.relationship(
        'Product', backref=db.backref('items'))

    cart_id = db.Column(
        UUID, db.ForeignKey('carts.id'), nullable=False)
    cart = db.relationship(
        'Cart', backref=db.backref('items'))

    quantity = db.Column(db.Integer)
    price  = db.Column(db.Float(precision=2), nullable=False)




    serializable = [
        'id', 'product_id', 'cart_id', 'quantity',
        'price', 'created_at', 'modified_at'
    ]

    def serialize(self):
        rv = super(Member, self).serialize()
        return rv
