from services.DbConnectionService import db_connection
from sqlalchemy.exc import OperationalError

def get_health_check_response(user_agent: str):

    return {
        "message": "Ai Microservice is Running Ok",
        "status": "success",
        "User-Agent": user_agent,
        "db_status": get_health_check_response_with_db_status(),
    }


def get_health_check_response_with_db_status():
    engine = db_connection()
    try:
        with engine.connect() as connection:
            db_status = "Database connection successful!"
    except OperationalError as e:
        db_status = f"Database connection failed: {e}"

    return db_status
    