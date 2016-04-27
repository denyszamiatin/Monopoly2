import random

import field
import observers


class Player:
    """
    """

    def __init__(self, name, color, bank):
        """
        """
        self.name = name
        self.color = color
        self.bank = bank
        self.position = 0
        self.previous_position = 0

    def roll_dice(self):
        """
        Get the result of rolling two dice
        :return: list of integers
        """
        return tuple([random.randint(1, 6) for _ in range(2)])

    @observers.player_observer
    def make_move(self):
        print('make_move')
        '''
        Get new player's position
        '''
        self.previous_position = self.position
        self.position = (sum(self.roll_dice()) + self.position) % (field.Field.get_field_count() - 1)
        return self

    def change_balance(self, cost):
        self.bank += cost

    def buy_real_estate(self, field):
        if self.input('{}, do you want to buy this real estate? \n input "yes": '.format(self.name)) == 'yes':
            if not self.bank >= field.cost:
                raise ValueError('not enough money!')
            self.change_balance(field.cost)
            field.owner = self
            field.rent = self.board[self.position].get_rent(0)
            print('{} owner is {}, bank: {}'.format(field.name, field.owner.name, self.bank))

    @staticmethod
    def get_player_information():
        name = input('input name: ')
        color = input('input color: ')
        bank = int(input('input bank: '))
        return name, color, bank


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

    def __iter__(self):
        for player in self.players:
            yield player
