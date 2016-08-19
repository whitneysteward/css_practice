def game():
    print("In game function")
    current_room = room0()
    while current_room != exit:
        current_room = current_room()
    current_room()


def process_user_movement(description, doors):
    """This is the process_user_movement function that will
       handle a user's inpt.


    Args:
        doors: A description of the current room
        description: dictionary with door:location sets

    """
    print(description)
    room = " or ".join(doors.keys())

    choice = input("Which direction would you like to go? {}\n".format(room))
    inpt = 'north south east west exit'
    while (not choice in inpt):
        print("I'm sorry, that's not a valid choice, please try again!")
        choice = input("Which direction would you like to go? {}".format(room))


    return doors[choice]



def room0():
    # description
    description = "room 0"
    doors = {"south": room1, "north":room0}
#print statement before the return, explain
    return process_user_movement(description, doors)

def room1():
    description = "room1"
    doors = {"north": room0, "south":room2}
    #print statement before the return, explain
    return process_user_movement(description, doors)

def room2():
    description= "room 2"
    doors ={"east":room3,"west":room2}
    #print statement before the return, explain
    return process_user_movement(description, doors)

def room3():
    description ="room 3"
    doors ={"north":room2,"east":room3,"exit":exit}
    #print statement before the return, explain
    return process_user_movement(description, doors)

# def room4():
#     description ="room 4"
#     doors ={"west":room4,"south":room3}
#     #print statement before the return, explain
#     return process_user_movement(description, doors)
#
# def room5():
#     description ="room5"
#     doors ={"right":room5, "north":room6}
#     #print statement before the return, explain
#     return process_user_movement(description, doors)
#
# def room6():
#     description ="room6"
#     doors = {"south":room6,"left":room4}
#     #print statement before the return, explain
#     return process_user_movement(description, doors)
# def room7():
#     description = "room 7"
#     doors = {"west":room7,"left":room4}
#     #print statement before the return, explain
#     return process_user_movement(description, doors)
# def room8():
#     description ="room 8"
#     doors = {"north":room8,"left":room9}
#     #print statement before the return, explain
#     return process_user_movement(description, doors)
# def room9():
    # description ="room9"
#     doors = {"west":room9,"south":room6}
# #print statement before the return, explain
#     return process_user_movement(description, doors)
# def room10():
#     doors = {"right":room10,"left":room9}

game()


#print('We are going{} direction!'.format(inpt))


#print("I'm sorry, that's not a valid answer!")
