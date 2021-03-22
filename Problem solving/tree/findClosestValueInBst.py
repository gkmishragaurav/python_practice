# Given a binary search tree and a target node K. 
# The task is to find the node with minimum absolute difference with given target value K.
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(root, target):
    return _findClosestValueInBst(root, target, root.value)

def _findClosestValueInBst(root, target, closest):
    if not closest:
        closest = root.value
    else:
        temp = abs(root.value - target)
        if temp < abs(closest - target):
            closest = root.value

    if root.left:
        closest= _findClosestValueInBst(root.left, target, closest)

    if root.right:
        closest= _findClosestValueInBst(root.right, target, closest)

    return closest

def printInorderTree(root):
    if root.left:
        printInorderTree(root.left)

    print(root.value,)

    if root.right:
        printInorderTree(root.right)

b1=BST(10);b2=BST(8);b3=BST(9)
b4=BST(11);b5=BST(112)
b1.left=b2;b2.right=b3
b1.right=b4;b4.right=b5
printInorderTree(b1)
print(findClosestValueInBst(b1, 2))
