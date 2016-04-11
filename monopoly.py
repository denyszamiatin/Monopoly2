import random


def roll_a_dice():
    """
    Function to get the result of rolling two dice
    :return: list of integers as a result of rolling two dice
    """
    return random.sample(range(1, 7), 2)


class Player:
    def __init__(self, name, color, bank, position):
        self.name = name
        self.color = color
        self.bank = bank
        self.position = position
