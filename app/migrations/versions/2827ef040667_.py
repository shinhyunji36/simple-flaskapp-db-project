"""empty message

Revision ID: 2827ef040667
Revises: 37688439c278
Create Date: 2021-12-14 23:21:28.332528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2827ef040667'
down_revision = '37688439c278'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('creator', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['gymposts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    op.drop_constraint('gymposts_user_id_fkey', 'gymposts', type_='foreignkey')
    op.drop_column('gymposts', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gymposts', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('gymposts_user_id_fkey', 'gymposts', 'users', ['user_id'], ['id'])
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.drop_table('comments')
    # ### end Alembic commands ###