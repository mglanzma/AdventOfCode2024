'''
HELPER METHODS
'''
# method to find next iteration of "don't()"
def findDont(myString):
    return myString.find("don't()")

# method to find next iteration of "do()" to re-enable problems
def findDo(myString):
    return myString.find("do()")

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

# helper method to parse through multiplication problems
# returns the product of the problem
def parseMul(problem):
    # splits problem up to make easier to parse numbers
    parts = problem.split(",")
   
    try:
        # num1 found after getting rid of 'mul('
        num1 = int(parts[0][4:])

        # num2 found after chopping of closing ')'
        probEnd = findProbEnd(parts[1])
        num2 = int(parts[1][0:probEnd])

        return num1 * num2
    except ValueError:
        return 0


'''
MAIN
'''
# creating file object of our input file
myFile = open("input.txt",'r')

# list to store all of the collected multiplication problems
multProbs = []

# do() operation is initially set to true
# when don't() appears value is switched to false
doEnable = True

# loop to iterate through input file
for line in myFile:
    
    # storing contents of line in string variable to manipulate
    myLine = line

    # loop to get all multiplication problems from text
    while (len(myLine) > 0):
        
        # if next problems should not be processed 
        if (doEnable == False):
            # if don't() is activated
            nextDo = findDo(myLine)
            # if don't() remains active through rest of line
            if(nextDo == -1):
                break
            # skips to next do() which activates problems
            myLine = myLine[nextDo:]
            doEnable = True
            continue


        # methods to get next multiplication problem from text
        nextMul = findNextProb(myLine)

        # checking if "don't()" gets activated before problem
        nextDont = findDont(myLine)
        if(nextDont != -1 and nextDont < nextMul):
            doEnable = False
            continue

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


# after all multiplication problems are collected
# use helper method to solve each of the problems
totalAnswer = 0

for problem in multProbs:
    # helper method to solve problem
    tempProduct = parseMul(problem)

    # adding partial product to total
    totalAnswer += tempProduct

# add all of the partial sums together (FINAL ANSWER)
print(totalAnswer)

