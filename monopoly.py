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

class Field:
    '''
    Field
    '''
    __fields = [
        ['Collect $200 salary as you pass GO', 200],
        ['Mediter-ranean Avenue $60', 'brown', -60],
        'Community Chest',
        ['Baltic Avenue $60', 'brown', -60],
        ['Income Tax (pay $200)', -200],
        ['Reading Railroad $200', -200],
        ['Oriental Avenue $100', 'light blue', -100],
        'Chance',
        ['Vermont Avenue $100', 'light blue', -100],
        ['Connecticut Avenue $120', 'light blue', -120],
        'In Jail/Just Visiting',
        ['St. Charles Place$140', 'pink', -140],
        ['Electric Company $150', -150],
        ['States Avenue $140', 'pink', -140],
        ['Virginia Avenue $160', 'pink', -160],
        ['Pennsylvania Railroad $200', -200],
        ['St. James Place $180', 'orange', -180],
        'Community Chest',
        ['Tennessee Avenue $180', 'orange', -180],
        ['New York Avenue $200', 'orange', -200],
        'Free Parking',
        ['Kentucky Avenue $220', 'red', -220],
        'Chance',
        ['Indiana Avenue $220',  'red', -220],
        ['Illinois Avenue $240', 'red', -240],
        ['B&O Railroad $200', -200],
        ['Atlantic Avenue $260', 'yellow', -260],
        ['Ventnor Avenue $260', 'yellow', -260],
        ['Water Works $150', -150],
        ['Marvin Gardens $280', 'yellow', -280],
        'Go To Jail',
        ['Pacific Avenue $300', 'green', -300],
        ['North Carolina Avenue $300', 'green', -300],
        'Community Chest',
        ['Pennsylvania Avenue $320', 'green', -320],
        ['Short Line $200', -200],
        'Chance',
        ['Park Place $350', 'blue', -350],
        ['Luxury Tax (pay $100)', -100],
        ['Boardwalk $400', 'blue', -350]
    ]
    def __init__(self, number):
        '''
        :param number: number field 0 - 39
        '''
        self.field = self.__fields[number]

class Board:
    '''
    Board
    '''
    def __init__(self):
        self.board = [Field(number) for number in range(40)]
    def __repr__(self):
        print('repr Board')
        return 'Board()'
    def __str__(self):
        print('str Board')
        return 'Board: \n {}'.format([field.field for field in self.board])
    def get_field_information(self, number):
        '''
        Return field information by number
        :param number: number field 0 - 39
        :return:
        >>> board = Board()
        >>> board.get_field_information(0)
        ['Collect $200 salary as you pass GO', 200]
        '''
        return self.board[number].field

def make_move(position):
    '''
    Get new player's position
    :param position:
    :return: new player's position
    '''
    return (position + sum(roll_dice())) % 39


if __name__ == "__main__":
    import doctest
    doctest.testmod()
