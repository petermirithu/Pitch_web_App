"""update username 

Revision ID: 0b026dea7cc6
Revises: 121063ccf6c3
Create Date: 2019-11-25 09:21:42.231994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b026dea7cc6'
down_revision = '121063ccf6c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usertable', sa.Column('pass_hash', sa.String(length=20), nullable=True))
    op.drop_column('usertable', 'pass_word')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usertable', sa.Column('pass_word', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('usertable', 'pass_hash')
    # ### end Alembic commands ###