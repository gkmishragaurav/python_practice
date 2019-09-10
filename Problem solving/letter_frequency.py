from collections import defaultdict

def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

s=[1,1,1,1,3,4,6,4,6,6,6,6]

print dict(letter_frequency(s))