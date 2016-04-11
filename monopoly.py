import random


def roll_a_dice():
    """
    Function to get the result of rolling two dice
    :return: tuple of integers as a result of rolling two dice
    """
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return (first, second)
