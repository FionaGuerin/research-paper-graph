"""init

Revision ID: 1131abd876d0
Revises: 
Create Date: 2019-12-17 02:14:07.667909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1131abd876d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paper',
    sa.Column('id', sa.String(length=42), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('abstract', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reference',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_paper', sa.String(length=42), nullable=True),
    sa.Column('to_paper', sa.String(length=42), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reference')
    op.drop_table('paper')
    # ### end Alembic commands ###