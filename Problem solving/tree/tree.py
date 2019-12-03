class Node:
    def __init__(self, data=None):
        self.val=data
        self.left=None
        self.right=None

    def get_child(self):
        left=None;right=None

        if self.left is not None:
            left = self.left.val

        if self.right is not None:
            right = self.right.val

        return left, right

def pre_order(root):
    if not root:
        return
    print root.val,
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print root.val,
    in_order(root.right)

def post_order(root):
    if not root:
        return None
    post_order(root.left)
    post_order(root.right)
    print root.val,

def level_order(root):
    '''This is level order traversal of tree which is BFS in Graph.'''
    q=[]
    q.insert(0, root)
    while(len(q)):
        temp = q.pop()
        print temp.val,
        if temp.left:
            q.insert(0, temp.left)
        if temp.right:
            q.insert(0, temp.right)

def reverse_level_order(root):
    q=[]
    s=[]
    q.insert(0, root)
    while(len(q)):
        temp=q.pop()
        if temp.left:
            q.insert(0, temp.left)
        if temp.right:
            q.insert(0, temp.right)
        s.append(temp)

    while(len(s)):
        print s.pop().val,

def zigzag_traversal(root):
    current=[]
    nxt=[]
    reverse=False
    current.append(root)
    while(len(current)):
        temp = current.pop()
        print temp.val,
        if temp.left:
            nxt.append(temp.left)
        if temp.right:
            nxt.append(temp.right)
        if not len(current):
            if len(nxt):
                if reverse:
                    current=nxt
                else:
                    current = nxt[::-1]
                nxt=[]
                reverse= not reverse
            else:
                return

def mirror_tree(node):
    '''This will mirror the tree.'''
    if not node.get_child():
        return
    else:
        if node.left and node.right:
            node.left, node.right = node.right, node.left
        elif node.left:
            node.right = node.left
            node.left=None
        else:
            node.left=node.right
            node.right=None
        if node.left:
            mirror_tree(node.left)
        if node.right:
            mirror_tree(node.right)

m=float("-infinity")
def max_in_tree(root):
    global m
    if not root:
        return
    if root.val > m:
        m=root.val
    max_in_tree(root.right)
    max_in_tree(root.left)
    return m

m1=float("infinity")
def min_in_tree(root):
    global m1
    if not root:
        return
    if root.val < m1:
        m1=root.val
    min_in_tree(root.right)
    min_in_tree(root.left)
    return m1

def search_in_tree(root, data):
    if not root:
        return False
    if root.val == data:
        return True
    if not search_in_tree(root.left, data):
        if not search_in_tree(root.right, data):
            return False
        else: return True
    else: return True

def insert_in_tree(root, data):
    q=[]
    temp = Node(data)
    if not root:
        root = temp
        return root
    else:
        print root, root.val,
        q.insert(0, root)
        while(len(q)):
            tail = q.pop()
            if not tail.left:
                tail.left = temp
                return root
            elif not tail.right:
                tail.right = temp
                return root
            if tail.left:
                q.insert(0, tail.left)
            if tail.right:
                q.insert(0, tail.right)

def size(root):
    if not root:
        return 0
    return size(root.left)+size(root.right)+1

def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right))+1

def non_recursive_depth(root):
    if not root:
        return 0
    q=[]
    q.append([root,1])
    temp=0
    while(len(q)):
        node, depth = q.pop()
        depth = max(temp, depth)
        if node.left:
            q.append([node.left, depth+1])
        if node.right:
            q.append([node.right, depth+1])

    return depth

def number_of_leaves(root):
    if not root:
        return 0
    q=[]
    q.append(root)
    count=0
    while(len(q)):
        node = q.pop()
        if not node.left and not node.right:
            count+=1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return count

def diameter(root):
    if not root:
        return 0

    return height(root.left)+height(root.right)

def sum_of_binary_tree(root):
    if not root:
        return 0

    return sum_of_binary_tree(root.left)+sum_of_binary_tree(root.right)+ root.val

def sum_of_binary_tree_iterative(root):
    if not root:
        return 0
    q=[]
    q.append(root)
    sum_bt=0
    while(len(q)):
        node = q.pop()
        sum_bt+=node.val
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return sum_bt

def max_sum_level(root):
    '''This will give max sum at any level in a tree'''
    q=[]
    q.append(root)
    q.append(None)
    current_sum=max_sum=0
    level=maxlevel=1
    while(len(q)):
        node=q.pop(0)
        if node:
            current_sum+=node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        else:
            # New level.
            if max_sum < current_sum:
                max_sum = current_sum
                maxlevel = level
            current_sum=0
            if len(q):
                q.append(None)
                level += 1

    return max_sum

leaf_sum={}
def root_to_leaf_path(root, paths):
    '''This will give all root to leaf paths, return will be a list'''
    if not root:
        return 0

    paths.append(root.val)

    if not root.left and not root.right:
        print paths
        sum=0
        for item in paths:
            sum=sum+item
        leaf_sum[tuple(paths)] = sum

    if root.left:
        root_to_leaf_path(root.left, paths)
    if root.right:
        root_to_leaf_path(root.right, paths)
    paths.pop()

def sum_root_to_leaf_number(root, paths):
    '''This will give sum for each root to leaf path'''
    if not root:
        return 0
    paths.append(root.val)

    if not root.left and not root.right:
        sum=0
        for item in paths:
            sum=sum+item
        print sum

    if root.left:
        sum_root_to_leaf_number(root.left, paths)
    if root.right:
        sum_root_to_leaf_number(root.right, paths)
    paths.pop()

def find_sum_path(root, s):
    '''A sum is given, find a path for which this sum exists'''
    # its a variation of above code.
    pass

sum_paths={}
def find_vertical_sum(root, current):
    if not root:
        return 0

    if not sum_paths.get(current):
        sum_paths[current] = 0

    sum_paths[current] = sum_paths[current]+root.val
    find_vertical_sum(root.left, current-1)
    find_vertical_sum(root.right, current+1)

def all_ancestors(root, node, ancestor):
    '''This will return all the ancestor of a node'''
    if not root:
        return 0
    if root.left == node or root.right == node or all_ancestors(root.left, node, ancestor) or all_ancestors(root.right, node, ancestor):
        print root.val
        return 1

    return 0

def find_lca_of_two_node(root,):
    if not root:
        return 0

    left = find_lca_of_two_node(root.left)

def merge_two_binary_tree(root1, root2):
    # Given two binary trees and imagine that when you put one of them to cover the other,
    # some nodes of the two trees are overlapped while the others are not.
    # You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
    # then sum node values up as the new value of the merged node. Otherwise, the NOT null node will
    # be used as the node of new tree.
    pass

n1=Node(1);n2=Node(2);n3=Node(3);n4=Node(4);n5=Node(5);n6=Node(6);n7=Node(7)
n1.left=n2;n2.left=n4;n2.right=n5
n1.right=n3;n3.left=n6;n3.right=n7
print 'pre order'
pre_order(n1)
print '\nin order'
in_order(n1)
print '\npost order'
post_order(n1)
print '\nlevel order'
level_order(n1)
print '\nmax=', max_in_tree(n1)
print '\nmin=', min_in_tree(n1)

print search_in_tree(n1, 41)
insert_in_tree(n1, 41)
print '\nlevel order11'
level_order(n1)
print '\nSize', size(n1)
reverse_level_order(n1)
print '\nheight', height(n1)
print '\nnon_recursive_depth', non_recursive_depth(n1)
print '\nnumber_of_leaves', number_of_leaves(n1)
print '\ndiameter', diameter(n1)

print '\nsum_of_binary_tree', sum_of_binary_tree(n1)
print '\nsum_of_binary_tree_iterative', sum_of_binary_tree_iterative(n1)
print '\nmax_sum_level', max_sum_level(n1)
print '\nroot_to_leaf_paths'
root_to_leaf_path(n1, [])
print '\nsum_root_to_leaf_number'
sum_root_to_leaf_number(n1,[])
print '\nsum_root_to_leaf_number1', leaf_sum
find_vertical_sum(n1, 0)
print '\nfind_vertical_sum', sum_paths
mirror_tree(n1)
print '\nPost mirror level order11'
level_order(n1)
print '\nzigzag_traversal'
zigzag_traversal(n1)








