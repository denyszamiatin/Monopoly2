import random


def roll_dice():
    """
    Get the result of rolling two dice
    :return: list of integers
    """
    return tuple([random.randint(1, 6) for _ in range(2)])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
