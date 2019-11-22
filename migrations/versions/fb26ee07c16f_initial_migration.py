"""Initial Migration

Revision ID: fb26ee07c16f
Revises: 
Create Date: 2019-11-22 23:19:54.150668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb26ee07c16f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commenttable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('pitch_title', sa.String(length=100), nullable=True),
    sa.Column('p_comment', sa.String(length=200), nullable=True),
    sa.Column('post_com', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitchtable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.Column('p_title', sa.String(length=100), nullable=True),
    sa.Column('pitch_it', sa.String(length=255), nullable=True),
    sa.Column('post', sa.DateTime(), nullable=True),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('downvote', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usertable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('pass_word', sa.String(length=20), nullable=True),
    sa.Column('bio', sa.String(length=100), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.Column('post_user', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['commenttable.id'], ),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitchtable.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usertable_email'), 'usertable', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usertable_email'), table_name='usertable')
    op.drop_table('usertable')
    op.drop_table('roles')
    op.drop_table('pitchtable')
    op.drop_table('commenttable')
    # ### end Alembic commands ###
