#
# https://github.com/watson-developer-cloud/personality-insights-twitter-python/blob/master/twitteranalyzer.py
#

import sys
import requests
import json
import twitter
import config

def convert_status_to_pi_content_item(s):
    # My code here
    return {
        'userid': str(s.user.id),
        'id': str(s.id),
        'sourceid': 'python-twitter',
        'contenttype': 'text/plain',
        'language': s.lang,
        'content': s.text,
        'created': s.created_at_in_seconds,
        'reply': (s.in_reply_to_status_id is None),
        'forward': False
    }


handle = sys.argv[1]

twitter_api = twitter.Api(consumer_key=config.twitter_consumer_key,
                  consumer_secret=config.twitter_consumer_secret,
                  access_token_key=config.twitter_access_token,
                  access_token_secret=config.twitter_access_secret,)

statuses = twitter_api.GetUserTimeline(screen_name=handle,
                  count=400,
                  include_rts=False)

pi_content_items_array = map(convert_status_to_pi_content_item, statuses)
pi_content_items = { 'contentItems' : pi_content_items_array }

r = requests.post(config.pi_url + '/v2/profile',
    auth=(config.pi_username, config.pi_password),
    headers = {
        'content-type': 'application/json',
        'accept': 'application/json'
    },
    data=json.dumps(pi_content_items)
)

print("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type']))
print json.loads(r.text)
