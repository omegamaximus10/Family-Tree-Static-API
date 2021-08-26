"""empty message

Revision ID: 11fe8cda7cdf
Revises: 4362d8f5d843
Create Date: 2021-08-26 17:55:48.553673

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11fe8cda7cdf'
down_revision = '4362d8f5d843'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('relationship', sa.String(length=250), nullable=False))
    op.drop_column('person', 'parentezco')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('parentezco', mysql.VARCHAR(length=250), nullable=False))
    op.drop_column('person', 'relationship')
    # ### end Alembic commands ###
