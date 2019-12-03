import os, inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# print currentdir
parentdir = os.path.dirname(currentdir)
# print parentdir
sys.path.insert(0, parentdir)

import LinkList.node as ll

class stack:
    '''This class is to make a stack using linklist'''
    def __init__(self):
        self.stack = ll.arr_to_linklist([])
        self.size = 0

    def append(self, data):
        node=ll.Node(data)
        self.stack = ll.insert_at_start(self.stack, node)
        self.size+=1

    def pop(self):
        if self.top():
            current, self.stack = ll.delete_head(self.stack)
            self.size-=1
            return current.val, self.stack

    def top(self):
        if self.size:
            return self.stack.val
        return None

    def print_stack(self):
        head=self.stack
        while(head):
            print head.val,
            head=head.next
        return

ss=stack()
ss.append(1);ss.append(2);ss.append(3)
print ss.top()
ss.print_stack()
print ss.size
print ss.pop()
print ss.pop()
print ss.pop()
print ss.pop()
ss.print_stack()
print ss.size


