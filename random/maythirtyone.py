# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
# def deposit (self, amount):
#     self.
# def withdraw(self, amount):
#     if self.balance - amount > 0:
#         self.balance -= amount
#         print("Thanks {n}! You withdrew {am}".format (n=self.name, am=amount))
#     else:
#         print(" You don\t have enough money to withdraw{am}!".format(am=amount))
# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, minimum_balance)
#
# chris = BankAccount('Chris', 100)
# account2 = BankAccount('Chelsea', 1000)
#         print(account1.name)
#         print(account1.balance)


#print(account1.name)

'''
Create a simple dice game with two players. Each player will take turns rolling dice.
Add the dice total to each players score. The first one to 20 wins, if a player rolls
a double 3 or 6 the score is reset. Use classes for the users.
'''
import random

class TwoPlayer_game:
    def __init__(self, player):
        self.name = player
        self.score = 0

    def roll_dice (self):
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1,6)

    def game (self):
        self.roll_dice()
        self.score += (self.die1 + self.die2)
        if  (self.die1 == 3 and  self.die2 == 3) or (self.die1 == 6 and self.die2 == 6):
            self.score == 0
            print("Reset! {p}! You received score of 0 ".format (p = self.name))

        elif self.score >= 20:

            print("WINNER!")
        else:
            print ("Keep playing!")

player_one = TwoPlayer_game("Mike")
player_two =TwoPlayer_game("Mitch")


print("player1 {}!".format(player_one.name))
print("player2 {}!".format(player_two.name))

while player_one.score < 20 and player_two.score < 20:
    player_one.game()
    player_two.game()
 #while players roll dice to reach a sum of 20
 #win - player_one
