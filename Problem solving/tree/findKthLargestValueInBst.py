# Q. https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/
# Given a Binary Search Tree (BST) and a positive integer k, find the k’th largest element in the Binary Search Tree.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def make_tree():
    b1=BST(10);b2=BST(5);b3=BST(5);b4=BST(2);b5=BST(1)
    b6=BST(13);b7=BST(14);b8=BST(15);b9=BST(22)

    root=b1
    b1.left=b2;b1.right=b8
    b2.left=b4;b2.right=b3
    b4.left=b5

    b8.left=b6;b8.right=b9
    b6.right=b7
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

def kth_largest_bst_util(root, array):
    if root == None:
        exit()

    if root.right:
        kth_largest_bst_util(root.right, array)

    array.append(root.value)

    if root.left:
        kth_largest_bst_util(root.left, array)

def findKthLargestValueInBst(root, k):
    array=[]
    kth_largest_bst_util(root, array)
    return array[k-1]

root = make_tree()
# level_order_traversal(root)
kth = findKthLargestValueInBst(root, 2)
print(kth)
