import tree

class Tree:
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None

    def get_root(self):
        return self.val

    def min_value_in_tree(self, node):
        while(node.left):
            node = node.left

        return node.val

    def max_value_in_tree(self, node):
        while(node.right):
            node = node.right

        return node.val

    def insert(self, data):
        # Compare the new value with the parent node
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def printInorderTree(self):

        if self.left:
            self.left.printInorderTree()

        print self.val,

        if self.right:
            self.right.printInorderTree()

    def printPostorderTree(self):

        if self.left:
            self.left.printPostorderTree()

        if self.right:
            self.right.printPostorderTree()

        print self.val,

    def printPreorderTree(self):
        print self.val,

        if self.left:
            self.left.printPreorderTree()

        if self.right:
            self.right.printPreorderTree()

    def get_child(self):
        left=None;right=None

        if self.left is not None:
            left = self.left.val

        if self.right is not None:
            right = self.right.val

        return left, right

def get_parent(node, value):

    if node:
        if node.left and node.left.val == value:
            return node

        if node.right and node.right.val == value:
            return node

        if node.val > value:
            return get_parent(node.left, value)

        if node.val < value:
            return get_parent(node.right, value)

    return

def search(node, value):
    '''
    :param node: This will represent the root of the tree at start.
    :param value: The value that we need to delete.
    :return: Node, which will be on node that has this value.
    '''
    if node:
        if node.val == value:
            return node

        if node.val > value:
            return search(node.left, value)

        if node.val < value:
            return search(node.right, value)

    return

def delete(node, value):
    parent = get_parent(node, value)
    # print parent.val
    current = search(node, value)
    if not current.left and not current.right:
        if parent.left.val == current.val:
            parent.left = None

        elif parent.right.val == current.val:
            parent.right = None

    elif current.left and not current.right:
        if parent.left.val == current.val:
            parent.left = current.left

        elif parent.right.val == current.val:
            parent.right = current.left

    elif not current.left and current.right:
        if parent.left.val == current.val:
            parent.left = current.right

        elif parent.right.val == current.val:
            parent.right = current.right

    else:
        # Both of the child exists.
        # find min value in right sub tree. This will be inorder successor.
        in_order_successor =  current.right.min_value_in_tree(current.right)
        in_order_successor_parent = get_parent(node, in_order_successor)

        if in_order_successor_parent.left.val == in_order_successor:
            in_order_successor_parent.left = None

        elif in_order_successor_parent.right.val == in_order_successor:
            in_order_successor_parent.right = None

        current.val = in_order_successor

    return



a = [97,28, 152, 25, 32, 142, 160, 23, 26, 132, 145, 155, 170]
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
n1=root

print('In order-')
root.printInorderTree()

print 'pre order'
tree.pre_order(n1)
print '\nin order'
tree.in_order(n1)
print '\npost order'
tree.post_order(n1)
print '\nlevel order'
tree.level_order(n1)
print '\nmax=', tree.max_in_tree(n1)
print '\nmin=', tree.min_in_tree(n1)

print tree.search_in_tree(n1, 41)
tree.insert_in_tree(n1, 41)
print '\nlevel order11'
tree.level_order(n1)
print '\nSize', tree.size(n1)
tree.reverse_level_order(n1)
print '\nheight', tree.height(n1)
print '\nnon_recursive_depth', tree.non_recursive_depth(n1)
print '\nnumber_of_leaves', tree.number_of_leaves(n1)
print '\ndiameter', tree.diameter(n1)
print '\nsum_of_binary_tree', tree.sum_of_binary_tree(n1)
print '\nsum_of_binary_tree_iterative', tree.sum_of_binary_tree_iterative(n1)
print '\nmax_sum_level', tree.max_sum_level(n1)
print '\nroot_to_leaf_paths'
tree.root_to_leaf_path(n1, [])
print '\nsum_root_to_leaf_number'
tree.sum_root_to_leaf_number(n1,[])
print '\nsum_root_to_leaf_number1', tree.leaf_sum
tree.find_vertical_sum(n1, 0)
print '\nfind_vertical_sum', tree.sum_paths
tree.mirror_tree(n1)
print '\nPost mirror level order11'
tree.level_order(n1)
print '\nzigzag_traversal'
tree.zigzag_traversal(n1)

# print 'p',get_parent(root, 25).val
# delete(root, 25)
# print '\n'
# root.printInorderTree()
# root.insert(25)
# print '\n'
# root.printInorderTree()
# print 'p',get_parent(root, 25).val





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
