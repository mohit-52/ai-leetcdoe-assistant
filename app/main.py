from fastapi import FastAPI
from app.routes.hint import router as hint_router

app = FastAPI()

app.include_router(hint_router)

@app.get("/")
def home():
    return {"status": "running"}

