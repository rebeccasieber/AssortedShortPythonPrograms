
#***************************************************
#PROGRAM NAME:          SieberRebecca_WeekFourHomework.PY
#PROGRAMMER:            SIEBER
#DATE OF PROGRAM: 	6/26/20
#PURPOSE:     		A PROGRAM THAT WILL TAKE USER INPUT AND CALCULATE
#                       THE BALANCE OF A BANK ACCOUNT AFTER CERTAIN TIME FRAME
#                       WHEN INTEREST COMPOUNDED YEARLY
#MODULES USED:          NONE
#INPUT VARIABLE(S):     interestRate (INTEREST RATE GIVEN BY BANK)
#                       ogBalance   (INITIAL ACCOUNT BALANCE)
#                       balanceTerm (HOW LONG BALANCE ACCRUES INTEREST)
#OUTPUT:                totalReturnBalance (TOTAL ENDING ACCOUNT BALANCE)           
#
#*******************************************************

def main():
    
    #running program test to make sure that any changes to the code do not
    #affect the program logic/core formulas. 

    programTest()

    #Starting loop that is dependant on user inputting valid info (numbers)
    #if they do not enter valid input they will be forced to try input again

    while True:

        #requesting user input

        interestRate = input("What is the interest rate at your bank? ")
        ogBalance = input("How much money are you Depositing? $")
        balanceTerm = input("How many years will you leave your money in the bank? " )

        #running user input validation function and breaking loop if input is
        #valid, or forcing user to reinput if input is invalid

        if inputValidation(interestRate, balanceTerm, ogBalance) == True:
            break

        elif inputValidation(interestRate, balanceTerm, ogBalance) == False:
            print("Please try again. Note all input values must be a NUMBER.")
            print()
            continue
        
    #Converting user input to floats now becuase I couldnt do it when they were
    #inputted in order to properly validate them.
        
    floatinterestRate = float(interestRate)
    floatbalanceTerm = float(balanceTerm)
    floatogBalance = float(ogBalance)

    #Calculating account balance given user input using compoundYearly function
    #as defined below
    #also rounding answer to 2 decimal places since its money
    
    totalReturnBalance = round(compoundYearly(floatinterestRate, floatbalanceTerm, floatogBalance),2)

    #printing results to user
    print("After ", balanceTerm, "years your total balance will be $",\
        totalReturnBalance, "at an interest rate of ", interestRate, "%")
        

##Function to calculate ending balance when account compounded yearly
#@ param    interest rate that accrues, how long the in initial balance is
#           acruing interest, and the starting/initial balance of the account
#@return    the ending balance of the account
#

def compoundYearly(interest, years, principle):
    import math
    totalBalance = principle * (pow((1+interest/100),years))
    return totalBalance

##Validates user input to confirm user input is anumber
#@ param    three values provided by the user
#@return    true if user input is all float values or false if not all float values
#

def inputValidation(interest, term, balance):

    try:
        float(interest) and float(term) and float(balance)
        return True

    except ValueError:
        return False


##tests main function with known true values to confirm logic is correct
#@ param    none
#@return    if test fails, returns message of failure, and terminates program
#    
def programTest():
    if compoundYearly(3.5, 5, 100) != 118.76863056468746:
        print("I'm sorry- there has been a logic error in this program.")
        exit()
        
#running program
main()




