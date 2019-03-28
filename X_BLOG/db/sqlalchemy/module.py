from sqlalchemy import Column
from sqlalchemy import DATE
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

ArticleTypes = Table('article_types', metadata,
                     Column('id', Integer(8), Sequence('article_type_id_seq'),
                            primary_key=True),
                     Column('name', String(16))
                     )


ArticleAndTypeRelations = \
    Table('article_type_relations', metadata,
          Column('id', Integer(8), Sequence('article_type_relation_seq_id'),
                 primary_key=True),
          Column('article_id', None, ForeignKey('articles.id')),
          Column('article_type_id', None, ForeignKey('article_types.id')),
          )


# path: the storage path
# statue: 0 is deleted, 1 is ok
Articles = Table('articles', metadata,
                 Column('id', String(30), Sequence('article_seq_id'),
                        primary_key=True),
                 Column('name', String),
                 Column('path', String),
                 Column('view_count', Integer),
                 Column('create_date', DATE),
                 Column('update_date', DATE),
                 Column('statue', Integer),
                 Colume('author', String)
                 )


# statue: 0 no show, 1 will show
Comments = Table('comments', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('article_id', None, ForeignKey('articles.id')),
                 Column('content', String),
                 Column('status', Integer),
                 Column('user_id', None, ForeignKey('users.id'))
                 )


Users = Table('users', metadata,
              Column('id', String, primary_key=True),
              Column('user_name', String),
              Column('email', String, nullable=False),
              Column('password', String, nullable=False)
              )
