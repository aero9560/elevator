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
#print(external)

"---------------------------------------------------end---------------------------------------------------------------"



print(starting_floor)
print(elevator_floor)
print(external)
#starting_floor = [[5,1], [8,0]]
#elevator_floor = [[2,7], [9,4]]
#external = [[3,1], [5,0], [12,1], [11,0], [10,1], [7,0]]

external_destination = [[],[]]
destination=[]
for i in range(2):
    if len(external) != 0:
        for k in range(len(external)):
            if starting_floor[i][1] == 1 and starting_floor[i][1] == external[k][1] and external[k][0] > starting_floor[i][0]:
                external_destination[i].append(external[k])
                external_destination[i].sort()
            elif starting_floor[i][1] == 0 and starting_floor[i][1] == external[k][1] and external[k][0] < starting_floor[i][0]:
                external_destination[i].append(external[k])
                external_destination[i].sort(reverse=True)
for i in range(len(external_destination)):
    for j in range(len(external_destination[i])):
        for k in range(len(external)):
            if external_destination[i][j] == external[k]:
                del external[k]
                break
print(external_destination)
print(external)

for i in range(len(external)):

    a = abs(external[i][0] - external_destination[0][-1][0])
    b = abs(external[i][0] - external_destination[1][-1][0])
    if a < b:
        external_destination[0].append(external[i])
    else:
        external_destination[1].append(external[i])

print(external_destination)

for i in range(2):
    up = []
    down = []
    total = []
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
#print(destination)

for i in range(2):
    move(starting_floor[i][0], destination[i],i+1)
    print(f"elevator {i+1} is idel")

