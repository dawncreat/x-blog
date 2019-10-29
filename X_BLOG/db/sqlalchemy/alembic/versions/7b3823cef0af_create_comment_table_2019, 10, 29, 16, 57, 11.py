"""create comment table

Revision ID: 7b3823cef0af
Revises: d36cddf7b469
Create Date: 2019-10-29 16:57:11.133638+08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b3823cef0af'
down_revision = 'd36cddf7b469'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comment',
        sa.Column('commentID', sa.String(32), primary_key=True),
        sa.Column('status', sa.Integer, default=0),
        sa.Column('authorID', sa.String(32), sa.ForeignKey('user.uid')),
        sa.Column('createTime', sa.DATETIME, nullable=False),
        sa.Column('updateTime', sa.DATETIME, nullable=False),
        sa.Column('content', sa.Text(1000), nullable=False)
    )


def downgrade():
    op.drop_table('comment')
