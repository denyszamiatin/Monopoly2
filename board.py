import field


class Board:
    '''

    '''
    def __init__(self):
        self.board = [
            field.Field(number)
            for number in range(field.Field.get_field_count())
        ]
        field.ChanceField._CHANCE_CARDS = field.ChanceField.shuffle_chance_cards()
        return field.ChanceField._CHANCE_CARDS

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
