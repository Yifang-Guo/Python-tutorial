import sys
import random
from enum import Enum

def rps(name='Player'):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            Rock = 1
            paper = 2
            scissors = 3

        playerChoice = input(f"\n{name}, enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

        if playerChoice not in ["1", "2","3"]:
            print(f"{name}, you must enter 1-3")
            return play_rps()

        player = int(playerChoice)

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(f"\n{name} chose {str(RPS(player)).replace("RPS.", "")}.")
        print(f"computer's chose {str(RPS(computer)).replace("RPS.", "")}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name} win!🥳"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name} win!🥳"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name} win!🥳"
            elif player ==  computer:
                return "tie game!🥹"
            else:
                computer_wins += 1
                return "computer win!🖥️"
            
        result = decide_winner(player, computer)
        print(result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"{name} win: {player_wins}")
        print(f"Computer win: {computer_wins}")

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
            sys.exit(f"Bye!👋🏻 {name}")

    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="provides a  personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", 
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()