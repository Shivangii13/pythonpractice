import numpy as np
twoDarray = np.array([[2,4,6,8,0],[1,3,5,7,9],[1,2,4,5,7],[3,6,9,8,0]])
print(twoDarray)

#insert in 2D array
newtwoDarray = np.insert(twoDarray , 1, [[1,2,3,4,5]], axis=0)
print(newtwoDarray)

#access elements from 2D array
def accessElements(array,rowindex,colindex):
    if rowindex >= len(array) and colindex >= len(array[0]):
        print("incorrect index")
    else:
        print(array[rowindex][colindex])

accessElements(twoDarray , 2 , 3)

def traversetwoDarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print([i][j])


#search in 2D array
def searchtwoDarray(array , value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return  ' the element located in the index ' +str(i)+""+str(j)
    return 'the elemnet is not found'    
    
print(searchtwoDarray(twoDarray,2 ))

#deletion in 2D array
newTDarray = np.delete(twoDarray ,0 ,axis=0)
print(newTDarray)
