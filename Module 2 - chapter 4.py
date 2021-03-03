#Loops


# Initialize offset
offset =8

# Code the while loop
while offset !=0:
    print("correcting...")
    offset = offset -1
    print(offset)

    #######################################
    # Initialize offset
    offset = -6

    # Code the while loop
    while offset != 0:
        print("correcting...")
        if offset > 0:
            offset = offset - 1
        else:
            offset = offset + 1
        print(offset)

##########################################
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
    print(i)

##################################
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for a, room in enumerate(areas) :
    print("room "+str(a)+": "+str(room))

    ################################
    # areas list
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Code the for loop
    for index, area in enumerate(areas):
        print("room " + str(index + 1) + ": " + str(area))

 ###################################
# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room in house:
    print("the " + str(room[0]) + " is " + str(room[1]) + " sqm")