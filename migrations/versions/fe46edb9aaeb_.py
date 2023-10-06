"""empty message

Revision ID: fe46edb9aaeb
Revises: 
Create Date: 2023-10-06 14:40:54.911034

"""
from alembic import op
import sqlalchemy as sa

revision = '1bb16490dce5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('naves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=80), nullable=False),
    sa.Column('length', sa.String(length=80), nullable=False),
    sa.Column('crew', sa.String(length=80), nullable=False),
    sa.Column('passengers', sa.String(length=80), nullable=False),
    sa.Column('model', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('manufacturer')
    )
    op.create_table('personajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('genero', sa.String(length=80), nullable=False),
    sa.Column('color_de_pelo', sa.String(length=80), nullable=False),
    sa.Column('especie', sa.String(length=80), nullable=False),
    sa.Column('color_de_ojos', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diametro', sa.String(length=120), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('clima', sa.String(length=80), nullable=False),
    sa.Column('gravedad', sa.String(length=80), nullable=False),
    sa.Column('poblacion', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('diametro')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=80), nullable=False),
    sa.Column('length', sa.String(length=80), nullable=False),
    sa.Column('crew', sa.String(length=80), nullable=False),
    sa.Column('passengers', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('manufacturer')
    )
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('personajes_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.Column('vehiculos_id', sa.Integer(), nullable=True),
    sa.Column('naves_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['naves_id'], ['naves.id'], ),
    sa.ForeignKeyConstraint(['personajes_id'], ['personajes.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehiculos_id'], ['vehiculos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('favoritos')
    op.drop_table('vehiculos')
    op.drop_table('user')
    op.drop_table('planets')
    op.drop_table('personajes')
    op.drop_table('naves')

revision = 'fe46edb9aaeb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('user')