
from pydantic import BaseModel

class HintRequest(BaseModel):
    question: str
    user_attempt: str
    hint_level: str
