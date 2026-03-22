from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    firebase_credentials_path: str
    allowed_email_domain: str = "@um6p.ma"
    stream_api_key: str = ""
    stream_api_secret: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
