import random

import player, observers
import field


def get_amount_players():
    '''
    The amount of players entering
    :return: amount of players > 2
    '''
    amount_players = int(input('input amount_players: '))
    if not amount_players >= 2:
        raise ValueError('not enough players!')
    return amount_players


def push_make_move(name):
    '''
    Waiting for the team to go
    '''
    return input('{}\ninput "go": '.format(name)) == 'go'


def show_field_after_motion(name, position):
    '''
    Display position of the player as a result of movement
    '''
    print('{} new position: {}'.format(name, position))


player_collection = player.CollectionPlayers(get_amount_players())
players_queue = player_collection.players

observers.obj_observers.register(observers.Observable.crossing_start)

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
