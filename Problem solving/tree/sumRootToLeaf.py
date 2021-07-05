# You are given the root of a binary tree where each node has a value 0 or 1.  
# Each root-to-leaf path represents a binary number starting with the most significant bit.  
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def make_tree():
    b1=BST(1);b2=BST(0);b3=BST(1);b4=BST(0);b5=BST(0)
    b6=BST(0);b7=BST(1);b8=BST(0);b9=BST(1)#;b10=BST(10)
    b11=BST(11);b12=BST(12)

    root=b1
    b1.left=b2;b1.right=b3
    b2.left=b4;b2.right=b5
    b3.left=b6;b3.right=b7
    b6.right=b8
    b7.right=b9

    # b5.left=b7;b5.right=b8
    # b6.left=b9#;b6.right=b10

    return root
def level_order_traversal(root):
    queue=[]
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        print (temp.value, end=' ')
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

def list_to_char(li):
    return ''.join(li)
def bit_to_dec(bi):
    return int(bi, 2)

def sumRootToLeaf(root):
    def root_to_leaf(root, arr):
        if not root:
            return
        arr.append(str(root.value))
        if not root.left and not root.right:
            temp.append(bit_to_dec(list_to_char(arr)))

        root_to_leaf(root.left, arr)
        root_to_leaf(root.right, arr)
        arr.pop()

    temp=[0]
    root_to_leaf(root, [])
    return sum(temp)
root = make_tree()
level_order_traversal(root)
print('\n')
x=sumRootToLeaf(root)
print(x)

