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

    # getting either the starting min or max depending on data
    tempVal = tempSet[0]

    # if first two neighboring values are the same, the set is unsafe
    if (tempVal == tempSet[1]):
        unsafe += 1
    # if the set is descending in value
    elif (tempVal > tempSet[1]):
        if checkDec(tempSet):
            safe += 1
        else:
            unsafe += 1
    # if the set is increasing in value
    else: 
        if checkInc(tempSet):
            safe += 1
        else:
            unsafe += 1

# print results
print(f"Safe: {safe}")
print(f"Unsafe: {unsafe}")
