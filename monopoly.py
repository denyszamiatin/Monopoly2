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

def create_player(name, color, bank, position):
    """
    create a player
    >>> create_player('Bob', 'red', 20000, 'a1') # doctest: +ELLIPSIS
    <__main__.Player object at 0x...
    """
    return Player(name, color, bank, position)

if __name__ == "__main__":
    import doctest
    doctest.testmod()