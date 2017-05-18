
# base url to scrape. first page only right now.
base_url = 'https://de.indeed.com/'
jobs_url = base_url + 'Jobs'
number_of_pages = 2 #there are 10 entries per page
show_top_num = 10 #number of results shown, after sorting

# search parameters
filters = {'q': 'Data Science',
           'l': 'Nurnberg',
           'radius': '25',
           'sort' : 'date'} #'start' : 0? for page number

# key words to match job recs to
key_phrases = ['machine learning','nurnberg','erlangen','physik','phd',
               'neural network','python','englischen','deep learning','scikit-learn','english',
               'physics', 'data mining', 'text mining', 'neural networks','sklearn','keras',
               'theano','tensorflow',
               ]