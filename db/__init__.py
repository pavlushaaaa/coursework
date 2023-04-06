import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, create_session

engine = os.environ['SQLALCHEMY_DATABASE_URI']
session = scoped_session(lambda: create_session(bind=engine, autocommit=False, autoflush=True))


def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs, pool_size=16)
    return engine
