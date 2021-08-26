"""empty message

Revision ID: 4362d8f5d843
Revises: 
Create Date: 2021-08-26 17:53:10.215889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4362d8f5d843'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('last_name', sa.String(length=250), nullable=False),
    sa.Column('parentezco', sa.String(length=250), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('father_id', sa.Integer(), nullable=True),
    sa.Column('mother_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['father_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['mother_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###
