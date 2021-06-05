# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

def topKFrequent( a, k: int):
    d={}
    for item in a:
        if item not in d:
            d[item]=0
        d[item]=d[item]+1

    a = [[k,v] for k,v in d.items()]
    d.clear()
    a.sort(key=lambda item:(-item[1],item[0]))
    print(a)
    ans=[]
    i=0
    while i<k:
        ans.append(a[0][0])
        a.pop(0)
        i=i+1
    return ans

x=topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
print(x)
