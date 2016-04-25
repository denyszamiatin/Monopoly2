import field


class Board:
    '''

    '''
    def __init__(self):
        self.board = [
            field.Field(number)
            for number in range(field.Field.get_field_count())
        ]

    def __repr__(self):
        return 'Board()'

    def __str__(self):
        return str(self.board) #'Board: \n {}'.format(''.join(self.board))

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
