# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
# Given the root of a binary tree, determine if it is a complete binary tree.
#
# In a complete binary tree, every level, except possibly the last, is completely filled, 
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes 
# inclusive at the last level h.

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

n1=Node(13);n2=Node(34);n3=Node(32);n4=Node(23);n5=Node(25);n6=Node(27);n7=Node(27)
n1.left=n2;n2.left=n4;n2.right=n5
n1.right=n3;n3.left=n6;n3.right=n7

print '\nin order'
in_order(n1)

def isCompleteTree(root):
  que = [root]
  leaf = False
  while que:
    temp = que.pop(0)
    if not leaf:
      if temp.left:
        if not temp.right:
          leaf = True
      else:
        leaf = True
        if temp.right:
          return False
    else:
      if temp.left or temp.right:
        return False

    if temp.left:
      que.append(temp.left)
    if temp.right:
      que.append(temp.right)

  return True

print(isCompleteTree(n1))



