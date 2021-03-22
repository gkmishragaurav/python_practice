# Given a singly linked list, rotate the linked list counter-clockwise/clockwise by k nodes. 
# Where k is a given positive/negetive integer. For example, if the given linked list is 10->20->30->40->50->60 
# and k is 4, the list should be modified to 50->60->10->20->30->40.

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(l1, k):
    # k can be positive and negative
    # Find p1, p2 and head
    if k==0:
        return l1
    first=l1; count=0
    # find length of linklist.
    while first:
        count=count+1
        first=first.next

    # rearrage value of k
    if k<0:
        k=count-(abs(k)%count)
    if abs(k)>=count:
        k=abs(k)%count

    if k==0: return l1

    # find final position of first and second pointer.
    first=l1;second=l1
    i=0
    while i<abs(k):
        second=second.next
        i=i+1

    while second.next:
        second=second.next
        first = first.next

    # Now rotate
    head = first.next
    first.next = None
    second.next = l1

    return head
