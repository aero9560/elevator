import time


def move(current_floor, desired_floor,x):

    while len(desired_floor) > 0:
        while desired_floor[0] != current_floor:
            if current_floor > desired_floor[0]:
                print(f"elevator {x} is on floor {current_floor}")
                current_floor -= 1
                print(f"elevator {x} going down")
                time.sleep(1)
            else:
                print(f"elevator {x} is on floor {current_floor}")
                current_floor += 1
                print(f"elevator {x} going up")
                time.sleep(1)
        print(f"reached floor {current_floor}")
        print("doors opening")
        time.sleep(1)
        print("door closing")

        del desired_floor[0]


elevator_floor = []
def elev_button(desired_floor):
    elevator_floor.append(desired_floor)


external = []
def floor_button(x):
    external.append(x)


"------------------------------------------- initial data input--------------------------------------------------------"

no_elevator = int(input("Enter no. of elevators"))
total_floor = int(input("Enter no. of floors  "))
starting_floor = []

for i in range(1,3):
    floor_direction = []
    start_floor = int(input(f"Enter  Elevator {i} staring floor between 1 and {total_floor}  "))
    if start_floor == 1:
        dir_elevator = 1
    elif start_floor == total_floor:
        dir_elevator = 0
    else:
            dir_elevator = int(input("Enter direction of elevator 1 for upward direction 0 for downward  "))
    floor_direction.append(start_floor)
    floor_direction.append(dir_elevator)
    starting_floor.append(floor_direction)

for j in range(1,3):
    no_des = int(input(f"Enter no. of destinations from inside elevator {j} "))
    destination_list = []
    for _ in range(1, no_des + 1):
        destination_floor = int(input("Enter floor number  "))
        destination_list.append(destination_floor)
    destination_list = list(set(destination_list))
    elev_button(destination_list)

des = int(input("Enter no. of destinations from floors "))
for _ in range(1, des+1):
    ext = []
    des_floor = int(input("Enter floor no  "))
    direc = int(input("Enter direction of elevator call button ( 1 for upward direction 0 for downward ) "))
    ext.append(des_floor)
    ext.append(direc)
    floor_button(ext)

"---------------------------------------------------end---------------------------------------------------------------"


external_destination = []  # store external request data for sorting
for _ in range(no_elevator):
    external_destination.append([])

destination = []    # store final data for moving elevator 

for i in range(len(external)):

    b = []
    c = []
    for j in range(no_elevator):
        a = []
        if starting_floor[j][1] == external[i][1] == 1 and external[i][0] > starting_floor[j][0]:
            a.append(abs(external[i][0] - starting_floor[j][0]))
            a.append(j)
            b.append(a)
        elif starting_floor[j][1] == external[i][1] == 0 and external[i][0] < starting_floor[j][0]:
            a.append(abs(external[i][0] - starting_floor[j][0]))
            a.append(j)
            b.append(a)
    if len(b) != 0:
        c = min(b, key=lambda x: x[0])
        external_destination[c[1]].append(external[i])

for i in range(no_elevator):
    if starting_floor[i][1] == 1:
        external_destination[i].sort()
    else:
        external_destination[i].sort(reverse=True)

for i in range(len(external_destination)):
    for j in range(len(external_destination[i])):
        for k in range(len(external)):
            if external_destination[i][j] == external[k]:
                del external[k]
                break


"=============for finding which elevator move for service at external request==========================="
for i in range(len(external)):

    b = []
    c = []
    for j in range(no_elevator):
        if len(external_destination[j]) != 0:
            a = []
            a.append(abs(external[i][0] - external_destination[j][-1][0]))
            a.append(j)
            b.append(a)
    if len(b) != 0:
        c = min(b, key=lambda x: x[0])
        external_destination[c[1]].append(external[i])

"==========================================================================================================="



"-------------------------------------order in which which floor request is serviced first----------------------------------------"

for i in range(no_elevator):
    up = []
    down = []
    total = []
    if len(external_destination[i]) != 0:
        for j in range(len(external_destination[i])):
            if starting_floor[i][1] == 1:
                if external_destination[i][j][1] == 1:
                    up.append(external_destination[i][j][0])
                else:
                    down.append(external_destination[i][j][0])
            if starting_floor[i][1] == 0:
                if external_destination[i][j][1] == 0:
                    down.append(external_destination[i][j][0])
                else:
                    up.append(external_destination[i][j][0])
    for l in range(len(elevator_floor[i])):
        if starting_floor[i][1] == 1:
            if starting_floor[i][0] < elevator_floor[i][l]:
                up.append(elevator_floor[i][l])
            else:
                down.append((elevator_floor[i][l]))
        if starting_floor[i][1] == 0:
            if starting_floor[i][0] > elevator_floor[i][l]:
                down.append((elevator_floor[i][l]))
            else:
                up.append(elevator_floor[i][l])

    up.sort()
    down.sort(reverse=True)
    if starting_floor[i][1] == 1:
        total.extend(up)
        total.extend(down)
    else:
        total.extend(down)
        total.extend(up)
    destination.append(total)
"---------------------------------------------------------------------------------------------------------------------"

for i in range(no_elevator):
    move(starting_floor[i][0], destination[i],i+1)
    print(f"elevator {i+1} is idel")

