# opening file with all stored input values
myFile = open("input.txt",'r')

# similarity score based on algorithm provided (FINAL ANSWER)
# For each number in left column:
# simScore += leftColumnNumber * numberOfTimesInRightColumn
simScore = 0

# list to store all of the numbers based on their column
col1 = []
col2 = []

# loop to go through all lines in input.txt
for line in myFile:

    # list with two line numbers stored as strings
    currLine = line.strip().split("   ")

    # turning input into ints
    num1 = int(currLine[0])
    num2 = int(currLine[1])

    # storing ints in lists based on column
    col1.append(num1)
    col2.append(num2)


# after we have two lists of ints based on column
# iterate through col1 list until empty
while(len(col1) > 0):

    # get next num to check for
    leftNum = col1[0]

    # find how many times leftNum is in the right column (col2)
    numTimes = col2.count(leftNum)

    # adding score to running similarity score counter
    simScore += (leftNum * numTimes)

    # removing index of leftNum from list (loop end condition)
    col1.pop(0)


# printing the final similarity score (FINAL ANSWER)
print(simScore)
