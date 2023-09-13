def missing_number(arr, n):
    
  # calculate total
  total = n*(n+1)//2

#calculate sum
  sum_arr = sum(arr)

 #find missing missing_number
  missing_number = total - sum_arr

  return missing_number


print(missing_number([1, 2, 3, 4, 6],6))