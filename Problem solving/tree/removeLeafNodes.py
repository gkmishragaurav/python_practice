# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target,
# if its parent node becomes a leaf node and has the value target,
# it should also be deleted (you need to continue doing that until you cannot).

class Node:
  def __init__(self, data=None):
    self.val = data
    self.left = None
    self.right = None

def in_order(root):
  if not root:
    return
  in_order(root.left)
  print root.val,
  in_order(root.right)

n1=Node(2);n2=Node(2);n3=Node(2);n4=Node(2);n5=Node(2);n6=Node(2);n7=Node(3)
n1.left=n2;n2.left=n4;n2.right=n5
n1.right=n3;n3.left=n6;n3.right=n7

print '\nin order'
in_order(n1)

def removeLeafNodes(root, target):
  if not root:
    return

  if root.left:
    root.left = removeLeafNodes(root.left, target)

  if root.right:
    root.right = removeLeafNodes(root.right, target)

  if root.val == target and not root.left and not root.right:
    return None

  return root

target=2
print(removeLeafNodes(n1, target))



