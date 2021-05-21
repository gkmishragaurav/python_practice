# Given a string, find the first non-repeating character in it. 
# For example, if the input string is “GeeksforGeeks”, then the output should be ‘f’ 
# and if the input string is “GeeksQuiz”, then the output should be ‘G’. 

def firstNonRepeatingCharacter(s):
    def util():
        d={}
        i=97
        while i<123:
            d[chr(i)] = 0
            i=i+1
        return d
    d=util()
    i=0
    while i<len(s):
        d[s[i]] = d[s[i]]+1
        i=i+1

    for index, item in enumerate(s):
        if d[item] == 1:
            return index

    return -1

s='abcdcaf'
print(firstNonRepeatingCharacter(s))
