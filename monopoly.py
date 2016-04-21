import random

import player


def roll_dice():
    """
    Get the result of rolling two dice
    :return: list of integers
    """
    return tuple([random.randint(1, 6) for _ in range(2)])


def get_amount_players():
    '''
    The amount of players entering
    :return: amount of players > 0
    '''
    return int(input('input amount_players: '))


def push_make_move(player):
    '''
    Waiting for the team to go
    '''
    print('{}'.format(player.name))
    return input('input "go": ') == 'go'


def show_field_after_motion():
    print('{} new position: {}'.format(goes_player.name, goes_player.position))


players_queue = player.CollectionPlayers(get_amount_players()).players

while True:
    for goes_player in players_queue:
        if push_make_move(goes_player):
            goes_player.make_move() #функція не враховує можливості дублю?!
            show_field_after_motion()


def check_field(field, RealEstate):
    '''

    :param field:
    :param RealEstate:
    :return: prints name and cost of real estate field
    '''
    if isinstance(field, RealEstate):
        print(field)


if __name__ == "__main__":
    import doctest
    doctest.testmod()