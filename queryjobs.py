''' Query the table and post updates to a slack channel '''
import settings
from jobdb import Base,Job
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from slackclient import SlackClient

engine = create_engine('sqlite:///jobs.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

#filter table by the score as set in the settings
jobs = session.query(Job).filter(Job.score>settings.score_filter).all()

def count_rows():
    '''number of entries that pass the filter'''
    rows = len(jobs)
    return str(rows)

def post_to_slack(sc,text):
    #post a message to SLACK_CHANNEL
    sc.api_call(
        "chat.postMessage", channel=settings.SLACK_CHANNEL, text=text,
        username='jobbot', icon_emoji=':robot_face:'
    )


if __name__ == "__main__":
    sc = SlackClient(settings.SLACK_TOKEN)
    post_to_slack(sc,text=count_rows()+" new jobs matching your criteria")
    #sc.api_call("chat.postMessage", channel=settings.SLACK_CHANNEL, text=count_rows()+" new jobs matching your criteria",
    #    username='jobbot', icon_emoji=':robot_face:')
    for job in jobs:
        desc = "{0} | score: {1} | {2} ".format(job.jobtitle, job.score, job.link)
        post_to_slack(sc,text=desc)
