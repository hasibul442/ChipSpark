from sqlmodel import SQLModel, Field, create_engine, Session
from constant.DbConstant import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def db_connection():
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)

    return engine