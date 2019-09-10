# Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.
# Print the number of letters in Sami's message that were altered by cosmic radiation.
# Sample Input 0
#
# SOSSPSSQSSOR
#
# Sample Output 0
#
# 3
base='SOS'
def substring(s):
  i=0
  count=0
  while (i<len(s)-2):
    # print s[i:i+3]
    if s[i] == 'S':
      if s[i:i+3] != 'SOS':
        print s[i:i+3]
        count=count+1
    i=i+1
  print count
  return count

def marsExploration(s):
  print substring(s)
  #return(len(s)/3 - substring(s))

s='OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS'
print marsExploration(s)