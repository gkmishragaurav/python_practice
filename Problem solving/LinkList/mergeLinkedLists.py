# merge linklist in-place.
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeLinkedLists(l1, l2):
    prev=None;head=None
    while l1 or l2:
        if l1 and l2:
            if l1.value <= l2.value:
                if not head:head=l1
                if not prev:
                    prev=l1
                else:
                    prev.next = l1
                    prev=l1
                if not l1.next: last = l1
                l1 = l1.next
            else:
                if not head:head = l2
                if not prev:
                    prev=l2
                else:
                    prev.next = l2
                    prev=l2
                if not l2.next: last = l2
                l2=l2.next

        elif l1:
            last.next = l1
            break

        elif l2:
            last.next = l2
            break

    return head


def print_linklist(ll):
    while(ll):
        print(ll.value)
        ll=ll.next

l1=LinkedList(1)
l2=LinkedList(3)
l3=LinkedList(5)
# l4=LinkedList(4)
l5=LinkedList(2)
l6=LinkedList(4)
# l7=LinkedList(7)


l1.next=l2;l2.next=l3#;l3.next=l4
# l4.next=l5;
l5.next=l6#;l6.next=l7

head = mergeLinkedLists(l1, l5)
print_linklist(head)
