from ecom.datastore import db
from ecom.models import Base
from ecom.models.custom_datatypes import UUID


class ProductSubcategory(Base):
    __tablename__ = 'product_subcategories'
    product_category_id = db.Column(
        UUID, db.ForeignKey('product_categories.id'), nullable=False)
    product_category = db.relationship(
        'ProductCategory', backref=db.backref('product_subcategories'))

    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)

    serializable = ['id', 'product_category_id', 'name', 'description']

    def serialize(self):
        rv = super(Subscription, self).serialize()
        return rv
