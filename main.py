import random
from enum import Enum
import time

#main method
def main():
    print("enter your action then the bot will respond")
    playerMove = getInput() 
    botMove  = botsMove()
    compareMoves(playerMove,botMove)
# this gets user input
def getInput():
    print("ROCK (R) | PAPER (P) | SCISSORS (S)")

    #Getting valid Input for the user
    userInput = input("Enter your input here: ")

    if userInput != "ROCK" and userInput != "PAPER" and userInput != "SCISSORS":
        print(f"{userInput} is not a valid input")
    else:
        return userInput    

# bots move
def botsMove():
    botChoice = random.randint(0, 2)
    match botChoice:
        case 0:
            botChoice = "ROCK"
        case 1:
            botChoice = "PAPER"
        case 2:
            botChoice = "SCISSORS"
            
    return botChoice
    
def compareMoves(playerMove, botMove): #string, int
    winner = ""
    #   rock > scissors
    #   scissors > paper
    #   paper > rock
    #   hi im jack and im a little monkey ooo oo ahha haaa
    #   

    if playerMove ==  "ROCK" and botMove != "PAPER":
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
    time.sleep(1)
    print(f"bot chose {botMove} you chose {playerMove} the result is {winner}")

    

    
if __name__ == "__main__":
    main()