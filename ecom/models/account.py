from ecom.constants import Gender
from ecom.datastore import db
from ecom.models import Base
from ecom.models.custom_datatypes import UUID


class Account(Base):
    __tablename__ = 'accounts'

    name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(20), index=True)
    email = db.Column(db.String(50), index=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(Gender))
    username = db.Column(db.String(50), index=True)
    password =  db.Column(db.String(50))
    shipping_address = db.Column(db.String(200))


    serializable = [
        'id', 'name',
        'mobile', 'email', 'age', 'gender', 'username', 'shipping_address', 'created_at', 'modified_at'
    ]

    def serialize(self):
        rv = super(Member, self).serialize()
        return rv
