#***************************************************
#PROGRAM NAME:          SieberRebecca_Week8Homework.PY
#PROGRAMMER:            SIEBER
#DATE OF PROGRAM: 	7/26/20
#PURPOSE:     		A PROGRAM THAT WILL RECORD A GROCERY
#                       LIST, REORDER THE LIST INTO DEPARTMENTS
#                       WHERE THE FOODS ARE FOUND AND ESTIMATE
#                       THE TOTAL COST OF THE LIST
#MODULES USED:          NONE
#INPUT VARIABLE(S):     groceryList = list of grocery items
#OUTPUT:                sortedGroceryList, totalCost    
#
#*******************************************************

#dictionary containing 49 top foods purchased (by me) at the grocery store
acceptedList = {"dairy":['eggs', 'milk', 'cream', 'cheese', 'cream cheese', 'yogurt', 'butter'],\
                "bakery":['bread', 'bagles', 'donuts', 'cookies', 'cake', 'pie', 'muffins'],\
                "fruit":['apples', 'bananas', 'grapes', 'strawberries', 'oranges', 'blueberries',\
                        'avocado'],\
                "vegtables": ['lettuce', 'potatoes', 'spinach', 'broccoli', 'peas',\
                            'carrots', 'cucumber'],\
                "meat":['chicken', 'pork', 'beef', 'shrimp', 'salmon', 'bacon', 'turkey'],\
                "dry-goods": ['pasta', 'rice', 'flour', 'sugar',\
                            'cereal', 'oil', 'vinegar'],\
                "frozen": ['pizza', 'waffles', 'ice cream', 'popsicles', 'chicken nuggets',\
                             'french fries', 'burgers']}
def main():

    #Printing hello message/instructions

    print("Welcome to this grocery program. This program will help you\n\
    make your grocery shopping as efficient as possible by sorting\n\
    your shopping list based on the department of the store that your\n\
    items are located! It will also give you an estimate as to how much\n\
    your trip will cost!\n\n")

    #printing optional list of grocery items to choose fr
    printOptions = input("Would you like to see a list of acceptable grocery items? Y/N ")

    if printOptions == "Y" or printOptions == "y":
        printList(acceptedList)

    #accepting list of any size from user       
    print("\nPlease enter the name of the item you would like to purchase\n\
followed by the <ENTER> key. When you are done type <Q>")

    #declaring variables
    groceryList = []
    groceryItem = 0

    #creating loop to determin when user is done entering info
    while groceryItem != "Q":

        groceryItem = input()

        #verifying that data inputted by the user is a valid selection
        #and forcing them to retry if not a valid item
        if groceryValidation(groceryItem) == True:
            groceryList.append(groceryItem)

        elif groceryValidation(groceryItem) == False:
            if groceryItem == "Q":
                print()
            else:
                print("That grocery item was not recognized. Please try again.")
            
    #printing shopping list back to user (FOR TESTING PURPOSES ONLY
    ##print(groceryList)
    ##print()

    #printing sorted grocery list to user
    print("Here is your sorted shopping list:\n")
    listsorter(groceryList)

    #Calculating total cost based on estimated costs for food items
    totalCost = 0
    for i in range(len(groceryList)):
        totalCost = totalCost + price(groceryList[i])

    #printing estimated total cost to user    
    print("\nYour estimated total cost is: $", totalCost)
    

##prints dictionary of acceptable valuse based on department
#@ param dictionary of acceptable values
#@return printed and sorted dictionary
#

def printList(acceptedList):

    print("\nDAIRY")
    for item in acceptedList['dairy']:
        print (item)

    print("\nBAKERY")
    for item in acceptedList['bakery']:
        print (item)

    print("\nFRUIT")
    for item in acceptedList['fruit']:
        print (item)

    print("\nVEGTABLES")
    for item in acceptedList['vegtables']:
        print (item)

    print("\nMEAT")
    for item in acceptedList['meat']:
        print (item)

    print("\nDRYGOODS")
    for item in acceptedList['dry-goods']:
        print (item)

    print("\nFROZEN")
    for item in acceptedList['frozen']:
        print (item)

##Validates user input by comparing user input to a dictionary of acceptable values
#@ param foods = input from user
#@return true if input matches acceptable value, and false if no match
#
def groceryValidation(food):
    if food in acceptedList['dairy'] or food in acceptedList['bakery']\
    or food in acceptedList['fruit'] or food in acceptedList['vegtables']\
    or food in acceptedList['meat'] or food in acceptedList['dry-goods']\
    or food in acceptedList['frozen']:
        return True
    else:
        return False

##Sorts foods by grocery department and prints sorted list
#@ param foods = input from user
#@return sorted list of foods inputted from user
#
def listsorter(foods):

    print("\nDAIRY: ")
    for i in range(len(foods)):
        if foods[i] in acceptedList['dairy']:
            print (foods[i])

    print("\nBAKERY:")
    for i in range(len(foods)):
        if foods[i] in acceptedList['bakery']:
            print (foods[i])

    print("\nFRUIT:")
    for i in range(len(foods)):
        if foods[i] in acceptedList['fruit']:
            print (foods[i])
            
    print("\nVEGTABLES:")
    for i in range(len(foods)):
        if foods[i] in acceptedList['vegtables']:
            print (foods[i])

    print("\nMEAT:")
    for i in range(len(foods)):
        if foods[i] in acceptedList['meat']:
            print (foods[i])

    print("\nDRY GOODS:")
    for i in range(len(foods)):
        if foods[i] in acceptedList['dry-goods']:
            print (foods[i])

    print("\nFROZEN:")
    for i in range(len(foods)):
        if foods[i] in acceptedList['frozen']:
            print (foods[i])

 ##Computes cost of items by using dictionary to match food names with ave cost
#@ param (describe parameters)
#@return (describe what function returns)
#           
def price(food):

    priceList = {'eggs': 1.89, 'milk': 2.35, 'cream': 4.99, 'cheese': 4.99,\
    'cream cheese': 1.99, 'butter': 4.99, 'yogurt': 2.99, 'bread': 1.99,\
    'bagles': 2.99, 'donuts': 2.99, 'cookies': 5.99, 'cake': 19.99,\
    'muffins': 4.99, 'pie': 7.99, 'apples': 1.99, 'bananas': 0.39, \
    'grapes': 1.29, 'strawberries': 2.5, 'oranges': 0.4,\
    'blueberries': 4.99, 'avocado': 0.99, 'lettuce': 0.29, \
    'potatoes': 0.29, 'spinach': 1.99, 'broccoli': 1.65,\
    'peas': 1.88, 'carrots': 1.99, 'cucumber': 0.5, 'chicken': 2.99,\
    'pork': 2.99, 'beef': 5.99, 'shrimp': 12.99, 'turkey': 3.99, 'salmon': 10.99,\
    'bacon': 6.99, 'pasta': 1, 'rice': 2.99, 'flour': 1.99, 'sugar': 1.99,\
    'jelly': 2.99, 'oil': 4.99, 'vinegar': 2.99, 'pizza': 6.99, 'waffles': 2.99,\
    'ice cream': 2.99, 'popsicles': 3.99, 'chicken nuggets': 4.99,\
    'french fries': 1.99, 'burgers': 9.99}

    return priceList[food]



main()
