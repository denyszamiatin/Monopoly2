import field

observers = []
def use_observers(f):
    def wraper(*args, **kwargs):
        result = f(*args, **kwargs)
        print('result', result)
        for observer in observers:
            observer(result)
        return result
    return wraper

def on_observer(observer):
    if observer not in observers:
        observers.append(observer)

def off_observer(observer):
    if observer in observers:
        observers.remove(observer)

def off_all_observer():
    if observers:
        del observers[:]

def crossing_start(going_player):
    if going_player.position < going_player.previous_position:
        going_player.bank += field.Field._FIELDS[0][-1]
        print(going_player.bank)