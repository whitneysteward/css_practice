import random

class Room:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.visited = False

    def _str_ (self):
        return self.name

    def _repr_(self):
        return self.name
r0 = Room ('Room Zero', " This is Room Zero")
r1 = Room ('Room One',  "This is Room one.")
r2 = Room ('Room Two', " This is Room two.")
r3 = Room ('Room Three', "This is Room three.")
r4 = Room ('Room Four', "This is Room four.")
r5 = Room('Room Five', "This is Room five.")
r6 = Room ('Room Six', "This is Room six")
r7 = Room ('Room Seven', "This is Room seven")
r8 = Room ('Room Eight', "This is Room eight")
r9 = Room ('Room Nine', "This is Room nine")
r10 = Room ('Exit',"" )

r0.doors = {'north':r1}
r1.doors = {'south':r2}
r2.doors = {'west':r3}
r3.doors = {'east':r4}
r4.doors = {'west':r5}
r5.doors = {'east':r6}
r6.doors = {'north':r7}
r7.doors = {'south':r8}
r8.doors = {'east':r9}
r9.doors = {'west':r10}



class Player:
    def __init__ (self, name, wardrobe, location):
        self.name = name
        self.wardrobe = wardrobe
        self.location = location
    def process_user_movement(self):
        if self.location.name == 'Exit':
            exit()
        else :
            print (self.location.description)
            choice = input("Do you want to move to " + ', '.join(self.location.doors.keys()))
            if choice in self.location.doors:
                self.move(self.location.doors[choice])
            else :
                print("I'm sorry, that location is not valid")

    def move (self, room):
        self.location = room
w0 = Player ('King', "This outfit has jems, ribbons of gold",r0)
w1 = Player ('Tactful Joker'," This outfit is laced with sliver and bells",r0)
w2 = Player ('Elephant man'," You grew tough skin, literally",r0)
w3 = Player ('Bravestarr'," Eyes of a hawk, ears of the wolf, strength of the bear,speed of a puma",r0)

# print (w0.location.description)
# w0.move(r2)
# print (w0.location.description)


users = {'King': w0, 'Tactful Joker': w1 ,'Elephant man': w2 ,'Bravestarr': w3}
print("Your choices are : " + ', '.join(users.keys()))
user = input ("What player would you like to be?")
player = users[user]
while True :
    player.process_user_movement()



#     """This is the process_user

#        handle a user's inpt.


    #Args:
        #doors: A description of the current room
        #description: dictionary w door:location sets
