# Importing modules
import random

$ python myawesomescript.py | tee textfile.txt

# Variables
answer = [1] * 4
result = ['-','-','-','-'] # convert using (''.join(result)) when printing
tempguess = []
tempanswer = []

# Main code
start = input("Start game (Y/N): ")

while (start.lower() == 'y'): # Query for another game can reset the value
    print ("\n------------------------- \n Starting new game... \n-------------------------")

    # Hidden pegs
    for i in range(4):
        answer[i] = random.randint(1,6)
    turn = 1

    # Instructions
    print (" [Instructions here]\n")
    print (" Color map: 1-White 2-Blue 3-Red 4-Yellow 5-Green 6-Purple\n-------------------------")
    print (" Number to guess:", answer, "\n-------------------------")

    while (turn <= 8):
        result = ['-','-','-','-'] # Result reset

        print ("Try", turn, ": ")
        guess = input("\tGuess: ")
        # Check if guess is within rules
        if (len(guess) != 4) or not(guess.isnumeric()) or (any(y in guess for y in ['7','8','9','0'])):
            print ("Invalid input. Try again... \n-----------")
            continue

        # Compare guess to answer
        hintpeg = 0
        tempguess = list(map(int,(list(guess))))
        tempanswer = list(map(int,(list(answer))))

        print (tempguess)
        print (tempanswer)
        
        # First run, find index matches and exclude them
        for x in range(4):
            if tempguess[x] == tempanswer[x]:
                result[hintpeg] = '1'
                tempguess[x] = '+'
                tempanswer[x] = '*'
                hintpeg += 1
        # Second run, find content matches
        for x in range (4):
            if tempguess[x] in tempanswer:
                result[hintpeg] = '0'
                hintpeg += 1

        print ("\n Result:", (' '.join(result)),"\n-------------------------")

        if result == ['1','1','1','1']:
            turn = 9
        else:
            turn += 1

    # Win/Loss check
    if result == ['1','1','1','1']:
        print ("You won!")
        start = input("Start new game (Y/N): ") # If N, loop is broken.
    else:
        print ("Better luck next time.")
        start = input("Start new game (Y/N): ") # If N, loop is broken.
                
    
print ("\n Exiting...")
empty = input("Press enter to terminate...")
