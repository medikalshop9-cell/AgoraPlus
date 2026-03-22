from fastapi import APIRouter, Depends
from app.middleware.rbac import require_member, require_admin

router = APIRouter(tags=["Announcements"])

@router.get("/announcements")
async def list_announcements(current_user: dict = Depends(require_member)):
    return {"status": "ok", "data": [], "error": None}

@router.post("/announcements")
async def create_announcement(current_user: dict = Depends(require_admin)):
    return {"status": "ok", "data": {}, "error": None}
