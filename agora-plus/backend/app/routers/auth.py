from fastapi import APIRouter, Depends
from app.middleware.auth import verify_token

router = APIRouter(tags=["Auth"])

@router.get("/me")
async def get_me(current_user: dict = Depends(verify_token)):
    return {"status": "ok", "data": current_user, "error": None}
