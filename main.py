import random
from enum import Enum

class RPS(Enum):
    ROCK = 0
    PAPER = 2
    SCISSORS = 3

#main method
def main():
    print("enter your action then the bot will respond")
    playerMove = getInput() 
    botMove  = botsMove()

# this gets user input
def getInput():
    # user input
    print("ROCK (R) | PAPER (P) | SCISSORS (S)")

    #Getting valid Input for the user
    userInput = input("Enter your input here").lower()

    if userInput == "rock" or "paper" or "scissors":


    
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
    
#def compareMoves(playerMove, botMove):
    #   rock > scissors
    #   scissors > paper
    #   paper > rock
    

if __name__ == "__main__":
    main()