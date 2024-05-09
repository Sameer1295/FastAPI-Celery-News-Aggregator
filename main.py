from fastapi import FastAPI, HTTPException
from celery import Celery
from datetime import datetime
from celery.schedules import crontab
from newsapi import NewsApiClient
from models import Article
from settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()
newsapi = NewsApiClient(api_key=settings.API_KEY)

DATABASE_URL = f"mysql+mysqldb://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

celery = Celery(
    'main',
    broker='redis://my-redis:6379/0',
    backend='redis://my-redis:6379/0'
)

celery.conf.beat_schedule = {
    'run-task-every-minute': {
        'task': 'main.scheduled_task',
        'schedule': crontab(minute='*'),
    },
}

@celery.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y

@celery.task(name='main.scheduled_task')
def scheduled_task():
    try:
        top_headlines = newsapi.get_top_headlines(language='en', country='us')

        article_data = top_headlines['articles'][0]
        
        article = Article(
            source_id=article_data.get('source', {}).get('id'),
            source_name=article_data.get('source', {}).get('name'),
            author=article_data.get('author'),
            title=article_data.get('title'),
            description=article_data.get('description'),
            url=article_data.get('url'),
            url_to_image="article_data.get('urlToImage')",
            published_at=datetime.strptime(article_data.get('publishedAt'),'%Y-%m-%dT%H:%M:%SZ'),
            content=article_data.get('content')
        )

        db = SessionLocal()
        db.add(article)
        db.commit()
        db.close()

        return {"message": "Article stored successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))