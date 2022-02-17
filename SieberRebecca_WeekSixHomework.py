#***************************************************
#PROGRAM NAME:          SieberRebecca_WeekSixHomework.PY
#PROGRAMMER:            SIEBER
#DATE OF PROGRAM: 	7/9/20
#PURPOSE:     		A PROGRAM THAT WILL CREATE A LIST OF 10
#                       RANDOM INTEGERS FROM 0-90, SORT THE LIST
#                       AND CREATE A MULTI-DIMENSIONAL TABLE
#MODULES USED:          RANDOM
#INPUT VARIABLE(S):     N/A
#OUTPUT:                randomList      
#
#*******************************************************

def main():
    
    randomList1 = randomListMaker()

    #printing randomList
    print("Here is a random list of 10 numbers from 0 to 90 ")
    print(randomList1)
    print()

    #sorting randomList in ascending order and printing it
    randomList1.sort()
    print("Here is the list sorted in acesnding order:")
    print(randomList1)
    print()

    #printing multidemensional table
    print("Here is a multidimensional table of 10 random list:")
    print()

    #Defining constants- how many lists used in table and how many
    #elements in each list
    RANDOMNUMBERS = 10
    RANDOMLIST = 10

    # Creating a list names for each random list (first column)
    randomLists = [ "Random List 1",
                  "Random List 2",
                  "Random List 3",
                  "Random List 4",
                  "Random List 5",
                  "Random List 6",
                  "Random List 7",
                  "Random List 8",
                  "Random List 9",
                  "Random List10"]
                  
    # Create a table of 10 random lists             
    randomTable = [ 
               randListSorted(),
               randListSorted(),
               randListSorted(),
               randListSorted(),
               randListSorted(),
               randListSorted(),
               randListSorted(),
               randListSorted(),
               randListSorted(),
               randListSorted()
             ]              

    # Printing the table header
    print("         Index Pos:""   0       1       2       3       4       5       6       7       8       9     Total of Random Number List")

    # Print column names, random numbers, and row totals.
    for i in range( RANDOMLIST) :
       print("%15s" % randomLists[i], end="")
       
       # Printing each row element and updating the row total.
       total = 0
       for j in range(RANDOMNUMBERS) : 
          print("%8d" % randomTable[i][j], end="")
          total = total + randomTable[i][j]
             
       # Displaying the row total and printing a new line.
       print("%8d" % total)



##Function creates list of 10 random numbers from 0-90
#@ param none
#@return list of 10 random numbers
#
def randomListMaker():

    import random

    #creating randomList and assigning a random sample of 10 numbers 0-90
    randomList = random.sample(range(0, 90), 10)
    return randomList

##Function creates list of 10 random numbers from 0-90 sorted low-high
#@ param none
#@return list of 10 random numbers sorted low-high
#
def randListSorted():

    import random

    #creating randomList and assigning a random sample of 10 numbers 0-90
    randomList = random.sample(range(0, 90), 10)
    randomList.sort()
    return randomList
main()
