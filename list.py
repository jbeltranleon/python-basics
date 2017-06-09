from colorama import init, Back
from datetime import datetime, time
from curtsies import Input

def start_stop():
    times = list()
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == '\n':
                break
            else:
                print(repr('Start/Stop'))
                store_time(times)

    for time in times:
        print('El resultado del {} tiempo es de {}'.format(times.index(time)+1, time))

def store_time(times):
    times.append(datetime.now().time())


if __name__ == '__main__':
    print('Para terminar y ver los datos presiona Enter')
    start_stop()