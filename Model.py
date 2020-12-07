import numpy as np
import random

rows = 23
columns = 6
time = []
for i in range(1000000):
    time.append([])

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
        passangers[i] = [seat,0]    #seat number, event_ongoing (deafault = 0)
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

        if passangers[passanger_id][0][0] != aisle.index(passanger_id) and aisle[aisle.index(passanger_id) + 1] == -1:
            aisle [aisle.index(passanger_id) + 1] = passanger_id
            aisle[aisle.index(passanger_id)] = -1



def start_putting_luggage(passanger_id): #1
    t = -1
    while t <= 0:
        t = np.random.normal(2, 1, 1)
        t = int(round(t[0]))
    time[current_time + t].append((2,passanger_id))
    passangers[passanger_id][1] = 2
    return t

def stop_putting_luggage(passanger_id):#2
    start_moving_to_column(passanger_id)

def start_moving_to_column(passanger_id):#3
    t = 0
    seat = passangers[passanger_id][0]
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
    time[current_time + t].append((4,passanger_id))
    passangers[passanger_id][1] = 4
    return t

def stop_moving_to_column(passanger_id):#4
    seat = passangers[passanger_id][0]
    seats[seat] = 1
    aisle[aisle.index(passanger_id)] = -1

#main

seats, passangers, aisle = initialize()
queue = boarding_order('random')
current_time = 0

while sum(list(seats.values())) != columns*rows:
    current_time += 1
    move_to_row()

    for passanger_id in aisle:
        if passanger_id == -1:
            continue
        if passangers[passanger_id][0][0] == aisle.index(passanger_id) and passangers[passanger_id][1] == 0:
            start_putting_luggage(passanger_id)

    for event in time[current_time]:
        if event[0] == 2:
            stop_putting_luggage(event[1])
        if event[0] == 4:
            stop_moving_to_column(event[1])

    if aisle[0] == -1 and queue != []:
        enter_asile(queue.pop(0))
print(current_time)