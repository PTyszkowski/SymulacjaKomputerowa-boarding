import numpy as np
import random

rows = 23
columns = 6
time = list(range(100000))

def initialize():
    #seats dictionary = {seat_id(row_number, seat_bumber) : seat_status('0' - free, '1' - taken)}
    seats_numeration = []
    for r in range(rows):
        for c in range(columns):
            seats_numeration.append((r,c))

    seats = {}
    for i in range(rows * columns):
        seats[seats_numeration[i]] = 0

    #passangers dictionary = {passanger_id : seat_assigned}
    #random seat assignment
    passangers = {}
    for i in range(rows * columns):
        seat = random.choice(seats_numeration)
        passangers[i] = seat
        seats_numeration.remove(seat)

    aisle = []
    for i in range(rows):
        aisle.append(-1)

    return seats, passangers, aisle

def boarding_order(method):
    queue = np.arange(0,rows * columns, 1)

    if method == 'random':
        np.random.shuffle(queue)
    return list(queue)

def enter_asile(passanger_id):
    aisle[0] = passanger_id

def move_to_row():
    C_aisle = aisle.copy()
    for passanger_id in C_aisle[::-1]:
        if passanger_id == -1:
            continue

        if passangers[passanger_id][0] != aisle.index(passanger_id) and aisle[aisle.index(passanger_id) + 1] == -1:
            aisle [aisle.index(passanger_id) + 1] = passanger_id
            aisle[aisle.index(passanger_id)] = -1



def start_putting_luggage():
    t = np.random.normal(2, 1, 1)
    return t

def stop_putting_luggage():


def start_move_to_column(passanger_id):
    t = 0
    seat = passangers[passanger_id]
    if seat[1] == 2 or seat[1] == 3:
        t += 1

    if seat[1] == 1 or seat[1] == 4:
        t += 2
        if seats[seat[0],2] == 1:
            t += 2

    if seat[1] == 0 or seat[1] == 5:
        t += 3
        if seats[seat[0],2] == 1:
            t += 2
            if seats[seat[0],1] == 1:
                t += 4
    seats[seat] = 1
    return t

seats, passangers, aisle = initialize()
queue = boarding_order('random')

current_time = 0
while sum(list(seats.values())) != columns*rows:
    print(aisle)
    current_time += 1
    move_to_row()
    if aisle[0] == -1 and queue != []:
        enter_asile(queue.pop(0))

    for passanger_id in aisle:
        if passanger_id == -1:
            continue
#zpisywanie zdarzeń do słownika i ich osługa
        if passangers[passanger_id][0] == aisle.index(passanger_id):
            start_putting_luggage()
            move_to_column(passanger_id)
            aisle[aisle.index(passanger_id)] = -1