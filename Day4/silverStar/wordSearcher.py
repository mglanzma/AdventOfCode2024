'''
HELPER METHODS
'''
# method used to find all of the horizontal "XMAS" in word search
# checks forwards and backwards, then returns number of times in total
def findXmasHorizontal(wordSearch):
    # running total for number of XMAS found
    numFound = 0

    # iterate through rows
    for row in wordSearch:
        # turning row back into string
        tempString = ''.join(row)

        # checking how many times xmas is in the line
        # both forwards and backwards
        numFound += tempString.count("XMAS")
        numFound += tempString.count("SAMX")
    
    # returning final number of horizontal words found
    return numFound

# method to find all vertical "XMAS" or "SAMX" in word search
# returns final number of vertical words found
def findXmasVertical(wordSearch):
    # running total for number of XMAS found
    numFound = 0

    # index values for reading correct column from each row
    curr = 0
    maxIndex = len(wordSearch[1])

    # temp list to store all letters collected
    tempList = []

    # adds all columns to a tempString then counts
    while(curr < maxIndex):
        for line in wordSearch:
            tempList.append(line[curr])

        # turn all collected values into string
        columnStr = ''.join(tempList)
        # count number of valid words in string
        numFound += columnStr.count("XMAS")
        numFound += columnStr.count("SAMX")

        # clear tempList and iterate loop
        tempList.clear()
        curr += 1

    # return total number of vertical words in word search
    return numFound


# method to find number of valid words in the diagonals
def findXmasDiagonals(wordSearch):
    # running total returned at the end
    numFound = 0

    # values used in loops
    numRows = len(wordSearch)
    numColumns = len(wordSearch[0])

    # making lists to hold diagonal lists
    forwardDiag = [[] for diagonal in range(numRows + numColumns -1)]
    backwardDiag = [[] for diagonal in range(len(forwardDiag))]
    minBackDiag = -numRows + 1

    # getting all diagonal lists
    for col in range(numColumns):
        for row in range(numRows):
            forwardDiag[col + row].append(wordSearch[row][col])
            backwardDiag[col - row - minBackDiag].append(wordSearch[row][col])

    # checking for valid words
    for diag in forwardDiag:
        tempString = ''.join(diag)
        numFound += tempString.count("XMAS")
        numFound += tempString.count("SAMX")

    # checking for valid words
    for diag in backwardDiag:
        tempString = ''.join(diag)
        numFound += tempString.count("XMAS")
        numFound += tempString.count("SAMX")

    # returning final answer of words found
    return numFound




'''
MAIN
'''

# word search input file
myFile = open("input.txt",'r')

# collective list of each row of characters (2D)
myRows = []

# running total of words found
wordsFound = 0

for line in myFile:
    # create list containing all individual characters
    tempList = list(line.strip())
    # store in 2D list
    myRows.append(tempList)

# after all rows are added
horizontal = findXmasHorizontal(myRows)
vertical = findXmasVertical(myRows)
diagonal = findXmasDiagonals(myRows)
wordsFound += horizontal
wordsFound += vertical
wordsFound += diagonal
print(f"horizontal: {horizontal}")
print(f"vertical: {vertical}")
print(f"diagonal: {diagonal}")
print(f"\nTotal: {wordsFound}")
