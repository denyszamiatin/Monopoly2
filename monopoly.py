import random

import player
import field


observers = []
def use_observers(f):
    def wraper(*args, **kwargs):
        result = f(*args, **kwargs)
        for observer in observers:
            observer()
        #return result
    #return wraper

def on_observer(observer):
    if observer not in observers:
        observers.append(observer)

def off_observer(observer):
    if observer in observers:
        observers.remove(observer)

def off_all_observer():
    if observers:
        del observers[:]

def crossing_start(going_player):
    if going_player.position < going_player.previous_position:
        going_player.bank = field.Field._FIELDS[-1]
        print(going_player.bank)


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

on_observer(crossing_start)
print(observers)
#@use_observers

while True:
    for going_player in players_queue:
        going_player.previous_position = going_player.position
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
