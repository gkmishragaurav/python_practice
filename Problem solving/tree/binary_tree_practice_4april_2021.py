class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def make_tree():
    b1=BST(10);b2=BST(25);b3=BST(5);b4=BST(12);b5=BST(21)
    b6=BST(23);b7=BST(14);b8=BST(15);b9=BST(22)

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
def find_max(root, maxi):
    # method1 - use level order traversal to find max - use above function to get that
    # method2 - traverse whole tree to get the maximum. - this is implementing
    if not root:
        return maxi

    if root.value > maxi:
        maxi = root.value

    if root.left:
        return find_max(root.left, maxi)

    if root.right:
        return find_max(root.right, maxi)

    return maxi
def insert(root, item):
    # in a binary tree we can insert at any spot, however
    # inserting at first node with empty left/right node
    queue = []
    queue.append(root)
    while(queue):
        temp = queue.pop(0)
        if temp.left and temp.right:
            queue.append(temp.left)
            queue.append(temp.right)

        elif not temp.left:
            temp.left = BST(item)
            break

        elif not temp.right:
            temp.right = BST(item)
            break
def size(root):
    if not root:
        return 0

    return size(root.left) + size(root.right) +1
def height_recursive(root):
    # recursive solution
    if not root:
        return 0
    return max(height_recursive(root.left), height_recursive(root.right))+1
def height(root):
    queue=[]
    queue.append((root,0))
    dep=1
    while queue:
        temp = queue.pop(0)
        if temp[0].left:
            queue.append((temp[0].left, temp[1]+1))

        if temp[0].right:
            queue.append((temp[0].right, temp[1]+1))

        dep = temp[1]+1

    return dep
def deepest_node(root):
    queue=[]
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        # print (temp.value,)
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    return temp.value
def delete(root, item):
    if not root: return
    queue=[]
    queue.append((None, root))
    while queue:
        parent, temp = queue.pop(0)
        if temp.value == item:
            if parent:
                if not temp.left and not temp.right:
                    if parent.left == temp:
                        parent.left = None
                    else:
                        parent.right = None

                elif temp.left and temp.right:
                    value = deepest_node(temp)
                    temp.value = value
                    delete(root.left, value)
                    delete(root.right, value)

                elif temp.left:
                    if parent.left == temp:
                        parent.left = temp.left
                    else:
                        parent.right = temp.left

                elif temp.right:
                    if parent.left == temp:
                        parent.left = temp.right
                    else:
                        parent.right = temp.right
            else:
                value = deepest_node(temp)
                temp.value = value
                delete(root.left, value)
                delete(root.right, value)

        if temp.left:
            queue.append((temp, temp.left))

        if temp.right:
            queue.append((temp, temp.right))

    return
def diameter(root):
    pass
def find_level_with_max_sum(root):
    queue=[]
    queue.append((root,0))
    max_sum = float("-inf")
    max_level = 0
    current_sum = 0
    current_level = 0
    while queue:
        temp, level = queue.pop(0)
        if current_level == level:
            current_sum = current_sum+temp.value
            if max_sum < current_sum:
                max_sum = current_sum
                max_level = level
        else:
            current_level = level+1
            current_sum = 0
        if temp.left:
            queue.append((temp.left, level+1))

        if temp.right:
            queue.append((temp.right, level+1))

    return max_level, max_sum
def root_to_leaf_path(root, paths):
    '''This will give all root to leaf paths, return will be a list'''
    if not root:
        return 0

    paths.append(root.value)

    if not root.left and not root.right:
        print (paths)

    if root.left:
        root_to_leaf_path(root.left, paths)
    if root.right:
        root_to_leaf_path(root.right, paths)
    paths.pop()
def max_root_to_leaf_path(root, current_sum, max_sum):
    if not root:
        return

    current_sum = current_sum + root.value
    if not root.left and not root.right:
        if max_sum < current_sum:
            max_sum = current_sum
            print(max_sum)
        current_sum = 0

    if root.left:
        max_root_to_leaf_path(root.left, current_sum, max_sum)
    if root.right:
        max_root_to_leaf_path(root.right, current_sum, max_sum)
def mirror_tree(root):
    if root.left:
        mirror_tree(root.left)

    if root.right:
        mirror_tree(root.right)

    if not root.left and not root.right:
        return 0
    if root.left and root.right:
        root.left, root.right = root.right, root.left
    if not root.left and root.right:
        root.left, root.right = root.right, root.left
    if root.left and not root.right:
        root.left, root.right = root.right, root.lefti
def zigzag_level_order(root):
    stack1 = [root]
    stack2 = []
    current = "stack1"
    while stack1 or stack2:
        if current == "stack1":
            temp = stack1.pop()
            print(temp.value)
            if temp.left:
                stack2.append(temp.left)
            if temp.right:
                stack2.append(temp.right)
            if not stack1:
                current = "stack2"

        else:
            temp = stack2.pop()
            print(temp.value)
            if temp.right:
                stack1.append(temp.right)
            if temp.left:
                stack1.append(temp.left)
            if not stack2:
                current = "stack1"


root = make_tree()
# insert(root, 4)
# delete(root, 10)
zigzag_level_order(root)

