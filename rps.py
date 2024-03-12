import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    paper = 2
    scissors = 3


print("")

playerChoice = input("enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

player = int(playerChoice)

if player < 1 or player > 3: 
    sys.exit('you must enter 1-3')

computerChoice = random.choice("123")

computer = int(computerChoice)

print("")
print("your chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("computer's chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("you win!🥳")
elif player == 2 and computer == 1:
    print("you win!🥳")
elif player == 3 and computer == 2:
    print("you win!🥳")
elif player ==  computer:
    print("tie game!🥹")
else:
    print("computer win!🖥️")