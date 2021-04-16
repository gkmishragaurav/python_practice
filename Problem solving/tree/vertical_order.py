# Q. https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def make_tree():
    b1=BST(1);b2=BST(2);b3=BST(3);b4=BST(4);b5=BST(5)
    b6=BST(6);b7=BST(7);b8=BST(8);b9=BST(9)#;b10=BST(10)
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
        print (temp.value,)
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)
def vertical_order(root):
    vertical={}
    queue = [(root, 0)]
    while queue:
        temp, level = queue.pop(0)
        if level in vertical.keys():
            vertical[level].append(temp.value)
        else:
            vertical[level] = [temp.value]

        if temp.left:
            queue.append((temp.left, level-1))

        if temp.right:
            queue.append((temp.right, level+1))

    return vertical

root = make_tree()
# level_order_traversal(root)
vertical = vertical_order(root)
keys = [key for key in vertical.keys()]
keys.sort()
for key in keys:
    print (vertical[key])

