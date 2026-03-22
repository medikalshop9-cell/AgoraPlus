import firebase_admin
from firebase_admin import credentials, auth
from app.config import settings

if not firebase_admin._apps:
    cred = credentials.Certificate(settings.firebase_credentials_path)
    firebase_admin.initialize_app(cred)

async def verify_firebase_token(token: str) -> dict:
    decoded = auth.verify_id_token(token)
    email = decoded.get("email", "")
    if not email.endswith(settings.allowed_email_domain):
        raise ValueError("Domain not allowed")
    return {
        "uid": decoded["uid"],
        "email": email,
        "name": decoded.get("name", ""),
        "role": decoded.get("role", "member"),
    }
