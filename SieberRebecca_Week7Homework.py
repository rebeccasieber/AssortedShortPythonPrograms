#***************************************************
#PROGRAM NAME:          SieberRebecca_Week7Homework.PY
#PROGRAMMER:            SIEBER
#DATE OF PROGRAM: 	7/14/20
#PURPOSE:     		A PROGRAM THAT WILL READ A TEXT AND
#                       WRITE A NEW TEXT THAT "CENSORS" KEY WORDS
#                       BY REPLACING THEM WITH AN ASTERIX FOR EACH
#                       LETTER IN THE WORD
#MODULES USED:          NONE
#INPUT VARIABLE(S):     SieberRebecca_Week7HomeworkInfile.txt
#OUTPUT:                SieberRebecca_Week7HomeworkOutfile.txt  
#
#*******************************************************

def main():

    #defining list of words to be censored
    badWords = ["Lord", "Voldemort", "killing", "kill"] 

    #opening text file to read 
    infile = open("SieberRebecca_Week7HomeworkInfile.txt", "r")
    
    #opening text file to write
    outfile = open("SieberRebecca_Week7HomeworkOutfile.txt", "w")

    #reading text and saving it into varible name "story"
    story = infile.read()

    #beginning loop to go through each string in the set of badWords
    for n in range(0,4):
        badWord = badWords[n]
        length = len(badWord)
                     
        #replacing badWord in the story with "*" for each letter in the badWord
        #and redefining the story with sensored version
        story = story.replace(badWord, "*"*length)

        #increasing counter to eventually end the for loop
        n = n+1
        
    #writing "censored" story to outfile
    outfile.write(story)

    #closing files
    infile.close()
    outfile.close()
    
main()
