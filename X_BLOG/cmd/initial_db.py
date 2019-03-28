from X_BLOG.db.sqlalchemy import get_engine
from X_BLOG.db.sqlalchemy.module import metadata


def initial_db():
    engine = get_engine()
    metadata.create_all(engine)
