# Write a function that takes in an array of words and returns the smallest array of characters
# needed to form all of the words. The characters don't need to be in any particular order.
# For example, the characters ["y", "", "0", "U"] are needed to form the words ["your", "you", "or", "yo"] .
# Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

def merge_dict(d1, d2):
    # merge d2 into d1
    for key in d2.keys():
        if key not in d1.keys() :
            d1[key] = d2[key]
        elif d2[key] > d1[key]:
            d1[key] = d2[key]

    return d1
def dict_to_list(d):
    l=[]
    for key in d.keys():
        l.extend([key for item in range(0,d[key])])

    return l

def minimumCharactersForWords(words):
    # Write your code here.
    d={}
    for word in words:
        temp_d = {}
        for item in word:
            if item not in temp_d:
                temp_d[item] = 0
            temp_d[item]=temp_d[item]+1

        d=merge_dict(d, temp_d)

    temp = list(d.keys())
    return temp

x=minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"])
print(x)
