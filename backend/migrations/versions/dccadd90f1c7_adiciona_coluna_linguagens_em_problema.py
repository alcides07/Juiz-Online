"""adiciona coluna linguagens em problema

Revision ID: dccadd90f1c7
Revises: 1a1487cd8300
Create Date: 2024-04-11 21:34:48.137203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dccadd90f1c7'
down_revision = '1a1487cd8300'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('problemas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linguagens', sa.ARRAY(sa.String())))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('problemas', schema=None) as batch_op:
        batch_op.drop_column('linguagens')

    # ### end Alembic commands ###