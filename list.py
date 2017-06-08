from colorama import init, Back
from datetime import datetime
from curtsies import Input

def start_stop():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == '\n':
                print('Stop')
            else:
                print(repr('Start/Stop'))
                store_time()

def store_time():
    times = list()
    times.append(datetime.now())
    print(times[0])


if __name__ == '__main__':
    print('Para cancelar presiona Ctrl c')
    start_stop()