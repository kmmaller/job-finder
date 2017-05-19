'''This modules creates the database that is updated with the job rec data'''

from indeedscraper import JobRec
from indeedscraper import get_indeed_pages
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
import settings

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
    #loop through dictionary and create JobRec instance for each entry
    for key, item in links.items():
        jobrec = JobRec(key,item)
        #look for current job in database
        job = session.query(Job).filter_by(jobtitle=key).first()
        #only add job if its not already in the database
        if job is None:
            #create Job db object
            job = Job(
                link = settings.base_url+item,
                jobtitle = key,
                score = jobrec.count_key_words()
                )
            session.add(job)
            session.commit()            

if __name__ == "__main__":
    links = get_indeed_pages()
    store_jobs(links)