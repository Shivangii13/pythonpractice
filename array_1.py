
#create an array
import array

my_array = array.array("i")
print(my_array)
my_array1 = array.array('i',[1,2,4])
print(my_array1)


import numpy as np
np_array = np.array([],dtype = int)
print(np_array)
np_array1 = np.array([1,2,5,6])
print(np_array1)


#insertion in array
import array
my_array = array.array('i',[0,2,4,8])
print(my_array)
my_array.insert(3, 6)
print(my_array)


# traversing in array

def traversearray(array):
    for i in array:
        print(i)
traversearray(my_array)


#access the element

from array import *
arr1 = array('i',[4,5,7,8,2,9,0])

def accesselement(array,index):
    if index > len(array):
        print("element not in the index")
    else:
        print(array[index])    

accesselement(arr1,4) 
accesselement(arr1,8)      


#search an element in array
#linearsearch

my_array = array('i',[1,4,7,9,2])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print (linear_search(my_array, 2))

#delete element
my_array.remove(7)
print(my_array)
