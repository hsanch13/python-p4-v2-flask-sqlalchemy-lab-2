"""add review

Revision ID: e7b15e0b202e
Revises: d8d2394dd977
Create Date: 2024-11-19 17:21:01.132639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7b15e0b202e'
down_revision = 'd8d2394dd977'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reviews', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reviews', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
