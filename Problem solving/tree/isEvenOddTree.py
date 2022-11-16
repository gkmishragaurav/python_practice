# https://leetcode.com/problems/even-odd-tree/description/
# A binary tree is named Even-Odd if it meets the following conditions:
#
# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

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

def isEvenOddTree(root):
  que = [(root,0)]
  last_item = None
  last_level = 0
  while que:
    temp, level = que.pop(0)
    if last_level != level:
      last_item = None
    if level%2 == 0: #even
      if temp.val%2 == 0:
        return False
      if not last_item:
        last_item = temp.val
        last_level = level
      else:
        if last_item >= temp.val:
          return False
        else:
          last_item = temp.val
    else: #odd
      if temp.val%2 != 0:
        return False
      if not last_item:
        last_item = temp.val
        last_level = level
      else:
        if last_item <= temp.val:
          return False
        else:
          last_item = temp.val

    if temp.left:
      que.append((temp.left, level+1))
    if temp.right:
      que.append((temp.right, level+1))

  return True




print(isEvenOddTree(n1))



