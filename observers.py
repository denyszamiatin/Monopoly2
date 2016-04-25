import field


class Observable():
    def __init__(self):
        self.observers = []
    def __call__(self, f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            for observer in self.observers:
                observer(result)
            return result
        return wrapper

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    @staticmethod
    def crossing_start(going_player):
        '''
        Check crossing start
        :param going_player:
        :return:
        '''
        if going_player.position < going_player.previous_position:
            going_player.bank += field.Field._FIELDS[0][-1]

    @staticmethod
    def check_real_estate(going_player):
        '''
        :param field:
        :param RealEstate:
        :return: prints name and cost of real estate field
        '''
        if isinstance(going_player.current_field, field.RealEstate):
            print(going_player.current_field)
            going_player.buy_real_estate()

obj_observers = Observable()