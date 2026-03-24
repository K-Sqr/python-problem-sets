# Problem Set Version 1
# Problem 1: Build a Binary Tree I
# Given the following TreeNode class, create the binary tree depicted in the image below.

# Binary Tree Example
#  10
#  /  \
# 4    6
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# ✨ AI Hint: Binary Trees

bin_tree = TreeNode(10,TreeNode(4,None,None),TreeNode(6,None,None))
root = TreeNode()
root_node = TreeNode(10,None,None)
left_node = TreeNode(4,None,None)
right_node = TreeNode(6,None,None)

root_node.left = left_node
root_node.right = right_node

# Problem 2: 3-Node Sum I
# Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check_tree(root):
    if root.val == (root.left.val + root.right.val):
        return True
    return False

# print(check_tree(bin_tree))
    

# Example Usage:

# Example Input Tree #1: 
#   10
#  /  \
# 4    6
# Input: root = 10
# Expected Output: True

# Example Input Tree #2: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False

# Problem 3: 3-Node Sum II
# Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True
#  if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check_tree(root):
    if not root or (not root.left and not root.right):
        return False
    tot = 0
    if root.left:
        tot += root.left.val
    if root.right:
        tot += root.right.val
    return tot == root.val


bin_tree = TreeNode(10,None,TreeNode(10,None,None))
print(check_tree(bin_tree))
# Example Usage:

# Example Input Tree #1: 
#   10
#  /  
# 10    
# Input: root = 10
# Expected Output: True

# Example Input Tree #2: 
#   5
#  / \
# 3   2
# Input: root = 5
# Expected Output: True

# Example Input Tree #3: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False

# Example Input Tree #4: 
# Empty Tree (None)
# Input: root = None
# Expected Output: False


# Problem 4: Find Leftmost Node I
# Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def left_most(root):
    if not root.left:
        return root.val
    return left_most(root.left)

bin_tree = TreeNode(10,TreeNode(1,TreeNode(101,TreeNode(120,TreeNode(15,TreeNode(112,None,None),None),None),None),None),TreeNode(10,None,None))
print(left_most(bin_tree))
# Example Usage:


# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4

# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1

# Example Input Tree #3: 

# Input: root = None
# Output: None


# Problem 5: Find Leftmost Node II
# If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.

# Evaluate the time complexity of the function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def left_most(root):
    node = root
    while node.left:
        node = node.left
    return node.val

# Example Usage:
bin_tree = TreeNode(10,TreeNode(1,TreeNode(101,TreeNode(120,TreeNode(15,TreeNode(11,None,None),None),None),None),None),TreeNode(10,None,None))
print(left_most(bin_tree))
# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4

# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1

# Example Input Tree #3:

# Input: root = None
# Output: None


# Problem 6: In-order Traversal
# Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

def inorder_traversal(root):
    node = root
    lst = []
    inorder_traversal_help(node,lst)
    return lst
# 	pass
def inorder_traversal_help(node,lst):
    if not node:
        return
    inorder_traversal_help(node.left,lst)
    lst.append(node.val)
    inorder_traversal_help(node.right,lst)
bin_tree = TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))
print(inorder_traversal(bin_tree))
     
# Example Usage:

# Example Input Tree #1: 
#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: [1,3,2]

# Example Input Tree #2 : 

# Input: root = None
# Output: []

# Example Input Tree #3:
#     1  

# Input: root = 1
# Output: [1]
# ✨ AI Hint: Traversing Trees

# Problem 7: Binary Tree Size
# Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
def size(root):
    if not root:
        return 0
    node = root
    s = 1 + size(node.left) + size(node.right)
    return s

bin_tree = TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))
print(size(bin_tree))

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

# Example Input Tree #2: 

# Empty tree (None)
# Input: root = None
# Expected Output: 0


# Problem 8: Binary Tree Find
# Given a value and the root of a tree, write a function find() that returns True if there is a node with the given value in the tree. 
# Assume the tree is balanced.

# Evaluate the time complexity of your solution.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
def find(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    return find(root.left,value) or find(root.right,value)

bin_tree = TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))
print(find(bin_tree,3))
# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1, value = 5
# Expected Output: True

# Example Input Tree #2: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1, value = 10
# Expected Output: False

# ✨ AI Hint: Balanced Trees

# Problem 9: Binary Search Tree Find
# Given a value and the root of a binary search tree, write a function find_bst() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
def find_bst(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    if root.val > value:
        return find(root.left,value)
    else:
        return find(root.right,value)


# # Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4, value = 5
# Expected Output: True

# Example Input Tree #2: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4, value = 10
# Expected Output: False

# ✨ AI Hint: Binary Search Trees

# Problem 10: BST Descending Leaves
# Given the root of a binary search tree, write a function descending_leaves() that returns a list of the values of all leaves in the BST in descending order.
#  Assume the tree is balanced.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
def descending_leaves(root):
    if not root:
        return []
    return descending_leaves(root.right) + [root.val] + descending_leaves(root.left)

# Example of a valid BST:
#        4
#      /   \
#     2     6
#    / \   / \
#   1   3 5   7

bin_tree = TreeNode(4,
    TreeNode(2,
        TreeNode(1, None, None),
        TreeNode(3, None, None)
    ),
    TreeNode(6,
        TreeNode(5, None, None),
        TreeNode(7, None, None)
    )
)

print(descending_leaves(bin_tree))

# Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: [5, 3, 1]

# Example Input Tree #2: 
#  10 

# Input: root = 4
# Expected Output: [10]

# Problem Set Version 2
# Problem 1: Build A Binary Tree II
# Given the following TreeNode class, create the binary tree that has a root with value 5. The root should have a left child with value 10, and a right child with value 20.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# ✨ AI Hint: Binary Trees

# Problem 2: 3-Node Product I
# Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True
#  if the value of the root is equal to the product of the values of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# #   10
# #  /  \
# # 2    5
# # Input: root = 10
# # Expected Output: True

# # Example Input Tree: 
# #   5
# #  / \
# # 3   1
# # Input: root = 5
# # Expected Output: False

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

def check_tree(root):
    return root.val == (root.left.val * root.right.val)



# Problem 3: 3-Node Product II
# Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True
#  if the value of the root is equal to the product of the values of its two children. Return False otherwise.
#  If the root has only one child, return False.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# #   10
# #  /  
# # 10    
# # Input: root = 10
# # Expected Output: True

# # Example Input Tree: 
# #   5
# #  / \
# # 3   1
# # Input: root = 5
# # Expected Output: True

# # Example Input Tree: 
# #   5
# #    \
# #     2
# # Input: root = 5
# # Expected Output: False

# # Example Input Tree: Empty Tree (None)
# # Input: root = None
# # Expected Output: False

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

def check_tree(root):
    if root is None or root.left is None or root.right is None:
        return False
    return root.value == (root.left.val * root.rght.val)



# Problem 4: Find Rightmost Node I
# Given the root of a binary tree, write a function that finds the value of the right most node in the tree.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    
# """
# # Input: root = 1
# # Expected Output: 5

# # Example Input Tree: 
# """
#      1
#       \
#        2
#       / 
#      3    
# """
# # Input: root = 1
# # Expected Output: 2

# # Input: root = None
# # Output: None


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

def right_most(root):
    if root.right is None:
        return root.val
    return right_most(root.right)

# Problem 5: Find Rightmost Node II
# If you implemented the previous right_most() function iteratively, implement it recursively. If you implemented it recursively, implement it recursively.

# Evaluate the time complexity of the function.

# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    
# """
# # Input: root = 1
# # Expected Output: 5

# # Example Input Tree: 
# """
#      1
#       \
#        2
#       / 
#      3    
# """
# # Input: root = 1
# # Expected Output: 2

# # Input: root = None
# # Output: None


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

def right_most(root):
    node = root
    while node is not None:
        node = node.right
    return node
    

# Problem 6: Post-order Traversal
# Given the root of a binary tree, return a list representing the postorder traversal of its nodes' values.
#  In an postorder traversal we traverse the left subtree, then the right subtree, then the current node.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# """For example:
#       1
#      / \
#     /   \ 
#    2     3
#   / \     \ 
#  4   5     6
# """
# # Input: root = 1
# # Expected Output: [4, 5, 2, 6, 3, 1]

# # Input: root = None
# # Output: []

# # Example Input Tree
# """ 1 """ 
# # Input: root = 1
# # Output: [1]

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]
# ✨ AI Hint: Traversing Trees


node2 = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(3,None,TreeNode(13,None, TreeNode(10)))))

print(postorder_traversal(node2))
# Problem 7: Binary Tree Product
# Given the root of a binary tree, write a function that returns the product of all nodes’ values in a binary tree. If the tree is empty, return 1.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4
# # Expected Output: 120

# # Example Input Tree: Empty tree (None)
# # Input: root = None
# # Expected Output: 1


# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
def product_tree(root):
    if root is None:
        return 1
    return root.val * product_tree(root.left) * product_tree(root.right)


node2 = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(3,None,TreeNode(13,None, TreeNode(10)))))

print(product_tree(node2))


# Problem 8: Binary Tree Is Leaf
# Given a value and the root of a binary search tree, write a function is_leaf_bst() that returns True 
# if a node with the given value is a leaf node and False otherwise.
#  Assume the tree is balanced.

# Evaluate the time complexity of your solution.


# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    
# """
# # Input: root = 1, value = 5
# # Expected Output: True

# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    2     5
#   /     
#  4       
# """
# # Input: root = 1, value = 2
# # Expected Output: False


# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def is_leaf(root, value):
# 	pass

# ✨ AI Hint: Balanced Trees

# Problem 9: BST Is Leaf
# Given a value and the root of a binary search tree, write a function is_leaf_bst() that returns True if a node with the given value is a leaf node and False otherwise. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4, value = 5
# # Expected Output: True

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4, value = 10
# # Expected Output: False


# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def is_leaf_bst(root, value):
# 	pass

# ✨ AI Hint: Binary Search Trees

# Problem 10: BST Is Full
# Given the root of a binary search tree, write a function is_full_tree() that returns True if the tree is full and False otherwise. A binary tree is full if every node has either zero or two children.

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4
# # Expected Output: True

# # Example Input Tree: 
# """ 10
# 	 /  \ 
# 	2    1
#    \
#     3
# """
# # Input: root = 4
# # Expected Output: [10]


# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def is_full_tree(root):
# 	pass

# Problem Set Version 3
# Problem 1: Build A Binary Tree III
# Given the following TreeNode class, create the binary tree depicted below.

# """
#     a
#    / \
#   b   c
#        \
#         d

# """

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
# ✨ AI Hint: Binary Trees

# Problem 2: 3-Node Booleans
# You are given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child. The left and right child have a boolean value of either True or False.

# The root has a string value of either AND or OR. Apply the boolean operation of the root to its two children. Return True if the result of the expression is truth and False otherwise.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# #    'OR'
# #    /   \
# #   /     \
# # True   False
# # Input: root = 'OR'
# # Expected Output: True

# # Example Input Tree: 
# #    'AND'
# #    /   \
# #   /     \
# # True   False
# # Input: root = 'AND'
# # Expected Output: False

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def tree_expression(root):
# 	pass


# Problem 3: 3-Node Equality
# You are given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child.

# Return True if the root’s children have equal value and False otherwise.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# #      1
# #     / \
# #    2   2
# # Input: root = 1
# # Expected Output: True

# # Example Input Tree: 
# #      1
# #     / 
# #    2   
# # Input: root = 1
# # Expected Output: False

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def equality(root):
# 	pass


# Problem 4: Find Leftmost Path I
# Given the root of a binary tree, write a function that finds that returns a list of the left most path of the tree.

# Evaluate the time complexity of your function.



# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    
# """
# # Input: root = 1
# # Expected Output: [1, 2, 4]

# # Example Input Tree: 
# """
#      1
#       \
#        2
#       / 
#      3    
# """
# # Input: root = 1
# # Expected Output: [1]

# # Input: root = None
# # Output: []


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def left_path(root):
# 	pass


# Problem 5: Find Leftmost Path II
# If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it recursively.

# Evaluate the time complexity of your implementation.

# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    
# """
# # Input: root = 1
# # Expected Output: [1, 2, 4]

# # Example Input Tree: 
# """
#      1
#       \
#        2
#       / 
#      3    
# """
# # Input: root = 1
# # Expected Output: [1]

# # Input: root = None
# # Output: []

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def left_path(root):
# 	pass


# Problem 6: Pre-order Traversal
# Given the root of a binary tree, return a list representing the preorder traversal of its nodes' values. In an preorder traversal we traverse the current node, then the left subtree, then the right subtree.

# # Example Input Tree: 
# """For example:
#      1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3 
# """
# # Input: root = 1
# # Expected Output: [1,3,2]

# # Input: root = None
# # Output: []

# # Example Input Tree
# """ 1 """ 
# # Input: root = 1
# # Output: [1]

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def preorder_traversal(root):
# 	pass

# ✨ AI Hint: Traversing Trees

# Problem 7: Binary Tree All Lesser
# Given the root of a binary tree and a value val, write a function is_lesser() that returns True if all the nodes in the tree have a value less than val and False otherwise. If the tree is empty, return False.

# Evaluate the time complexity of your function.

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4, val = 5
# # Expected Output: False

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4, val = 6
# # Expected Output: True


# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def is_lesser(root):
# 	pass


# Problem 8: Binary Tree Any Greater
# Given a value and the root of a binary tree, write a function contains_greater() which returns True if any nodes greater than value exist in the tree. If no node greater than value exist, return False. Assume the tree is balanced.

# Evaluate the time complexity of your solution.


# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    5     2
#   / \    
#  4   3    
# """
# # Input: root = 1, value = 3
# # Expected Output: True

# # Example Input Tree: 
# """
#       1
#      / \
#     /   \
#    5     2
#   / \    
#  4   3    
# """
# # Input: root = 1, value = 10
# # Expected Output: False

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def contains_greater(root, value):
# 	pass

# ✨ AI Hint: Balanced Trees

# Problem 9: BST Any Greater
# Given a value and the root of a binary search tree, write a function contains_greater_bst() which returns True if any nodes greater than value exist in the tree. If no node greater than value exists, return False. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4, value = 3
# # Expected Output:  True

# # Example Input Tree: 
# """
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    
# """
# # Input: root = 4, value = 10
# # Expected Output: False


# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def contains_greater_bst(root, value):
# 	pass

# ✨ AI Hint: Binary Search Trees

# Problem 10: BST Leaves Sum to Root
# Given the root of a binary tree, write a function leaf_sum() that returns True if the sum of the values of all the leaves equal the sum of the value of the root. Return False otherwise.

# Evaluate the time complexity of your function

# # Example Input Tree: 
# """
#       4
#      / 
#     /   
#    2     
#   / \    
#  1   3    
# """
# # Input: root = 4
# # Expected Output: True

# # Example Input Tree: 
# """ 10  
# """
# # Input: root = 10
# # Expected Output: False


# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def sum_leaves(root):
# 	pass