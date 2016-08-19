'''But how do I play?!

Angry Dice is a game to be played by yourself or with a partner.

Simply roll numbers 1-6 sequentially to win the game. There are three rounds.

1. Round 1 Goal: roll both a 1 and a 2 to move onto round 2

2. Roll two dice until you roll a 1, a 2, or both a 1 and a 2. Hold one of the dies if you roll a 1 or a 2.
Roll the remaining die until you roll a the remaining number you need.
When you have both values you need, move on to the next round.

3. If you roll two angry dice, start over!

Round 2 Goal: Roll both an 4 and an angry die to move onto the final round.

Very similar to round 1, roll and hold until you have an angry die and a 4. When you have both values you need, move on to the next round.

If you roll two angry dice, start over!

Round 3 Goal: Roll both a 5 and 6 to win!

You may hold a 5, but you may not hold a six. You must either roll a 5 and a 6 simultaniously, or hold a 5 before holding a six. When you have both values you need, your game ends.

If you roll two angry dice, start over!

The first player to get through all three rounds wins!'''

import random

class Angry_dice:
    def __init__(self, player):
        self.name = player
        self.held1 = False
        self.held2 = False
        self.die1 = 0
        self.die2 = 0
        self.round = 1

    def dice (self):
        if self.held1 == True:
                self.die2 = random.randint(1,6)

        elif self.held2 == True:
                self.die1 = random.randint(1,6)


        else:
                self.die1 = random.randint(1,6)
                self.die2 = random.randint(1,6)
        print ("die1:{i} die2:{j}".format (i = self.die1, j = self.die2))


    def round_1(self):
        if (self.die1 == 2 and self.die2 == 1) or (self.die1 == 1 and self.die2 ==  2):
            self.held = True
        print ('Would you like to hold one of the dice? And roll until n\ you receive both a 1 and 2?')
        if (self.die1 == 2 and self.die2 == 1) or (self.die1 == 1 and self.die2 ==  2):
            print("You're onto stage 2 {p}!  ".format (p = self.name))
            self.round = 2


    def round_2(self):
        if (self.die1 == 3 and self.die2 == 4) or (self.die1 == 4 and self.die2 == 3):
            self.held = True
        print ('Would you like to hold one of the dice? And continue to roll until you receive both 3 and 4?')
        if (self.die1 == 3 and self.die2 == 4) or (self.die1 == 4 and self.die2 == 3):
            self.held = True
            print("You're onto stage 3 {p}!  ".format(p = self.name))
            self.round = 3


    def round_3(self):
        if (self.die1 == 5 and self.die2 == 6) or (self.die1 == 6 and self.die2 == 5):
            self.round = 4
            print ("You're the winner {p}! ".format(p = self.name))
            quit()
        else:
            print ("Keep rollin'!")

player = Angry_dice("Whitney")
print("player {}!".format(player.name))

players = []
plcount = input ("How many players are there?")
for pl in range (int(plcount)):
    player = (input("What is your your name? "))

while True:

    player.dice()

    if player.round == 1 :
        print (" You're in round one!")
        input()
        player.round_1()

    elif player.round == 2 :
        print("You're in round two!")
        input()
        player.round_2()

    elif player.round == 3 :
        print("You're in round 3!")
        input()
        player.round_3()

    else:
        player.round == 4
        print ("You won!")
        quit()

    #the first thing i'll do is roll
    #chose to hold
    #check
