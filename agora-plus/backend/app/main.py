import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.routers import auth, events, announcements, rsvps

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("agora.api")

app = FastAPI(title="AGORA+ API", version="0.1.0")

app.include_router(auth.router, prefix="/v1")
app.include_router(events.router, prefix="/v1")
app.include_router(announcements.router, prefix="/v1")
app.include_router(rsvps.router, prefix="/v1")

@app.get("/")
async def root():
    return {"service": "agora-plus-backend", "status": "ok"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
