import random
from enum import Enum
import time

class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

#main method
def main():
    print("enter your action then the bot will respond")
    playerMove = getInput() 
    botMove  = botsMove()

def validInput(input):
    return{ #0, 1, 2
        "rock": RPS.ROCK,
        "paper": RPS.PAPER,
        "scissors": RPS.SCISSORS
    }.get(input, "invalid")

# this gets user input
def getInput():
    # user input
    print("ROCK (R) | PAPER (P) | SCISSORS (S)")

    #Getting valid Input for the user
    userInput = input("Enter your input here").lower()
    
    if validInput(userInput) == "invalid":
        print("shit.")

    
            
    if userInput != "ROCK" or userInput != "PAPER" or userInput != "SCISSORS":
        print("please enter a valid input")
    else:
        return userInput    

def botsMove():
    botChoice = random.randint(1, 3)
    match botChoice:
        case 1:
            botChoice = "ROCK"
        case 2:
            botChoice = "PAPER"
        case 3:
            botChoice = "SCISSORS"
    return botChoice
    
def compareMoves(playerMove, botMove):
    winner = ""
    #   rock > scissors
    #   scissors > paper
    #   paper > rock
    if playerMove == "ROCK" and botMove != "PAPER":
        winner = "Player wins"
    elif playerMove == "PAPER" and botMove != "SCISSORS":
        winner = "Player wins"
    elif playerMove == "SCISSORS" and botMove != "ROCK":
        winner = "Player wins"
    elif playerMove == botMove:
        winner = "A draw"
    else:
        winner = "Bot wins"
    print("3...")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1..")
    print(f"bot chose {botMove} you chose {playerMove} the result is {winner}")

    

    
if __name__ == "__main__":
    main()