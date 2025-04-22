from fastapi import FastAPI, APIRouter, Header
from typing import Annotated
from sqlmodel import SQLModel, Field, create_engine, Session

from constant.URLConstant import HEALTH_CHECK, API_PREFIX
from controller.HealthController import get_health_check_response
from services.DbConnectionService import db_connection


engine = db_connection()
app = FastAPI()

# Create a router with a prefix
api_router = APIRouter(prefix=API_PREFIX)




@api_router.get(HEALTH_CHECK)
async def health(user_agent: Annotated[str | None, Header()] = None):
    return get_health_check_response(user_agent)

@api_router.get("/test")
async def test(user_agent: Annotated[str | None, Header()] = None):

    try:
        with engine.connect() as connection:
            db_status = "Database connection successful!"
    except OperationalError as e:
        db_status = f"Database connection failed: {e}"
    response = {
        "message": "Hello Test",
        "status": "success",
        "User-Agent": user_agent,
        "engine": str(engine),
        "db_status": db_status,
    }
    return response

# Include the router in the main app
app.include_router(api_router)