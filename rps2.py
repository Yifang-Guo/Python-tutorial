import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    paper = 2
    scissors = 3

playAgain = True

while playAgain:

    playerChoice = input("\nenter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

    player = int(playerChoice)

    if player < 1 or player > 3: 
        sys.exit('you must enter 1-3')

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("\nyour chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("computer's chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

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

    playAgain = input("\nPlay again? \nY for yes or \nQ to quit \n\n")

    if playAgain.lower() == "y":
        continue
    else:
        print("\n✨✨✨✨")
        print("Thank you for playing\n")
        playAgain = False