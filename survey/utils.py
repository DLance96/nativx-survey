import random


EAT_OPTIONS_FILE = "eat_options.txt"
PLAY_OPTIONS_FILE = "play_options.txt"


def get_all_eat_options():
    eat_options = [line.rstrip('\n') for line in open(EAT_OPTIONS_FILE)]
    return eat_options


def get_all_play_options():
    play_options = [line.rstrip('\n') for line in open(PLAY_OPTIONS_FILE)]
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
    return get_random_options(num, EAT_OPTIONS_FILE)


def get_play_options(num):
    return get_random_options(num, PLAY_OPTIONS_FILE)