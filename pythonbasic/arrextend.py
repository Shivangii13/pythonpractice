from array import *
 
my_array = array('i',[2,4,6,8,1])
print(my_array)
my_array1 = array('i',[6,2,8,4])
my_array.extend(my_array1)
print(my_array)