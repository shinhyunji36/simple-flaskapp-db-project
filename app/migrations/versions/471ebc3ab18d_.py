"""empty message

Revision ID: 471ebc3ab18d
Revises: e3b8349a5248
Create Date: 2021-12-14 22:09:38.877132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '471ebc3ab18d'
down_revision = 'e3b8349a5248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gymposts', sa.Column('name', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gymposts', 'name')
    # ### end Alembic commands ###