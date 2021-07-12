# We are given a binary tree (with root node root), a target node, and an integer value k.
# Return a list of the values of all nodes that have a distance k from the target node.
# The answer can be returned in any order.

class BST:
    def __init__(self, value):
        self.val = value
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
        print (temp.val, end=' ')
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

def solution(root, target, k):
    def get_hash(root):
        if not root:
            return
        if root.left:
            d[root.left] = root
            get_hash(root.left)

        if root.right:
            d[root.right] = root
            get_hash(root.right)
    def get_down(root, k, dir=None):
        if not root:
            return
        if k==0:
            print(root.val)
            ans[root.val]=1

        if not dir:
            get_down(root.left, k-1, dir)
            get_down(root.right, k-1, dir)
        elif dir == 'left':
            get_down(root.left, k-1, dir)
        else:
            get_down(root.right, k-1, dir)

    def get_up(root, k):
        if not root:
            return
        parent=d[root]
        if parent.left == root:
            get_down(parent, k-1, 'right')
        else:
            get_down(parent, k-1, 'left')
    def target_node(root, target):
        queue=[]
        queue.append(root)
        while queue:
            temp = queue.pop(0)
            if temp.val == target:
                return temp
            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)
    d={}
    ans={}
    # save all node and parent pair in hash
    get_hash(root)

    # reach to target
    temp=target_node(root, target)

    # get node k in down direction
    get_down(temp, k)

    # get node k in up+ direction
    get_up(temp, k)
    # print(ans, d)
    return list(ans.keys())

root = make_tree()
level_order_traversal(root)
print('\n')

x=solution(root, 3, 2)
print(x)
