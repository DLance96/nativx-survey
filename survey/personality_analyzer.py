#
# https://github.com/watson-developer-cloud/personality-insights-twitter-python/blob/master/twitteranalyzer.py
#

import sys
import os
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


def run_twitter(handle):
    twitter_api = twitter.Api(consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
                              consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
                              access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN'),
                              access_token_secret=os.environ.get('TWITTER_ACCESS_SECRET'), )

    max_id = None
    statuses = []
    for x in range(0, 16):  # Pulls max number of tweets from an account
        if x == 0:
            statuses_portion = twitter_api.GetUserTimeline(screen_name=handle,
                                                           count=200,
                                                           include_rts=False)
            status_count = len(statuses_portion)
            if status_count is not 0:
                max_id = statuses_portion[status_count - 1].id - 1
                # get id of last tweet and bump below for next tweet set
        else:
            statuses_portion = twitter_api.GetUserTimeline(screen_name=handle,
                                                           count=200,
                                                           max_id=max_id,
                                                           include_rts=False)
            status_count = len(statuses_portion)
            if status_count is not 0:
                max_id = statuses_portion[status_count - 1].id - 1
                # get id of last tweet and bump below for next tweet set
        for status in statuses_portion:
            statuses.append(status)

    pi_content_items_array = map(convert_status_to_pi_content_item, statuses)
    pi_content_items = {'contentItems': pi_content_items_array}

    r = requests.post(os.environ.get('PI_URL') + '/v2/profile',
                      auth=(os.environ.get('PI_USERNAME'), os.environ.get('PI_PASSWORD')),
                      headers={
                          'content-type': 'application/json',
                          'accept': 'application/json'
                      },
                      data=json.dumps(pi_content_items)
                      )

    print("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type']))
    return json.loads(r.text)


def run_text(text):
    r = requests.post(os.environ.get('PI_URL') + '/v2/profile',
                      auth=(os.environ.get('PI_USERNAME'), os.environ.get('PI_PASSWORD')),
                      headers={
                          'content-type': 'text/plain',
                          'accept': 'application/json'
                      },
                      data=text
                      )

    print("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type']))
    return json.loads(r.text)
