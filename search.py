# Tamsin Rogers
# October 9, 2019
# CS 152 
# Project 6 Lab: Searching
#run this program from the Terminal by entering "python3 search.py"

import random

def searchSortedList( myList, value ):
    # assign to the variable done, the value False
    done = False
    # assign to the variable found, the value False
    found = False
    # assign to the variable count, the value 0
    count = 0
    # assign to the variable maxIdx, the one less than the length of mylist 
    maxIdx = (len(myList)-1)
    # assign to the variable minIdx, the value 0
    minIdx = 0

    # start a while loop that executes while done is not True    
    while done != True:
        # increment count  (which keeps track of how many times the loop executes
        count+=1
        # assign to testIndex the average of maxIdx and minIdx (use integer math)        
        testIndex = (maxIdx+minIdx)//2
        # if the myList value at testIndex is less than value
        if myList[testIndex] < value:
            # assign to minIdx the value testIndex + 1
            minIdx = testIndex+1
        # elif the myList value at testIndex is greater than value
        elif myList[testIndex] > value:
            # assign to maxIdx the value testIndex - 1
            maxIdx = testIndex-1
        # else
        else:
            # set done to True
            done = True
            # set found to True
            found = True

        # if maxIdx is less than minIdx
        if maxIdx < minIdx:
            # set done to True
            done = True
            # set found to False
            found = False

    return (found, count)
    
def test():

    a = []
    for i in range(10000):
        a.append( random.randint(0,100000) )

    a.append(42)

    a.sort()

    print(searchSortedList( a, 42 ))

if __name__ == "__main__":
    test() 