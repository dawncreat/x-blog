from x-blog.db.sqlalchemy import get_engine
from x-blog.db.sqlalchemy.module import metadata


def initial_db():
    engine = get_engine()
    metadata.create_all(engine)
