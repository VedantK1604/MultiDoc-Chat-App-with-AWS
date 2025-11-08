from fastapi import FastAPI
from backend.logger_config import logger

app = FastAPI()


@app.get("/")
def home():
    try:
        logger.info("Home Endpoint Accessed!!")
        return {"message": "fastAPI is runing..."}
    except Exception as e:
        logger.error(f"Error Occured {e}")
        return {"message": "Something bad happed"}
