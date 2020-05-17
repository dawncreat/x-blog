import os
import sys

FILE_PATH = os.path.abspath(__file__)
APP_DIR = os.path.dirname(os.path.dirname(FILE_PATH))
PROJECT_DIR = os.path.dirname(APP_DIR)
# PROJECT_DIR = os.path.dirname(APP_DIR)

sys.path.append(PROJECT_DIR)

from x-blog.db.sqlalchemy import get_engine
from x-blog.db.sqlalchemy.module import metadata

engine_url = 'sqlite:////Users/robot/code/interests/x-blog/db.sqlite3'
engine = get_engine(url=engine_url, echo=True)
metadata.create_all(engine)
