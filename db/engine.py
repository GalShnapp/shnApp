from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secret_store import SANDBOX_DB_PASSWORD, SANDBOX_DB_USERNAME, SANDBOX_DB_SCHEMA

CONNECTION_STRING = f'postgresql://{SANDBOX_DB_USERNAME}:{SANDBOX_DB_PASSWORD}@localhost/{SANDBOX_DB_SCHEMA}?currentSchema={SANDBOX_DB_SCHEMA}'

def get_sandbox_db_engine():
    return create_engine(CONNECTION_STRING)

def get_sandbox_db_session():
    return sessionmaker(get_sandbox_db_engine)