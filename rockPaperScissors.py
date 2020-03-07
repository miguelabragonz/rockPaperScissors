'''
Created on Mar 7, 2020

@author: ITAUser
'''
import random

#set variable keepPlaying to true
keepPlaying = True   
while(keepPlaying):
    
    #print statement welcoming players to the game
    print("Welcome to Rock Paper Scissors!")
    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)
    print("Rules:The first to win 2 out of 3 wins. Press Q to quit")
    #make a key that assigns a number to each choice for the computer
    
    #1 = "Rock";
    #2 = "Paper";
    #3 = "Scissors";
    
    #import the random function - the computer makes its choice randomly from its function
    #set computer score to 0
    computerScore = 0
    #set player's score to 0
    playerScore = 0
    #while player's score is less than 2 and computer's score is less than 2: -- this means that the game is still on

    while(computerScore < 2 and playerScore < 2):
         
    #computer's choice = random number between 1 and 3 (random function gets used here)
        index = random.randint(1,3)
    #player's choices = input(ask player to select Rock, Paper or Scissors)
        playerChoice = input("Choice Rock, Paper or Scissors:")
    #start checking user options
        if(playerChoice == "q" or playerChoice =="Q"):
            keepPlaying = False
            break
    #userChoice = userChoice.lower()
    #if player inputs 'q': --player wants to end the game
    #   set keepPlaying to False -- ends the loop
    #   stop the loop -- who! break statement
    
    
    #else if (player inputs rock and computer chooses rock) or
    #(player inputs paper and computer chooses paper) or 
    #(player inputs scissors and computer chooses scissors):
    #   print out DRAW
    #   print out player's score and computer's score 
        elif(playerChoice.lower()=="rock" and index == 1) or (playerChoice.lower()== "paper" and index == 2) or (playerChoice.lower()== "scissors" and index == 3):
            print("Draw")
            print("humanScore:" + str(playerScore) , "computerScore:" + str(computerScore) )
        #else of (player inputs rock and computer scissors) or 
        #(player inputs scissors and computer chooses paper) or
        #(player inputs paper and computer chooses rock):
        #   add one to the player's score
        #   print out player's score and computer's score
        elif(playerChoice.lower()=="rock" and index == 3) or (playerChoice.lower()== "paper" and index == 1 ) or (playerChoice.lower()== "scissors" and index == 2):
            print("Win")
            playerScore += 1 
            print("humanScore:" + str(playerScore) , "computerScore:" + str(computerScore) )
        
        #else if(player inputs rock and computer paper) or 
        #(player inputs scissors and computer chooses rock) or 
        #(player inputs paper and computer chooses scissors):
        #   add one to the computer's score
        #   print out player's score and computer's score
        elif(playerChoice.lower()=="rock" and index == 2 ) or (playerChoice.lower()== "paper" and index == 3 ) or (playerChoice.lower()== "scissors" and index == 1):
            print("Lose")
            computerScore += 1
            print("humanScore:" + str(playerScore) , "computerScore:" + str(computerScore) ) 
        
        else: print("invalid input")
    #   tell the user their input was not valid
    
    #print statement thanking the players for playing 
    #if player's score is 2:
    #   print statement letting player know they Won 
    #if computer's score is 2 
    #   print statement letting player know the computer Won
    #print out player's score and computer's score
    
    if(playerScore == 2):
        print ("you WON")
    if(computerScore == 2):
        print("you Lose")
    print("humanScore:" + str(playerScore) , "computerScore:" + str(computerScore) )
    print("Thanks for Playing")