"""recria models com nomes em fk

Revision ID: 9b2c9985c469
Revises: 
Create Date: 2024-02-12 21:35:51.479826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b2c9985c469'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administradores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('administradores', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_administradores_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_administradores_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_administradores_username'), ['username'], unique=True)

    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tags_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_tags_nome'), ['nome'], unique=False)

    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    op.create_table('problemas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('privado', sa.Boolean(), nullable=False),
    sa.Column('nome_arquivo_entrada', sa.String(length=64), nullable=False),
    sa.Column('nome_arquivo_saida', sa.String(length=64), nullable=False),
    sa.Column('tempo_limite', sa.Integer(), nullable=False),
    sa.Column('memoria_limite', sa.Integer(), nullable=False),
    sa.Column('verificador_id', sa.Integer(), nullable=True),
    sa.Column('validador_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['users.id'], name='problemas_usuario_id_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['validador_id'], ['validadores.id'], name='problemas_validador_id_fkey', ondelete='SET NULL', use_alter=True),
    sa.ForeignKeyConstraint(['verificador_id'], ['verificadores.id'], name='problemas_verificador_id_fkey', ondelete='SET NULL', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('validador_id'),
    sa.UniqueConstraint('verificador_id')
    )
    with op.batch_alter_table('problemas', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_problemas_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_problemas_nome'), ['nome'], unique=False)
        batch_op.create_index(batch_op.f('ix_problemas_privado'), ['privado'], unique=False)

    op.create_table('arquivos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('corpo', sa.String(length=250000), nullable=False),
    sa.Column('secao', sa.Enum('RECURSO', 'FONTE', 'ANEXO', 'SOLUCAO', name='secaoenum'), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('problema_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problema_id'], ['problemas.id'], name='arquivos_problema_id_fkey'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('arquivos', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_arquivos_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_arquivos_nome'), ['nome'], unique=False)
        batch_op.create_index(batch_op.f('ix_arquivos_secao'), ['secao'], unique=False)
        batch_op.create_index(batch_op.f('ix_arquivos_status'), ['status'], unique=False)

    op.create_table('declaracoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=64), nullable=False),
    sa.Column('contextualizacao', sa.String(length=10240), nullable=False),
    sa.Column('formatacao_entrada', sa.String(length=10240), nullable=False),
    sa.Column('formatacao_saida', sa.String(length=10240), nullable=False),
    sa.Column('observacao', sa.String(length=10240), nullable=True),
    sa.Column('tutorial', sa.String(length=80240), nullable=True),
    sa.Column('problema_id', sa.Integer(), nullable=True),
    sa.Column('idioma', sa.Enum('AF', 'AR', 'HY', 'AZ', 'BE', 'BN', 'BG', 'CA', 'ZH', 'HR', 'CS', 'DA', 'NL', 'EN', 'ET', 'TL', 'FI', 'FR', 'KA', 'DE', 'EL', 'HE', 'HI', 'HU', 'IS', 'ID', 'GA', 'JA', 'KK', 'KO', 'KY', 'LT', 'MK', 'MS', 'MN', 'NO', 'FA', 'PL', 'PT', 'RO', 'RU', 'SR', 'SI', 'SK', 'SL', 'ES', 'SV', 'TG', 'TH', 'TR', 'TK', 'UK', 'UR', 'UZ', 'VI', 'OT', name='idiomaenum'), nullable=False),
    sa.ForeignKeyConstraint(['problema_id'], ['problemas.id'], name='declaracoes_problema_id_fkey'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('declaracoes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_declaracoes_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_declaracoes_titulo'), ['titulo'], unique=False)

    op.create_table('problema_tag',
    sa.Column('problema_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problema_id'], ['problemas.id'], name='problema_tag_problema_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='problema_tag_tag_id_fkey')
    )
    op.create_table('problema_testes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.Enum('MANUAL', 'GERADO', name='tipotesteproblemaenum'), nullable=False),
    sa.Column('entrada', sa.String(length=250000), nullable=False),
    sa.Column('exemplo', sa.Boolean(), nullable=False),
    sa.Column('descricao', sa.String(length=250000), nullable=True),
    sa.Column('problema_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problema_id'], ['problemas.id'], name='problema_testes_problema_id_fkey'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('problema_testes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_problema_testes_id'), ['id'], unique=False)

    op.create_table('validadores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('corpo', sa.String(length=250000), nullable=False),
    sa.Column('linguagem', sa.String(), nullable=False),
    sa.Column('problema_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problema_id'], ['problemas.id'], name='validadores_problema_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('problema_id')
    )
    with op.batch_alter_table('validadores', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_validadores_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_validadores_nome'), ['nome'], unique=False)

    op.create_table('verificadores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('corpo', sa.String(length=250000), nullable=False),
    sa.Column('linguagem', sa.String(), nullable=False),
    sa.Column('problema_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problema_id'], ['problemas.id'], name='verificadores_problema_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('problema_id')
    )
    with op.batch_alter_table('verificadores', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_verificadores_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_verificadores_nome'), ['nome'], unique=False)

    op.create_table('validador_testes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('entrada', sa.String(length=250000), nullable=False),
    sa.Column('veredito', sa.Enum('VALID', 'INVALID', name='vereditovalidadortesteenum'), nullable=False),
    sa.Column('validador_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['validador_id'], ['validadores.id'], name='validador_testes_validador_id_fkey'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('validador_testes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_validador_testes_id'), ['id'], unique=False)

    op.create_table('verificador_testes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('entrada', sa.String(length=250000), nullable=False),
    sa.Column('veredito', sa.Enum('OK', 'WA', 'PE', 'CA', name='vereditoverificadortesteenum'), nullable=False),
    sa.Column('verificador_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['verificador_id'], ['verificadores.id'], name='verificador_testes_verificador_id_fkey'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('verificador_testes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_verificador_testes_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('verificador_testes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_verificador_testes_id'))

    op.drop_table('verificador_testes')
    with op.batch_alter_table('validador_testes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_validador_testes_id'))

    op.drop_table('validador_testes')
    with op.batch_alter_table('verificadores', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_verificadores_nome'))
        batch_op.drop_index(batch_op.f('ix_verificadores_id'))

    op.drop_table('verificadores')
    with op.batch_alter_table('validadores', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_validadores_nome'))
        batch_op.drop_index(batch_op.f('ix_validadores_id'))

    op.drop_table('validadores')
    with op.batch_alter_table('problema_testes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_problema_testes_id'))

    op.drop_table('problema_testes')
    op.drop_table('problema_tag')
    with op.batch_alter_table('declaracoes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_declaracoes_titulo'))
        batch_op.drop_index(batch_op.f('ix_declaracoes_id'))

    op.drop_table('declaracoes')
    with op.batch_alter_table('arquivos', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_arquivos_status'))
        batch_op.drop_index(batch_op.f('ix_arquivos_secao'))
        batch_op.drop_index(batch_op.f('ix_arquivos_nome'))
        batch_op.drop_index(batch_op.f('ix_arquivos_id'))

    op.drop_table('arquivos')
    with op.batch_alter_table('problemas', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_problemas_privado'))
        batch_op.drop_index(batch_op.f('ix_problemas_nome'))
        batch_op.drop_index(batch_op.f('ix_problemas_id'))

    op.drop_table('problemas')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_id'))
        batch_op.drop_index(batch_op.f('ix_users_email'))

    op.drop_table('users')
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tags_nome'))
        batch_op.drop_index(batch_op.f('ix_tags_id'))

    op.drop_table('tags')
    with op.batch_alter_table('administradores', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_administradores_username'))
        batch_op.drop_index(batch_op.f('ix_administradores_id'))
        batch_op.drop_index(batch_op.f('ix_administradores_email'))

    op.drop_table('administradores')
    # ### end Alembic commands ###
