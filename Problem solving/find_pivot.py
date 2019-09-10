# https://www.geeksforgeeks.org/find-element-array-sum-left-array-equal-sum-right-array/
# Find an element in array such that sum of left array is equal to sum of right array
# Given, an array of size n. Find an element which divides the array in two sub-arrays with equal sum.

def sum_of_array(a, start, end):
 sum=0;i=start
 while(i<=end):
  sum=sum+a[i]
  i=i+1
 return sum

def find_pivot(a):
 pivot = 1
 left_sum = sum_of_array(a, 0, pivot-1 )
 right_sum = sum_of_array(a, pivot+1, len(a)-1)
 while(pivot != len(a)-1):
  if left_sum == right_sum:
   return pivot
  else:
   left_sum=left_sum + a[pivot]
   pivot = pivot+1
   right_sum = right_sum - a[pivot]

a=[1,4,1]
print find_pivot(a)