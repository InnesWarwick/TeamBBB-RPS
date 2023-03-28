import random
import time
import explorerhat
import sys
from smbus import SMBus
import time
#main method
def main(playerMove):

    print("enter your action then the bot will respond") 
    botMove,botMoveByte  = botsMove()
    compareMoves(playerMove,botMove,botMoveByte)
# this gets user input
def getInput(ch,evt):
    print("input ran")
    if ch == 5:
        playerMove = "ROCK"
    elif ch == 6:
        playerMove = "PAPER"
    elif ch == 7:
        playerMove = "SCISSORS"
    elif ch == 4:
        print("ch 4 ran")
        sys.exit()
    main(playerMove)  

# bots move
def botsMove():
    botChoiceByte = random.randint(1, 3)
    if botChoiceByte == 1:
        botChoice = "ROCK"
    elif botChoiceByte == 2:
        botChoice = "PAPER"
    elif botChoiceByte == 3:
        botChoice = "SCISSORS"
            
    return botChoice,botChoiceByte
    
def compareMoves(playerMove, botMove, botMovesByte): #string, int
    i2cbus = SMBus(1)
    i2caddress = 0x14
    winner = ""
    #   rock > scissors
    #   scissors > paper
    #   paper > rock
    #   hi im jack and im a little monkey ooo oo ahha haaa
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
    i2cbus.write_byte(i2caddress,botMovesByte)
    time.sleep(3)
    i2cbus.write_byte(i2caddress,0)
if __name__ == "__main__":
    print("1 = ROCK 2 = PAPER 3 = SCISSORS")
    while True:
        explorerhat.touch.pressed(getInput)
