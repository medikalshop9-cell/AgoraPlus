from fastapi import APIRouter, Depends
from app.middleware.rbac import require_member, require_admin

router = APIRouter(tags=["Events"])

@router.get("/events")
async def list_events(current_user: dict = Depends(require_member)):
    return {"status": "ok", "data": [], "error": None}

@router.post("/events")
async def create_event(current_user: dict = Depends(require_admin)):
    return {"status": "ok", "data": {}, "error": None}
