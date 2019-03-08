"""empty message

Revision ID: 19f508ac5aa9
Revises: 39dcab9aac40
Create Date: 2019-03-06 17:14:39.455344

"""
from alembic import op
import sqlalchemy as sa
from ecom.models import custom_datatypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '19f508ac5aa9'
down_revision = '39dcab9aac40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('carts', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('items', 'price',
               existing_type=mysql.FLOAT(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
    op.alter_column('products', 'image',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=40),
               existing_nullable=False)
    op.alter_column('products', 'price',
               existing_type=mysql.FLOAT(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.Float(precision=2),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('products', 'image',
               existing_type=sa.String(length=40),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)
    op.alter_column('items', 'price',
               existing_type=sa.Float(precision=2),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('carts', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###