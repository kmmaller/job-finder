import os

base_url = 'https://de.indeed.com/' 
jobs_url = base_url + 'Jobs'
number_of_pages = 10 #there are 10 entries per page
score_filter = 3 #only show jobs that score above this number. Set to 0 to see all jobs.

'''search parameters:
    q: query (key word)
    l: location
    radius: distance to search from location in km
    sort: 'date' or or relavance (leave blank)'''
filters = {'q': 'Data Science',
           'l': 'Nurnberg',
           'radius': '25',
           'sort' : 'date' } #'start' : 0? for page number

# key words to match job recs to. Use "buzzwords" you would use in your resume. use lowercase
key_phrases = ['machine learning','nurnberg','erlangen','physik','phd',
               'neural networks','python','englischen','deep learning','scikit-learn','english',
               'physics', 'data mining', 'text mining', 'neural networks','sklearn','keras',
               'theano','tensorflow','matlab','statistics'
               ]
#resolving issues with the SSL certificates.  Setting this so false ignores the issue but could be a security risk
VERIFY_SSL = False

SLACK_CHANNEL = "#jobs"

# The token that allows us to connect to slack.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass