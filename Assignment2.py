# Assingment #2 CSC 217-470
# Programmer: Rebecca Sieber
# Date Created: 6/28/2021
# Date of Final Update: 7/2/2021

############PROGRAM OVERVIEW############
# This program is interactive and demonstrates 2 original
# classes.
#
# Class 1 is for a customer loyalty discount program
# it allows the user to make unlimited "purchases" and when 
# the customer hits $200 or more in purchases they qualify for 
# 10% off thier next order. The class stores customer objects and keeps
# track of how much the customer has spent and any future discounts.
#
# Class 2 is an email generator. It allows the user to input  sender and
# recipient email addresses, an email body, and a signature line. It also
# allows for the body of the message to be appended infinitely. The class
# contains email objects with data inputted by user.
#
# For readability both of the classes have been written/stored below
# and not in separate files.
#
############LIBRARIES############
# No libraries outside of the standard library were used in this program.
#
#
############MAIN PROGRAM############
# The main program calls on objects for both of the required classes
# and allows user to test all the classes/functions in an 
# interactive manner

def main():

    ###DEMONSTRATING CLASS 1- CUSTOMER LOYALTY###
    payAgain = "Y"                              #Setting default to enter loop below allowing user to make unlimited "purchases"
    purchaseAmount = 0.0                        #Amount of each purchase made by user
    customer = customerLoyalty()                #Creating new customerLoyalty object    

    print("Welcome to Blue Sky Corporation!")

    #Getting/Setting object Name 
    name = input("\nPlease enter the name to be associated with your NEW Customer Loyalty account\n")
    customer.setUserName(name)

    #Getting/Setting object Email   
    email = input("\nPlease enter the email address associated with your Customer Loyalty account\n")
    customer.setUserEmail(email)

    purchaseAmount = float(input("\nHow much was your total purchase today? $" ))
    customer.sellPurchase(purchaseAmount)

    #calculating if user gets future discount based on above purchase
    futureDiscount = customer.totalDiscount()

    #Printing message displaying status of future discount for user.
    if futureDiscount == 0.10:
        print("Congrats! You earned a 10% discount for your next purchase!")
    else:
        print("Keep spending to earn future discounts! For every $200 spent you get 10% off your next order!")

    #Starting loop to allow user to make unlimited purchases and decide when to stop making purchases
    while True: 

        payAgain = input("\nWould you like to make another purchase? y or n: ")

        #Determining if loop should be broken or not based on provided input. Breaking loop if user types "N", "n", "NO" or "no"
        if payAgain.upper() == "N" or payAgain.upper() == "NO" :
            break

        #Requesting next purchase amount
        purchaseAmount = float(input("How much was your total purchase today? $" ))

        #if customer qualified for discount based on previous purchases, calculating and saving modified purchase total and printing data to screen. 
        if customer.totalDiscount() == 0.10:
            purchaseAmount = purchaseAmount * 0.90
            formated_float = "{:.2f}".format(purchaseAmount)                  #forcing amount to be shown with exactly 2 decimal places since its money
            print("Congrats! You earned 10% off last time you shopped, making your new total $", formated_float)

            #resetting discount to zero since it was just used
            customer.resetTotalDiscount()

        #If customer did not qualify for %10 off, updating purchase amount calulator for future discounts and calculating any future discounts
        else:
            customer.sellPurchase(purchaseAmount)
            futureDiscount = customer.totalDiscount() 

            #Printing whether or not there is a discount on the next purchase
            if futureDiscount == 0.10:
                print("Congrats! You earned a 10% discount for your next purchase!")

            else:
                print("Keep spending to earn future discounts! For every $200 spent you get 10% off your next order!")


    #user has indicated they are done shopping- terminating loop and printing goodbye message
    print("Thank you for shopping with us- please come again!\n\n")
    #exit

    ###DEMONSTRATING CLASS 2- EMAIL GENERATOR###
    print("Welcome to the Email Generator!")
    
    myEmail = emailCreator()                    #Creating new email object
    myEmail.promptEmailCreation()               #calling function to prompt/set input values

    print("Here is your email: ")
    myEmail.printEmail()                        #printing email to screen 

    # APPEND: allowing user to append unlimited lines to the body of the message
    while True:
        appendYorN = input("\nWould you like to add anything else to the end of the email? Y or N: ")
        if appendYorN.upper() == "Y" or appendYorN.upper() == "YES":
            addOnLine = input("Line to append: ")
            myEmail.append(addOnLine)
            continue
        else:
            print("Thank You. Your email has been sent. ")
            break

    exit                                       #Terminating program successfully   
########################################################################################################################
#CLASS 1: customer loyalty marketing campaign.
#After accumulating $200 in purchases, each customer will receive
#a ten percent discount on their next purchase. This class contains
#data surrounding customers total purchases and applicable discounts

class customerLoyalty:
    def __init__(self) :
        self._userName = ""                 #To be provided by customer/user
        self._userEmail = ""                #To be provided by customer/user
        self._purchaseTotal = 0.0           #Keeps track of purchase amounts to calculate future discounts
        self._discount = 0.0                #Will either be 0 or 0.10 depending on how much money the customer has "spent"

    ### GETTERS AND SETTERS- for user inputted private data members###
    def getUserName(self) :
        return self._userName
 
    def setUserName(self, newName) :
        self._userName = newName

    def getUserEmail(self) :
        return self._userEmail
 
    def setUserEmail(self, newEmail) :
        self._userEmail = newEmail

    ###PUBLIC METHODS###
        
    #This function calcutes whether a discount should be applied to the customers purchase
    #based on past purchase history    
    def totalDiscount(self):
        if self._purchaseTotal >= 200:      #If customer spends at least $200, they get 10% off their next purchase
            self._discount = 0.10           #Setting discount to represent 10% off
            self._purchaseTotal = 0         #starting back at zero after discount applied

        return self._discount
    
    #This function adds sales amounts together into a total, and saves
    #that total for future reference
    def sellPurchase(self, amount):
        self._purchaseTotal = self._purchaseTotal + amount

    #This function resets the totalDiscount back to zero once discount has been used.
    def resetTotalDiscount(self):
        self._discount = 0
        
##########################################################################################################################
#CLASS 2: Email generator.
# this class contains email objects with data inputted by user.
# It allows the user to input  sender and
# recipient email addresses, an email body, and a signature line. It also
# allows for the body of the message to be appended infinitely. 
        
class emailCreator:
    def __init__(self) :
        self._senderAddress = ""        #Sender Address (PRIVATE)- To be inputted by user
        self._recipientAddress = ""     #Recipient Address (PRIVATE)- To be inputted by user
        self._bodyOfMessage = ""        #Body of email (PRIVATE)- To be inputted by user and appended as needed
        self._signatureLine = ""        #Signature line (PRIVATE)- To be inputted by user
        self._wholeEmail = ""           #Whole Email  (PRIVATE)- all four above strings combined into one whole string         
        self._addOnLine = ""            #Appended Line (PRIVATE)- holds any line user chooses to append into body of email
        
    ### GETTERS AND SETTERS- for user inputted private data members###
    def getSenderAddress(self) :
        return self._senderAddress
 
    def setSenderAddress(self, address) :
        self._senderAddress  = address

    def getRecipientAddress(self) :
        return self._recipientAddress
 
    def setRecipientAddress(self, address) :
        self._recipientAddress = address

    def getBodyOfMessage(self) :
        return self._bodyOfMessage
 
    def setBodyOfMessage(self, message) :
        self._bodyOfMessage = message

    def getSignatureLine(self) :
        return self._signatureLine
 
    def setSignatureLine(self, signature) :
        self._signatureLine = signature

    ###PRIVATE METHODS###

    #This function creates 1 string that combines all four strings inputted by user
    #and formats it to appear like an email.
    def _emailToString(self):
        self._wholeEmail =("        From: " + self._senderAddress
        + """
        To:   """ + self._recipientAddress
        + """

        """ + self._bodyOfMessage
        + """

        """ + """Sincerely,
        """ + self._signatureLine)

    ###PUBLIC METHODS###

    #This method walks user through inputting all 4 required strings and sets private data members.
    #It also calls the private function that compiles all of the inputted strings into one string
    def promptEmailCreation(self):

        ###Getting and setting Sender Email###
        sAddress = input("Sender email address: ")
        self.setSenderAddress(sAddress)

        ###Getting and setting Recipient Email###
        rAddress = input("Recipient email address: ")
        self.setRecipientAddress(rAddress)

        ###Getting and setting Email body###
        message = input("Message: ")
        self.setBodyOfMessage(message)

        ###Getting and setting signature line###
        signature = input("Signature: ")
        self.setSignatureLine(signature)

        self._emailToString()               #Calling private method to compile email into 1 long string
                          
    #This method prints the email (as one string) to the console for user review                  
    def printEmail(self):
        print("")                           #Printing newline for readability
        print(self._wholeEmail)             #Printing email as 1 string
        print("")                           #Printing newline for readability

    
    #This method allows user to append a line to the end of the body of the message
    #and automatically reprints the new/updated email to the user for review
    def append(self, lineToAppend):
        self._bodyOfMessage = self._bodyOfMessage + " " + lineToAppend      #Adding line to append to end of body and saving it as the updated body
        self._emailToString()                                               #Recompiling email into 1 string
        print("Here is your updated email: ")
        print(self._wholeEmail)                                             #Reprinting email for review
        

main()

