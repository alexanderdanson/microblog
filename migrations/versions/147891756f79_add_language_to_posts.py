"""add language to posts

Revision ID: 147891756f79
Revises: fed308bde8bf
Create Date: 2019-11-22 22:24:49.791766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '147891756f79'
down_revision = 'fed308bde8bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###