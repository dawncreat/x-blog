from sqlalchemy import Column
from sqlalchemy import DATE
from sqlalchemy import DATETIME
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import Sequence
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Text


metadata = MetaData()


ArticleTag = Table('articleTag', metadata,
                   Column('tagID', String(32), primary_key=True),
                   Column('tagName', String(32), nullable=False),
                   Column('articleCounts', Integer, default=0),
                   Column('tagHits', Integer, default=0),
                   Column('createTime', DATETIME, nullable=False),
                   Column('updateTime', DATETIME, nullable=False))


# path: the storage path
# statue: 0 is deleted, 1 is ok
Article = Table('article', metadata,
                 Column('aID', String(32), primary_key=True),
                 Column('categories', String(64), nullable=False),
                 Column('title', Text(1000), nullable=False),
                 Column('filePath', String(255), nullable=False),
                 Column('authorID', String(32), ForeignKey('user.uid')),
                 Column('createTime', DATETIME, nullable=False),
                 Column('updateTime', DATETIME, nullable=False),
                 Column('contentType', String(32), nullable=False),
                 Column('articleTagID', String(32), nullable=False),
                 Column('hits', Integer, nullable=False),
                 Column('statue', Integer, nullable=False),
                 Column('allowedComment', Integer, nullable=False),
                 Column('articleUrl', String(128), nullable=False))


# statue: 0 no show, 1 will show
Comment = Table('comment', metadata,
                 Column('commentID', String(32), primary_key=True),
                 Column('status', Integer, default=0),
                 Column('authorID', String(32), ForeignKey('user.uid')),
                 Column('createTime', DATETIME, nullable=False),
                 Column('updateTime', DATETIME, nullable=False),
                 Column('content', Text(1000), nullable=False),
                 Column('articleID', String(32), ForeignKey('article.aID')))


User = Table('user', metadata,
              Column('uid', String(32), primary_key=True),
              Column('username', String(32), nullable=False),
              Column('password', String(32), nullable=False),
              Column('displayName', String(32), nullable=False),
              Column('email', String(32), nullable=False),
              Column('age', Integer, nullable=False),
              Column('sex', Integer, nullable=False),
              Column('hobbies', Text(1000), nullable=False),
              Column('phone', String(32), nullable=False),
              Column('groupName', String(32), nullable=False),
              Column('createTime', DATETIME, nullable=False),
              Column('updateTime', DATETIME, nullable=False),
              Column('lastLoggedTime', DATETIME, nullable=False),
              Column('status', Integer, nullable=False, default=1),
              Column('articleCount', Integer, nullable=False, default=0))
