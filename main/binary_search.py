import math as mt
def binarySearch(array, target):
    leftPointer = 0
    rightPointer = len(array) - 1
    middlePosition = mt.floor((leftPointer + rightPointer) / 2)

    while(len(array) > middlePosition):
        element = array[middlePosition]
        if(element == target):
            return element
        if(target < element):
            rightPointer = middlePosition - 1

        else:
            leftPointer = middlePosition + 1

        if(leftPointer > rightPointer): return -1

        middlePosition = mt.floor((leftPointer + rightPointer) / 2)
    return -1 

result = binarySearch([1,2,3,4,5], 6)
print(result)