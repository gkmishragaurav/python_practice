# You are given a Double Link List with one pointer of each node pointing to the next node just like in a single link list.
# The second pointer however CAN point to any node in the list and not just the previous node.
# Now write a program in O(n) time to duplicate this list. That is, write a program which will create a copy of this list.

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None

def odd_even_split(head):
    head1=head.next
    first=head
    sec=head1
    while first.next and sec.next:
        if sec.next:
            first.next = sec.next
        first = first.next
        if first.next:
            sec.next = first.next
        sec = sec.next
    first.next=None
    return head, head1

def adjust_random(head):
    first=head
    sec=head.next

    while first.random and sec:
        if first.random:
            sec.random = first.random.next
        if sec.next:
            first = sec.next
        if first.next:
            sec = first.next

def copyRandomList(head):
    """
    :type head: Node
    :rtype: Node
    """
    # copy and insert node in LL
    first=head
    while first:
        temp = Node(first.val)
        sec = first.next
        first.next = temp
        temp.next = sec
        first=sec

    # adjust random node for LL
    adjust_random(head)

    # odd-even split of LL
    head, head1 = odd_even_split(head)

    return head, head1

def print_linklist_rnd(ll):
    while(ll):
        print(ll.val, end=' ')
        ll=ll.random

def print_linklist_next(ll):
    while(ll):
        print(ll.val, end=' ')
        ll=ll.random

l1=Node(1)
l2=Node(2)
l3=Node(3)
l4=Node(4)
# l5=Node(5)
# l6=Node(6)
# l7=Node(7)

l1.next=l2;l2.next=l3;l3.next=l4
# l4.next=l5;l5.next=l6;l6.next=l7

# l1.random=l5;l2.random=l6;l3.random=l7
# l7.random=l2;l5.random=l3;l6.random=l4

l1.random=l3;l2.random=l4;l3.random=l2

head, head1 = copyRandomList(l1)
print_linklist_next(head)
print('\ncopy')
print_linklist_next(head1)

