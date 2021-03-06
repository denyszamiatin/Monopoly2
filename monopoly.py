import player, observers, board


def get_amount_players():
    '''
    The amount of players entering
    :return: amount of players > 2
    '''
    amount_players = int(input('input amount_players: '))
    if not amount_players >= 2:
        raise ValueError('not enough players!')
    return amount_players


def push_make_move(name):
    '''
    Waiting for the team to go
    '''
    return input('{}\ninput "go": '.format(name)) == 'go'


def show_field_after_motion(name, position):
    '''
    Display position of the player as a result of movement
    '''
    print('{} new position: {}'.format(name, position))


player_collection = player.CollectionPlayers(get_amount_players())
player.Player.player_collection = player_collection
game_board = board.Board()
player.Player.board = game_board
player.Player.input = input

observers.player_observer.register(observers.Observable.crossing_start)


while True:
    for going_player in player_collection:
        if push_make_move(going_player.name):
            # TODO: функція make_move не враховує можливості дублю?!
            going_player.make_move()
            show_field_after_motion(going_player.name, going_player.position)
            game_board[going_player.position].do(going_player)
