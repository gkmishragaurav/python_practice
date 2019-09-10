# Print a single integer denoting the maximum length of t for the given s; if it is not possible to form string , print 0 instead.
#  Complete the alternate function below.
# use chr(ord('a')) and ord('a') functions.--- for changing ascii value to normal value.
import pdb
from itertools import combinations
def generate_pairs(a):
  yield list(combinations(a,2))

def form_string(s, pair):
  str=''
  for x in s:
    if x in pair:
      str=str+x
  return str

def unique(ll):
  temp=[]
  for x in ll:
    if x not in temp:
      temp.append(x)
  return temp

def string_alternate(a):
  i=0
  while i<len(a)-1:
    if a[i] == a[i+1]:
      return False
    else:
      i=i+1
  return True

def alternate(s):
  max=0
  pairs=list(generate_pairs(s))
  for pair in unique(pairs[0]):
    temp=form_string(s, pair)
    if string_alternate(temp):
      if len(temp) > max:
        max=len(temp)

  return max

s='aaaa'
print len(s)
print alternate(s)

