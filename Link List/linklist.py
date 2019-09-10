import pdb
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

id = 0

class LinkedList:
    def __init__(self):
        self.head = None
        global id
        id += 1
        self.length = id

    def print_list(self):
        print "\nPrinting List-\n"
        temp=self.head
        while(temp):
          print temp.data,
          temp = temp.next

    def push(self, data):
        temp = Node(data)
        if self.head is None:
          self.head = temp
          return
        last = self.head
        while (last.next):
            last = last.next
        last.next = temp

    def delete(self, key):
        if self.head is None:
            print "Empty list, can't delete"
            return
        prev = self.head
        while prev.next:
            if prev.data == key:
                self.head=self.head.next
                prev.next=None
                return
            if prev.next.data == key:
                prev.next = prev.next.next
                return
            prev = prev.next

    def find_last(self):
        last = self.head
        while last.next:
            last=last.next
        return last

    def find_middle(self):
        mid = self.head
        last = self.head
        while last.next:
            last = last.next
            if last.next:
                last = last.next
                mid = mid.next
        return mid

    def first(self):
        return self.head.data

    def find_kth_from_last(self, k):
        mark = self.head
        temp = self.head
        i=0
        while mark.next:
            mark=mark.next
            i=i+1
            if i >= k:
                temp = temp.next
        print '-',temp.data

    def size(self):
        curr = self.head
        count = 0
        while(curr):
            count=count+1
            curr = curr.next

        return count

def mearge_linklist(l1,l2, sorted=True):
    # This function is for merging two sorted link list to make a 3rd list.
    l3 = LinkedList()

    head1 = l1.head
    head2 = l2.head

    if sorted:
        while head1 and head2:
            if head1 and head2:
                if head1.data > head2.data:
                    l3.push(head2.data)
                    head2=head2.next

                elif head1.data < head2.data:
                    l3.push(head1.data)
                    head1 = head1.next

                else:
                    l3.push(head1.data)
                    head1 = head1.next
                    l3.push(head2.data)
                    head2 = head2.next

    while head1:
        l3.push(head1.data)
        head1 = head1.next

    while head2:
        l3.push(head2.data)
        head2 = head2.next

    return l3

def reverse_linklist(ll):
    prev = None
    current = ll.head
    while(current):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    ll.head = prev

def break_linklist_from_mid(ll):
    mid = ll.find_middle()
    head1 = mid.next
    mid.next = None
    l2 = LinkedList()
    while(head1):
        l2.push(head1.data)
        head1=head1.next
    return ll, l2

def is_same_linklist(ll1, ll2):
    top1 = ll1.head
    top2 = ll2.head
    while (top2):
        if top1.data != top2.data:
            return False
        top1=top1.next
        top2=top2.next
    return True

def is_Palendrom(ll):
    # This function will check if a link list is palendrom or not.
    ll1, ll2 = break_linklist_from_mid(ll)
    ll1.print_list()
    ll2.print_list()
    reverse_linklist(ll2)
    status = is_same_linklist(ll1, ll2)
    reverse_linklist(ll2)
    mearge_linklist(ll1, ll2, False)
    return status

def reverse_chunk_2(ll):
    first = ll.head
    second = first.next
    while(second.next and first.next):
        first.data, second.data = second.data, first.data
        if second.next:
            first = second.next
        if first.next:
            second = first.next
    if not second.next:
        first.data, second.data = second.data, first.data

def reverse_linklist_modified(ll, end):
    prev = None
    current = ll.head
    while(current):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    ll.head = end

def reverse_chunk_2_pointer(ll):
    first = ll.head
    second = first.next
    three = second.next
    new_list = LinkedList()
    while(1):
        temp_list = LinkedList()
        temp_list.push(first.data)
        temp_list.push(second.data)
        reverse_linklist_modified(temp_list, three)
        mearge_linklist(new_list, temp_list)
        first=three;second=first.next;three=second.next
    ll.print_list()

def create_loop(ll, value):
    current = ll.head
    loop_end = ll.head
    while(current.next):
        if current.data == value:
            loop_end = current
        current=current.next

    current.next = loop_end

def detect_loop(ll):
    slow=ll.head
    fast= slow.next
    while(fast):
        if fast == slow:
            return 'yes'
        slow=slow.next
        fast=fast.next
        if fast:
            fast = fast.next

    return 'No'

def remove_loop(ll):
    if detect_loop(ll) == 'yes':
        _hash = {}
        slow = ll.head
        while (1):
            if not _hash.has_key(slow.next):
                _hash[slow.next] = {}

            else:
                break
        slow1 = slow.next
        while(slow1.next != slow):
            slow1 = slow1.next

        slow1.next = None

def  add_linklist(l1,l2):
    # You are given two non-empty linked lists representing two non-negative integers.
    # The digits are stored in reverse order and each of their nodes contain a single digit.
    # Add the two numbers and return it as a linked list.
    # You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    # Example:
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.
    l3=LinkedList()
    first=l1.head
    second=l2.head
    carry=0
    while(first and second):
        l3.push((first.data+second.data+carry)%10)
        carry = (first.data+second.data+carry)/10
        first=first.next
        second=second.next

    if first:
        while(first):
            l3.push((first.data+carry)%10)
            carry = (first.data + carry)/10
            first = first.next

    if second:
        while(second):
            l3.push((second.data+carry)%10)
            carry = (second.data + carry)/10
            second = second.next

    if carry:
        while(carry):
            l3.push(carry%10)
            carry=carry/10

    return l3

def list_intersection_point(l1, l2):
    #Write a program to find the node at which the intersection of two singly linked lists begins.

    # 1. If the two linked lists have no intersection at all, return null.
    # 2. The linked lists must retain their original structure after the function returns.
    # 3. You may assume there are no cycles anywhere in the entire linked structure.
    # 4. Your code should preferably run in O(n) time and use only O(1) memory.
    c1 = l1.size()
    c2 = l2.size()
    first = l1.head
    second = l2.head
    if c1>c2:
        i=0
        while(i<c1-c2):
            first=first.next
            i=i+1
    else:
        i = 0
        while (i < c2 - c1):
            second = second.next
            i = i + 1

    while(l1):
        if first.next == second.next:
            return first.next.data, first.next

        first=first.next
        second=second.next

    return None

duplicates = []
def remove_duplicates(l1):
    # Given a sorted linked list, delete all duplicates such that each element appear only once.
    first=l1.head
    while(first and first.next):
        if first.data == first.next.data:
            if first.data not in duplicates:
                duplicates.append(first.data)
            temp = first.next
            first.next = first.next.next
            temp.next=None
        else:
            first=first.next

    return l1

def remove_all_duplicates(l1):
    print duplicates

    for x in duplicates:

        if l1.size() == 1:
            l1 = LinkedList()
        l1.delete(x)

def mearge_linklist2(head1, head2):
    # This function is for merging two sorted link list to make a 3rd list.
    while head1 and head2:
        if head1.data > head2.data:
            pdb.set_trace()
            temp = Node(head2.data)
            head2=head2.next
            temp.next = head1
            head1=temp
            print head1.data

        elif head1.data < head2.data:
            head1 = head1.next

        else:
            temp = Node(head2.data)
            temp1 = head1.next
            head1.next = temp
            temp.next=temp1
            head2 = head2.next

    while head2:
        l1.push(head2.data)
        head2 = head2.next

    return l1

def rotate_linklist(ll, k):
    # Given a list, rotate the list to the right by k places, where k is non-negative.

    size=ll.head;count=0
    while(size):
        size=size.next
        count+=1

    k=k%count
    print k, count
    if k:
        second = ll.head
        first = ll.head
        if not first.next:
            return ll

        i=0
        while(i<k):
            first=first.next
            i=i+1

        while(first.next):
            first=first.next
            second=second.next

        three=second.next
        # pdb.set_trace()

        first.next=ll.head
        second.next=None
        ll.head=three

    return ll


if __name__ == '__main__':
    # Start with the empty list
    # pdb.set_trace()
    l1 = LinkedList()
    arr = [3, 2]
    while(arr):
        l1.push(arr.pop(0))

    l1 = rotate_linklist(l1, 1)
    l1.print_list()
    print 'length',l1.length








    # l1 = mearge_linklist2(l1.head, l2.head)
    # l1.print_list()


    ##### list_intersection_point

    # l2 = LinkedList()
    # arr = [9,6]
    # while (arr):
    #     l2.push(arr.pop(0))
    # # l2.print_list()
    #
    # l3 = LinkedList()
    #
    # arr = [1, 2]
    # while (arr):
    #     l3.push(arr.pop(0))
    #
    # last1 = ll.find_last()
    # last1.next = l3.head
    # ll.print_list()
    #
    # last2 = l2.find_last()
    # last2.next = l3.head
    # l2.print_list()
    #
    # print ll.size()
    #
    # print list_intersection_point(ll, l2)
    # ------------------------------------------------

    # l3 = add_linklist(ll, l2)
    #
    # reverse_linklist(l3)
    # l3.print_list()



    # create_loop(ll, 1)
    # # ll.print_list()
    # print detect_loop(ll)
    # remove_loop(ll)
    # ll.print_list()





    # print is_Palendrom(ll)
    # ll.print_list()
    # reverse_linklist(ll)
    # ll.print_list()

    # ll1 = LinkedList()
    # arr1 = [3,4,5,6]
    # for x in arr1:
    #     ll1.push(x)
    #
    # ll.print_list()
    # ll1.print_list()
    # l3 = mearge_linklist(ll, ll1)
    # l3.print_list()

  # ll.print_list()

  # ll.delete(1)
  # # ll.print_list()
  # ll.delete(8)
  # # ll.print_list()
  # # ll.push(2)
  # # ll.print_list()
  # print ll.find_last()
  # print ll.find_middle()
  # print ll.first()
  # ll.print_list()
  # ll.find_kth_from_last(4)
