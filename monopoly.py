import random

import player, observers
import field


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
    '''
    Display position of the player as a result of movement
    '''
    print('{} new position: {}'.format(name, position))


player_collection = player.CollectionPlayers(get_amount_players())
players_queue = player_collection.players

observers.on_observer(observers.crossing_start)

while True:
    for going_player in players_queue:
        if push_make_move(going_player.name):
            # TODO: функція не враховує можливості дублю?!
            going_player.make_move()
            show_field_after_motion(going_player.name, going_player.position)
            print(going_player.name, going_player.position, going_player.bank)

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
