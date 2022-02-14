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


uplist = []
downlist = []


def floor_button(desired_floor, direction):

    if direction == 1:  # direction ==1 is going up
        uplist.append(desired_floor)

    else:
        downlist.append(desired_floor)

# elevator_no = int(input("enter no. of elevators"))


total_floor = int(input("Enter no. of floors  "))
start_floor = int(input(f"Elevator staring floor between 1 and {total_floor}  "))
if start_floor == 1:
    dir_elevator = 1
elif start_floor == total_floor:
    dir_elevator = 0
else:
    dir_elevator = int(input("Enter direction of elevator 1 for upward direction 0 for downward  "))

no_des = int(input("Enter no. of destinations from inside elevator "))
for i in range(1, no_des + 1):
    destination_floor = int(input("Enter floor number  "))
    elev_button(destination_floor)

des = int(input("Enter no. of destinations from floors "))
for i in range(1, des+1):
    des_floor = int(input("Enter floor no  "))
    direc = int(input("Enter direction of elevator call button ( 1 for upward direction 0 for downward ) "))
    floor_button(des_floor, direc)

elev_floor = list(set(elev_floor))
uplist = list(set(uplist))
downlist = list(set(downlist))


elev_floor.extend(uplist)
elev_floor.extend(downlist)
# print(elev_floor)
elev_floor = list(set(elev_floor))
# print(elev_floor)
desired_floor_uplist = []
desired_floor_downlist = []
for k in range(len(elev_floor)):
    if elev_floor[k] > start_floor:
        desired_floor_uplist.append(elev_floor[k])
    else:
        desired_floor_downlist.append(elev_floor[k])
    desired_floor_uplist.sort()
    desired_floor_downlist.sort(reverse=True)
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
