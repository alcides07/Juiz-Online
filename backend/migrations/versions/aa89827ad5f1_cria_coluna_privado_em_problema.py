"""cria coluna privado em problema

Revision ID: aa89827ad5f1
Revises: 766346bd7212
Create Date: 2024-01-20 02:09:15.194468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa89827ad5f1'
down_revision = '766346bd7212'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problemas', sa.Column('privado', sa.Boolean(), nullable=False))
    op.create_index(op.f('ix_problemas_privado'), 'problemas', ['privado'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_problemas_privado'), table_name='problemas')
    op.drop_column('problemas', 'privado')
    # ### end Alembic commands ###