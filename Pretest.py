# Pretest CSC 217-470
# Programmer: Rebecca Sieber
# Date Created: 6/8/2021
# Date of Final Update: 6/17/2021

############PROGRAM OVERVIEW############
# This program uses 5 functions to demonstrate competency
# in all of the topics covered in  csc 119:
# User input, Arithmetic’s and variables,
# If statements and “Nested” “if” statements, Loops,
# Strings TuplesLists/Dictionaries, Files/Exceptions
#
#
############LIBRARIES############
# No libraries outside of the standard library were used in this program.
#
#
############VARIABLES############
# No variables were used for the main function of this program
# as purpose of the main function is strictly to call on all
# 5 functions. Variables contained within the functions are all
# declared in thier respective function definitions seen below.
#
#
############MAIN PROGRAM############
# The main program calls on all 5 required functions.
#
#
def main():

    # Calling all 5 required functions
    scrabbleAnalysis()                              # calling function to analyze an inputted string
    print("\n\n")                                   # for better readability and transition between functions
    guessMyFavFoods()                               # calling function to utilize tuples in a guessing game
    print("\n\n")                                   # for better readability and transition between functions
    stateCapitals()                                 # calling function to utilize lists/dictionaries with state capitals
    print("\n\n")                                   # for better readability and transition between functions
    fillInTheBlanks()                               # calling function to demonstrate file I/O in a "fill in the blanks" game
    print("\n\n")                                   # for better readability and transition between functions
    minMaxAverage5()                                # calling function to compute min, max, and average of 5 integers
    quit()                                          # Terminating program
    
############FUNCTION 1: scrabbleAnalysis ############
# This function demonstrates Userinput/Arithmetic/variables/If/“Nested” “if”/For
# and While loops/Strings. It requests input from the user and analyzes the input
# to caluate the "value" of a string according to the game of scrabble.
# it also calculates the length of the input string and reverses the string and
# prints the reversed string

def scrabbleAnalysis():
    #VARIABLES#
    userName = "?"              #String inputted by user
    nameLenght = -1             #Stores length of userName
    letterPoints = 0            #Used to caluclate and store scrabble value of userName 
    characterIndex = 0          #Keeps track of index of letters in userName of analysis

    # Calculating legnth of inputted string
    userName = input("Please enter your first and last name: ") # Requesting input from user
    userName = userName.lower()                                 # updating name to all lowercase to elimate case sensitivity
    nameLenght = len(userName)                                  # Calculating length of string
    print("Your name has ", nameLenght,                         #Printing results to the screen
          " characters, including spaces/dashes/numbers/etc") 

    # Reversing inputted string
    characterIndex = nameLenght - 1                 # finding index of last character in the string
    print("Backwards, your name is: ", end = '')    # ending print statement without a newline
    while characterIndex >= 0:                      # Looping through chars in string backwards. Loop ends after first character in string.
        print(userName[characterIndex], end = '')   # Printing each char and ending print statement without a newline
        characterIndex = characterIndex - 1         # decrimenting character index to move backwards through string

    # Calculating scrabble value of string
    for x in userName:
        if (x ==  "a" or
            x ==  "e" or
            x ==  "i" or
            x ==  "l" or
            x ==  "n" or
            x ==  "o" or
            x ==  "r" or
            x ==  "s" or
            x ==  "t" or
            x ==  "u"):
            letterPoints = letterPoints + 1         # scrabble gives 1 point for a, e, i, l, n, o, r, s, t and u
        elif (x ==  "d" or x ==  "g"):
            letterPoints = letterPoints + 2         # scrabble gives 2 points for d and g
        elif (x == "b" or
              x ==  "c" or
              x ==  "m" or
              x ==  "p"):
            letterPoints = letterPoints + 3         # scrabble gives 3 points for b, c, m, and p
        elif (x == "f" or
              x ==  "h" or
              x ==  "v" or
              x ==  "w" or
              x ==  "y"):
            letterPoints = letterPoints + 4         # scrabble gives 4 points for f, h, v, w, and y
        elif x == "k" :
            letterPoints = letterPoints + 5         # scrabble gives 5 points for k
        elif x == "j" or x == "x":
            letterPoints = letterPoints + 8         # scrabble gives 8 points for j and x         
        elif (x == "q" or x == "z"):
            letterPoints = letterPoints + 10        # scrabble gives 8 points for j and x  
        else:
            letterPoints = letterPoints             # ignores and does not give pointes for spaces, dashes, numbers, etc

    # Printing scrabble value to screen
    print("\nIn the game of scrabble, your name would be worth ", letterPoints, " points!") 

    #END OF FUNCTION#
##########################################################################

###########FUNCTION 2: guessMyFavFoods ############
# This function demonstrates tuples by storing static data in a tuple and
# searching said tuple for inputted values

def guessMyFavFoods():
    #VARIABLES#
    my5FavoriteFoods = ("pizza", "enchiladas",                  # tuple containing strings (my 5 fav foods)
                        "bacon", "sushi", "blueberries") 
    userGuess = "?"                                             # String to be inputted by user
    guessCheck = False                                          # Bool- if user guess was found in tuple or not
    wrongGuessCounter = 0                                       # Keeps track of times user has guessed incorreclty (max 10)
    correctGuessCounter = 0                                     # Keeps track of times user has guessed correctly (max 5 = win)

    # Prompting user to play guessing game
    print("Try and guess some my 5 favorite foods. You get 10 wrong guesses!\n")
          
    while (wrongGuessCounter <10 and correctGuessCounter <5):   # stops game if user guesses all 5 correctly or runs out of 10 allotted guesses
        userGuess = input("Guess: ")                            # Requesting/accepting input from user
        userGuess = userGuess.lower()                           # turning userguess into all lowercase to avoid case sensitivity
        guessCheck = False                                      # resetting for users next guess
        
        for item in my5FavoriteFoods:                           # Looping through each item in tuple
            guessCheck = False                                  # resetting for users next guess
            
            if item == userGuess:                               # If user guess is found in tuple...
                guessCheck = True                               # setting bool variable to denote correct guess
                correctGuessCounter = correctGuessCounter + 1   # incrimenting counter
                print("Nice- that IS one of my favorite foods!")# printing message to user affirming correct guess
                break                                           # break out of for loop to go to next guess
            
        if guessCheck == False:                                 # no match was found in tuple...
            wrongGuessCounter = wrongGuessCounter + 1           # incrimenting counter
            print("Nope- that's NOT one of my favorite foods")  # printing message to user

    # Game over - Printing final game stats to user     
    print("You guessed ", correctGuessCounter, " foods correctly and ", wrongGuessCounter, "foods incorrectly.")

    #END OF FUNCTION#
##########################################################################

###########FUNCTION 3: stateCapitals ############
# This function demonstrates Lists/Dictionaries  by storing states and their corresponding
# capital cities in a dictionary and allowing the user to learn the capital of a state by
# simply typing in the name of the state. The function then allows user to input the states
# that they have traveled to into a list. The function then sorts the list in alphabetical order
# before printing the list back to the user

def stateCapitals():
    #VARIABLES#
    userState = "?"                         # Stores user string input
    userStates=[]                           # empty list to hold user input
    stateCounter = 1                        # counter for amount of data inputted into empty list
                                            # Dictionary of states and thier capital cities
    stateCapitals = {"Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix",            
                     "Arkansas":"Little Rock", "California":"Sacramento" ,
                     "Colorado":"Denver", "Connecticut":"Hartford", "Delaware":"Dover",
                     "Florida":"Tallahassee", "Georgia":"Atlanta", "Hawaii":"Honolulu",
                     "Idaho":"Boise", "Illinois":"Springfield"	, "Indiana":"Indianapolis",
                     "Iowa":"Des Moines", "Kansas":"Topeka", "Kentucky":"Frankfort",
                     "Louisiana":"Baton Rouge", "Maine":"Augusta", "Maryland":"Annapolis",
                     "Massachusetts":"Boston", "Michigan":"Lansing", "Minnesota":"Saint Paul",
                     "Mississippi":"Jackson", "Missouri":"Jefferson City", "Montana":"Helena",
                     "Nebraska":"Lincoln", "Nevada":"Carson City", "New Hampshire":"Concord",
                     "New Jersey":"Trenton", "New Mexico":"Santa Fe", "New York":"Albany",
                     "North Carolina":"Raleigh", "North Dakota":"Bismarck", "Ohio":"Columbus",
                     "Oklahoma":"Oklahoma City"	, "Oregon":"Salem", "Pennsylvania":"Harrisburg",
                     "Rhode Island":"Providence", "South Carolina":"Columbia",
                     "South Dakota":"Pierre", "Tennessee":"Nashville", "Texas":"Austin",
                     "Utah":"Salt Lake City", "Vermont":"Montpelier", "Virginia":"Richmond",
                     "Washington":"Olympia", "West Virginia":"Charleston", "Wisconsin":"Madison",
                     "Wyoming":"Cheyenne"}
    
    #prompting user how to interact with program
    print("Type in a state and I will tell you its Capital city or 'quit' to quit.")

    while True:                             # Starting loop to allow user to engage in program for as long as they want
        userState = input("State: ")        # Accepting input from user
        userState = userState.lower()       # Formatting user input into all lowercase
        userState = userState.title()       # Formatting user input to have capital letter beginning each word
        
        if userState == "Quit":             # If user would like to quit this portion of the function...
            print("\n")                     # adding newline for better readability
            break                           # Breaking loop and continueing with the rest of the function
        
        if userState in stateCapitals:      # If user input is correct and contained in dictionary then printing corresponding data
            print("The capital of ", userState, " is ", stateCapitals.get(userState))
            continue                        # returing to top of the loop 
        
        else:                               # User input was not found in the dictionary- printing error message
            print("I'm sorry, I do not know that state. Please check your spelling and try again.")
            continue                        # returing to top of the loop for user to retry input

    # Once user decides to quit learning about state capitals... printing instructional message
    print("What States have you been to?\nHit <enter> inbetween each state, and type 'done' when you're done!")

    while True:                             # starting loop to accept unlimited amount of data from user
        userState = input()                 # accepting string input from user
        userState = userState.lower()       # converting inputted string to all lower case
        userState = userState.title()       # making first letter of each word capitalized
        if userState == "Done":             # When user is done inputting data...
            break                           # breaking out of loop
        else:
            userStates.append(userState)    # adding data to list
            continue                        # continue to top of loop to continue accepting additional data
        
    print("States You have been to: ")      # printing list back to user
    
    for item in sorted(userStates):         # sorting user list and looping through each item for printing
        print (stateCounter, ".", item)     # printing list with number bullets
        stateCounter = stateCounter + 1     # increasing counter

    #END OF FUNCTION#
        
##########################################################################

###########FUNCTION 4: fillInTheBlanks ############
# This function demonstrates Files/Exceptions by reading data from a file,
# editing that data based on user input, and writing update data to a new .txt
# file. This function operates similarly to a madlib- it requests certain types
# of words from the user blindly, and turns the users input into a unique and
# potentially bizarre  story.

def fillInTheBlanks():
    
    #VARIABLES#
    nameOfPerson = "?"                      # Value to be inputted by user
    adjective = "?"                         # Value to be inputted by user
    skill = "?"                             # Value to be inputted by user
    month = "?"                             # Value to be inputted by user
    pluralNoun = "?"                        # Value to be inputted by user
    verb = "?"                              # Value to be inputted by user
    food = "?"                              # Value to be inputted by user
    noun = "?"                              # Value to be inputted by user
    blankStory = "?"                        # Holds default story imported from .txt file
    customStory  = "?"                      # Holds updated story using user input

    # Printing instructions to user
    print("Welcome to 'Fill in the blank!'. Please provide the following wordtypes: ")

    # Accepting input from user and saving to corresponding variable
    name = input("Name of a person: ")      
    adjective = input ("Adjective: ")       
    skill = input ("Skill: ")               
    month = input ("Month of the Year: ")   
    pluralNoun = input ("Plural Noun: ")    
    verb = input ("Verb ending in 'ing': ") 
    food = input ("Food: ")                 
    noun = input ("Noun: ")                 

    # Attempting to open file for reading- producing exception/error if unable to open
    try:
        inFile = open("fillInTheBlanks.txt", "r") 
    except IOError :
        print("Error- Could not open correct input file. Please confirm that 'fillInTheBlanks.txt' is saved to the correct home file and try again.")

    # Reading from .txt file and saving into string variable
    blankStory = inFile.read()

    # Replacing required words with user input and updating users custom story
    customStory = blankStory.replace("(name)", name)
    customStory = customStory.replace("(adjective)", adjective)
    customStory = customStory.replace("(skill)", skill)
    customStory = customStory.replace("(month)", month)
    customStory = customStory.replace("(plural noun)", pluralNoun)
    customStory = customStory.replace("(verb)", verb)
    customStory = customStory.replace("(food)", food)
    customStory = customStory.replace("(noun)", noun)

    # Printing updated custom to user
    print ("\nYOUR CUSTOM STORY:\n", customStory)     
    print ("*Your custom story has been saved to the file 'customFillInTheBlanks.txt'")

    #opening new txt file to save custom story, and writing story to file. Producing exception/error if unable
    try:
        outFile = open("customFillInTheBlanks.txt", "w")
        outFile.write(customStory)

    except IOError :
        print("Error- could not save story to new txt file. Please try again.")

    #closing files
    inFile.close()
    outFile.close()

    #END OF FUNCTION#
    
##########################################################################
###########FUNCTION 5: minMaxAverage ############
# This function accepts 5 integer inputs from the user, then caluclates the minimum
# value, maximum value, and the average(mean). The function then prints the calculations
# to the screen.

def minMaxAverage5():
    #VARIABLES#
    int1 = 0                                            # integer to be provided by user
    int2 = 0                                            # integer to be provided by user
    int3 = 0                                            # integer to be provided by user
    int4 = 0                                            # integer to be provided by user
    int5 = 0                                            # integer to be provided by user
    min = 0                                             # Minimum of 5 integers provided by user
    max = 0                                             # Maximum of 5 integers provided by user
    average = 0                                         # Average (mean) of 5 integers provided by user
    
    print("Please enter 5 integers.")                   # printing instructions to user

    #Starting loop and requesting 1st integer and verifying input is actually an integer
    while True:
        try: int1 = int(input("Integer 1: "))           # try line to see if input was integer
        except ValueError:                              # if there is a value error (input not integer)
            print("Sorry, please input an integer.")    # printing error message
            continue                                    # restarting loop to force user to try again
        else: break                                     # if user entered an integer, continuing to next program line

    #Requesting 2nd integer and verifying input is actually an integer
    while True:
        try: int2 = int(input("Integer 2: "))           # try line to see if input was integer
        except ValueError:                              # if there is a value error (input not integer)
            print("Sorry, please input an integer.")    # printing error message
            continue                                    # restarting loop to force user to try again
        else: break                                     # if user entered an integer, continuing to next program line
        
    #Requesting 3rd integer and verifying input is actually an integer
    while True:
        try: int3 = int(input("Integer 3: "))           # try line to see if input was integer
        except ValueError:                              # if there is a value error (input not integer)
            print("Sorry, please input an integer.")    # printing error message
            continue                                    # restarting loop to force user to try again
        else: break                                     # if user entered an integer, continuing to next program line
        
    #Requesting 4th integer and verifying input is actually an integer
    while True:
        try: int4 = int(input("Integer 4: "))           # try line to see if input was integer
        except ValueError:                              # if there is a value error (input not integer)
            print("Sorry, please input an integer.")    # printing error message
            continue                                    # restarting loop to force user to try again
        else: break                                     # if user entered an integer, continuing to next program line
        
    #Requesting 5th integer and verifying input is actually an integer
    while True:
        try: int5 = int(input("Integer 5: "))           # try line to see if input was integer
        except ValueError:                              # if there is a value error (input not integer)
            print("Sorry, please input an integer.")    # printing error message
            continue                                    # restarting loop to force user to try again
        else: break                                     # if user entered an integer, continuing to next program line     


    
    #Calculating minimum of 5 integers by comparint each integer to the other 4 to determine which is the
    #smallest. Using <= since there could be a "tie" for smallest.
    if int1 <= int2 and int1 <= int3 and int1 <= int4 and int1 <= int5:
        min = int1
    elif int2 <= int1 and int2 <= int3 and int2 <= int4 and int2 <= int5:
        min = int2
    elif int3 <= int1 and int3 <= int2 and int3 <= int4 and int3 <= int5:
        min = int3
    elif int4 <= int1 and int4 <= int2 and int4 <= int3 and int4 <= int5:
        min = int4
    else:
        min = int5

    #Calculating maximum of 5 integers by comparint each integer to the other 4 to determine which is the
    #biggest. Using >= since there could be a "tie" for biggest.
    if int1 >= int2 and int1 >= int3 and int1 >= int4 and int1 >= int5:
        max = int1
    elif int2 >= int1 and int2 >= int3 and int2 >= int4 and int2 >= int5:
        max = int2
    elif int3 >= int1 and int3 >= int2 and int3 >= int4 and int3 >= int5:
        max = int3
    elif int4 >= int1 and int4 >= int2 and int4 >= int3 and int4 >= int5:
        max = int4
    else: max = int5
        
    #Calculating mean/average of 5 integers
    average = (int1 + int2 + int3 + int4 + int5)/5

    #Printing results of min/max/average
    print("Miniumum:", min, "Maximum: ", max, "Average: ", average)

############END OF PROGRAM############

main()  #calling main function to begin program
