from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from py_code.news_api_data import news_data
from datetime import datetime

engine = create_engine('sqlite:///news_data.db', echo=True)

Base = declarative_base()

class NewsData(Base):
    __tablename__ = 'news_data'
    def __init__(self, title, description, content, url, publishedAt, source_name, source_id):
        self.title = title
        self.description = description
        self.content = content
        self.url = url
        self.publishedAt = publishedAt
        self.source_name = source_name
        self.source_id = source_id

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    content = Column(String)
    url = Column(String)
    publishedAt = Column(DateTime)
    source_name = Column(String)
    source_id = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def insert_news_data(data):
    if data is None:
        print("No data to insert")
    session = Session()
    for article in data['articles']:
        publication_at = datetime.fromisoformat(article['publishedAt'].rstrip('Z'))
        news_data = NewsData(
            title = article['title'],
            description = article['description'],
            content = article['content'],
            url = article['url'],
            publishedAt = publication_at,
            source_name = article['source']['name'],
            source_id = article['source']['id']
        )
        session.add(news_data)
    session.commit()
    session.close()

if __name__ == "__main__":
    news_data = news_data()
    insert_news_data(news_data)
