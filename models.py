from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    source_id = Column(String)
    source_name = Column(String)
    author = Column(String)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    url_to_image = Column(String)
    published_at = Column(DateTime)
    content = Column(String)
