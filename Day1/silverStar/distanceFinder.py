# opening file with all stored input values
myFile = open("input.txt",'r')

# running total for distance between numbers (final ansewr)
totDist = 0

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
# iterate through lists until they are empty
while(len(col1) > 0):

    # get smallest from each column
    min1 = min(col1)
    min2 = min(col2)

    # adding their distance apart to running distance total
    if min2 >= min1:
        totDist += (min2 - min1)
    else:
        totDist += (min1 - min2)

    # removing both min values from their respective columns
    col1.remove(min1)
    col2.remove(min2)

# after we go through all of the values
# print final distance between column values
print(totDist)
