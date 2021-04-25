# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def height(root):
            if not root:
                return 0           
            
            temp = [height(child) for child in root.children]
            print (temp, root.val)
            if temp:
                return 1+max(temp)
            else:
                return 1
        if not root:
            return 0
        depth=float('-inf')
        temp = height(root)   
        if temp > depth:
            depth = temp
            
        temp = [self.maxDepth(child) for child in root.children]
        if temp:
            return 1+max(temp)
        else:
            return 1
        
        
        
        
        
    
