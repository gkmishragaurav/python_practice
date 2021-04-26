# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in
# the sequence has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any path.
# https://leetcode.com/problems/binary-tree-maximum-path-sum/


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def make_tree():
    b1=BST(1);b2=BST(-2);b3=BST(3);b4=BST(-4);b5=BST(-5)
    b6=BST(-6);b7=BST(7);b8=BST(-8);b9=BST(9)#;b10=BST(10)
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
def maxPathSum(root):
    # Write your code here.
    def util(root):
        if not root:
            return float('-inf'), 0

        left_include, left_down = util(root.left)
        right_include, right_down = util(root.right)

        # include root
        include = max(root.value + max(0, left_down) + max(0, right_down), left_include, right_include)

        # down root
        down = root.value + max(0, left_down, right_down)

        return include, down


    return util(root)[0]
root = make_tree()
level_order_traversal(root)

print(maxPathSum(root))
