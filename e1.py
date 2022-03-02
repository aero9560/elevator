import time


def move(current_floor, desired_floor):

    while len(desired_floor) > 0:
        while desired_floor[0] != current_floor:
            if current_floor > desired_floor[0]:
                print(f"elevator is on floor {current_floor}")
                current_floor -= 1
                print("elevator going down")
                time.sleep(1)
            else:
                print(f"elevator is on floor {current_floor}")
                current_floor += 1
                print("elevator going up")
                time.sleep(1)
        print(f"reached floor {current_floor}")
        print("doors opening")
        time.sleep(1)
        print("door closing")

        del desired_floor[0]


elev_floor = []
def elev_button(desired_floor):
    elev_floor.append(desired_floor)


external = []
def floor_button(x):
    external.append(x)

#elevator_no = int(input("enter no. of elevators"))

# provide initial data
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
#print(starting_floor)
for j in range(1,3):
    no_des = int(input(f"Enter no. of destinations from inside elevator {j} "))
    destination_list = []
    for _ in range(1, no_des + 1):
        destination_floor = int(input("Enter floor number  "))
        destination_list.append(destination_floor)
    destination_list = list(set(destination_list))
    elev_button(destination_list)
#print(elev_floor)
des = int(input("Enter no. of destinations from floors "))
for _ in range(1, des+1):
    ext = []
    des_floor = int(input("Enter floor no  "))
    direc = int(input("Enter direction of elevator call button ( 1 for upward direction 0 for downward ) "))
    ext.append(des_floor)
    ext.append(direc)
    floor_button(ext)
#print(external)
external_destination = [[], []]
for i in range(2):
    if len(external) != 0:
        for k in range(len(external)):
            if starting_floor[i][1] == 1 and starting_floor[i][1] == external[k][1] and external[k][0] > starting_floor[i][0]:
                external_destination[i].append(external[k][0])
            elif starting_floor[i][1] == 0 and starting_floor[i][1] == external[k][1] and external[k][0] < starting_floor[i][0]:
                external_destination[i].append(external[k][0])
for i in range(len(external_destination)):
    for k in range(len(external)):
        if external_destination[i][0] == external[k][0]:
            del external[k]
            break
#print(external_destination)
#print(external)
for i in range(len(external)):

    a = abs(external[i][0] - external_destination[0][-1])
    b = abs(external[i][0] - external_destination[1][-1])
    if a < b:
        external_destination[0].append(external[i][0])
    else:
        external_destination[1].append(external[i][0])

#print(external_destination)
            #desired_floor_downlist.append(elev_floor[k])
   # desired_floor_uplist.sort()
   #desired_floor_downlist.sort(reverse=True)'''
elev_floor.clear()
if dir_elevator == 1:
    elev_floor.extend(desired_floor_uplist)
    elev_floor.extend(desired_floor_downlist)
else:
    elev_floor.extend(desired_floor_downlist)
    elev_floor.extend(desired_floor_uplist)
# print(desired_floor_uplist, desired_floor_downlist)
# print(elev_floor)
move(start_floor, elev_floor)
print("elevator is idel")

