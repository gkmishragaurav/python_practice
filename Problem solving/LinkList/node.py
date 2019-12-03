import gc

class Node(object):
    def __init__(self, data=None):
        self.val = data
        self.next = None

    def setVal(self, data):
        self.val = data

    def getVal(self):
        return self.val

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

def print_linklist(head):
    if not head: print []
    while(head):
        print head.val,
        head=head.next
    print '\n'

def make_link_list(arr=None):
    '''This will give you a dummy linklist'''
    head=None
    if not arr:
        head=Node(1);n2=Node(2);n3=Node(3);n4=Node(4);n5=Node(5)
        head.setNext(n2);n2.setNext(n3);n3.setNext(n4);n4.setNext(n5);n5.next = None
    else:
        #yet to write
        pass
    return head

def arr_to_linklist(arr):
    '''An arr is given and a linklist need to make.'''
    head=None
    if arr:
        for item in arr:
            head=make_linklist(head, Node(item))
    return head

def make_linklist(head, node):
    '''
    :param head: head of a link list, object of a Node class
    :param node: the node that to be enter, object of a Node class
    :return: head node for linklist
    '''
    if not head:
        insert = insert_at_start
    else:
        insert = insert_at_last

    return insert(head, node)

def insert_at_start(head, node):
    '''Insert at the start of linklist, return will be new head of linklist'''
    node.next=head
    head=node
    return head

def insert_at_last(head, node):
    '''Insert at the last of linklist'''
    last=head
    while(last.next):
        last=last.next
    last.setNext(node)
    return head

def append(head, node, pos):
    if pos==0:
        head = insert_at_start(head, node)
    else:
        head = insert_at_mid(head, node, pos)
    return head

def insert_at_mid(head, node, pos):
    '''Insert at some pos from head.'''
    mid=head
    count=1
    while(count!=pos):
        mid=mid.next
        count+=1
    if mid:
        temp=mid.next; mid.next=node
        node.next=temp
    else:
        raise TypeError('Value of pos is more than length of linklist.')
    return head

def clear_listlist(head):
    head=None
    return head

def delete_node_linklist(head, prev, node):
    if not prev:
        head = head.next
        node.next = None
    else:
        prev.next = node.next
        node.next = None

    return head, prev, node

def delete_head(head):
    current=head
    head=head.next
    current.next=None
    return current, head

def delete_duplicate(head):
    current=head
    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current=current.next

    return head

def delete_by_data(head, data):
    '''
    This is for delete based on data.
    :param head: head of linklist
    :param data: data of note to be deleted
    :return: Head node for linklist
    '''
    prev=None
    node=head
    count=0
    while(node):
        if node.val == data:
            count+=1
            head, prev, node = delete_node_linklist(head, prev, node)
        prev=node;node=node.next
    if prev:
        if prev.val == data:
            delete_by_data(head, data)

    return head

def merge_two_linklist(head1, head2):
    '''This function is for merging 2 linklist in-place'''
    prev=dummy=Node(None)
    while(head1 and head2):
        if head1.val <= head2.val:
            prev.next=head1
            head1=head1.next
        else:
            prev.next=head2
            head2=head2.next
        prev=prev.next

    prev.next = head1 or head2
    return dummy.next

def find_middle(head):
    '''This will find the middle of a link list'''
    last=head
    while(last and last.next):
        head=head.next
        last=last.next.next

    return head.val, head

def reverse(head):
    '''This is to reverse a link list.'''
    prev=None;first=head
    while(first):
        sec = first.next
        first.next = prev
        prev=first
        first=sec
    return prev

def make_loop(head, value):
    '''This will make a random loop in linklist, based on the value of the node.'''
    first=head;end=None
    while(first.next):
        if first.val == value:
            end=first
        first=first.next
    first.next=end
    return head

def detect_loop(head):
    '''This will detect a loop in a linklist.'''
    fast=head;slow=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            return True, fast, slow

    return False, fast, slow

def find_head_of_loop(head):
    '''This will find the head of the loop, if detect loop is True.'''
    status, fast, slow = detect_loop(head)
    if status:
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
    return False

def length_of_loop(head):
    status, fast, slow = detect_loop(head)
    if status:
        count=0;temp=None
        while(1):
            if count==0:
                temp=fast
            fast=fast.next
            count+=1
            if fast == temp:
                return count

def copy_linklist(head):
    '''This will copy linklist and return new linklist head'''
    head1=Node(None)
    while(head):
        head1 = make_linklist(head1, Node(head.val))
        head=head.next
    return head1.next

def compare(head1, head2):
    while(head1 or head2):
        if head1.val != head2.val:
            return False
        head1=head1.next;head2=head2.next

    if head1 or head2:
        return False

    return True

def isPelindrome(head):
    head1=reverse(copy_linklist(head))
    if compare(head, head1):
        return True
    return False

def intersection_link_list(head1, head2, head3):
    '''Making Intersection of Two Linked Lists, head1 and head2 will point to head3.'''
    while(head1.next):
        head1=head1.next

    while(head2.next):
        head2=head2.next

    head1.next, head2.next=head3,head3

def find_intersaction_linklist(head1, head2):
    '''This will find the intersection of two given link list.'''
    len1=0;len2=0
    if not head1 and not head2:
        return None
    head11=head1;head22=head2
    while(head1):
        len1+=1
        head1=head1.next
    while(head2):
        len2+=1
        head2=head2.next

    if head1 != head2: return False
    diff = abs(len2-len1)

    if len2>len1:
        while(diff):
            head22=head22.next
            diff-=1
    else:
        while (diff):
            head11 = head11.next
            diff -= 1

    while (head11 != head22):
        head11 = head11.next
        head22 = head22.next

    gc.collect()
    return head11

def linklist_to_num(head):
    num=0
    while(head):
        num=num*10+head.val
        head=head.next
    return num

def num_to_linklist(num):
    head=None
    while(num):
        head = make_linklist(head, Node(num%10))
        num=num/10

    return head

def add_two_linklist_2(head1, head2):
    total=linklist_to_num(head1) + linklist_to_num(head2)
    if total:
        return reverse(num_to_linklist(total))

    return Node(0)

def oddEvenList(head):
    '''All odd nodes at top and all even nodes at end.Note that this is on the basis of node order and not value.'''
    # The first node is considered odd, the second node even and so on
    odd=oldhead=Node(None)
    even=evenhead=Node(None)
    count=1
    while(head):
        if count%2:  #odd
            if not oldhead:
                oldhead=oldhead.next
            odd.next=head
            odd=odd.next
        else:   #even
            if not evenhead:
                evenhead=evenhead.next
            even.next=head
            even=even.next
        head=head.next
        count+=1
    even.next=None
    odd.next=evenhead.next
    return oldhead.next

def recursive_sum(head, sum=0):
    '''Recursive code to find the sum for all nodes in linklist'''
    if not head:
        return sum

    return recursive_sum(head.next, sum+head.val)















