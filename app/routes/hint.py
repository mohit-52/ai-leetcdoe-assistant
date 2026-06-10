from fastapi import APIRouter
from app.models.request_models import HintRequest
from app.services.hint_service import generate_hint

router = APIRouter(
    prefix="/hint",
    tags=["hint"]
)

@router.post("/")
def get_hint(req: HintRequest):
    hint = generate_hint(
        req.question,
        req.user_attempt,
        req.hint_level
    )
    return {
        "hint": hint
    }




