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
        self.previous_position = self.position
        self.position = (sum(self.roll_dice()) + self.position) % (field.Field.get_field_count() - 1)
        return self

    def check_bank(self, amount):
        return self.bank >= abs(amount)

    def change_balance(self, cost):
        self.bank += cost

    def set_ownership(self, field, cost):
        self.change_balance(cost)
        field.owner = self
        field.rent = field.get_rent(0)
        print('{} owner is {}, bank: {}'.format(field.name, field.owner.name, self.bank))

    def get_auction_offer(self):
        try:
            offer = int(input('{}, input receive auction offer: '.format(self.name)))
        except:
            offer = 0
        return offer

    def show_auction_winner(self, name, max_offer):
        print('auction winner is', name, ', max_offer is:', max_offer)

    def realize_auction(self, field):
        print("Let's auction!!!")
        '''
        Conducted an auction to buy real estate
        '''
        auction_participants = self.player_collection.players[:]
        max_offer = 0
        while len(auction_participants) > 1:
            bidders = auction_participants[:]
            for auction_participant in bidders:
                offer = auction_participant.get_auction_offer()
                if offer <= max_offer:
                    if len(auction_participants) > 1:
                        auction_participants.remove(auction_participant)
                else:
                    max_offer = offer
        winner = auction_participants[0]
        if winner.check_bank(max_offer):
            self.show_auction_winner(winner.name, max_offer)
            winner.set_ownership(field, -max_offer)
        else:
            print(winner.name, ', not enough money to buying real estate!')
            self.realize_auction(field)

    def buy_real_estate(self, field):
        '''
        A buying real estate
        :param field:
        '''
        try:
            if self.input('{}, do you want to buy this real estate? \n input "yes": '.format(self.name)) == 'yes':
                if not self.check_bank(field.cost):
                    raise ValueError('not enough money to buying real estate!')
                self.change_balance(field.cost)
                field.owner = self
                field.rent = self.board[self.position].get_rent(0)
                print('{} owner is {}, bank: {}'.format(field.name, field.owner.name, self.bank))
            else:
                raise ValueError('player refused the buying real estate')
        except ValueError:
            self.realize_auction(field)

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
