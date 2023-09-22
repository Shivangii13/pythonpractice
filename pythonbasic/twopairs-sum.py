def findpairs(num, target):
    for i in range(len(num)):
        for j in range(i+1 ,len(num)):
            if num[i] == num[j]:
                continue
            elif num[i] + num[j] == target:
                print(i,j)

mylist = [1,2,3,4,5,6]
findpairs(mylist,6)

