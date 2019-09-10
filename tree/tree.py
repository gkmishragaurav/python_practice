import pdb

class Tree:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    def get_root(self):
        return self.data

    def min_value_in_tree(self, node):
        while(node.left):
            node = node.left

        return node.data

    def max_value_in_tree(self, node):
        while(node.right):
            node = node.right

        return node.data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printInorderTree(self):

        if self.left:
            self.left.printInorderTree()

        print self.data,

        if self.right:
            self.right.printInorderTree()

    def printPostorderTree(self):

        if self.left:
            self.left.printPostorderTree()

        if self.right:
            self.right.printPostorderTree()

        print self.data,

    def printPreorderTree(self):
        print self.data,

        if self.left:
            self.left.printPreorderTree()

        if self.right:
            self.right.printPreorderTree()

    def get_child(self):
        left=None;right=None

        if self.left is not None:
            left = self.left.data

        if self.right is not None:
            right = self.right.data

        return left, right

def get_parent(node, value):

    if node:
        if node.left and node.left.data == value:
            return node

        if node.right and node.right.data == value:
            return node

        if node.data > value:
            return get_parent(node.left, value)

        if node.data < value:
            return get_parent(node.right, value)

    return

def search(node, value):
    '''
    :param node: This will represent the root of the tree at start.
    :param value: The value that we need to delete.
    :return: Node, which will be on node that has this value.
    '''
    if node:
        if node.data == value:
            return node

        if node.data > value:
            return search(node.left, value)

        if node.data < value:
            return search(node.right, value)

    return

def delete(node, value):
    parent = get_parent(node, value)
    # print parent.data
    current = search(node, value)
    if not current.left and not current.right:
        if parent.left.data == current.data:
            parent.left = None

        elif parent.right.data == current.data:
            parent.right = None

    elif current.left and not current.right:
        if parent.left.data == current.data:
            parent.left = current.left

        elif parent.right.data == current.data:
            parent.right = current.left

    elif not current.left and current.right:
        if parent.left.data == current.data:
            parent.left = current.right

        elif parent.right.data == current.data:
            parent.right = current.right

    else:
        # Both of the child exists.
        # find min value in right sub tree. This will be inorder successor.
        in_order_successor =  current.right.min_value_in_tree(current.right)
        in_order_successor_parent = get_parent(node, in_order_successor)

        if in_order_successor_parent.left.data == in_order_successor:
            in_order_successor_parent.left = None

        elif in_order_successor_parent.right.data == in_order_successor:
            in_order_successor_parent.right = None

        current.data = in_order_successor

    return

def mirror_tree(node):
    if not node.get_child():
        return
    else:
        if node.left and node.right:
            temp = node.left
            node.left = node.right
            node.right=temp
        elif node.left:
            node.right = node.left
            node.left=None
        else:
            node.left=node.right
            node.right=None

class Queue():
    def __init__(self):
        self.queue = []

    def set(self, value):
        self.queue.insert(0, value)

    def get(self):
        if self.queue:
            return self.queue.pop()

    def printQ(self):
        for x in self.queue:
            print x,

    def isEmpty(self):
        if self.queue: return True
        return False

def bfs_tree(node):
    # This is level order traversal for tree.
    q = Queue()
    q.set(node.data)
    left, right = node.get_child()
    q.set(left);q.set(right)
    print q.get(),
    if node.left:
        bfs_tree(node.left)
    if node.right:
        bfs_tree(node.right)
    # pdb.set_trace()


a = ['a', 'b', 'c']
root = Tree(a[0])
i=1
while (i<len(a)):
    root.insert(a[i])
    i=i+1

# root.insert(28)
# root.insert(35)
# root.insert(24)
print('In order-')
root.printInorderTree()
# print root.get_root()
# root.printInorderTree()
# bfs_tree(root)

mirror_tree(root)

print('In order-')
root.printInorderTree()



# print 'p',get_parent(root, 25).data
# delete(root, 25)
# print '\n'
# root.printInorderTree()
# root.insert(25)
# print '\n'
# root.printInorderTree()
# print 'p',get_parent(root, 25).data





# print root.max_value_in_tree(current)

# search_node= search(root, 100)
# if search_node:
#     print search_node.get_child()
# else:
#     print 'This node is not present'


# print('Post order-')
# root.printPostorderTree()
# print('Pre order-')
# root.printPreorderTree()
