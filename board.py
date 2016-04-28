import random

import field


class Board:
    '''

    '''
    def __init__(self):
        self.board = [
            field.Field(number)
            for number in range(field.Field.get_field_count())
        ]
        self.chance_cards = ChanceDeck()
        self.chance_cards.shuffle_chance_cards()

    def __repr__(self):
        return 'Board()'

    def __str__(self):
        return 'Board: \n {}'.format(''.join([str(field_.__dict__) for field_ in self.board])) #str(self.board)

    def __getitem__(self, item):
        '''
        Return field information by number
        :param number: number field 0 - 39
        :return:
        >>> board = Board()
        >>> board[0]
        ['Collect $200 salary as you pass GO', 200]
        '''
        return self.board[item]

    def take_chance_card(self):
        return self.chance_cards.take_card()

class ChanceDeck:
    _CHANCE_CARDS = [
        ['GO BACK THREE SPACES'],
        ['PAY SCHOOL TAX: 150'],
        ['PARKING FINE: 15'],
        ['GET OUT OF JAIL FREE'],
        ["ADVANCE TO 'GO'"],
        ["ADVANCE TO ILLINOIS AVENUE, IF YOU PASS 'GO' COLLECT 200"],
        ['PAY POOR TAX: 12'],
        ['MAKE GENERAL REPAIRS ON ALL OF YOUR HOUSES: 25 FOR EACH HOUSE, 100 FOR EACH HOTEL'],
        ['YOU ARE ASSESSED FOR STREET REPAIRS: 40 PER HOUSE, 115 PER HOTEL'],
        ['YOUR XMAS FUND MATURES: 100'],
        ['YOUR BUILDING AND LOAN MATURES: 150'],
        ["ADVANCE TO ST. CHARLES PLACE, IF YOU PASS 'GO' COLLECT 200"],
        ["GO TO JAIL, MOVE DIRECTLY TO JAIL, DO NOT PASS 'GO', DO NOT COLLECT 200"],
        ['TAKE A WALK ON THE BOARDWALK'],
        ["TAKE A RIDE ON THE REDING ADVANCE TOKEN AND IF YOU PASS 'GO' COLLECT 200"],
        ['BANK PAYS YOU DIVIDEND: 50']
    ]

    def shuffle_chance_cards(self):
        random.shuffle(self.cards)

    def __init__(self):
        self.cards = self._CHANCE_CARDS[:]

    def take_card(self):
        card = self.cards.pop(0)
        self.cards.append(card)
        return card
