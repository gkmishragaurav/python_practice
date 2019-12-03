class Node:
    def __init__(self, x=None):
        self.val=x
        self.prev=None
        self.next=None

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

def print_linklist(head):
    if not head: print []
    while(head):
        print head.val,
        head=head.next
    print '\n'

def print_linklist_rev(head):
    if not head: print []
    while(head.next):
        head=head.next

    while(head):
        print head.val,
        head=head.prev
    print '\n'

def make_link_list(arr=None):
    '''This will give you a dummy doubly linklist'''
    head=None
    if not arr:
        head=Node(1);n2=Node(2);n3=Node(3);n4=Node(4);n5=Node(5)
        head.setNext(n2);n2.setNext(n3);n3.setNext(n4);n4.setNext(n5);n5.next = None
        head.setPrev(None);n2.setPrev(head);n3.setPrev(n2);n4.setPrev(n3);n5.setPrev(n4)
    else:
        #yet to write
        pass
    return head

def insert_at_end(head, node):
    '''Insert a node at the last of the linklist.'''
    head1=head
    while(head.next):
        head=head.next
    node.prev = head
    head.next = node
    return head1

def insert_at_start(head, node):
    '''Insert a node at the start of the linklist'''
    return node

def make_linklist(head, node):
    if not head:
        insert = insert_at_start
    else:
        insert = insert_at_end

    return insert(head, node)

def arr_to_linklist(arr):
    '''An arr is given and a linklist need to make.'''
    head=None
    if arr:
        for item in arr:
            head=make_linklist(head, Node(item))
    return head

def delete(head, data):
    '''This will be a deletion based on data'''
    head1=head; prev=Node(None)
    prev.next=head
    while(head.val != data):
        prev=head
        head=head.next

    if not head.prev:
        prev=head
        head=head.next
        prev.next=None
        head.prev=None
        return head
    else:
        prev.next=head.next
        head.next.prev=prev
        head.next=head.prev=None

        return head1




