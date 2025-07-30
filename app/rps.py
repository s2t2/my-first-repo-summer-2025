# THIS IS MY ROCK PAPER SCISSORS GAME
# this is the "app/rps.py" file...

import random

VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(u, c):
    if u == c:
        result = "TIE GAME"
    elif u == "rock" and c == "scissors":
        result = "USER WINS"
    elif u == "rock" and c == "paper":
        result = "COMP WINS"
    elif u == "scissors" and c == "rock":
        result = "COMP WINS"
    elif u == "scissors" and c == "paper":
        result = "USER WINS"
    elif u == "paper" and c == "rock":
        #result = "COMP WINS" # OOPS THAT WAS A BUG :-/
        result = "USER WINS" # BUG FIXED!!! :-)
    elif u == "paper" and c == "scissors":
        result = "COMP WINS"
    return result


# ONLY RUN THE CODE INDENTED INSIDE
# ... IF WE ARE RUNNING THIS SCRIPT FROM THE COMMAND LINE
# ... BUT NOT IF WE ARE IMPORTING
if __name__ == "__main__":

    print("WELCOME TO MY GAME...")

    player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ")
    print("USER CHOSE:", player_choice)

    # todo: validation step

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMPUTER CHOSE:", computer_choice)

    result_message = determine_winner(player_choice, computer_choice)
    print(result_message)
