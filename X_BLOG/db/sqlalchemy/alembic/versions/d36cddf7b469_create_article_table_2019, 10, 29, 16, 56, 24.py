"""create article table

Revision ID: d36cddf7b469
Revises: 6d38cfafa45b
Create Date: 2019-10-29 16:56:24.905405+08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd36cddf7b469'
down_revision = '6d38cfafa45b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
       'article',
        sa.Column('articleID', sa.String(32), primary_key=True),
        sa.Column('categories', sa.String(64), nullable=False),
        sa.Column('title', sa.Text(1000), nullable=False),
        sa.Column('filePath', sa.String(255), nullable=False),
        sa.Column('authorID', sa.String(32), sa.ForeignKey('user.uid')),
        sa.Column('createTime', sa.DATETIME, nullable=False),
        sa.Column('updateTime', sa.DATETIME, nullable=False),
        sa.Column('contentType', sa.String(32), nullable=False),
        sa.Column('articleTagID', sa.String(32), nullable=False),
        sa.Column('hits', sa.Integer, nullable=False),
        sa.Column('statue', sa.Integer, nullable=False),
        sa.Column('allowedComment', sa.Integer, nullable=False),
        sa.Column('articleUrl', sa.String(128), nullable=False)
    )


def downgrade():
    op.drop_table('article')
