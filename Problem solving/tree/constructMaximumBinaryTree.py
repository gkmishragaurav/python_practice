# You are given an integer array nums with no duplicates.
# A maximum binary tree can be built recursively from nums using the following algorithm:
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.
# https://leetcode.com/problems/maximum-binary-tree/

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
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

def find_max(nums):
    index, max = 0, float('-inf')
    i=0
    while i < len(nums):
        if nums[i] > max:
            max = nums[i]
            index = i
        i=i+1

    return index, max

def constructMaximumBinaryTree(nums):
    if not nums:
        return
    index, max = find_max(nums)
    root = BST(max)
    root.left = constructMaximumBinaryTree(nums[:index])
    root.right = constructMaximumBinaryTree(nums[index+1:])

    return root

nums=[3,2,1,6,0,5]
root = constructMaximumBinaryTree(nums)
level_order_traversal(root)

