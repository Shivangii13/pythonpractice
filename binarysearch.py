import math
def binarysearch(array , value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value):
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start+end)/2)
        print(start, middle, end)
    return middle



custArray = [8,9,2,0,1,6,4,3,10]
print(binarysearch(custArray , 0))