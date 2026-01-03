from fastapi import APIRouter, HTTPException
from .schemas.chat import ChatRequest

from ..SERVICES.query_logic import analyze_query
from ..SERVICES.dataset_resolver import resolve_dataset
from ..SERVICES.ai_service import get_ai_response
from ..SERVICES.marine_data_service import fetch_mean_sst

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest) -> dict:
    try:
        analysis = analyze_query(request.query)

        if analysis["type"] == "non-marine":
            return {"response": analysis["message"]}

        dataset_info = resolve_dataset(request.query)

        if dataset_info.get("type") == "concept":
            return {"response": get_ai_response(request.query)}

        if dataset_info.get("dataset") == "sst":
            return {"response": fetch_mean_sst()}

        if dataset_info.get("status") == "not_supported":
            return {"response": dataset_info["message"]}

        return {"response": "Unable to process the query."}
    except Exception as e:
        print(f"/chat error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
