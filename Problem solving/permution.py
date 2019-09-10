import copy

class Queue():
    def __init__(self):
        self.queue = []

    def set(self, value):
        self.queue.insert(0, value)

    def get(self):
        if self.queue:
            return self.queue.pop()

    def last(self):
        if self.queue:
            return self.queue[-1]

    def printQ(self):
        for x in self.queue:
            print toString(x),

    def isEmpty(self):
        if self.queue: return True
        return False

q=Queue()

def insert_char(s1, k, c):
    # This will enter a charecter c on K position
    s=copy.deepcopy(s1)
    n=len(s);i=n-1
    if k>=n:
        s.append(c)
    else:
        s.append(s[n - 1])
        while(i!=k):
            s[i],s[i-1] = s[i-1], s[i]
            i=i-1
        s[k] = c
    return s

def to_arr(s):
    # make str to arr.
    return list(map(str, s))

def toString(List):
    # to make arr to list.
    return ''.join(List)

def permute(a):
    q.set([a[0]])
    j=1
    while(1):
        string = q.get()
        i=0
        if len(string) == len(a):
            print toString(string),
            q.printQ()
            break
        else:
            while(i<=len(string)):
                temp=insert_char(string, i, a[j])
                q.set(temp)
                i=i+1
        if len(string) != len(q.last()):
            j=j+1

a='abc'
permute(a)

############ method 2 ##########
from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = permutations('abc')

# Print the obtained permutations
for i in list(perm):
    print "".join(i)

############ method 3 ##########
# https://github.com/davidmasse/blog-permute
pd=[]
def perm(org, curr=''):
    diff = set(org) - set(curr)
    if len(diff) == 0:
        pd.append(curr)
        return

    else:
        for ch in diff:
            perm(org, curr+ch)

perm(a)
print pd