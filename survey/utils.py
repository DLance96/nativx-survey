import random
import twitter
import config


EAT_OPTIONS_FILE = "eat_options.txt"
PLAY_OPTIONS_FILE = "play_options.txt"


def get_all_eat_options():
    eat_options = [line.strip() for line in open(EAT_OPTIONS_FILE)]
    return eat_options


def get_all_play_options():
    play_options = [line.strip() for line in open(PLAY_OPTIONS_FILE)]
    return play_options


def get_random_options(num, option_list):
    options = []
    num_list = []
    for x in range(0, num):
        random_selection = random.randrange(0, len(option_list))
        while random_selection in num_list:
            random_selection = random.randrange(0, len(option_list))
        num_list.append(random_selection)

    for selector in num_list:
        options.append(option_list[selector])

    return options


def get_eat_options(num):
    return get_random_options(num, get_all_eat_options())


def get_play_options(num):
    return get_random_options(num, get_all_play_options())


def forms_is_valid(form_list):
    for form in form_list:
        if not form.is_valid():
            return False
    return True


def validate_user(user):
    """ Function not originally from link above. Returns whether or not twitter user is real """
    twitter_api = twitter.Api(consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
                              consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
                              access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN'),
                              access_token_secret=os.environ.get('TWITTER_ACCESS_SECRET'), )

    try:
        twitter_api.GetUser(screen_name=user)
        return True
    except twitter.error.TwitterError:
        return False
