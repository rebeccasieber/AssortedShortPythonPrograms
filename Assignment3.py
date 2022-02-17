# Assignment #3 CSC 217-470
# Programmer: Rebecca Sieber
# Date Created: 7/5/2021
# Date of Final Update: 7/9/2021

############PROGRAM OVERVIEW############
# This program demonstrates superclasses and subclasses. The super class
# is called "Appointments" and contains a description and date (month,
# day, and year) of an appointment as well as a few methods and abstract methods.
# There are three subclasses: First_time, Every_Day, and Monthly. These subclasses
# handle special appointment situations. The program is interactive and allows the 
# user to input and search appointments.
#
############LIBRARIES############
# No libraries outside of the standard library were used in this program.
#
#
############MAIN PROGRAM############
# The main program is interactive with the user. It saves appointments in a list
# as dictated by the user. The user can input unlimited appointments. It will then
# print the entire list of appointments to the user as well as print out appointments
# for any given/specific date. The program calls on 3 subclasses to operate.
#

def main():

    ### VARIABLES ###
    anotherAppt = "Y"       #Stop case for while loop seen below
    myAppointments = []     #empty list to hold appointment objects
    frequency = 0           #provided by user- frequency of appointment (once, everyday, or monthy) 
    month = 1               #provided by user- numerical month of date to search for appoinments
    day = 1                 #provided by user- numerical day of date to search for appoinments
    year = 1970             #provided by user- numerical year of date to search for appoinments
    
    print("Welcome to your calendar! Let's add an appointment.")

    # Starting loop to allow user to add as many appointments as needed
    while anotherAppt.upper() == "Y" or anotherAppt.upper() == "YES":

        # Starting loop to force user to input a correct value corresponding to appt frequency
        while True:  
            frequency = int(input("Is the appointment: \n 1 - Only once\n 2 - Daily \n 3 - Monthly \n "))         

            # If user does not input either a 1, 2, or 3 then print error message and rerequest
            if frequency != 1 and frequency != 2 and frequency != 3:
                print("Please enter either 1, 2, 3")
                continue

            #user entered either a 1, 3 or 3
            else: break 

        if frequency == 1:                              #IF USER CHOOSES 1- ONLY ONCE
            newAppointment = First_Time()               #Creating New object of superclass First_Time()
            newAppointment.setDate()                    #setting date according to subclass override
            newAppointment.setDescription()             #setting description according to superclass definition
            myAppointments.append(newAppointment)       #adding this appointment to list
       
        elif frequency == 2:                            #IF USER CHOOSES 2- DAILY 
            newAppointment = Every_Day()                #Creating New object of subclass Every_Day
            newAppointment.setDate()                    #setting date according to subclass override
            newAppointment.setDescription()             #setting description according to superclass definition
            myAppointments.append(newAppointment)       #adding this appointment to list
         
        elif frequency == 3:                            #IF USER CHOOSES 3- MONTHLY 
            newAppointment = Every_Month()              #Creating New object of subclass Every_Month
            newAppointment.setDate()                    #setting date according to subclass override
            newAppointment.setDescription()             #setting description according to superclass definition
            myAppointments.append(newAppointment)       #adding this appointment to list

        else:                                           #just in-case something goes wrong...
            print("There has been a logistical error in this program. Sorry for the inconvenience.")
            exit()
            
        #Prompting the user to see if loop should continue
        anotherAppt = input("Would you like to add another appointment? Y/N: ")

    #Printing appointments user inputted- from list
    print("\n\nYour appointments:")
    for x in myAppointments:
        x.printAppointment()
        
    #Allowing user to input a date and look up all appointments scheduled for that date
    print("\n\nThank you for setting up your calendar! Please type in a date to get all of the appointments scheduled for that day")

    #Loop to verify user input and confirm they enter a number and avoid crashing program
    while True:
        try:
            month = int(input("Month (MM): "))      #Obtaining month for date to search
            break
        except ValueError:
            print("Please enter a 2 digit number from 01 - 12")
            continue

    #Loop to verify user input and confirm they enter a number and avoid crashing program
    while True:
        try:
            day = int(input("Day (DD): "))          #Obtaining day for date to search
            break
        except ValueError:
            print("Please enter a 2 digit number from 01 - 31")
            continue

    #Loop to verify user input and confirm they enter a number and avoid crashing program
    while True:
        try:
            year = int(input("Year (YYYY): "))      #Obtaining year for date to search
            break
        except ValueError:
            print("Please enter a 4 digit number from 0000 - 9999")
            continue

    #Printing out appointments on day provided by user
    print("\nYour appointments on ", month, "/", day, "/", year)
    for x in myAppointments:                        #looping through list of appointments
        if x.occursOn(year, month, day) == True:
            print("\t", x.getDescription())         #printing description for appt
        #else:
            #print("NOT FOUND")                      
    
    exit                                            #Terminating program successfully   
########################################################################################################################
# SUPER CLASS: Appointment
# This class is the framework for the three subclasses. It defines that an appointment
# as a numerical month, numerical day, numerical year, and string description. it also
# provides getters/setters for all the private data members, and 2 abstract methods forcing
# subclasses to define getDate for proper formatting as well as an occuresOn method

class Appointment:

    ### DEFAULT CONSTRUCTOR ###
    def __init__(self) :
        self._description = "UNKNOWN"
        self._month = 1
        self._day = 1
        self._year = 1970

        
    ### GETTERS AND SETTERS ###
    def setDescription(self):
        self._description = input("Appointment Description: ")
        
    def setDate(self):
        #Loop around try/accept to force user to input a number and prevent program from crashing
        while True:
            try:
                self._month = int(input("Month (MM): "))            #Requesting/saving numerical month
                break
            except ValueError:
                print("Please enter a 2 digit number from 01 - 12")
                continue

        #Loop around try/accept to force user to input a number and prevent program from crashing     
        while True:
            try:
                self._day = int(input("Day (DD): "))                #Requesting/saving numerical day
                break
            except ValueError:
                print("Please enter a 2 digit number from 01 - 31")
                continue

        #Loop around try/accept to force user to input a number and prevent program from crashing 
        while True:
            try:
                self._year = int(input("Year (YYYY): "))            #Requesting/saving numerical year
                break
            except ValueError:
                print("Please enter a 4 digit number from 0000 - 9999")
                continue
    #This function returns a private data member- string description    
    def getDescription(self):
        return self._description

    ### PUBLIC METHODS ###
    
    #This method formats appointmentto appear like "4/8/2021    Dentist"
    def printAppointment(self):
        print(self.getDate(), "\t", self._description)
        
    ### ABSTRACT METHODS ###
        
    #This function forces subclasses to define how the date obtained/returned as
    #each type of appointment will benefit from modified formating
    def getDate(self):
        pass

    #This function forces subclasses to define how dates for different types of
    #appointments are compared for date equality.
    def occursOn(self, year, month, day):
        pass
        
 
        
##########################################################################################################################
# SUB CLASS 1: First_Time
# This class is a subclass of the above Appointments class. It allows for appointments
# to be set for one day and one day only.
        
class First_Time(Appointment):

    ###DEFAULT CONSTRUCTOR- same as super class###
    def __init__(self) :
        super().__init__()

    ### OVERRIDDEN METHODS ###
    #This method is the same as the super classes appointment, but it adds extra instruction
    def setDate(self):
        print("On what day is/was this appointment?")
        super().setDate()

    #This method formats appointmentto appear like "4/8/2021        Dentist"
    def printAppointment(self):
        print(self.getDate(), "\t\t\t", self._description)
        
    ### ABSTRACT METHODS DEFINED ###
    #This method returns data as MM/DD/YYYY formatting
    def getDate(self):
        return str(self._month) + "/" + str(self._day) + "/" + str(self._year)

    #This method compares the numerical month, numerical day, and numerical year to a
    #given numerical month, numerical day, and numerical year to confirm if two dates
    #are the same or not
    def occursOn(self, year, month, day): #that checks whether the appointment occurs on that date. For example, fora monthly appointment, you must check whether the day of the month matches.
        if self._month == month and self._day == day and self._year == year:
            return True
        else:
            return False 


##########################################################################################################################
# SUB CLASS 2: Every_Day
# This class defines an daily appointment based on a starting date. Therefore the appointment
# actually occures every day starting at a date given by the user.
        
class Every_Day(Appointment):

    ###DEFAULT CONSTRUCTOR- same as super class###
    def __init__(self) :
        super().__init__()

    ### OVERRIDDEN METHODS ###
    #This method uses the supers method but adds additional instruction at the beginning
    def setDate(self):
        print("On what day does/did this appointment first start?")
        super().setDate()

    ### ABSTRACT METHODS DEFINED ###
    #This function defines asbstract method for how to compare dates with a daily appointment
    #if the date provided occures on or after the start date, then it returns true, and
    #false if it occures before the start day
    def occursOn(self, year, month, day): #that checks whether the appointment occurs on that date. For example, fora monthly appointment, you must check whether the day of the month matches.

        if self._year <= year:
            return True

        elif self._year == year and self._month <= month:
            return True

        elif self._year == year and self._month == month and self._day <= day:
            return True

        else:
            return False 

    ### This function returns date formatted "Everyday starting 4/8/2021"    
    def getDate(self):
        return "Everyday starting "+ str(self._month) + "/" + str(self._day) + "/" + str(self._year)

##########################################################################################################################
# SUB CLASS 3: Every_Month
# This class defines an appointment that occures every month on the same numerical day 
# beginning on a start day provided by the user
        
class Every_Month(Appointment):

    ###DEFAULT CONSTRUCTOR- same as super class###
    def __init__(self) :
        super().__init__()

    ### OVERRIDDEN METHODS ###
    #This method uses the supers method but adds additional instruction at the beginning
    def setDate(self):
        print("On what day does/did this monthly appoint start?: ")
        super().setDate()
        

    ### ABSTRACT METHODS DEFINED ###
    #This function confirms that an appointment exists on a given date by comparing the
    #numerical day and confirming that the date provided is after or on the start date
    def occursOn(self, year, month, day):
        if self._day == day:
            if self._year < year:
                return True                                     #numerical day is the same AND date is after/on when monthly appointment began
            elif self._year == year and self._month <= month:
                return True                                     #numerical day is the same AND date is after/on when monthly appointment began
            else:
                return False                                    #numerical day is the same BUT date is before monthly appointment began
        else:
            return False                                        #numerical day is NOT the same

    #This function prints out a readable version of the monthly appointment date. Example: "Every 1st day of the month" but adjusts "st" given the
    #number to be printed.
    def getDate(self):
        if self._month == 1:
            return "Every " + str(self._month) + "st day of the month"
        elif self._month == 2:
            return "Every " + str(self._month) + "nd day of the month"
        elif self._month == 3:
            return "Every " + str(self._month) + "rd day of the month"
        else:
            return "Every " + str(self._month) + "th day of the month"                    


main()

