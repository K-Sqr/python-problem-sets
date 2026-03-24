# Problem Set Version 1
# Problem 1: Is Symmetric Tree
# Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def is_symmetric(root):
# 	pass

# Example Usage:

# Example Tree #1:

#        1
#      /   \
#     /     \
#    2       2
#   / \     / \
#  3   4   4   3
#            |
 

# Input: root = 1
# Expected Output: True


# Example Tree #2:

#         1
#       /   \
#      /     \
#     2       2
#      \       \
#       3       3
         

# Input: root = 1
# Expected Output: False


# Problem 2: Root-to-Leaf Paths
# Given the root of a binary tree, return a list of all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def binary_tree_paths(root):
# 	pass

# Example Usage:

# Example Input Tree #1:

#   1
#  / \
# 2   3
#  \  
#   5         

# Example Input: root = 1
# Expected Output: ["1->2->5", "1->3"]
# ["1->3", "1->2->5"] is also valid

# Example Input Tree #2:

#   1    

# Example Input: root = 1
# Expected Output: ["1"]


# Problem 3: Minimum Difference in BST
# Given the root of a binary search tree, return the minimum difference between the values of any two different nodes in the tree.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def min_diff_in_bst(root):
# 	pass

# Example Usage:

# Example Input Tree #1:

#     4
#    / \
#   2   6
#  / \  
# 1   3

# Example Input: root = 4
# Expected Output: 1 
# Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)

# Example Input Tree  #2: 

#    1
#   / \
#  0  48
#     / \  
#    12 49

# Example Input: root = 1
# Expected Output: 1 
# Explanation: The smallest difference between any two nodes is 1 (1 - 0 = 1)

# ✨ AI Hint: Representing Infinite Values

# Problem 4: Increasing Order Search Tree
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node of the tree is now the root of tree and every node has no left child and only one right child.

# Return the root of the modified tree

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def increasing_bst(root):
# 	pass

# Example Usage:

# Example Input Tree #1:

#     5
#    / \
#   1   7


# Example Input: root = 5
# Expected Output: root = 1

# Expected Output Tree #1:

# 1 
#  \
#   5
#    \
#     7


# Example Input Tree #2:

#        5
#       / \
#      /   \
#     3     6
#    / \     \  
#   2   4     8
#  /         / \
# 1         7   9

# Input: root = 5
# Expected Output: root = 1
# Expected Output Tree #2:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5 
#          \
#           6
#            \
#             7
#              \
#               8
#                \ 
#                 9


# Problem 5: Equal Tree Split
# Given the root of a binary tree, return True if removing an edge between two nodes can split the tree into two trees with an equal number of nodes. Return False otherwise.

# Evaluate the time complexity of the function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def can_split(root):
# 	pass

# Example Usage:

# Example Input Tree #1:

#        1
#       / \
#      /   \
#     2     3
#    / \     \  
#   4   5     7

# Example Input: root = 1
# Expected Output: True
# Explanation: Deleting the edge between node 1 and its left child, node 2 gives the following
# two trees, each of size 3

#   Tree 1    Tree 2        
#               1
#                \
#     2           3
#    / \           \  
#   4   5           7



# Example Input Tree #2:

#        1
#       /  \
#      /    \
#     2      3
#    / \    / \  
#   4   5  6   7

# Example Input: root = 1
# Expected Output: False
# Explanation: It is not possible to split the tree into two trees of equal size by deleting 
# an edge

# Problem Set Version 2
# Problem 1: Evaluate Boolean Full Binary Tree
# You are given the root of a full binary tree with the following properties:

# Leaf nodes have either the boolean value True or False .
# Non-leaf nodes have either the string value OR or AND.
# The evaluation of a node is as follows:

# If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
# Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return result of evaluating the root node. Return the result of evaluating the root nod

# A full binary tree is a binary tree where each node has either 0 or 2 children.

# A leaf node is a node that has zero children.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def evaluate_tree(root):
# 	pass

# Example Input Tree #1:

#        OR
#       /  \
#      /    \
#   True    AND
#          /   \
#        False True  

# Input: root = OR
# Expected Output: True
# Explanation:

#        OR                       OR
#       /  \                     /  \
#      /    \         -->       /    \          -->    True
#   True    AND               True   False
#          /   \
#        False True  


# Problem 2: Find Lonely Nodes
# Given the root of a binary tree, return a list containing the values of all lonely nodes in the tree. Return the list in any order.

# A lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def find_lonely_nodes(root):
# 	pass

# Example Input Tree #1:

#     1
#    / \
#   2   3
#    \
#     4

# Input: root = 1
# Expected Output: [4]
# Explanation: Node 4 is the only lonely node. 
# Node 1 is the root and is not lonely
# Node 2 and 3 have the same parent and are not lonely


# Example Input Tree #2:

#      7
#     / \
#    1   4
#   /   / \  
#  6   5   3
#           \
#            2

# Input: root = 7
# Expected Output: [6,2]  
# [2,6] is also an acceptable answer

# Example Input Tree #3:

#            11
#           /  \
#          99  88
#         /      \  
#        77       66
#       /          \
#      55           44
#     /              \
#    33               22       

# Input: root = 11
# Expected Output: [77, 55, 33, 66, 44, 22]  
# List elements may be returned in any order
# Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
# All other nodes are lonely.


# Problem 3: Kth Smallest node in a BST
# Given the root of a binary search tree and a positive integer k, return the value of the kth smallest node in the tree. All nodes in the tree are guaranteed to be unique.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
# def kth_smallest(root):
# 	pass

# Example Input Tree

#           15                     
#          /  \                    
#         /    \                  
#        /      \                 
#       10      20               
#      /  \     / \            
#     8   12   16 26         

# Example Input: root = 15, k = 4
# Expected Output: 15
# Explanation: The 4th smallest value in the 


# Problem 4: Find Rightmost Node I
# Given the root of a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero children. If the node has two children, then this node's value is the smaller value among its two children. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, write a function that returns the second minimum value in the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.

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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def find_second_minimum_value(root):
# 	pass

# Example Input Tree #1:

#       2
#      / \
#     2   5
#        / \
#       5   7

# Example Input: root = 2
# Expected Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.


# Example Input Tree #2:

#       2
#      / \
#     2   2

# Example Input: root = 2
# Expected Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value. 


# Problem 5: Find Rightmost Node II
# Given the roots of two binary trees root1 and root2, write a function can_transform() that returns True if the tree represented by root1 can be converted to the tree represented by root2 by doing any number of swaps of the first tree’s right and left branches.

# Evaluate the time complexity of the function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        

# def can_swap(root1, root2):
# 	pass

# Example Input Tree:

#        root1                     root2
#          6                         6
#         / \                       / \
#        /   \                     /   \
#       /     \                   /     \
#      3       8                 8       3 
#     / \     / \               / \     / \
#    1   7   4   2             2   4   7   1
#           / \   \           /   / \
#          7   1   3         3    1  7

# Input: root1 = 6, root2 = 6
# Expected Output: True
# Explanation: 

#          6                         6                    6                    6
#         / \                       / \                  / \                  / \
#        /   \                     /   \                /   \                /   \
#       /     \                   /     \              /     \              /     \
#      3       8      -->        8       3            8       3            8       3 
#     / \     / \               / \     / \          / \     / \          / \     / \
#    1   7   4   2             4   2   1   7  -->   2   4   7   1        2   4   7   1
#           / \   \           / \   \               \  / \              /   / \
#          7   1   3         1   7   3               3 1  7        -->  3   7   1



# Problem Set Version 3
# Problem 1: Build A Binary Tree III
# Evaluate Mathematical Expression Tree You are given the root of a full binary tree with the following properties:

# Leaf nodes have an integer value.
# Non-leaf nodes have either the string value +, -, *, or /
# The evaluation of a node is as follows:

# If the node is a leaf node, the evaluation is the value of the node, i.e. the integer.
# Otherwise, evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.

# A full binary tree is a binary tree where each node has either 0 or 2 children.

# A leaf node is a node that has zero children.

# Evaluate the time complexity of the function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def evaluate_tree(root):
# 	pass

# Example Usage:

# Example Input Tree

#         +
#       /   \
#      /     \
#     *       -
#    / \     / \
#   5   2   60 20 

# Input: root = +
# Expected Output: 50
# Explanation:

#         +                         +
#       /   \                     /  \
#      /     \         -->       10  40          -->    50
#     *       -               
#    / \     / \
#   5   2   60 20 



# Problem 2: Find Corresponding Node in Cloned Tree
# You are given the roots of two binary trees, original and cloned. You are also give a TreeNode target which is a reference to a node in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node as target in the cloned tree.

# You may not change any of the two trees or the target node. The answer must be a reference to a node in the cloned tree.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
        
# def get_target_copy(original, cloned, target):
# 	pass

# Example 1:Example 1

# Input: tree = [7,4,3,null,null,6,19], target = 3
# Output: 3
# Explanation: In all examples the original and cloned trees are shown. 
# The target node is a green node from the original tree. 
# The answer is the yellow node from the cloned tree.
# Example 2:Example 2

# Input: tree = [7], target =  7
# Output: 7
# Example 3:Example 3

# Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
# Output: 4

# Problem 3: Path Sum in Binary Tree
# Given the root of a binary tree and an integer target_sum, return True if the tree has a root-to-leaf path such that adding up all the values along the path equals target_sum. Return False otherwise.

# A leaf is a node with no children.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def has_path_sum(root, target_sum):
# 	pass

# Example Input Tree #1:

#       5
#      / \
#     4   8
#    /   / \  
#   11  13  4
#  / \       \
# 7   2       1

# Input: root = 5, target_sum = 22
# Expected Output: True
# Explanation: The root to leaf path 5 -> 4 -> 11 -> 2 sums to 22.

# Example Input Tree #2:

#     1
#    / \
#   2   3

# Input: root = 1 , target_sum = 5
# Expected Output: False
# Explanation: There two root-to-leaf paths in the tree:
# 1 -> 2: The sum is 3.
# 1 -> 3: The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Problem 4: Check Balanced Binary Tree
# Given the root of a binary tree, return True if the tree is balanced and False otherwise.

# A balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def is_balanced(root):
# 	pass

# Example Input Tree #1:

#       3
#      /  \
#     9   20
#        /  \  
#       15   7

# Example Input: root = 3
# Expected Output: True

# Example Input Tree #2:

#           1
#          / \
#         2   2
#        / \  
#       3   3
#      / \
#     4   4  

# Example Input: root = 1
# Expected Output: False

# Example Input Tree: Empty Tree
# Example Input: root = 1
# Expected Output: True


# Problem 5: Replace Node Value with Sum of Subtree
# Given a binary tree, in-place replace each node’s value as the sum of all elements present in its left and right subtree. You may assume the value of an empty child node to be 0.

# Return the root of the modified tree.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def sum_transform(root):
# 	pass

# Example Usage:

# Example Input Tree

#             1
#            / \
#           /   \ 
#          /     \
#         2       3
#          \     / \
#           4    5  6
#               / \
#              7   8  

# Example Input: root = 1
# Expected Output: root = 35
# Expected Output Tree:

#             35
#            /  \
#           /    \ 
#          /      \
#         4       26
#          \      / \
#           0    15  0
#               / \
#              0   0