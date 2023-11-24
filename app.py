#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

#Create a rock, paper and scissor game using the terminal. 
#The game should ask the user to choose between rock, paper and scissor.
#The input of the user has to be case insensitive (rock, Rock, ROCK should all be accepted)   
#If the input is not rock, paper or scissor, the game should ask the user to choose again.
#The game should then randomly choose between rock, paper and scissor.
#The game should then print out the result of the game.
#The game should then ask the user if they want to play again.
#If the user says yes, the game should start over.
#If the user says no, the game should end.
#The game should keep track of the number of wins and losses of the user.

#Write your code here

import random
import time

wins = 0
losses = 0
ties = 0

while True:
    print("%s Rounds, %s Wins, %s Losses, %s Ties" % (wins+losses+ties,wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            print("Thanks for playing!")
            exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type one of r, p, s, or q.")

    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")
    time.sleep(0.5)

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")
    time.sleep(0.5)

    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses = losses + 1
