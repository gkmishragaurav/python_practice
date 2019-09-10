class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_link_list(head):
    while(head):
        print head.val,
        head=head.next

l1=ListNode(1)
# ;l3=ListNode(3)
# l1.next=l2;l2.next=l3;l3.next=None
l1.next=None
l4=ListNode(4);l5=ListNode(5);l6=ListNode(6)
l4.next=l5;l5.next=l6;l6.next=None

def addTwoNumbers(l1,l2):
    carry=0
    prev=head=ListNode(None)
    while(l1 or l2 or carry):
        if l1:
            carry=carry+l1.val
            l1=l1.next
        if l2:
            carry=carry+l2.val
            l2=l2.next
        prev.next=ListNode(carry%10)
        carry=carry/10
        prev=prev.next

    head=head.next
    return head

addTwoNumbers(l1,l4)
