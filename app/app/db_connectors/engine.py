from typing import Callable
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine.url import URL
from typing import ContextManager
import os

try:
    from secret_store import SANDBOX_DB_USERNAME, SANDBOX_DB_PASSWORD, SANDBOX_DB_SCHEMA, SANDBOX_DB_HOST
except:
    SANDBOX_DB_USERNAME = os.environ.get("SANDBOX_DB_USERNAME", None)
    SANDBOX_DB_PASSWORD = os.environ.get("SANDBOX_DB_PASSWORD", None)
    SANDBOX_DB_SCHEMA = os.environ.get("SANDBOX_DB_SCHEMA", None)
    SANDBOX_DB_HOST = os.environ.get("SANDBOX_DB_HOST", None)

CONNECTION_STRING = str(URL('postgresql+psycopg2',
                            username=SANDBOX_DB_USERNAME,
                            password=SANDBOX_DB_PASSWORD,
                            host=SANDBOX_DB_HOST,
                            port=5432,
                            database=SANDBOX_DB_SCHEMA
                            ))

def get_sandbox_db_engine():
    return create_engine(CONNECTION_STRING, connect_args={
        'options': f'-csearch_path={SANDBOX_DB_SCHEMA}'
    })

def get_sandbox_db_session() -> Session:
    return sessionmaker(bind=get_sandbox_db_engine())

@contextmanager
def get_sandbox_db_transaction() -> ContextManager[Session]:
    session_maker = get_sandbox_db_session()
    session = session_maker()
    try:
        yield session
    except Exception as e:
        print("exceptions suck")
        print(e)
        session.rollback()
    finally:
        session.close()
    