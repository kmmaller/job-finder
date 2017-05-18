from indeedscraper import JobRec
from indeedscraper import get_indeed_pages
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
import time

engine = create_engine('sqlite:///jobs.db', echo=False)
Base = declarative_base()

class Job(Base):
    '''Table for storing data '''
    __tablename__ = 'jobs'
    
    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    jobtitle = Column(String, unique=True)
    score = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def store_jobs(links):
    for key, item in links.items():
        jobrec = JobRec(key,item)
        job = session.query(Job).filter_by(jobtitle=key).first()
        #only ad job if its not found in the database
        if job is None:
            #create job object
            job = Job(
                link = item,
                jobtitle = key,
                score = jobrec.results()['score'],
                )
            session.add(job)
            session.commit()            

if __name__ == "__main__":
    links = get_indeed_pages()
    store_jobs(links)