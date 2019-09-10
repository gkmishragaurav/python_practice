codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
s=["gin", "zen", "gig", "msg"]

def morse_code(st):
    res=''
    for x in st:
        res=res+codes[ord(x)-ord('a')]
    return res

def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    all_str = []
    for word in words:
        all_str.append(morse_code(word))

    return len(set(all_str))

print uniqueMorseRepresentations(s)