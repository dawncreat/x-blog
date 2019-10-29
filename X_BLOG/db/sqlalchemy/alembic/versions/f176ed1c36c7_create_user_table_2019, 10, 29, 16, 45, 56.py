"""create user table

Revision ID: f176ed1c36c7
Revises: 
Create Date: 2019-10-29 16:45:56.031714+08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f176ed1c36c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('uid', sa.String(32), primary_key=True),
        sa.Column('username', sa.String(32), nullable=False),
        sa.Column('password', sa.String(32), nullable=False),
        sa.Column('displayName', sa.String(32), nullable=False),
        sa.Column('email', sa.String(32), nullable=False),
        sa.Column('age', sa.Integer, nullable=False),
        sa.Column('sex', sa.Integer, nullable=False),
        sa.Column('hobbies', sa.Text(1000), nullable=False),
        sa.Column('phone', sa.String(32), nullable=False),
        sa.Column('groupName', sa.String(32), nullable=False),
        sa.Column('createTime', sa.DATETIME, nullable=False),
        sa.Column('updateTime', sa.DATETIME, nullable=False),
        sa.Column('lastLoggedTime', sa.DATETIME, nullable=False),
        sa.Column('status', sa.Integer, nullable=False, default=1),
        sa.Column('articleCount', sa.Integer, nullable=False, default=0)
    )


def downgrade():
    op.drop_table('user')

