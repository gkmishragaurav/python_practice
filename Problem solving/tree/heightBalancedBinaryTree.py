# An empty tree is height-balanced. A non-empty binary tree T is balanced if:
# 1) Left subtree of T is balanced
# 2) Right subtree of T is balanced
# 3) The difference between heights of left subtree and right subtree is not more than 1.
#
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

def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right))+1

def heightBalancedBinaryTree(root):
    # Write your code here.
    queue=[]
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        l=height(temp.left)
        r=height(temp.right)
        if abs(l-r) > 1:
            return False

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    return True

root = make_tree()
print(heightBalancedBinaryTree(root))

