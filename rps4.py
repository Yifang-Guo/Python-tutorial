import sys
import random
from enum import Enum

game_count = 0

def play_rps():
    class RPS(Enum):
        Rock = 1
        paper = 2
        scissors = 3

    playerChoice = input("\nenter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

    if playerChoice not in ["1", "2","3"]:
        print('you must enter 1-3')
        return play_rps()

    player = int(playerChoice)

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("\nyour chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("computer's chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "you win!🥳"
        elif player == 2 and computer == 1:
            return "you win!🥳"
        elif player == 3 and computer == 2:
            return "you win!🥳"
        elif player ==  computer:
            return "tie game!🥹"
        else:
            return "computer win!🖥️"
        
    result = decide_winner(player, computer)
    print(result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\nPlay again?")

    while True:
        playAgain = input("\nY for yes or \nQ to quit \n\n")
        if playAgain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playAgain.lower() == "y":
        return play_rps()
    else:
        print("\n✨✨✨✨")
        print("Thank you for playing\n")
        sys.exit("Bye!👋🏻")

play_rps()