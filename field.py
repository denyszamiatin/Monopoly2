class Field:
    """
    Field of Monopoly Game Board
    """
    _FIELDS = [
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
        if not 0 < number < Field.get_field_count():
            raise IndexError("Field doesn't exist")
        self.field = self._FIELDS[number]

    @staticmethod
    def get_field_count():
        return len(Field._FIELDS)

    def __str__(self):
        return self.field
