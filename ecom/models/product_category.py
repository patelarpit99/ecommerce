from ecom.datastore import db
from ecom.models import Base
from ecom.models.custom_datatypes import UUID


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)

    serializable = ['id', 'name', 'description']

    def serialize(self):
        rv = super(Subscription, self).serialize()
        return rv
