from fastapi import Depends, HTTPException, status
from app.middleware.auth import verify_token

async def require_member(current_user: dict = Depends(verify_token)) -> dict:
    return current_user

async def require_admin(current_user: dict = Depends(verify_token)) -> dict:
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return current_user
