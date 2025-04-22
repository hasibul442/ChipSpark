def get_health_check_response(user_agent: str):
    return {
        "message": "Ai Microservice is Running Ok",
        "status": "success",
        "User-Agent": user_agent
    }