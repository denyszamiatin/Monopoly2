import random

class Field:
    """
    Field of Monopoly Game Board
    """
    _FIELDS = [
        ['Start', 'Collect $200 salary as you pass GO', 200],
        ['RealEstate', 'Mediter-ranean Avenue $60', 'brown', [-2, -10, -30, -90, -160, -250], -60],
        ['Community Chest'],
        ['RealEstate', 'Baltic Avenue $60', 'brown', [-4, -20, -60, -180, -320, -450], -60],
        ['Income Tax (pay $200)', -200],
        ['Reading Railroad $200', -200],
        ['RealEstate', 'Oriental Avenue $100', 'light blue', [-6, -30, -90, -270, -400, -550], -100],
        ['Chance'],
        ['RealEstate', 'Vermont Avenue $100', 'light blue', [-6, -30, -90, -270, -400, -550], -100],
        ['RealEstate', 'Connecticut Avenue $120', 'light blue', [-8, -40, -100, -300, -450, -600], -120],
        ['In Jail/Just Visiting'],
        ['RealEstate', 'St. Charles Place$140', 'pink', [-12, -60, -180, -500, -700, -900], -140],
        ['Electric Company $150', -150],
        ['RealEstate', 'States Avenue $140', 'pink', [-10, -50, -150, -450, -625, -750], -140],
        ['RealEstate', 'Virginia Avenue $160', 'pink', [-10, -50, -150, -450, -625, -750], -160],
        ['Pennsylvania Railroad $200', -200],
        ['RealEstate', 'St. James Place $180', 'orange', [-14, -70, -200, -550, -750, -950], -180],
        ['Community Chest'],
        ['RealEstate', 'Tennessee Avenue $180', 'orange', [-14, -70, -200, -550, -750, -950], -180],
        ['RealEstate', 'New York Avenue $200', 'orange', [-16, -80, -220, -600, -800, -1000], -200],
        ['Free Parking'],
        ['RealEstate', 'Kentucky Avenue $220', 'red', [-20, -100, -300, -750, -925, -1100], -220],
        ['Chance'],
        ['RealEstate', 'Indiana Avenue $220',  'red', [-18, -90, -250, -700, -875, -1050], -220],
        ['RealEstate', 'Illinois Avenue $240', 'red', [-18, -90, -250, -700, -875, -1050], -240],
        ['B&O Railroad $200', -200],
        ['RealEstate', 'Atlantic Avenue $260', 'yellow', [-24, -120, -360, -850, -1025, -1200], -260],
        ['RealEstate', 'Ventnor Avenue $260', 'yellow', [-22, -110, -330, -800, -975, -1150], -260],
        ['Water Works $150', -150],
        ['RealEstate', 'Marvin Gardens $280', 'yellow', [-22, -110, -330, -800, -975, -1150], -280],
        ['Go To Jail'],
        ['RealEstate', 'Pacific Avenue $300', 'green', [-26, -130, -390, -900, -1100, -1275], -300],
        ['RealEstate', 'North Carolina Avenue $300', 'green', [-26, -130, -390, -900, -1100, -1275], -300],
        ['Community Chest'],
        ['RealEstate', 'Pennsylvania Avenue $320', 'green', [-28, -150, -450, -1000, -1200, -1400], -320],
        ['Short Line $200', -200],
        ['Chance'],
        ['RealEstate', 'Park Place $350', 'blue', [-35, -175, -500, -1100, -1300, -1500], -350],
        ['Luxury Tax (pay $100)', -100],
        ['RealEstate', 'Boardwalk $400', 'blue', [-50, -200, -600, -1400, -1700, -2000], -350]
    ]

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
        elif desc == 'Chance':
            return ChanceField(*args)
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
    def __init__(self, name, color, rent_levels, cost):
        self.name = name
        self.color = color
        self.cost = cost
        self.rent_levels = rent_levels
        self.rent = None
        self.owner = None

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.color, self.cost)

    def _transfer_money(self, going_player):
        print('{} owner is {},\n {}, you must pay rents: {}'.format
              (self.name, self.owner.name, going_player.name, self.rent)
              )
        going_player.change_balance(-self.rent)
        print('{} bank: {}'.format(going_player.name, going_player.bank))
        self.owner.change_balance(self.rent)
        print('{} bank: {}'.format(self.owner.name, self.owner.bank))

    def _is_not_owner(self, player):
        return self.owner is not player

    def do(self, going_player):
        print(self)
        if not self.owner:
            going_player.buy_real_estate(self)
        elif self._is_not_owner(going_player):
            self._transfer_money(going_player)


    def get_rent(self, level):
        return self.rent_levels[level]

    def set_owner(self, owner):
        self.owner = owner

class StartField:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return '{}, {}'.format(self.name, self.cost)

    def do(self, going_player):
        pass


class ChanceField:
    def do(self, going_player):
        card = going_player.board.take_chance_card()
        if card == ['GO BACK THREE SPACES']:
            going_player.change_position(-3)

        elif card == ['PAY SCHOOL TAX: 150']:
            going_player.change_balance(-150)

        



