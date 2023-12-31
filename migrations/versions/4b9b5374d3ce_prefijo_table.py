"""prefijo table

Revision ID: 4b9b5374d3ce
Revises: 
Create Date: 2023-09-10 15:57:22.751764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b9b5374d3ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catprefijos',
    sa.Column('keyx', sa.Integer(), nullable=False),
    sa.Column('fechaalta', sa.DateTime(), nullable=True),
    sa.Column('prefijo', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('keyx')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('catprefijos')
    # ### end Alembic commands ###
