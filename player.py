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
        '''
        Get new player's position
        '''
        self.change_position(sum(self.roll_dice()))
        return self

    def change_position(self, position):
        self.previous_position = self.position
        self.position = (self.position + position) \
            % (field.Field.get_field_count() - 1)

    def check_bank(self, amount):
        return self.bank >= abs(amount)

    def change_balance(self, cost):
        self.bank += cost

    def set_ownership(self, field, cost):
        self.change_balance(cost)
        field.set_owner(self)
        field.rent = field.get_rent(0)
        print('{} owner is {}, bank: {}'.format(field.name, field.owner.name, self.bank))

    def get_auction_offer(self):
        try:
            offer = int(input('{}, input receive auction offer: '.
                              format(self.name)))
            if self.check_bank(offer):
                return offer
        except ValueError:
            pass
        return 0

    def _ask_for_buy(self):
        return input(
                '{}, do you want to buy this real estate? \n input "yes": '
                .format(self.name)
            ) == 'yes'

    def buy_real_estate(self, field):
        '''
        A buying real estate
        :param field:
        '''
        if self._ask_for_buy() and self.check_bank(field.cost):
            self.set_ownership(field, field.cost)
        else:
            self.player_collection.realize_auction(field)

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

    def get_max_offer(self, max_offer, winner):
        is_winner_changed = False
        for bidder in self.players:
            offer = bidder.get_auction_offer()
            if offer > max_offer:
                max_offer, winner = offer, bidder
                is_winner_changed = True
        return is_winner_changed, winner, max_offer

    def get_auction_winner(self):
        max_offer, winner = 0, None
        is_winner_changed = True
        while is_winner_changed:
            is_winner_changed, winner, max_offer = \
                self.get_max_offer(max_offer, winner)
        return winner, max_offer

    @staticmethod
    def show_auction_winner(name, max_offer):
        print('auction winner is', name, ', max_offer is:', max_offer)

    def realize_auction(self, field):
        print("Let's auction!!!")
        '''
        Conducted an auction to buy real estate
        '''
        winner, max_offer = self.get_auction_winner()
        self.show_auction_winner(winner.name, max_offer)
        winner.set_ownership(field, -max_offer)
