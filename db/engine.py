from sqlalchemy import create_engine, sessionmaker
from secret_store import SANDBOX_DB_PASSWORD, SANDBOX_DB_USERNAME, SANDBOX_DB_SCHEMA


def get_sandbox_db_session():
    return sessionmaker(create_engine(f'postgresql://{SANDBOX_DB_USERNAME}:{SANDBOX_DB_PASSWORD}@localhost/{SANDBOX_DB_SCHEMA}'))