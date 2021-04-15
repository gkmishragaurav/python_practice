# merge linklist in-place.

import copy
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def _linkedListPalindrome(head, mid):
    while mid:
        if head.value != mid.value:
            return False
        head=head.next
        mid=mid.next

    return True

def linkedListPalindrome(head):
    if head.next == None:
        return True
    mid, prev = get_mid(head)
    temp = copy.deepcopy(mid)
    last = reverseLinkedList(temp.next)
    mid.next = last
    print(mid.value)
    return _linkedListPalindrome(head, mid.next)

def reverseLinkedList(head):
    current = head
    prev=None
    while current:
        nxt = current.next
        current.next = prev
        prev=current
        current = nxt

    return prev

def get_mid(head):
    slow = head
    fast = head
    while fast.next:
        prev=slow
        fast=fast.next
        if fast.next:
            fast=fast.next
            slow=slow.next

    return slow, prev
def print_linklist(ll):
    while(ll):
        print(ll.value)
        ll=ll.next

l1=LinkedList(1)
l2=LinkedList(2)
l3=LinkedList(3)
# l4=LinkedList(4)
l5=LinkedList(3)
l6=LinkedList(2)
l7=LinkedList(1)


l1.next=l2;l2.next=l3#;l3.next=l4
l3.next=l5
l5.next=l6;l6.next=l7
print(linkedListPalindrome(l1))

