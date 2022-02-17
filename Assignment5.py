# Assignment #5 CSC 217-470
# Programmer: Rebecca Sieber
# Date Created: 7/17/2021
# Date of Final Update: 7/20/2021
#
############PROGRAM OVERVIEW############
# To demonstrate use of sorts and searches in a Python environment. 
# Create a structured program, with a Menu,
# which allows the user to execute the following
# programs, found in your text:
#
# P12.10- Implement the radix sort algorithm described in Exercise •• R12.20
# to sort lists of numbers between 0 and 999.
#
# P12.11- Implement the radix sort algorithm described in Exercise •• R12.20
# to sort lists of numbers between 0 and 999. However, use a single auxiliary
# list, not ten.
#
# P12.11- Implement the radix sort algorithm described in Exercise •• R12.20
# to sort lists of numbers between 0 and 999. However, use a single auxiliary
# list, not ten.
#
# P12.15- Consider the binary search algorithm from Section 12.6.2. If no match
# is found, the binarySearch function returns –1. Modify the function so that
# if target is not found, the function returns –k – 1, where k is the position
# before which the element should be inserted.
#
############LIBRARIES############
# from random import randint - used to create a list of random integers from 0-999
# from time import time- used to calculate how long a function took to run
#
############MAIN PROGRAM############
# The main program is interactive with the user. It will :
# 1) Allow the user to make a list of as many random numbers as the user would like
# 2) Allow the user to sort the list using a radix sort, a radix sort with only 1 aux
#    list, or use a merge sort. It will also allow the user to do a binary search of the
#    list for whatever value they chose
# 3) After each sort/search the time elapsed will print to the screen
# 4) Allow the user to start over as many times as they wish


def main():
     from random import randint
     from time import time
     from itertools import chain
     
     ### VARIABLES ###
     playAgain = "yes" #Default to get loop to start

     # Starting loop to allow user to "play" for as long as they want
     while playAgain.upper() == "YES" or playAgain.upper() == "Y":

          # Creating empty list, requesting how many random numbers user wants to add to list
          someList = []
          numberOfValues = int(input("Welcome to the random list sorter and searcher! \nHow many random integers would you like to sort? \nN = "))

          #Adding random nubers up 1-999 into list
          for i in range(numberOfValues) :
               someList.append(randint(1, 1000))   

          print("Here are your random integers:", someList)

          #Starting loop to validate user input. Requesting user to choose between 4 options and input "1", "2", "3", or "4"
          while True:
               sortChoice = input("\nHow would you like to sort/search your list?\
                                   \n1-Radix sort\
                                   \n2-Radix sort with single auxiliary\
                                   \n3-Merge sort without recursion\
                                   \n4-Binary search\
                                   \n\nPlease enter 1, 2, 3, or 4: ")
               
               # If user correctly inputs "1", "2", "3", or "4", breaking out of validation loop
               if sortChoice == "1" or sortChoice == "2" or sortChoice == "3" or sortChoice == "4" :
                    break

               # Else User did not input correct value- printing error message and going back to top of loop
               else:
                    print("ERROR: please enter either 1, 2, 3, or 4")
                    continue

          #User chooses radix sort:
          if sortChoice == "1":
               
               startTime = time()                                                    # Calculating start time
               RadixSort(someList)                                                   # Calling function to sort and print list
               endTime = time()                                                      # Calculating end time
               print("Elapsed time: %.9f seconds" % (endTime - startTime))           # Printing elapsed time

          #User chooses radix single aux sort:
          if sortChoice == "2":
               startTime = time()                                                    # Calculating start time
               RadixSortSingleAux(someList)                                          # Calling function to sort and print list
               endTime = time()                                                      # Calculating end time
               print("Elapsed time: %.9f seconds" % (endTime - startTime))           # Printing elapsed time

          #User chooses merger sort:     
          if sortChoice == "3":
               startTime = time()                                                    # Calculating start time
               MergeSort(someList)                                                   # Calling function to sort and print list
               endTime = time()                                                      # Calculating end time
               print("Elapsed time: %.9f seconds" % (endTime - startTime))           # Printing elapsed time

          if sortChoice == "4":
               selectionSort(someList)                                               # binary searches REQUIRE a sorted list, so sorting list
               print("Here is your list sorted:",  someList)                         # Printing sorted list to user
               searchNum = int(input("What integer would you like to search for? ")) # Requesting number to find in list
               startTime = time()                                                    # Calculating start time
               index = binarySearch(someList, 0, len(someList)-1, searchNum)         # Calling binary search function
               endTime = time()                                                      # Calculating end time

               if index < 0:                                                              # If binary search returns negative, number, then number was not found
                    print("Not found. It should have been at index", ((index*(-1)+1)))    # Printing index where number should have been
               else: print("Found at index", index)                                       # Number was found, printing index where it was found

               print("Elapsed time: %.9f seconds" % (endTime - startTime))                # Printing elapsed time


          playAgain = input("Would you like to play again? Y/N: " )                  #Asking user if they want to "play" again and if they say "yes" or "y", looping back to top
     
     exit()                                                                          # Terminating program succssfully 


########################################################################################################################
# FUNCTION: P12.10- Implement the radix sort algorithm described in Exercise •• R12.20
# to sort lists of numbers between 0 and 999.
# R12.20- The radix sort algorithm sorts a list of n integers with d digits, using ten
# auxiliary lists. First place each value v into the auxiliary list whose index
# corresponds to the last digit of v. Then move all values back into the original
# list, preserving their order. Repeat the process, now using the next-to-last
# (tens) digit, then the hundreds digit, and so on.

def RadixSort(someList):
     from itertools import chain                  # Using chain to merge auxillary lists back into original list
     
     if len(someList) == 0:                       # If the list is empty
          print("Cannot sort an empty list.")     # Printing message and terminating function
          return 0
     
     #Declaring empty auxillary lists
     auxList0 = []
     auxList1 = []
     auxList2 = []
     auxList3 = []
     auxList4 = []
     auxList5 = []
     auxList6 = []
     auxList7 = []
     auxList8 = []
     auxList9 = []

     #Looking at least significant (last) digit and placing it in corresponding aux list       
     for x in someList:
          if x%10 == 0:
               auxList0.append(x)
          elif x%10 == 1:
               auxList1.append(x)
          elif x%10 == 2:
               auxList2.append(x)
          elif x%10 == 3:
               auxList3.append(x)
          elif x%10 == 4:
               auxList4.append(x)
          elif x%10 == 5:
               auxList5.append(x)
          elif x%10 == 6:
               auxList6.append(x)
          elif x%10 == 7:
               auxList7.append(x)
          elif x%10 == 8:
               auxList8.append(x)
          elif x%10 == 9:
               auxList9.append(x)

     # Merging auxillary lists back into the original list
     someList = list(chain(auxList0, auxList1, auxList2, auxList3, auxList4, auxList5, auxList6, auxList7, auxList8, auxList9))

     # Emptying auxillary lists
     auxList0.clear()
     auxList1.clear()
     auxList2.clear()
     auxList3.clear()
     auxList4.clear()
     auxList5.clear()
     auxList6.clear()
     auxList7.clear()
     auxList8.clear()
     auxList9.clear()

     # Looking at next (second to last) digit. Placing it in corresponding auxillary list
     for x in someList:
          if ((x%100)//10) == 0:
               auxList0.append(x)
          elif ((x%100)//10) == 1:
               auxList1.append(x)
          elif ((x%100)//10) == 2:
               auxList2.append(x)
          elif ((x%100)//10) == 3:
               auxList3.append(x)
          elif ((x%100)//10) == 4:
               auxList4.append(x)
          elif ((x%100)//10) == 5:
               auxList5.append(x)
          elif ((x%100)//10) == 6:
               auxList6.append(x)
          elif ((x%100)//10) == 7:
               auxList7.append(x)
          elif ((x%100)//10) == 8:
               auxList8.append(x)
          elif ((x%100)//10) == 9:
               auxList9.append(x)

     # Merging aux lists back into original list
     someList = list(chain(auxList0, auxList1, auxList2, auxList3, auxList4, auxList5, auxList6, auxList7, auxList8, auxList9))

     # Emptying auxillary lists
     auxList0.clear()
     auxList1.clear()
     auxList2.clear()
     auxList3.clear()
     auxList4.clear()
     auxList5.clear()
     auxList6.clear()
     auxList7.clear()
     auxList8.clear()
     auxList9.clear()
    
     # Looking at first digit and placing it in corresponding aux list
     for x in someList:
          if ((x%1000)//100) == 0:
               auxList0.append(x)
          elif ((x%1000)//100) == 1:
               auxList1.append(x)
          elif ((x%1000)//100) == 2:
               auxList2.append(x)
          elif ((x%1000)//100) == 3:
               auxList3.append(x)
          elif ((x%1000)//100) == 4:
               auxList4.append(x)
          elif ((x%1000)//100) == 5:
               auxList5.append(x)
          elif ((x%1000)//100) == 6:
               auxList6.append(x)
          elif ((x%1000)//100) == 7:
               auxList7.append(x)
          elif ((x%1000)//100) == 8:
               auxList8.append(x)
          elif ((x%1000)//100) == 9:
               auxList9.append(x)

     # Merging aux lists back into original list
     someList = list(chain(auxList0, auxList1, auxList2, auxList3, auxList4, auxList5, auxList6, auxList7, auxList8, auxList9))
    
     print("Here is your sorted list:", someList)
     
########################################################################################################################
# FUNCTION: P12.11- Implement the radix sort algorithm described in Exercise •• R12.20
# to sort lists of numbers between 0 and 999. However, use a single auxiliary
# list, not ten.

def RadixSortSingleAux(someList):
     if len(someList) == 0:                  # If the list is empty, returning message and terminating function
          print("Cannot sort an empty list.")
          return 0

     # Declaring auxillary list
     auxList = []

     # Finding all items in the list with last number of 0, adding them to the aux list, then looking for
     # all items with last number 1 and adding them to the aux list...until all finally adding all with last number 9
     for x in range (0,10):
          for y in someList:
               if y%10 == x:
                    auxList.append(y)

     # Merging auxillary list back into the original list
     someList = list(auxList)
    
     # Emptying auxillary list
     auxList.clear()

     # Finding all items in the list with middle number of 0, adding them to the aux list, then looking for
     # all items with middle number 1 and adding them to the aux list...until all finally adding all with midding numer 9
     for x in range (0,10):
          for y in someList:
               if ((y%100)//10) == x:
                    auxList.append(y)

     # Merging aux list back into original list
     someList = list(auxList)

     # Emptying auxillary list
     auxList.clear()

 
     # Finding all items in the list that start with 0, adding them to the aux list, then looking for
     # all items that start with 1 and adding them to the aux list...until finally adding all with first numer 9
     for x in range (0,10):
          for y in someList:
               if ((y%1000)//100) == x:
                    auxList.append(y)
                                
     # Merging aux list back into original list
     someList = list(auxList)

     print("Here is your sorted list:", someList)

########################################################################################################################
# FUNCTION: P12.17- Implement the merge sort algorithm without recursion, where the
# length of the list is an arbitrary number. Keep merging adjacent regions
# whose size is a power of 2, and pay special attention to the last area
# whose size is less.

def MergeSort(someList):

     # If list is empty, printing error message and returning to main
     if len(someList) == 0:
          print("Cannot sort an empty list.")
          return 0

     midpoint = len(someList)//2                       # Finding middle of list
    
     subList1 = someList[0:midpoint]                   # Creating first sublist of 1st half of values
     selectionSort(subList1)                           # Using selection sort to sort first half
     subList2 = someList[midpoint: len(someList)]      # Creating first sublist of 2nd half of values
     selectionSort(subList2)                           # Using selection sort to sort second half 
    
     list1Index = 0                                    # intializing value to use as counter in loop below
     list2Index = 0                                    # intializing value to use as counter in loop below
     someListIndex = 0                                 #intializing value to use as counter in loop below

     while list1Index < len(subList1) and list2Index < len(subList2):

          # If next item of list 1 is less than next list 2, add it to main list and increase list 1 and main list counters
          if subList1[list1Index] <= subList2[list2Index]:
               someList[someListIndex] = subList1[list1Index]
               list1Index = list1Index + 1
               someListIndex = someListIndex + 1

          # else next item of list 2 is less than next list 1, add it to main list and increase list 2 and main list counters
          else:
               someList[someListIndex] = subList2[list2Index]
               list2Index = list2Index + 1
               someListIndex = someListIndex + 1
     
     # If list1 gets emptied, filling the main list with the rest of the contents of list2 and increase counters
     if list1Index == len(subList1):
          while list2Index < len(subList2):
               someList[someListIndex] = subList2[list2Index]
               list2Index = list2Index + 1
               someListIndex = someListIndex + 1

     # If list2 gets emptied, filling the main list with the rest of the contents of list1 and increase counters
     if list2Index == len(subList2):
          while list1Index < len(subList1):
               someList[someListIndex] = subList1[list1Index]
               list1Index = list1Index + 1
               someListIndex = someListIndex + 1
        
     print("Here is your sorted list:", someList)

########################################################################################################################
# FUNCTIONS:
# P12.15- Consider the binary search algorithm from Section 12.6.2. If no match
# is found, the binarySearch function returns –1. Modify the function so that
# if target is not found, the function returns –k – 1, where k is the position
# before which the element should be inserted.
#

def binarySearch(values, low, high, target) :
     mid = (low + high) // 2                                          # Calculating middle of list to use as search
     if low <= high :
          #mid = (low + high) // 2
      
          if values[mid] == target :                                  # If guess is the same as list value, return index
               return mid
          elif values[mid] < target :                                 # If guess is greater than list value, search again
               return binarySearch(values, mid + 1, high, target)
          else :                                                      # Guess is less than list value, search again
               return binarySearch(values, low, mid - 1, target)
         
     else :
          return mid*(-1)                                             #If guess does not exist in list, returning index where it should have been


###################################################################################
#THE FOLLOWING CODE WAS TAKEN FROM THE TEXT BOOK FOR USE WITH IN THE PROGRAM
def selectionSort(values) :
   for i in range(len(values)) :
      minPos = minimumPosition(values, i)
      temp = values[minPos]  # swap the two elements
      values[minPos] = values[i]
      values[i] = temp

## Finds the smallest element in a tail range of the list.
#  @param values the list to sort
#  @param start the first position in values to compare
#  @return the position of the smallest element in the
#  range values[start] . . . values[len(values) - 1]
#
def minimumPosition(values, start) :
   minPos = start
   for i in range(start + 1, len(values)) :
      if values[i] < values[minPos] :
         minPos = i
         
   return minPos

###################################################################################
main()
