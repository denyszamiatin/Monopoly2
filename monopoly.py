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


def push_make_move(name):
    '''
    Waiting for the team to go
    '''
    return input('{}\ninput "go": '.format(name)) == 'go'


def show_field_after_motion(name, position):
    print('{} new position: {}'.format(name, position))


player_collection = player.CollectionPlayers(get_amount_players())
players_queue = player_collection.players

while True:
    for going_player in players_queue:
        if push_make_move(going_player.name):
            # TODO: функція не враховує можливості дублю?!
            going_player.make_move()
            show_field_after_motion(going_player.name, going_player.position)


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