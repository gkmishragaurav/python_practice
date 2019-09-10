# Print all possible strings that can be made by placing spaces
#
# Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.
#
# Input:  str[] = "ABC"
# Output: ABC
#         AB C
#         A BC
#         A B C
import copy
class Queue():
    def __init__(self):
        self.queue = []

    def set(self, value):
        self.queue.append(value)

    def get(self):
        if self.queue:
            return self.queue.pop(0)

    def printQ(self):
        for x in self.queue:
            print x,

    def isEmpty(self):
        if self.queue: return True
        return False

q = Queue()

def toString(List):
    s = ""
    for x in List:
        if x == '\0':
            break
        s += x
    return s

def insert_space(s, k):
    # This will enter an space on K position
    s= copy.deepcopy(s)
    n=len(s);i=n-1;s.append(s[n-1])
    while(i!=k):
        s[i],s[i-1] = s[i-1], s[i]
        i=i-1
    s[k] = ' '
    return s

def find_last_space(s):
    # This will give the last space in string
    n=len(s);i=n-1
    while(i>=1):
        if s[i] == ' ':
            return i
        i=i-1
    return False

def print_Pattern(s):
    q.set(s)
    while(q.isEmpty()):
        string = q.get()
        print toString(string)
        i = find_last_space(string)
        if not i: i=1
        else:i=i+2
        length = len(string)
        while(i<length):
            temp=insert_space(string, i)
            q.set(temp)
            i=i+1

s=['a', 'b', 'c', 'd', 'e', 'f']
print_Pattern(s)