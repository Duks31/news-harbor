import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from py_code.news_api_data import news_data
from datetime import datetime

db_path = 'sqlite:///news_data.db'

if os.path.exists(db_path):
    os.remove(db_path)
    
engine = create_engine(db_path, echo=True)

Base = declarative_base()

class NewsData(Base):
    __tablename__ = 'news_data'

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
        return 

    session = Session()
    try:
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
    except Exception as e:
        print(f"Error while inserting data: {e}")
        # session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    retrieved_news_data = news_data()
    print(retrieved_news_data)
    insert_news_data(retrieved_news_data)   

