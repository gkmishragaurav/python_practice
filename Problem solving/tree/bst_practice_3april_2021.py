class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def print_inorder(root):
    if root.left:
        print_inorder(root.left)

    print (root.value)

    if root.right:
        print_inorder(root.right)
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
def search(root, item):
    # this is for search item in bst
    if root:
        if item < root.value:
            return search(root.left, item)

        elif item > root.value:
            return search(root.right, item)

        elif item == root.value:
            return True

    return False
root = make_tree()
# print_inorder(root)
def find_min(root):
    if root.left:
        return find_min(root.left)

    else:
        return root.value
def insert(root, item):
    if root.value > item:
        if root.left:
            insert(root.left, item)
        else:
            root.left = BST(item)

    else:
        if root.right:
            insert(root.right, item)
        else:
            root.right = BST(item)
def get_minimum(root):
    while root.left:
        root=root.left

    return root.value
def delete(root, item, parent=None):
    if root.value > item:
        delete(root.left, item, root)

    elif root.value < item:
        delete(root.right, item, root)

    else:
        # we found the node to delete, now actual delete
        if not root.left and not root.right:
            # deletion of leaf nodes
            if parent.left == root:
                parent.left = None

            else:
                parent.right = None

        elif root.left and root.right:
            # delete when both leaf are there
            value = get_minimum(root.right)
            root.value = value
            delete(root.right, value, root)

        elif root.left:
            if parent:
                if parent.left == root:
                    parent.left = root.left

                else:
                    parent.right = root.left

            else:
                # deletion of root node
                root=root.left

        elif root.right:
            if parent:
                if parent.left == root:
                    parent.left = root.right

                else:
                    parent.right = root.right

            else:
                root=root.right
def validateBst_helper(tree, minvalue, maxvalue):
    if not tree:
        return True

    if tree.value < minvalue or tree.value >= maxvalue:
        print(tree.value, maxvalue, minvalue)
        return False

    check_left = validateBst_helper(tree.left, minvalue, tree.value)
    return check_left and validateBst_helper(tree.right, tree.value, maxvalue)
def validateBst(tree):
    return validateBst_helper(tree, float('-inf'), float('inf'))
def LCA(root, node1, node2):
    # returns least common ancestor of node1/node2
    if root.value < node1.value and root.value < node2.value:
        return LCA(root.left, node1, node2)

    elif root.value > node1.value and root.value > node2.value:
        return LCA(root.left, node1, node2)

    else:
        return root.value
def height_bst(root):
    pass
array=[]
def kth_largest_bst_util(root):
    global array
    if root == None:
        exit()

    if root.right:
        right = kth_largest_bst_util(root.right)
        if right:
            return right

    array.append(root.value)

    if root.left:
        left = kth_largest_bst_util(root.left)
        if left:
            return left
def findKthLargestValueInBst(root, k):
    kth_largest_bst_util(root)
    return array[k-1]
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


print(level_order_traversal(root))
