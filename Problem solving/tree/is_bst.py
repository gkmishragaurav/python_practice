class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def make_tree():
    b1=BST(10);b2=BST(5);b3=BST(5);b4=BST(2);b5=BST(1)
    b6=BST(13);b7=BST(14);b8=BST(15);b9=BST(2)

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
        print (temp.value,end = ' ')
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

def is_bst(root):
    def helper(root, mini, maxi):
        if not root:
            return True

        if mini >= root.val:
            return False

        if maxi <= root.val:
            return False

        l = helper(root.left, mini, root.val)
        return l and helper(root.right, root.val, maxi)
        
    return helper(root, float('-inf'), float('inf') )


root=make_tree()
level_order_traversal(root)
print(is_bst(root))
