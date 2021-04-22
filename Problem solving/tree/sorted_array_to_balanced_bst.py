# Sorted Array to Balanced BST
# Given a sorted array. 
# Write a function that creates a Balanced Binary Search Tree using array elements.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    queue=[]
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        print (temp.value, end = ' ')
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

def sorted_array_to_balanced_bst(a):
    if not a:
        return
    mid = int(len(a)/2)
    root = BST(a[mid])
    root.left = sorted_array_to_balanced_bst(a[:mid])
    root.right = sorted_array_to_balanced_bst(a[mid+1:])

    return root

head = sorted_array_to_balanced_bst([1,2,3,4,5,6,7,8,9])
level_order_traversal(head)
