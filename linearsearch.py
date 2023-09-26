def linearsearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linearsearch([20,40,50,60,80,90],10))