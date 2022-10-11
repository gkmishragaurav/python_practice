# Write a function that takes a non-empty array and an integer representing a target sum.
# That function should find all triplets in the array that sum up to the target sum.

a=[-1,0,1,2,-1,-4]
a.sort()

def three_sum(a, right, target):
  if len(a)<3:
    return None
  for i in range(len(a)-2):
    temp = two_sum(a, i+1, right, target-a[i])
    if temp:
      print a[i], temp


def two_sum(a, left, right, target):
  while right > left:
    temp = a[left] + a[right]
    if temp == target:
      return a[left], a[right]
    elif temp > target:
      right = right - 1
    else:
      left = left + 1

three_sum(a, len(a)-1, 0)
