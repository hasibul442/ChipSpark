from fastapi import FastAPI, APIRouter
from constant.URLConstant import HEALTH_CHECK, API_PREFIX

app = FastAPI()

# Create a router with a prefix
api_router = APIRouter(prefix=API_PREFIX)


@api_router.get(HEALTH_CHECK)
async def health():
    response = {
        "message": "Ai Microservice is Running Ok",
        "status": "success"
    }
    return response

@api_router.get("/test")
async def test():
    response = {
        "message": "Hello Test",
        "status": "success"
    }
    return response

# Include the router in the main app
app.include_router(api_router)