import random

import field, observers


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
        self.previous_position = 0
        self.current_field = field.Field(self.position)
        self.collection_real_estate = {}

    def roll_dice(self):
        """
        Get the result of rolling two dice
        :return: list of integers
        """
        return tuple([random.randint(1, 6) for _ in range(2)])

    @observers.obj_observers
    def make_move(self):
        print('make_move')
        '''
        Get new player's position
        '''
        self.previous_position = self.position
        self.position = (sum(self.roll_dice()) + self.position) % (field.Field.get_field_count() - 1)
        self.current_field = field.Field(self.position)
        return self


    @staticmethod
    def get_player_information():
        name = input('input name: ')
        color = input('input color: ')
        bank = int(input('input bank: '))
        position = int(input('input position: '))
        return name, color, bank, position


    @staticmethod
    def create_player(get_player_information=get_player_information):
        """
        Create a player
        >>>
        >>> p = Player.create_player(get_player_information=lambda: ('x', 'x', 2000, 0))
        >>> p.name
        'x'
        """
        return Player(*Player.get_player_information())

    def buy_real_estate(self):
        '''
        It gives the opportunity to buy property if the player has enough money
        :return:
        '''
        if input('{}, do you want to buy this real estate? \n input "yes": '.format(self.name)) == 'yes':
            if not self.bank >= self.current_field.cost:
                raise ValueError('not enough money!')
            self.bank -= self.current_field.cost
            self.collection_real_estate[self.current_field.name] = self.current_field


class CollectionPlayers:
    '''
    Collection of players
    '''
    def __init__(self, amount_players):
        '''
        :param amount of players
        '''
        self.players = [
            Player.create_player() for _ in range(amount_players)
        ]
        self.shuffle_players()

    def shuffle_players(self):
        """
        Returns list of players sorted by roll dice result
        """
        random.shuffle(self.players)
