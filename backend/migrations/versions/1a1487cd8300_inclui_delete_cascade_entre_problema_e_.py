"""inclui delete CASCADE entre problema e tag

Revision ID: 1a1487cd8300
Revises: c4ad22aed76f
Create Date: 2024-03-30 14:40:12.157055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a1487cd8300'
down_revision = 'c4ad22aed76f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('problema_tag', schema=None) as batch_op:
        batch_op.drop_constraint('problema_tag_problema_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('problema_tag_tag_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key('problema_tag_tag_id_fkey', 'tags', ['tag_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('problema_tag_problema_id_fkey', 'problemas', ['problema_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('problema_tag', schema=None) as batch_op:
        batch_op.drop_constraint('problema_tag_problema_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('problema_tag_tag_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key('problema_tag_tag_id_fkey', 'tags', ['tag_id'], ['id'])
        batch_op.create_foreign_key('problema_tag_problema_id_fkey', 'problemas', ['problema_id'], ['id'])

    # ### end Alembic commands ###
