"""insere coluna imagens em declaracao.

Revision ID: 7289f9a18ec4
Revises: 1a1487cd8300
Create Date: 2024-04-14 19:34:40.945000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7289f9a18ec4'
down_revision = '1a1487cd8300'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('declaracoes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imagens', sa.ARRAY(
            sa.String()), nullable=True, default=[]))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('declaracoes', schema=None) as batch_op:
        batch_op.drop_column('imagens')

    # ### end Alembic commands ###