import random


def roll_dice():
    """
    Get the result of rolling two dice
    :return: list of integers
    """
    return tuple([random.randint(1, 6) for i in range(2)])


class Player:
    """
    """
    def __init__(self, name, color, bank, position):
        """
        """
        self.name = name
        self.color = color
        self.bank = bank
        self.position = position


def get_player_information():
    name = input('input name: ')
    color = input('input color: ')
    bank = input('input bank: ')
    position = input('input position: ')
    return name, color, bank, position


def create_player(get_player_information=get_player_information):
    """
    Create a player
    >>>
    >>> p = create_player(get_player_information=lambda: ('x', 'x', 2000, 0))
    >>> p.name
    'x'
    """
    return Player(*get_player_information())


class CollectionPlayers:
    '''
    Collection of players
    '''
    def __init__(self, amount_players):
        '''
        :param amount of players
        '''
        self.players = [
            create_player() for _ in range(amount_players)
        ]


def make_move(position):
    '''
    Get new player's position
    :param position:
    :return: new player's position
    '''
    return (position + sum(roll_dice())) % 36


if __name__ == "__main__":
    import doctest
    doctest.testmod()