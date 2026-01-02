from fastapi import APIRouter
from app.routes.schemas.chat import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "user_query": request.query,
        "response": "This is a placeholder response. AI will come later."
    }
