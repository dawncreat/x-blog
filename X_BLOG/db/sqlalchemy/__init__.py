# -*- coding: utf-8 -*-
from sqlalchemy import create_engine


def get_engine(url='sqlite://', echo=False):
    engine = create_engine(url, echo=echo)
    return engine
