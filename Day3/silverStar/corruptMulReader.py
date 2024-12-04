'''
HELPER METHODS
'''
# method to find next multiplication problem in text
# returns -1 if not found
def findNextProb(myString):
    return myString.find("mul(")

# method to find the end of the multiplication problem
# returns -1 if not found or out of bounds
def findProbEnd(myString):
    # finding index of the closing ')'
    tempIndex = myString.find(")")

    # at most the mul() expression can be 12 characters long
    # if invalid format, return -1
    if (tempIndex == -1 or tempIndex > 11 or tempIndex < 7):
        return -1

    # else return index of closing ')'
    return tempIndex


'''
MAIN
'''
# creating file object of our input file
myFile = open("input.txt",'r')

# list to store all of the collected multiplication problems
multProbs = []

# loop to iterate through input file
for line in myFile:
    
    # storing contents of line in string variable to manipulate
    myLine = line

    # loop to get all multiplication problems from text
    while (len(myLine) > 0):

        # methods to get next multiplication problem from text
        nextMul = findNextProb(myLine)

        # break condition if no more problems
        if (nextMul == -1):
            myLine = ""
            continue

        # cutting off leading corrupt characters
        myLine = myLine[nextMul:]

        # finding end of most recent problem
        mulEnd = findProbEnd(myLine)

        # go to next problem if no valid close to current problem
        if (mulEnd == -1):
            myLine = myLine[1:]
            continue

        # putting valid problem into list
        tempProb = myLine[0:mulEnd+1]
        multProbs.append(tempProb)

        # iterating loop condition
        myLine = myLine[1:]

