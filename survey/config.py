# Twitter Credentials
#
# To obtain the credentials, you must first have a Twitter account.
# Then, go to https://dev.twitter.com/, login, and click on "Manage Your Apps" to reach https://apps.twitter.com/.
# Then, click "Create New App", fill in the relevant fields, and click "Create your Twitter application".
# With the application created, navigate to the API Keys page and click "Create my access token".
# You now have the four necessary credentials. Copy the API key, API secret,
# Access token, and Access token secret here.
# NOTE: API key and API secret go in the twitter_consumer_key and twitter_consumer_secret vars.
#

twitter_consumer_key = '2FeaO2uQtMapdKfyYow4UWIBY'
twitter_consumer_secret = 'g0cwSiBhGhHhviwYY49mxAbe3KJevnvD1ziOLqDhy8J8jfAs61'
twitter_access_token = '4754053322-qNOi35XY0bHUL4FpoqrKKeiYLSafteIrXS3k9D7'
twitter_access_secret = '0oczGRjonuq21QuBDP1ZvFzoXzyprcTAYF2T0Z6GGJwJJ'

# Personality Insights credentials and URL
#
# You can obtain these credentials by b  inding a PI service to an application in bluemix and
# and clicking the "show credentials" link on the service in the application dashboard.
# Or you can use "cf env <application name>" from the command line to get the credentials.

pi_url = 'https://gateway.watsonplatform.net/personality-insights/api'
pi_username = '764ad7bc-5d1d-4e68-8969-37a4a43e3009'
pi_password = 'sA6IrVsa6dgL'

# Database Credentials
#
# USed to store personality insights and preferences on activities

db_host = 'nativx-db.cgwaxbkpsxvg.us-east-1.rds.amazonaws.com'
db_port = 3306
db_user = 'nativxmaster'
db_passwd = 'nativxtravel'
db = "personality_insights"
