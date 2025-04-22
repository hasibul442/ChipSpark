from fastapi import FastAPI, APIRouter, Header
from typing import Annotated
from sqlmodel import SQLModel, Field, create_engine, Session

from constant.URLConstant import HEALTH_CHECK, API_PREFIX
from constant.DbConstant import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from controller.HealthController import *


DATABASE_URL = f"mysql+mysqlclient://{DB_USER}:''@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

app = FastAPI()

# Create a router with a prefix
api_router = APIRouter(prefix=API_PREFIX)




@api_router.get(HEALTH_CHECK)
async def health(user_agent: Annotated[str | None, Header()] = None):
    return get_health_check_response(user_agent)

@api_router.get("/test")
async def test(user_agent: Annotated[str | None, Header()] = None):
    response = {
        "message": "Hello Test",
        "status": "success",
        "User-Agent": user_agent
    }
    return response

# Include the router in the main app
app.include_router(api_router)