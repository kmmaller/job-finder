''' Some simple queries on the created table '''

import settings
from jobdb import Base,Job
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///jobs.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

jobs = session.query(Job).filter(Job.score>settings.score_filter).all()

def first_job():
    job = session.query(Job).first()
    return job

def count_rows():
    rows = session.query(Job).count()
    return rows

if __name__ == "__main__":
    print("total: ", count_rows())
    #print(first_job().jobtitle,': ',first_job().score)
    for job in jobs:
        print(job.id, " " ,job.jobtitle,": ",job.score)