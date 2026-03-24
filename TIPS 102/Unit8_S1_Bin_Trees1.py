from collections import deque
# Problem 1: Monstera Madness
# Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant,
#  return the number of Monstera leaves 🍃 that have an odd number of splits.

# Evaluate the time complexity of your function. 
# Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

# Note: The term leaf in this problem refers to the plant leaf 🍃 of a Monstera plant, not the type of node leaf nodes which are nodes with no children.
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

'''
U: I: Root of a BT
   O: int: number of nodes with an odd value
   E: if root is empty return 0

P: 
    if the root is None then we return 0

I
'''
def count_odd_splits(root):
    if not root:
        return 0
    if root.val % 2 != 0:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    return  count_odd_splits(root.left) + count_odd_splits(root.right)
    
# Example Usage:

# """
#       2
#      / \
#     /   \
#    3     5
#   / \     \
#  6   7     12
# """

# # Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
# Example Output:

# 3
# Example 1 Explanation: Three Monstera leaves (nodes) have an odd number of fenestrations (3, 5, and 7).
# 0
# ✨ AI Hint: Traversing Trees

# Problem 2: Flower Finding
# You are looking to buy a new flower plant for your garden. 
# The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. 
# The plants are organized according to their names (vals) in alphabetical order in the BST.

# Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that
#  returns True if the flower is present in the garden and False otherwise.

# Evaluate the time complexity of your function. 
# Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
#  Assume the input tree is balanced when calculating time complexity.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right

#U: Input: a value and a tree, Output: T/F if value is in tree, E: if tree is empty return False,
#P: base case if inventory is empty return false, if root is value, return true
    # recursively searc h the binary tree depending on alphabetical order

         
def find_flower(inventory, name):
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    if name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right,name)

# Example Usage:

# """
#          Rose
#         /    \                            
#       Lilac   Tulip
#      /  \       \
#   Daisy  Lily  Violet
# """

# """
#          5
#         /  \
#       2      8
#      /  \      \
#     1    4      10
# """

# # using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 
# Example Output:

# True
# False
# ✨ AI Hint: Binary Search Trees

# Problem 3: Flower Finding II
# Consider the following function non_bst_find_flower() which accepts the root of a binary tree inventory and a flower name,
#  and returns True if a flower (node) with name exists in the binary tree. 
# Unlike the previous problem, this tree is not a binary search tree.

# Compare your solution to find_flower() in Problem 2 to the following solution. Discuss with your group: How is the code different? Why?
# What is the time complexity of non_bst_find_flower()? How does it compare to the time complexity of find_flower() in Problem 2?
# How would the time complexity of find_flower() from Problem 2 change if the tree inventory was not balanced?

#U: Return Ture is the name exits in the tree. 

class TreeNode:
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)
# Example Usage:

# """
#          Daisy
#         /    \
#       Lily   Tulip
#      /  \       \
#   Rose  Violet  Lilac
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
# garden = build_tree(values)

# print(non_bst_find_flower(garden, "Lilac"))  
# print(non_bst_find_flower(garden, "Sunflower"))  
# Example Output:

# True
# False

# Problem 4: Adding a New Plant to the Collection
# You have just purchased a new houseplant and are excited to add it to your collection! 
# Your collection is meticulously organized using a Binary Search Tree (BST) where each node in the tree represents a houseplant in your collection, 
# and houseplants are organized alphabetically by name (val).

# Given the root of your BST collection and a new houseplant name, insert a new node with value name into your collection. 
# Return the root of your updated collection. 
# If another plant with name already exists in the tree, add the new node in the existing node's right subtree.

# Evaluate the time complexity of your function. 
# Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
# Assume the input tree is balanced when calculating time complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def add_plant(collection, name):
#     pass
# Example Usage:

# """
#             Money Tree
#         /              \
# Fiddle Leaf Fig    Snake Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Aloe"))
# Example Output:

# ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

# Explanation: 
# Tree should have the following structure:
#            Money Tree
#         /              \
#  Fiddle Leaf Fig   Snake Plant
#    /
#  Aloe
# ✨ AI Hint: Binary Search Trees

# Problem 5: Sorting Plants by Rarity
# You are going to a plant swap where you can exchange cuttings of your plants for new plants from other plant enthusiasts. You want to bring a mix of cuttings from both common and rare plants in your collection. You track your plant collection in a BST where each node has a key and a val. The val contains the plant name, and the key is an integer representing the plant's rarity. Plants are organized in the BST by their key.

# To help choose which plants to bring, write a function sort_plants() which takes in the BST root collection and returns an array of plant nodes as tuples in the form (key, val) sorted from least to most rare. Sorted order can be achieved by performing an inorder traversal of the BST.

# class TreeNode:
#     def __init__(self, key, value, left=None, right=None):
#         self.key = key      # Plant rarity
#         self.val = value      # Plant name
#         self.left = left
#         self.right = right


# def sort_plants(collection):
#     pass
# Example Usage:

# """
#          (3, "Monstera")
#         /               \
#    (1, "Pothos")     (5, "Witchcraft Orchid")
#         \                 /
#   (2, "Spider Plant")   (4, "Hoya Motoskei")
# """

# # Using build_tree() function at the top of page
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))
# Example Output:

# [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]

# Problem 6: Finding a New Plant Within Budget
# You are looking for a new plant and have a max budget. The plant store that you are shopping at stores their inventory in a BST where each node has a key representing the price of the plant and value contains the plant's name. Plants are ordered by their prices. You want to find a plant that is close to but lower than your budget.

# Given the root of the BST inventory and an integer budget, write a function pick_plant() that returns the plant with the highest price below budget. If no plant with a price strictly below budget exists, the function should return None.

# class TreeNode:
#     def __init__(self, key, val, left=None, right=None):
#         self.key = key      # Plant price
#         self.val = val      # Plant name
#         self.left = left
#         self.right = right

# def pick_plant(inventory, budget):
#     pass
# Example Usage:

# """
#                (50, "Fiddle Leaf Fig")
#              /                       \
#     (25, "Monstera")           (70, "Snake Plant")
#        /        \                   /         \
# (15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")
# """

# # Using build_tree() function at the top of page
# values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
#             (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
# inventory = build_tree(values)

# print(pick_plant(inventory, 50)) 
# print(pick_plant(inventory, 25)) 
# print(pick_plant(inventory, 15)) 
# Example Output:

# Pothos
# Aloe
# None
# 💡 Hint: Inorder Predecessor

# Problem 7: Remove Plant
# A plant in your houseplant collection has become infested with aphids, and unfortunately you need to throw it out. Given the root of a BST collection where each node represents a plant in your collection, and a plant name, remove the plant node with value name from the collection. Return the root of the modified collection. Plants are organized alphabetically in the tree by value.

# If the node with name has two children in the tree, replace it with its inorder predecessor (rightmost node in its left subtree). You do not need to maintain a balanced tree.

# Pseudocode has been provided for you.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def remove_plant(collection, name):
#     # Find the node to remove
#     # If the node has no children
#         # Remove the node by setting parent pointer to None
#     # If the node has one child
#         # Replace the node with its child
#     # If the node has two children
#         # Find the inorder predecessor 
#         # Replace the node's value with inorder predecessor value
#         # Remove inorder predecessor
#     # Return root of updated tree
#     pass
# Example Usage:

# """
#               Money Tree
#              /         \
#            Hoya        Pilea
#               \        /   \
#              Ivy    Orchid  ZZ Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(remove_plant(collection, "Pilea"))
# Example Output:

# ['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

# Explanation:
# The resulting tree structure:
#              Money Tree
#             /         \
#           Hoya       Orchid
#               \          \
#               Ivy      ZZ Plant

# Standard Problem Set Version 2
# Problem 1: Find Lonely Cichlids
# Sibling cichlid fish often form strong bonds after hatching, staying close to each other for protection. Given the root of a binary tree representing a family of cichlids where each node is a cichlid, return an array containing the values of all lonely cichlids in the family. A lonely cichlid is a fish (node) that is the only child of its parent. The matriarch (root) is not lonely because it does not have a parent. Return the array in any order.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

# class Cichlid:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def find_lonely_cichlids(root):
#     pass
# Example Input:

# """
#     A
#    / \
#   B   C
#    \
#     D
# """

# # Using build_tree() function at the top of page
# values = ['A', 'B', 'C', None, 'D']
# family_1 = build_tree(values)

# """
#      A
#     / \
#    B   C
#   /   / \ 
#  D   E   F
#           \
#            G
# """

# values = ['A', 'B', 'C', None, 'D', None, 'E', 'F', None, None, None, None, None, 'G']
# family_2 = build_tree(values)

# """
#                  A
#                 / \
#                B   C
#               /     \ 
#              D       E
#             /         \
#            F           G
#           /             \
#          H               I  
# """

# values = ["A", "B", "C", "D", None, None, "E", "F", None, None, "G", "H", None, None, "I"]
# family_3 = build_tree(values)

# print(find_lonely_cichlids(family_1))
# print(find_lonely_cichlids(family_2))
# print(find_lonely_cichlids(family_3))
# Example Output:

# ['D']
# ['D', 'G']
# ['D', 'F', 'H', 'E', 'G', 'I']

# Note: The elements of the list may be returned in any order.
# ✨ AI Hint: Traversing Trees