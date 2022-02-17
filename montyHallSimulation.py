#***************************************************
#PROGRAM NAME:          montyHallSimulation.PY
#PROGRAMMER:            SIEBER
#DATE OF PROGRAM: 	JUNE 18, 2019
#PURPOSE:     		A PROGRAM THAT WILL 
#                       be used to run a monty hall game
#                       1000 times using computer generated
#                       ("random") input
#MODULES USED:          NONE
#INPUT VARIABLE(S):     None- Computes Random variables for input
#OUTPUT:                Game statistics after 1000 games simualted                   
#
#*******************************************************

def main():

    #this program will be used to run a monty hall game
    #1000 times using computer generated ("random") input

    from random import randint

    #announcing counter variables and setting them to initial value of zero
    programRuns = 0
    door1Pick = 0
    door2Pick = 0
    door3Pick = 0
    switchNo = 0
    switchYes = 0
    won = 0
    lost = 0
    wonSwitched = 0
    lostSwitched = 0
    wonNotSwitched = 0
    lostNotSwitched = 0

    #Starting loop to end after 1000 iterations/program runs
    while programRuns<1000:

        #Instead of user picking door and whether to switch, it will be
        #done "randomly" by the computer. for whether to switch or not, 0
        #represents NO SWITCH and 1 represents chosing to switch
        doorPick = randint(1,3)
        switchPick = randint(0,1)

        #converting variable names from previous program modified below to current
        #variable names for this counter program
        firstGuess = doorPick
        secondGuess = switchPick

        #below is code writen for monty hall game, but simplified to only print
        #whether the game was won or lost 

        #Using a random number generator to determine case 1-3 (where car is located)
        randomCase = randint(1,3)
        
        #Evaluating if its case 1 (Car is behind door 1)
        if randomCase == 1:
        
            #evaluating if computer choses door number 1
            if firstGuess == 1:
                if secondGuess == 1:
                    result = 0
                    print("LOST")                
                else:
                    result = 1
                    print("WON")

            #evaluating if computer choses door number 2
            if firstGuess == 2:

                if secondGuess == 1:
                    result = 1
                    print("WON")
                else:
                    result = 0
                    print("LOST")

            #evaluating if computer choses door number 3
            if firstGuess == 3:

                if secondGuess == 1:
                    result = 1
                    print("WON")

                else:
                    result = 0
                    print("LOST")

        #Evaluating if its case 2 (Car is behind door 1)
        if randomCase == 2:
        
            #evaluating if computer choses  door number 1
            if firstGuess == 1:

                if secondGuess == 1:
                    result = 1
                    print("WON")
                    
                else:
                    result = 0
                    print("LOST")

            #evaluating if computer choses door number 2
            if firstGuess == 2:
                
                if secondGuess == 1:
                    result = 0
                    print("LOST")

                else:
                    result = 1
                    print("WON")

            #evaluating if computer choses door number 3
            if firstGuess == 3:

                if secondGuess == 1:
                    result = 0
                    print("WON")

                else:
                    result = 1
                    print("LOST")

        #Evaluating if its case 3 (car behind door 3)  
        if randomCase == 3:
        
            #evaluating if computer choses door number 1
            if firstGuess == 1:
                
                if secondGuess == 1:
                    result = 1
                    print("WON")
                else:
                    result = 0
                    print("LOST")

            #evaluating if computer choses door number 2
            if firstGuess == 2:

                if secondGuess == 1:
                    result = 1
                    print("WON")
                    
                else:
                    result = 0
                    print("LOST")

            #evaluating if computer choses door number 3
            if firstGuess == 3:

                if secondGuess == 1:
                    result = 0
                    print("LOST")

                else:
                    result = 1
                    print("WON")


        #This is my counter so the program stops at so many iterations
        programRuns=programRuns+1

        #This counter calcualtes the number of times the computer picks a door
        if doorPick == 1:
            door1Pick = door1Pick + 1

        elif doorPick == 2:
            door2Pick = door2Pick + 1

        elif doorPick == 3:
            door3Pick = door3Pick + 1

        #This counter calcualtes the number of times the computer
        #decides to switch or not switch doors
        if switchPick == 0:
            switchNo = switchNo + 1
     
        else:
            switchYes = switchYes + 1

        #This counter calcualtes the number of times the computer
        #wins the game or loses the game
        if result == 1:
            won = won + 1

        elif result == 0:
            lost = lost + 1

        #This counter calcualtes the number of times the computer
        #wins the game or loses the game compared to if
        #switch or not
            
        if result == 1 and switchPick == 1:
            wonSwitched = wonSwitched + 1

        elif result==1 and switchPick == 0:
            wonNotSwitched = wonNotSwitched + 1

        elif result==0 and switchPick == 1:
            lostSwitched = lostSwitched + 1

        elif result==0 and switchPick == 0:
            lostNotSwitched = lostNotSwitched + 1

    #printing out all of the data from the counters after 1000 iterations
    print()
    print("There were ", won, " games won" )
    print("There were ", lost, " games lost" )
    print()
    print("Door #1 was chosen by the computer ", door1Pick, " times")
    print("Door #2 was chosen by the computer ", door2Pick, " times")
    print("Door #3 was chosen by the computer ", door3Pick, " times")
    print()
    print("The door was switched ",switchYes," times")
    print("The door was not switched ", switchNo, " times")
    print()
    print("There were",wonSwitched," wins when the door was switched")
    print("There were", wonNotSwitched," wins when the door was NOT switched")
    print("There were",lostSwitched," losses when the door was switched")
    print("There were",lostNotSwitched," losses when the door was NOT switched")

main()





