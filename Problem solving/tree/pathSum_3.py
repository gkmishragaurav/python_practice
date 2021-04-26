# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def root_to_leaf(root, targetSum, path):
            if not root:
                return
            
            path.append(root.val)
            if sum(path) == targetSum:
                arr[0] = arr[0] + 1
        
            root_to_leaf(root.left, targetSum, path)
            root_to_leaf(root.right, targetSum, path)
            path.pop()
            
        def util(root, targetSum):
            if not root:
                return 
            print(root.val)
            root_to_leaf(root, targetSum, [])
            
            util(root.left, targetSum)
            util(root.right, targetSum)            
            
        arr = [0]
        util(root, targetSum)
        return arr[0]
