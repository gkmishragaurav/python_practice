# Given a binary tree in which each node element contains a number.
# Find the maximum possible sum from one leaf node to another.
# The maximum sum path may or may not go through root.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def make_tree():
    b1=BST(1);b2=BST(2);b3=BST(3);b4=BST(4);b5=BST(5)
    b6=BST(6);b7=BST(7);b8=BST(8);b9=BST(9);b10=BST(10)
    b11=BST(11);b12=BST(12)

    root=b1
    b1.left=b2;b1.right=b3
    b2.left=b4;b2.right=b5
    b3.right=b6
    b5.left=b7;b5.right=b8
    b6.left=b9;b6.right=b10

    return root
def level_order_traversal(root):
    queue=[]
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        print (temp.value,)
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

def right_view_util(root, level, last):
    if not root:
        return

    if last[0] < level:
        print(root.value)
        last[0] = level

    right_view_util(root.left, level+1, last)
    right_view_util(root.right, level+1, last)

def right_view_bt(root):
    last = [0]
    right_view_util(root, 1, last)
    print(last)

root = make_tree()
print(right_view_bt(root))
