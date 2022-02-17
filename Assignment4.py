# Assignment #4 CSC 217-470
# Programmer: Rebecca Sieber
# Date Created: 7/10/2021
# Date of Final Update: 7/16/2021

############PROGRAM OVERVIEW############
# This program demonstrates the use of recursion with strings, lists, and math.
# This program will contain 6 functions that solve simple problems recursively
#
############LIBRARIES############
# No libraries outside of the standard library were used in this program.
#
#
############MAIN PROGRAM############
# The main program is interactive with the user. It will prompt the user
# for input and then use that input to solve 6 problems RECURSIVELY:
# 1) Count substrings with the same first and last characters
# 2) Find the length of a string using recursion
# 3) Print all possible combinations of r elements in a given list of size n
# 4) Find the minimum and maximum element of an array
# 5) Print a pattern without using any loop
# 6) Find the product of 2 numbers using Recursion

def main():

     ### VARIABLES ###
     inputArray = []               # Empty list to function as an array where the user will input
     number = 0                    # To be inputted by user- placed into an array (list)
     someString = ""               # To be inputted by user- to be evaluated for length and substrings
     numberOfElements = 0          # To be inputted by user- its the "r" in all possible combinations of r elements in a given list of size n
     character = '0'               # To be inputted by user- Character will be used to make a recursive pattern
     layers = 0                    # To be inputted by user- dictates how many layers will be included in the recursive pattern
     int1 = 0                      # To be inputted by user- one of the 2 integers used to find the product recursively
     int2 = 0                      # To be inputted by user- one of the 2 integers used to find the product recursively


     ### RECURSIVE STRING LENGTH ###
     someString = input("Enter a string: ")
     print("The length of ", someString, "is ", stringLength(someString), "\n\n")


     ### RECURSIVE SUBSTRING ###
     someString = someString.lower()                                  # Changing string to all lower case for comparison
     print("Substrings of your string that have the same first and last character: ")
     subStringFirstLast(someString)


     ### RECURSIVE MIN/MAX OF ARRAY ###
     print("\n\nPlease enter numbers pressing <enter> after each number and 'END' when you are done.")
     while True:                                                      # starting loop for user to input as many numbers as they want
          try:                                                        # Setting up try/except so the loop comntiues as long as the user inputs a float/int
               number = float(input("Number: "))                      # Accepting user input
               inputArray.append(number)                              # Adding number to array/list
               continue
          except:                                                     # when user enters any non-numerical input, loop terminates
               break

     print("The max of your numbers is: ", maxArray(inputArray))      # Calling max function and printing results
     print("The min of your numbers is: ", minArray(inputArray))      # Calling min function and printing results

     ### RECURSIVE COMBINATIONS OF R ELEMENTS ###
     print("\n\nNow I will find all of the possible combinations a certain number elements from the list of integers you just provided." )
     numberOfElements = int(input("Number of elements: "))            # Getting r = number of elements in each combination
     for x in allPossibleCombos(inputArray, numberOfElements):        # Calling function and printing out combinations one at a time on newlines
          print (x)
          
     ### RECURSIVE PATTERN PRINTING ###
     print("\n\nPlease enter a character and an integer to create your own unique hourglass pattern.")
     character = input("Character: ")                                 # Obtaining character to make pattern out of
     layers = int(input("Integer: "))                                 # Obtaining # of layers of the pattern
         
     patternPrint(character, layers)                                  # Calling function to print pattern based on inputted data

     ### RECURSIVE PRODUCT OF 2 INTEGERS ###
     int1 = int(input("\n\nPlease enter 2 integers below, and I will find the product recursively.\nInteger 1: "))
     int2 = int(input("Integer 2: "))

     productOf2Nums(int1, int2)                                       # Calling function to print product of the two integers provided

     print("The end- I hope you enjoyed!")                            # Printing goodbye message
     exit()                                                           # Terminating program succssfully 


########################################################################################################################
# FUNCTION: Recursive solution to count substrings with the same first and last characters
def subStringFirstLast(someString, indexCounter=0, substrCounter = 0, lengthCounter=1 ):

    if indexCounter == len(someString)-1:                             # BASE CASE: when it reaches last letter in string
        return print("There are", substrCounter, "total.")            # Printing number of substrings with the same first and last number
    
    while lengthCounter <= (len(someString)):                         # Creating loop to go thru the entire string
        if someString[indexCounter] == someString[lengthCounter-1]:   # If the string has the same first and last letter
            if len(someString[indexCounter : lengthCounter]) > 1:     # If the substring contains more than one character
                print(someString[indexCounter : lengthCounter])       # Print the substring
                substrCounter = substrCounter + 1                     # Increase substring counter
        lengthCounter = lengthCounter + 1                             # Increasing length counter

    subStringFirstLast(someString, indexCounter + 1, substrCounter)   # recursive function call- updating index counter

     
########################################################################################################################
# FUNCTION: Program for length of a string using recursion
def stringLength(someString):

     if someString == "":                                             # If string is empty, return 0
          return 0
     else:                                                            # if string is not empty
          return 1 + stringLength(someString[1:])                     # adding one and moving to next character- RECURSIVE CALL


########################################################################################################################
# FUNCTION: Print all possible combinations of r elements in a given list of size n
#def allPossibleCombos(r, someList[n]):
          
def allPossibleCombos(someList, numElements, previousList=[]):                            # Inclused previousList to hold each combination
     if len(previousList) == numElements:                                                 # If the number of elements in each combination is the same as the number of elements in the list, there is only one possible combo. Return the list.
          return [previousList]    
     returnList = []                                                                      # emtpy list to hold all possible n combinations

     for i, value in enumerate(someList):                                                 # using enumerate() to create counter for for loop
          previousListPlus = previousList.copy()                                          # Making copy of last combo
          previousListPlus.append(value)                                                  # Appending new value to list
          returnList += allPossibleCombos(someList[i+1:], numElements, previousListPlus)  # Recursive call- since all combos with first element created, "deleting" first element and focusing only on the rest.
 
     return returnList

########################################################################################################################
# FUNCTIONS: ProgramS to find the minimum and maximum element of an array
def maxArray(someArray):

    if len(someArray) == 1:                     # If there is is only one item in the array, it must be the max
        return someArray[0]
    else:
        maxValue = maxArray(someArray[1:])      # Recursive call to check rest of the array 
        if maxValue > someArray[0]:             # If next element is larger than first, then it is the max
            return maxValue
        else:
            return someArray[0]                 # If nothing is larger than the first, then it is max

def minArray(someArray):

    if len(someArray) == 1:                     # If there is is only one item in the array, it must be the min
        return someArray[0]
    else:
        minValue = minArray(someArray[1:])      # Recursive call to check rest of the array
        if minValue < someArray[0]:             # If next element is larger than first, then it is the min
            return minValue
        else:
            return someArray[0]                 # If nothing is larger than the first, then it is min
          

########################################################################################################################
# FUNCTION: Print a hourglass pattern without using any loop
def patternPrint(characterToUse, numberOfLayers, counter = 1):


    if numberOfLayers == 0:                                           # BASE CASE 1- when you get to the bottom of the top part of hourglass
        printBottom(characterToUse, counter)                          # Calling fucntion to print bottom half of the hourglass
        return 0 

    else:
        print(" " * (counter), characterToUse * numberOfLayers*2)     # Printing spaces and characters
        patternPrint(characterToUse, numberOfLayers-1, counter+1)     # Recursive funcion call updating layer counter, character counter

def printBottom(characterToUse, counter, startValue = 2):             # Recursive Function for printing bottom of the hourglass
    if counter == 2:                                                  # BASE CASE 2- getting to the end of the bottom half
        return 0
    else:
        print(" " * (counter-2), characterToUse * startValue*2)       # Printing spaces and characters
        printBottom(characterToUse, counter-1, startValue+1)          # Recursive function call updating layer counter and start value counter
        
########################################################################################################################
# FUNCTION: Product of 2 numbers using Recursion. Using principal that multiplying is simply
# Adding int1 to itself int2 number of times.

def productOf2Nums(num1, num2, counter = 1):
    if num1 == 0 or num2 == 0:                                   # If either of the numbers is zero, the product will be zero
        print("The product is", 0)
        return 0
     
    if counter == num2:                                          # BASE CASE- counted up to the value of int2 
        print("The product is", int(num1))                       
        return 0
    else:
        productOf2Nums(num1 + (num1/counter), num2, counter+1)   # Adding num1 to itself, increasing counter
          

main()

