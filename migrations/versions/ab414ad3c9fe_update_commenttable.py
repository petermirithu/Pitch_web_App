"""update commenttable 

Revision ID: ab414ad3c9fe
Revises: e42bb70ee140
Create Date: 2019-11-24 00:19:19.607991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab414ad3c9fe'
down_revision = 'e42bb70ee140'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('commenttable', sa.Column('comment_by', sa.String(length=20), nullable=True))
    op.drop_column('commenttable', 'pitch_title')
    op.add_column('pitchtable', sa.Column('posted_by', sa.String(length=20), nullable=True))
    op.drop_column('pitchtable', 'poster_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchtable', sa.Column('poster_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('pitchtable', 'posted_by')
    op.add_column('commenttable', sa.Column('pitch_title', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('commenttable', 'comment_by')
    # ### end Alembic commands ###