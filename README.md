# job-finder

This bot scrapes the search results of indeed.com (or indeed.de in my case) then scrapes the resulting job reqs and scores each one based on key word matching. The resulting job titles, key word matching score, and links are posted on a Slack channel.

I am currently searching for a job in Germany and this helps me sort through results to find the best jobs to apply for, without doing any German to English translation!

Settings
--------------------

`settings.py` contains full list of all the configuration options.

* `base_url` -- indeed page relevant to your country, `https://de.indeed.com/` in my case
* `number_of_pages` -- number of pages on indeed you wish to sort through.  There are 10 links on a page
* `score_filter` -- key word score thershold for posting result on slack. Set to 0 to post all results
* search parameters --
    - `q`: query (key word)
    - `l`: location
    - `radius`: distance to search from location in km
    - `sort`: 'date' or or relevance (leave blank)
* `key_phrases` -- list of words to look for. `score` is the number of words in this list that our found
* `VERIFY_SSL` -- I am currently running into SSL certification issues for some pages. I am working to resolved this issue but the current work around is setting this value to False. This could be a potential security issue, however.
* `SLACK_CHANNEL` -- to post results in such as `#jobs`
* `SLACK_TOKEN` -- to communicate with slack api.  Keep this private by storing in `private.py` and adding `private.py` to `.gitignore`

Setup
--------------------

* To use this bot, you'll need a Slack team, Slack channel and a Slack API key --
    - Create a Slack team [here](https://slack.com/create#email).  
    - Create a channel. [Here](https://get.slack.help/hc/en-us/articles/201402297-Creating-a-channel) are instructions. Update the name of your channel to `settings.SLACK_CHANNEL`.
    - Get a Slack API token [here](https://api.slack.com/docs/oauth-test-tokens).
* After cloning this repo, install the Python requirements with `pip install -r requirements.txt`.

Run
--------------------

* After updating the configurations in `settings.py` run `python jobdb.py`.  This will do all the scraping and store the results in a `.db` file.
* Run `python queryjobs.py` to query the resulting table and post the results to your Slack channel!

Further Work
--------------------
* Fix SSL certification verification issue.
* Add capability to scrape other job search websites, aggregating the results to the Slack channel.
* Add a time filter to post to the channel only jobs added to the database in the last 24 hours (for example).
* Make scoring mechanism for sophisticated.  For example, instead of a list of key words, input an entire resume/CV and find the similarties between the resume and the job rec.
