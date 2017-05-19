import settings
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import string

    
class IndeedPage(object):
    def __init__(self,pagenum):
        self.Pagenum = pagenum
    
    def scrape(self):
        ''' scrape data from search results'''
        params = settings.filters
        params['start'] = (self.Pagenum - 1)*10
        r = requests.get(settings.jobs_url, params=params)
        soup = BeautifulSoup(r.content, 'html.parser')
        soup_data = soup.find_all('a',{'class': "turnstileLink","data-tn-element":"jobTitle"})
        return soup_data
        
class JobRec(object):
    def __init__(self,title,link):        
        self.Title = title
        self.Link = link
    
    def scrape(self):
        '''scrap page and return the text, all in lower case with no punctuation'''
        # get page html
        try:
            r = requests.get(settings.base_url+self.Link)
        except RequestException as exc:
            r = requests.get(settings.base_url+self.Link,verify=settings.VERIFY_SSL)
        soup = BeautifulSoup(r.content,'html.parser')
        # get visible text on the page
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText()
        # get rid of punctuation and make lowercase
        translator = str.maketrans('', '', string.punctuation)
        visible_text = visible_text.lower().translate(translator)
        return visible_text
    
    def count_key_words(self):
        ''' count the number of words that match the words in key_phrases. '''
        text = self.scrape()
        score = 0
        for key in settings.key_phrases:
            if key in text:
                score += 1
        return score
    
def get_indeed_pages():
    ''' from scraped indeed pages, create a dictionary with job titles and links'''
    links = dict()
    for num in range(settings.number_of_pages):
        page = IndeedPage(num+1)
        soup_data = page.scrape()
        for row in soup_data:
            links[row.get('title')] = row.get('href')
    return links

if __name__ == "__main__":
   pass
