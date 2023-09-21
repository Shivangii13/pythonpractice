prev_list = [1,3,5,7,9]
new_list = [i*2 for i in prev_list]
print(prev_list)
print(new_list)


language = 'python'
new1_list = [letter for letter in language]
print(new1_list)


#conditoonal list comprehension
prev1_list = [-1 , 10 , -20, 2, -90, 60, 45]
new2_list = [number for number in prev1_list if number>0]
print(new2_list)
new3_list = [number*number for number in prev1_list if number<0]
print(new3_list)