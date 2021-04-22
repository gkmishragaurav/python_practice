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
    b1.right=b3
    b2.left=b4
    b3.right=b6
    b5.left=b7;b5.right=b8
    b6.left=b9;b6.right=b10
    b10.left=b11;b11.right=b12
    b9.left=b5
    b7.left=b2

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
def height(root):
    if not root:
        return 0

    l = height(root.left)
    r = height(root.right)

    return 1+max(l, r)
max_l = float('-inf')
max_v = None
def max_leaf_2_leaf(root):
    global max_l
    global max_v
    if not root:
        return 0

    l = height(root.left)
    r = height(root.right)

    if max_l < l+r+1:
        max_l = l+r+1
        max_v = root.value

    if root.left:
        max_leaf_2_leaf(root.left)

    if root.right:
        max_leaf_2_leaf(root.right)

root = make_tree()
print(height(root))
max_leaf_2_leaf(root)
print("max_l-",max_l)
print("max_v-",max_v)
