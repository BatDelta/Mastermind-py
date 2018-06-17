# Importing modules
from random import randint
from time import strftime
from pathlib import *

# Variables
answer = [0] * 4
result = ['-','-','-','-'] # convert using (''.join(result)) when printing
tempGuess = []
tempAnswer = []
logFileName = ("MastermindLog " +str(strftime('%d-%m-%Y')) +(".txt")) # Log file name, generated with current date

# Main code
gameStart = input("Start game (Y/N): ")

if (gameStart.lower() == 'y'): # Open log file only if starting. Statement in seperate 'if' so as not to be repeated in loop
    if (Path(logFileName).is_file()): # If first game of day, write this
        logFile = open(logFileName, 'a')
    else:
        logFile = open(logFileName, 'a')
        logFile.write(("GAME SESSION START - ") +str(strftime('%d-%m-%Y')) +("\n===================================\n"))

    
while (gameStart.lower() == 'y'): # Query for another game can reset the value               
    print ("\n----------------------------------------------------------------------------- \n Starting new game... \n-----------------------------------------------------------------------------") # Game start block

    # Hidden pegs
    for i in range(4):
        answer[i] = randint(1,6)
    turn = 1

    # Instructions
    print ("A set of 4 colors is generated, with the numbers 1-6 representing the colors.\nYou must attempt to figure out the sequence by guessing. You have 8 tries.\n")
    print (" Color map: 1-White 2-Blue 3-Red 4-Yellow 5-Green 6-Purple\n-----------------------------------------------------------------------------")
    # print (" Number to guess:", answer, "\n-----------------------------------------------------------------------------") # For debugging purposes, comment when not needed

    # Log file prints
    logFile.write(("\n\nGame start!\t(Time: ") +str(strftime('%T')) +(")\n--------------------------------------------\n Answer: " +str(answer) +("\n--------------------------------------------\n\t\tGuess\t\tHint\n")))

    # Guessing section, limited for 8 turns
    while (turn <= 8):
        result = ['-','-','-','-'] # Result reset

        print ("Try", turn, ": ")
        guess = input("\tGuess: ")
        
        # '0000' termination
        if (guess == '0000'):
            logFile.write("Try " +str(turn) +("\t\t") +str(guess) +("\t\t") +(''.join(result)) +("\n"))
            break
        # Check if guess is within rules
        elif (len(guess) != 4) or not(guess.isnumeric()) or (any(y in guess for y in ['7','8','9','0'])):
            print ("Invalid input. Try again... \n-----------------------------------------------------------------------------")
            continue

        # Compare guess to answer
        hintpeg = 0
        tempGuess = list(map(int,(list(guess))))
        tempAnswer = list(map(int,(list(answer))))
        # First run, find index matches and exclude them
        for indexCheck in range(4):
            if tempGuess[indexCheck] == tempAnswer[indexCheck]:
                result[hintpeg] = '1'
                tempGuess[indexCheck] = '+'
                tempAnswer[indexCheck] = '*'
                hintpeg += 1
        # Second run, find content matches
        for valueCheck in range (4):
            if tempGuess[valueCheck] in tempAnswer:
                result[hintpeg] = '0'
                tempAnswer[tempAnswer.index(tempGuess[valueCheck])] = '*'
                tempGuess[valueCheck] = '+'
                hintpeg += 1

        print ("\n Result:", (' '.join(result)),"\n-----------------------------------------------------------------------------")
        
        # Log file prints
        logFile.write("Try " +str(turn) +("\t\t") +str(guess) +("\t\t") +(''.join(result)) +("\n"))

        # Correct answer check
        if result == ['1','1','1','1']:
            turn = 9
        else:
            turn += 1

    logFile.write("--------------------------------------------\n")
    # Win/Loss check
    if result == ['1','1','1','1']:
        print ("You won!")
        logFile.write("Game end - User won.\n--------------------------------------------\n")
        gameStart = input("Start new game (Y/N): ") # If N, loop is broken.
    elif (guess == '0000'): # '0000' without win/loss state
        print ("\nManual termination accepted.")
        logFile.write("Game end - User terminated program.\n--------------------------------------------\n")
        gameStart = 'N'
    else:
        print ("Better luck next time.")
        logFile.write("Game end - User lost.\n--------------------------------------------\n")
        gameStart = input("Start new game (Y/N): ") # If N, loop is broken.
                
logFile.close() # Close log file    
print ("\n Exiting...")
empty = input("Press enter to terminate...")
