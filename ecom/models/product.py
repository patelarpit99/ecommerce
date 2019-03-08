from ecom.datastore import db
from ecom.models import Base
from ecom.models.custom_datatypes import UUID


class Product(Base):
    __tablename__ = 'products'
    product_subcategory_id = db.Column(
        UUID, db.ForeignKey('product_subcategories.id'), nullable=False)
    product_subcategory = db.relationship(
        'ProductSubcategory', backref=db.backref('products'))

    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    price  = db.Column(db.Float(precision=2), nullable=False)
    available_item_count = db.Column(db.Integer)
    image = db.Column(db.String(40), nullable=False)



    serializable = [
        'id', 'product_subcategory_id', 'name',
        'description', 'price', 'available_item_count', 'created_at', 'modified_at'
    ]

    def serialize(self):
        rv = super(Member, self).serialize()
        return rv
