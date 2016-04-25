class Field:
    """
    Field of Monopoly Game Board
    """
    _FIELDS = [
        ['Start', 'Collect $200 salary as you pass GO', 200],
        ['RealEstate', 'Mediter-ranean Avenue $60', 'brown', -60],
        ['Community Chest'],
        ['RealEstate', 'Baltic Avenue $60', 'brown', -60],
        ['Income Tax (pay $200)', -200],
        ['Reading Railroad $200', -200],
        ['RealEstate', 'Oriental Avenue $100', 'light blue', -100],
        ['Chance'],
        ['RealEstate', 'Vermont Avenue $100', 'light blue', -100],
        ['RealEstate', 'Connecticut Avenue $120', 'light blue', -120],
        ['In Jail/Just Visiting'],
        ['RealEstate', 'St. Charles Place$140', 'pink', -140],
        ['Electric Company $150', -150],
        ['RealEstate', 'States Avenue $140', 'pink', -140],
        ['RealEstate', 'Virginia Avenue $160', 'pink', -160],
        ['Pennsylvania Railroad $200', -200],
        ['RealEstate', 'St. James Place $180', 'orange', -180],
        ['Community Chest'],
        ['RealEstate', 'Tennessee Avenue $180', 'orange', -180],
        ['RealEstate', 'New York Avenue $200', 'orange', -200],
        ['Free Parking'],
        ['RealEstate', 'Kentucky Avenue $220', 'red', -220],
        ['Chance'],
        ['RealEstate', 'Indiana Avenue $220',  'red', -220],
        ['RealEstate', 'Illinois Avenue $240', 'red', -240],
        ['B&O Railroad $200', -200],
        ['RealEstate', 'Atlantic Avenue $260', 'yellow', -260],
        ['RealEstate', 'Ventnor Avenue $260', 'yellow', -260],
        ['Water Works $150', -150],
        ['RealEstate', 'Marvin Gardens $280', 'yellow', -280],
        ['Go To Jail'],
        ['RealEstate', 'Pacific Avenue $300', 'green', -300],
        ['RealEstate', 'North Carolina Avenue $300', 'green', -300],
        ['Community Chest'],
        ['RealEstate', 'Pennsylvania Avenue $320', 'green', -320],
        ['Short Line $200', -200],
        ['Chance'],
        ['RealEstate', 'Park Place $350', 'blue', -350],
        ['Luxury Tax (pay $100)', -100],
        ['RealEstate', 'Boardwalk $400', 'blue', -350]
    ]

    #TODO: метод по всіх викликах повертає None
    def __new__(cls, number):
        '''

        :param desc:
        :return: an instance of RealEstate class
        '''
        if not 0 <= number < Field.get_field_count():
            raise IndexError("Field doesn't exist")
        desc, *args = Field._FIELDS[number]

        if desc == 'RealEstate':
            return RealEstateField(*args)
        elif desc == 'Start':
            return StartField(*args)
        else:
            return NoneField()


    @staticmethod
    def get_field_count():
        return len(Field._FIELDS)

    def do(self, going_player):
        pass


class NoneField:
    def do(self, going_player):
        pass


class RealEstateField:
    def __init__(self, name, color, cost):
        self.name = name
        self.color = color
        self.cost = cost
        self.owner = None

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.color, self.cost)

    def do(self, going_player):
        going_player.buy_real_estate(self)


class StartField:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return '{}, {}'.format(self.name, self.cost)

    def do(self, going_player):
        pass