from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "FloatChat backend is running"}

""""
To run the FastAPI application, use the following commands:
cd floatchat\backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload
"""
