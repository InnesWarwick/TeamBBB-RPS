import random
import time
import explorerhat
import signal
import sys
#main method
def main(playerMove):
    print("enter your action then the bot will respond") 
    botMove  = botsMove()
    compareMoves(playerMove,botMove)
# this gets user input
def getInput(ch,evt):
    print("input ran")
    if ch ==5:
        playerMove = "ROCK"
    elif ch == 6:
        playerMove = "PAPER"
    elif ch == 7:
        playerMove = "SCISSORS"
    elif ch == 8:
        print("ch 4 ran")
        sys.exit()
    main(playerMove)  

# bots move
def botsMove():
    botChoice = random.randint(0, 2)
    if botChoice == 0:
        botChoice = "ROCK"
    elif botChoice == 1:
        botChoice = "PAPER"
    elif botChoice == 2:
        botChoice = "SCISSORS"
            
    return botChoice
    
def compareMoves(playerMove, botMove): #string, int
    winner = ""
    #   rock > scissors
    #   scissors > paper
    #   paper > rock
    #   hi im jack and im a little monkey ooo oo ahha haaa
    #   

    if playerMove ==  "ROCK" and botMove != "PAPER" and botMove != "ROCK":
        winner = "Player wins"
    elif playerMove == "PAPER" and botMove != "SCISSORS" and botMove != "PAPER":
        winner = "Player wins"
    elif playerMove == "SCISSORS" and botMove != "ROCK" and botMove != "SCISSORS":
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
    print("1 = ROCK 2 = PAPER 3 = SCISSORS")
    while True:
        explorerhat.touch.pressed(getInput)