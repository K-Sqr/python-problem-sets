# Problem Set Version 1
# Problem 1: Is Uni-valued
# A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

# Evaluate the time complexity of your solution.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
def is_univalued(root):
    if not root:
        return True
# 	pass
# Example Usage:

# Example Input Tree #1

#       1
#      / \
#     /   \
#    1     1
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: True

# Example Input Tree #2

#       1
#      / \
#     /   \
#    1     2
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: False
# ✨ AI Hint: Binary Trees

# Problem 2: Binary Tree Height
# Given the root of a binary tree, write a function height() that returns the height of a binary tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
   
# def height(root):
# 	pass
# Example Usage:

# Example Input Tree #1

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 3

# Example Input Tree #2 

#       4 

# Input: root = 4
# Expected Output: 1

# Problem 3: BST Insert
# Given the root of a binary search tree, insert a new node with a given key and value into the tree. Return the root of the modified tree. The tree is sorted by key. If a node with the given key already exists, update the the existing key’s value. You do not need to maintain a balanced tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, key, value, left=None, right=None):
#             self.key = key
#             self.val = value
#             self.left = left
#             self.right = right
   
# def insert(root, key, value):
# 	pass
# Example Usage:

# Example Input Tree #1: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \    
#  1   6    

# Input: root = 10, key = 9, value = 'Naruto' 
# Expected Output: root = 10
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    5      15
#   / \    
#  1   6
#       \
#        9    


# Example Input Tree #2: Empty Tree (None)

# Input: root = None, key = 4, value = "Sailor Moon"
# Expected Output: root = 4
# Expected Output Tree:

#       4

# ✨ AI Hint: Binary Search Trees

# Problem 4: BST Remove I
# Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, remove the node with the given key. Return the root of the modified tree.

# The tree is sorted by key. If multiple nodes with the given key exist, remove the first node you find. If you need to remove a node with two children, use the in-order successor of that node, which is the smallest value in its right subtree. You do not need to maintain a balanced tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, key, value, left=None, right=None):
# 		     self.key = key
#          self.val = value
#          self.left = left
#          self.right = right
         
# def remove_bst(root, key):
# 	# Locate the node to be removed
# 	# If the node is a leaf node:
# 		# Remove the node by redirecting the appropriate child reference of its parent to None
# 	# If the node has one parent:
# 		# Replace the node with its child, updating its parent's nodes child reference appropriately
# 	# If the node has two children:
# 		# Find the node's inorder successor (smallest node in right subtree)
# 		# Swap the value of the node and its inorder successor
# 		# Recursively remove the successor (which now has the current node's value)
# 	# Return the root of the updated tree
# 	pass
# Example Usage:

# Example Input Tree #1: (tree depicted using keys) 

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16


# Input: root = 10, key = 10
# Expected Output: 13
# Expected Output Tree:

#       13
#      /  \
#     /    \
#    5      15
#   / \       \
#  1   8      16


# Example Input Tree #2: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9 

# Input: root = 10, key = 8
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   9  13  16


# Example Input Tree #3: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9 

# Input: root = 10, key = 9
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8  13  16


# Problem 5: BST In-order Successor
# In the remove_bst() problem, we summarized the in-order successor of a given node as the smallest node in the given node’s right subtree. This is true if the given node has a right subtree.

# More generally, the in-order successor is the node with the smallest key greater than the key of the given node. Given the root of a binary search tree, and a TreeNode current, write a function that returns the in-order successor of the current node. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

# class TreeNode():
#       def __init__(self, key, value, left=None, right=None):
#             self.key = key
#             self.val = value
#             self.left = left
#             self.right = right
            
# def inorder_successor(root, current):
#       pass
# Example Usage:

# Example Input Tree #1: (tree depicted using keys)

#           10
#          /  \
#         /    \
#        5      15
#       / \    
#      1   8
#         / \
#        6   9

# Input: root = 10, current = 5
# Expected Output: 6 (Should return a node object)

# Example Input Tree #2: (tree depicted using keys)

#           10
#          /  \
#         /    \
#        5      15
#       / \    
#      1   8
#         / \
#        6   9 

# Input: root = 10, current = 6
# Expected Output: 8 (Should return a node object)

# Problem 6: Merge Binary Trees
# You are given two binary trees with roots root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# def merge_trees(self, root1, root2):
# 	pass
# Example Usage:

# Example Input Trees: 

#           1                 2 
#          / \               / \
#         /   \             /   \
#        3     2           1     3
#       /                   \     \
#      5                     4     7

# Input: root1 = 1, root2 = 2
# Expected Output: 3
# Expected Output Tree

#       3
#      / \
#     /   \
#    4     5
#   / \     \  
#  5   4     7


# Problem Set Version 2
# Problem 1: Is Even-valued
# Given the root of a binary tree, return True if every node in the tree has an even value and False otherwise.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def is_even(root):
# 	pass
# Example Usage:

# Example Input Tree #1

#       2
#      / \
#     /   \
#    4     10
#   / \     \
#  6   8     12

# Input: root = 2
# Expected Output: True

# Example Input Tree #2

#       2
#      / \
#     /   \
#    4     2
#   / \     \
#  1   6     8

# Input: root = 2
# Expected Output: False
# ✨ AI Hint: Binary Trees

# Problem 2: Binary Tree Max
# Given the root of a binary tree, write a function tree_max() that returns the node with the greatest value inside of a binary tree.
# If the tree is empty return None.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
   
# def tree_max(root):
# 	pass
# Example Usage:

# Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 5

# Example Input Tree #2: Empty Tree (None)
# Input: root = None
# Expected Output: None

# Problem 3: BST Insert II
# Given the root of a binary search tree, insert a new node with a given value into the tree. Return the root of the modified tree.\
# If a node with the given value already exists, place the new node in the right subtree.
# You do not need to maintain a balanced tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
   
# def insert_with_duplicates(root, value):
# 	pass
# Example Usage:

# Example Input Tree #1: 

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6    

# Input: root = 10, value = 9 
# Expected Output: root = 10
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6
#       \
#        9    


# Example Input Tree #2: 

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6    

# Input: root = 10, value = 8
# Expected Output: root = 10
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6
#       \
#        8    


# Example Input Tree #3: Empty Tree (None)

# Input: root = None, value = 4
# Expected Output: root = 4
# Expected Output Tree:

#       4 

# ✨ AI Hint: Binary Search Trees

# Problem 4: BST Remove II
# Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, remove the node with the given key. Return the root of the modified tree.

# The tree is sorted by key. If multiple nodes with the given key exist, remove the first node you find. If you need to remove a node with two children, use the in-order predecessor of that node, which is the largest node in its left subtree. You do not need to maintain a balanced tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, key, value, left=None, right=None):
# 		     self.key = key
#          self.val = value
#          self.left = left
#          self.right = right
         
# def remove_bst(root, key):
# 	# Locate the node to be removed
# 	# If the node is a leaf node:
# 		# Remove the node by redirecting the appropriate child reference of its parent to None
# 	# If the node has one parent:
# 		# Replace the node with its child, updating its parent's nodes child reference appropriately
# 	# If the node has two children:
# 		# Find the node's inorder predecessor (largest node in left subtree)
# 		# Swap the value of the node and its inorder successor
# 		# Recursively remove the predecessor (which now has the current node's value)
# 	# Return the root of the updated tree
# 	pass
# Example Usage:

# Example Input Tree #1: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16


# Input: root = 10, key = 10
# Expected Output: 8
# Expected Output Tree:

#       8
#      / \
#     /   \
#    5     15
#   /      / \
#  1      13 16


# Example Input Tree #2: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#     / 
#    7    

# Input: root = 10, key = 8
# Expected Output: 10 (Should return a node object)
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   7  13  16


# Example Input Tree #3: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9 

# Input: root = 10, key = 9
# Expected Output: 10 (Should return a node object)
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8  13  16


# Problem 5: BST In-order Predecessor
# In the remove_bst() problem, we summarized the in-order predecessor of a given node as the largest node in the given node’s left subtree. This is true if the given node has a left subtree.

# More generally, the in-order predecessor is the node with the largest key less than the key of the given node. Given the root of a binary search tree, and a TreeNode current, write a function that returns the in-order predecessor of the current node. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

# class TreeNode():
#       def __init__(self, key, value, left=None, right=None):
#             self.key = key
#             self.val = value
#             self.left = left
#             self.right = right
            
# def inorder_predecessor(root, current):
#       pass
# Example Usage:

# Example Input Tree #1: (tree depicted using keys)

#           10
#          /  \
#         /    \
#        5      15
#       / \    
#      2   8
#     / \
#    1   3

# Input: root = 10, current = 5
# Expected Output: 3

# Example Input Tree #2: (tree depicted using keys)

#           10
#          /  \
#         /    \
#        5      15
#       / \    
#      1   8
#         / \
#        6   9 
 
# Input: root = 10, current = 9
# Expected Output: 8

# Problem 6: Identical Binary Trees
# Given the roots of two binary trees root1 and root2, write a function that returns True if they are identical and False otherwise. Two binary trees are considered the same if they are structurally identical and the nodes have the same values.

# def is_identical(root1, root2):
# 	pass
# Example Usage:

# Example Input Trees #1:

#       1                1
#      / \              / \
#     2   3            2   3  

# Input: root1 = 1, root2 = 1
# Expected Output: True

# Example Input Trees #2:

#       1                1
#      /                  \
#     2                    2  

# Input: root1 = 1, root2 = 1
# Expected Output: False

# Example Input Trees #3:

#       1                1
#      / \              / \
#     2   1            1   2  

# Input: root1 = 1, root2 = 1
# Expected Output: False

# Problem Set Version 3
# Problem 1: Is Odd-valued
# Given the root of a binary tree, return the number of nodes that have odd values.

# Evaluate the time complexity of your solution.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def count_odds(root):
# 	pass
# Example Usage:

# Example Input Tree #1:

#       2
#      / \
#     /   \
#    3     5
#   / \     \
#  6   7     12

# Input: root = 2
# Expected Output: 3

# Example Input Tree #2:

#       2
#      / \
#     /   \
#    4     2
#   / \     \
#  1   6     8

# Input: root = 2
# Expected Output: 1
# ✨ AI Hint: Binary Trees

# Problem 2: Binary Tree Min
# Given the root of a binary tree, write a function tree_min() that returns the node with the least value inside of a binary tree. If the tree is empty return None.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
   
# def tree_min(root):
# 	pass
# Example Usage:

# Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 1

# Example Input Tree #2: Empty Tree (None)
# Input: root = None
# Expected Output: None

# Problem 3: BST Insert III
# Given the root of a binary search tree, insert a new node with a given value into the tree. Return the root of the modified tree. If a node with the given value already exists, place the new node in the left subtree. You do not need to maintain a balanced tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
   
# def insert_with_duplicates(root, value):
# 	pass
# Example Usage:

# Example Input Tree #1: 

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6    

# Input: root = 10, value = 9 
# Expected Output: root = 10
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6
#       \
#        9    


# Example Input Tree #2: 

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6    

# Input: root = 10, value = 8
# Expected Output: root = 10
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6
#   \
#    8       


# Example Input Tree #3: Empty Tree (None)

# Input: root = None, value = 4
# Expected Output: root = 4
# Expected Output Tree:

#       4 

# ✨ AI Hint: Binary Search Trees

# Problem 4: BST Remove III
# Use the provided pseudocode to solve the problem below. Given a value and the root of a binary search tree, remove the node with the given value. Return the root of the modified tree.

# If multiple nodes with the given value exist, remove the first node you find.

# If you need to remove a node with two children, use the deletion by merging strategy. When you delete by merging, you take the two subtrees of the given node and attach the root of the right subtree to the largest node in the left subtree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, key, value, left=None, right=None):
# 		     self.key = key
#          self.val = value
#          self.left = left
#          self.right = right
         
# def remove_bst(root, key):
# 	# Locate the node to be removed
# 	# If the node is a leaf node:
# 		# Remove the node by redirecting the appropriate child reference of its parent to None
# 	# If the node has one parent:
# 		# Replace the node with its child, updating its parent's nodes child reference appropriately
# 	# If the node has two children:
# 		# Find the largest node in the node's left subtree.
# 		# Set the root of the node's right subtree as the right child of the largest node in the node's left subtree.
# 	# Return the root of the updated tree
# 	pass
# Example Usage:

# Example Input Tree #1: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16


# Input: root = 10, key = 10
# Expected Output: 5
# Expected Output Tree:

#    5      
#   / \     
#  1   8
#       \
#       15
#       / \
#      13  16       

# Explanation: Deleting 10 leaves you with two subtrees. The left subtree has root 5. The right subtree has root 15.
# 8 is the largest node in the left subtree, so it's right child becomes 15 which is the root of the right subtree.

# Example Input Tree #2: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9 

# Input: root = 10, key = 8
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   9  13  16


# Example Input Tree #3: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9 

# Input: root = 10, key = 9
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8  13  16


# Problem 5: BST Find Floor
# Given a value and the root of a binary search tree, write a function find_floor() that finds the largest value in the binary search tree less than or equal to the given value. If no such node exists, return None. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def find_floor(root, value):
# 	pass


# Problem 6: Nested Binary Trees
# Given the roots of two binary trees root and sub_root, return True if there is a subtree of root with the same structure and node values of sub_root and False otherwise.

# A subtree of a binary tree is a tree that consists of a node in and all of this node's descendants. The tree could also be considered as a subtree of itself.

# Evaluate the time complexity of your solution.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def is_subtree(root, sub_root):
# 	pass
# Example Usage:

# Example Input Trees #1:

#       2                3
#      / \              / \
#     /   \            6   7  
#    3     5
#   / \     \
#  6   7     12

# Input: root = 2, sub_root = 3
# Expected Output: True

# Example Input Trees #2:

#       2                3
#      / \              / \
#     /   \            1   2  
#    3     5
#   / \     \
#  6   7     12

# Input: root = 2, sub_root = 3
# Expected Output: False