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


def create_player():
    """
    create a player
    >>> create_player() # doctest: +ELLIPSIS
    input name: input color: input bank: input position: <__main__.Player object at 0x...
    """
    return Player(*get_player_information())


class Collection_Players:
    '''
    class collection of players
    '''
    def __init__(self, amount_players):
        '''
        creating attribute names of players with values-objects a class Player
        :param amount_players: amount of players
        '''
        for number_player in range(amount_players):
            player = create_player()
            self.__dict__[player.name] = player






#amount_players = int(input('input amount of players: '))
#collection_players = Collection_Players(amount_players)
#print(collection_players.Bob.__dict__)

if __name__ == "__main__":
    import doctest
    doctest.testmod()