import numpy as  np

myarray = np.array([1,7,3,4,16,18,10,15,2,5,17,13,19,0])
def findNumber( array , number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)


findNumber(myarray , 18)