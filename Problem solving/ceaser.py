# Print a single integer denoting the maximum length of t for the given s; if it is not possible to form string , print 0 instead.
#  Complete the alternate function below.
# use chr(ord('a')) and ord('a') functions.--- for changing ascii value to normal value.
#a-97,z-122
import pdb

# Complete the caesarCipher function below.
def caesarCipher(s, k):
  temp=''
  k=k%26
  for x in s:
    # pdb.set_trace()
    if 97<=ord(x)<=122 :
      if 97<=ord(x)+k<=122 :
        temp=temp+chr(ord(x)+k)
      elif ord(x)+k>122:
        temp = temp + chr(ord('a') + k + ord(x) - ord('z')-1)

    elif 65 <= ord(x) <= 90:
      if 65 <= ord(x) + k <= 90:
        temp = temp + chr(ord(x) + k)
      elif ord(x) + k > 90:
        temp = temp + chr(ord('A') + k + ord(x) - ord('Z') - 1)
    else:
      temp = temp + x
  return temp

s='www.abc.xy'
k=9
print caesarCipher(s, k)