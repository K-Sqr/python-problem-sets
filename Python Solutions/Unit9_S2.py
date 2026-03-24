# Problem Set Version 1
# Problem 1: Level Order Traversal of Binary Tree
# Given the following pseudocode and the root of a binary tree, return a list of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def level_order(root):
#     # If the tree is empty:
#     # return an empty list

#     # Create an empty queue using deque
#     # Create an empty list to store the explored nodes

#     # Add the root to the queue

#     # While the queue is not empty:
#     # Pop the next node off the queue (pop from the left side!)
#     # Add the popped node to the list of explored nodes

#     # Add each of the popped node's children to the end of the queue

#     # Return the list of visited nodes
#     pass


# Example Usage:

# Example Input Tree:

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: [4, 2, 6, 1, 3]
# Explanation: 
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3
# ✨ AI Hint: Breadth First Search Traversal

# Problem 2: Find Minimum Depth of Binary Tree
# Given the root of a binary tree, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the root down to the nearest leaf node.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
        
# def min_depth(root):
# 	pass

# Example Usage:

# Example Input Tree #1:

#    3
#   / \
#  9  20
#     / \  
#    15  7

# Example Input: root = 3
# Expected Output: 2
# Shortest path from root node to a leaf node is 3 -> 9. Number of nodes in path is 2.

# Example Input Tree #2:

#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6        

# Example Input: root = 2
# Expected Output: 5
# Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6.
# Number of nodes in path is 5.

# 💡 Hint: Choosing your Traversal Method

# Problem 3: Odd-Even Level Sum Difference in Binary Tree
# Given the root of a binary tree, return the difference between the sum of all node values in odd levels and sum of all node values in even levels.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def level_difference(root):
# 	pass

# Example Usage:

# Example Input Tree
#           6
#          / \
#         3   8
#        /   / \  
#       5   4   2
#          / \   \
#         1   7   3
# Expected Output: -5
# Explanation: 
# Odd level sum: 6 + 5 + 4 + 2 = 17
# Even level sum: 3 + 8 + 1 + 7 + 3 = 22
# Odd level sum - even level sum: 17 - 22 = -5


# Problem 4: Level Order Traversal of Binary Tree with Nested Lists
# Given the root of a binary tree, write a function level_order() that returns the level order traversal of its nodes’ values (i.e., from left to right, level by level). level_order() should return a list of lists, where each inner list contains the node values of a single level in the tree.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def level_order(root):
# 	pass
	
# Example Usage:

# Example Input Tree
#      3
#     / \
#    9  20
#       / \
#      15  7

# Input: root = 3
# Expected Output: [ [3], [9, 20], [15, 7]]

# ✨ AI Hint: Nested lists

# Problem 5: Sum of Binary Tree Node Tilts
# Given the root of a binary tree, return the sum of every tree node’s tilt. The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
        
        
# def find_tilt(root):
# 	pass

# Example Usage:

# Example Input Tree #1:

#      1
#     / \
#    2   3

# Input: root = 1
# Expected Output: 1
# Explanation
# Tilt of node 2: |0 - 0| = 0 (no children)
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
# Sum of every tilt : 0 + 0 + 1 = 1



# Example Input Tree #2:

#       4
#      / \
#     2   9
#    / \   \ 
#   3   5   7

# Example Input: root = 4
# Expected Output: 15
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 5 : |0-0| = 0 (no children)
# Tilt of node 7 : |0-0| = 0 (no children)
# Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
# Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
# Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
# Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15

# ✨ AI Hint: Absolute Value
# 💡 Hint: Choosing your Traversal Method
# Problem Set Version 2
# Problem 1: Print Level Order Traversal of Binary Tree
# Given the following pseudocode and the root of a binary tree, print the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# from collections import deque # This is a popular library used for queues

# from collections import deque # This is a popular library used for queues

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def print_by_level(root):
#     # If the tree is empty:
#     # return

#     # Create an empty queue using deque

#     # Add the root to the queue

#     # While the queue is not empty:
#     # Pop the next node off the queue (pop from the left side!)
#     # Print the popped node

#     # Add each of the popped node's children to the end of the queue
#     pass

# Example Usage:

# Example Input Tree

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: (Printed)
# 4
# 2
# 6
# 1
# 3
# Explanation: 
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3

# ✨ AI Hint: Breadth First Search Traversal

# Problem 2: Sum of Node Values by Level in Binary Tree
# Given the root of a binary tree, return a list of the sums of node values in each level in the binary tree.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
        
# def level_sum(root):
# 	pass

# Example Usage:

# Example Input Tree

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: [4, 8, 4]
# Explanation: 
# Level 1: 4
# Level 2: 2 + 6 = 8
# Level 3: 1 + 3 = 4


# Problem 3: Maximum Nodes at Any Level in Binary Tree
# Given the root of a binary tree, return the maximum number of nodes in any level of the binary tree.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def level_max(root):
# 	pass

# Example Usage:

# Example Input Tree #1:

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: 2
# Explanation: Levels 2 & 3 have 2 nodes each. 

# Example Input Tree #2:

#        1
#       / \
#      /   \
#     2     3
#    / \   / \ 
#   4   5 6   7

# Example Input: root = 1
# Expected Output: 4
# Explanation: Level 3 has 4 nodes, the most of any level


# Problem 4: Vertical Order Traversal of Binary Tree
# Given the root of a binary tree, return the vertical order traversal of its nodes’ values. (i.e., from top to bottom, column by column). If two nodes are in the same row and column, the order should be from left to right.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
# def vertical_order(root):
# 	pass

# Example Usages:

# Example Number

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Example Number

# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# Example Number

# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

# Problem 5: Find the Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def find_diameter(root):
# 	pass

# Example Usage:

# Example Input Tree:

#      1
#     / \
#    2   3
#   / \  
#  4   5

# Example Input: root = 1
# Output: 3 
# 3 is the length of the path [4,2,1,3] or [5,2,1,3]

# 💡 Hint: Choosing your Traversal Method

# Problem Set Version 3
# Problem 1: Level Order Traversal in Dictionary
# Given the following pseudocode and the root of a binary tree, return a dictionary storing the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

# The dictionary’s key should be an integer representing the level. The corresponding value for each key should be a list of node values in that level from left to right.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def level_dict(root):
#     # If the tree is empty:
#     # return an empty dictionary

#     # Create an empty dictionary
#     # Create an empty queue using deque

#     # Append a tuple (root, 1) to the queue. The queue will store tuples of (node, level)

#     # While the queue is not empty:
#     # Pop the next node, level pair off the queue (pop from the left side!)

#     # If the level is not yet a key in the dictionary
#     # Add to dictionary with empty list as a value

#     # Add a tuple with each of the popped node's children
#     # and incremented level to the end of the queue
#     pass


# Example Usage:

# Example Input Tree

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: {1: [4], 2: [2, 6], 3: [1, 3]}
# Explanation: 
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3

# ✨ AI Hint: Breadth First Search Traversal

# Problem 2: Node Values Between Given Levels in Binary Tree
# Given the root of a binary tree, return a list of all the node values between to given levels start_level and end_level in a binary tree.

# You may assume 1 <= start_level <= end_level <= tree depth.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
# def get_level_range(root, start_level, end_level):
# 	pass

# Example Usage:

# Example Input Tree

#         3
#        / \
#       /   \
#      /     \
#     5       1
#    / \     / \  
#   6   2   0   8
#      / \  
#     7   4

# Example input: root = 3, start_level = 2, end_level = 4
# Expected Output: [5, 1, 6, 2, 0, 8, 7, 4]
# Explanation:
# Level 2 nodes: 5, 1
# Level 3 nodes: 6, 2, 0, 8
# Level 4 nodes: 7, 4


# Problem 3: Cousins in Binary Tree
# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return True if the nodes corresponding to the values x and y in the tree are cousins, or False otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def is_cousins(root, x, y):
# 	pass

# Example Input Tree #1:
#       1
#      / \
#     2   3
#    / 
#   4  
# Input: root = 1, x = 4, y = 3
# Expected Output: False

# Example Input Tree #2:
#       1
#      / \
#     2   3
#      \   \
#       4   5
# Input: root = 1, x = 5, y = 4
# Expected Output: True

# Example Input Tree #3:
#       1
#      / \
#     2   3
#      \   \
#       4   5
# Input: root = 1, x = 2, y = 3
# Expected Output: False


# Problem 4: Print Corner Nodes of Each Level in Binary Tree
# Given the root of a binary tree, print the value of the corner nodes of every level in a binary tree. The corner nodes are the first and last node in each level of a binary tree.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
# def print_corner_nodes(root):
# 	pass

# Example Input Tree 

#       6
#      / \
#     3   8
#    /   / \  
#   5   4   2
#      / \   \
#     1   7   3

# Expected Output: (Printed)
# 6
# 3
# 8
# 5 
# 2
# 1
# 3
# Explanation:
# Level 1: first and last node is 6
# Level 2: first node in 3, last node is 8
# Level 3: first node is 5, last node is 2
# Level 4: first node is 1, last node is 3


# Problem 5: Lowest Common Ancestor in Binary Tree
# Given the root of a binary tree, find the lowest common ancestor (LCA) of two nodes p and q in the tree. The LCA is the lowest node t that has both p and q as descendant. A node can be considered a descendant of itself.

# Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
        
# def find_lca(root, p, q):
# 	pass

# Example Usage:

# Example Input Tree

#         3
#        / \
#       /   \
#      /     \
#     5       1
#    / \     / \  
#   6   2   0   8
#      / \  
#     7   4

# Example input: root = 3, p = 5, q = 1
# Expected Output: 3
# The LCA of nodes 5 and 1 is 3. 

# Example Input Tree

#         3
#        / \
#       /   \
#      /     \
#     5       1
#    / \     / \  
#   6   2   0   8
#      / \  
#     7   4

# Example input: root = 3, p = 5, q = 4
# Expected Output: 5
# The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.

# 💡 Hint: Choosing your Traversal Method
# This problem can be solved multiple ways, but may work best with a modified depth first search traversal. To learn more about how to choose a traversal algorithm visit the How to Pick a Traversal Algorithm section of the Unit 9 Cheatsheet.