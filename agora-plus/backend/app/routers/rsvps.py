from fastapi import APIRouter, Depends
from app.middleware.rbac import require_member

router = APIRouter(tags=["RSVPs"])

@router.post("/rsvp")
async def create_rsvp(current_user: dict = Depends(require_member)):
    return {"status": "ok", "data": {}, "error": None}
