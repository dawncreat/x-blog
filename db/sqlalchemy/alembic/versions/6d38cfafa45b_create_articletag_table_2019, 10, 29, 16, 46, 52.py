"""create articleTag table

Revision ID: 6d38cfafa45b
Revises: f176ed1c36c7
Create Date: 2019-10-29 16:46:52.795212+08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d38cfafa45b'
down_revision = 'f176ed1c36c7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'articleTag',
        sa.Column('tagID', sa.String(32), primary_key=True),
        sa.Column('tagName', sa.String(32), nullable=False),
        sa.Column('articleCounts', sa.Integer, default=0),
        sa.Column('tagHits', sa.Integer, default=0),
        sa.Column('createTime', sa.DATETIME, nullable=False),
        sa.Column('updateTime', sa.DATETIME, nullable=False)
    )


def downgrade():
    op.drop_table('articleTag')
