import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY = os.getenv("NEWS_API_KEY")
    DB_NAME = os.getenv("DB_NAME")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv('DB_HOST')
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL","redis://127.0.0.1:6379/0")
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND","redis://127.0.0.1:6379/0")

settings = Settings()
