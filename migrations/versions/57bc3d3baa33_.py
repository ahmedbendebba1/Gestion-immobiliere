"""empty message

Revision ID: 57bc3d3baa33
Revises: 
Create Date: 2018-09-09 16:49:18.718000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57bc3d3baa33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_bien_immobilier_id_utilisateur'), 'bien_immobilier', ['id_utilisateur'], unique=False)
    op.drop_index('id_utilisateur', table_name='bien_immobilier')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('id_utilisateur', 'bien_immobilier', ['id_utilisateur'], unique=True)
    op.drop_index(op.f('ix_bien_immobilier_id_utilisateur'), table_name='bien_immobilier')
    # ### end Alembic commands ###