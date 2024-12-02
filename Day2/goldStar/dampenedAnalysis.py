'''
HELPER METHODS
'''
# function used to see if report data increases smoothly
# returns 1 if safe, 0 if unsafe
def checkInc(reportList):
    # variables used for loop progression
    listLen = len(reportList)
    counter = 0

    # iterate through data and check if safe
    while (counter < listLen - 1):
        # getting two neighboring report values
        val1 = reportList[counter]
        val2 = reportList[counter+1]

        # check for conditions that make report unsafe
        if (val1 >= val2):
            return 0
        elif (val2 - val1 > 3):
            return 0

        # increment counter/loop condition
        counter += 1

    # made it through while loop check, so data was safe
    return 1


# function used to see if report data decreases smoothly
# returns 1 if safe, 0 if unsafe
def checkDec(reportList):
    # variables used for loop progression
    listLen = len(reportList)
    counter = 0

    # iterate through data and check if safe
    while (counter < listLen - 1):
        # getting two neighboring report values
        val1 = reportList[counter]
        val2 = reportList[counter+1]

        # check for conditions that make report unsafe
        if (val1 <= val2):
            return 0
        elif (val1 - val2 > 3):
            return 0

        # increment counter/loop condition
        counter += 1

    # made it through while loop check, so data was safe
    return 1


# Problem Dampener Fuctionality
# Goes through unsafe tests and checks if removing a value
# allows the test to be safe
# Returns Safe: 1, Unsafe: 0
def checkDampener(reportList):
    # variables used for loop progression
    listLen = len(reportList)
    counter = 0

    while(counter < listLen):
        # copying parameter list to temp list
        tempList = reportList.copy()
        # getting rid of an element
        tempList.pop(counter)

        # if the list is now safe return 1
        if ((checkInc(tempList)) or (checkDec(tempList))):
            return 1

        # increment loop counter
        counter += 1

    # report is still unsafe even after dampening
    return 0

'''
MAIN
'''
# opening file with testing reports
myFile = open("input.txt",'r')

# storing total number of safe and unsafe reports
safe = 0
unsafe = 0

# iterating through myFile lab reports
for line in myFile:

    # putting each line in a list to compare
    tempStrSet = line.split(" ")
    #turning all strings into ints using list comprehension
    tempSet = [int(string) for string in tempStrSet]

    # if the set is descending in value
    if (tempSet[0] > tempSet[1]):
        if checkDec(tempSet):
            safe += 1
        else:
            if checkDampener(tempSet):
                safe += 1
            else:
                unsafe += 1
    # if the set is increasing in value
    else: 
        if checkInc(tempSet):
            safe += 1
        else:
            if checkDampener(tempSet):
                safe += 1
            else:
                unsafe += 1

# print results
print(f"Safe: {safe}")
print(f"Unsafe: {unsafe}")
