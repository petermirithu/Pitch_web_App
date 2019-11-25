"""update user table

Revision ID: 0a909e2b59a1
Revises: 0b026dea7cc6
Create Date: 2019-11-25 10:15:20.875486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a909e2b59a1'
down_revision = '0b026dea7cc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usertable', sa.Column('site', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usertable', 'site')
    # ### end Alembic commands ###