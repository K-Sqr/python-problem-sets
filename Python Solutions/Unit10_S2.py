# Problem Set Version 1
# Problem 1: Contains Duplicates
# Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

# def contains_duplicate(nums):
# 	pass

# Example Usage:

# Example #1: 
# Input: nums = [1,2,3,1]
# Output: True

# Example #2:
# Input: nums = [1,2,3,4]
# Output: False

# Example #3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True


# Problem 2: Remove Element
# Given a list of integers nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, for your response to be acceptable, you need to do the following things:

# Change the list nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k
# def remove_element(nums, val):
# 	pass

# Example #1:
# Input: nums = [3,2,2,3], val = 3
# Expected Output: 2
# nums should be [2,2,_,_]
# Explanation: Your function should return k = 2,
# with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example #2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5
# nums should be [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Problem 3: Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# def gcd_of_stings(str1, str2):
# 	pass


# Example #1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example #2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example #3:
# Input: st1 = "LEET", str2 = "CODE"
# Output: ""


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

# Example Usage:

# Input Tree #1:

#       3
#      /  \
#     9   20
#        /  \  
#       15   7

# Input: root = 3
# Output: True

# Input Tree #2:

#           1
#          / \
#         2   2
#        / \  
#       3   3
#      / \
#     4   4  

# Input: root = 1
# Output: False


# Input Tree #3: Empty Tree
# Input: root = 1
# Output: True


# Problem 5: Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# def subarray_sum(nums, k):
# 	pass

# Example Usage:

# Example #1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2

# Example #2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2

# Problem 6: Add Two Numbers Represented By Linked Lists
# You are given the heads of two non-empty linked lists l1 and l2 representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself

# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def add_two_numbers(l1, l2):
# 	pass

# Example Usage:

# Example Input Lists
# list1: 2 -> 4 -> 3
# list2: 5 -> 6 -> 4

# Example Input: l1= 2, l2 = 5
# Expected Output: 7
# Expected Output List: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807

# Problem Set Version 2
# Problem 1: Flip Game
# You are playing a Flip Game with your friend.

# You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

# Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].

# def generate_possible_next_moves(current_state):
# 	pass

# Example Usage:

# Example #1:
# Input: current_state = "++++"
# Output: ["--++","+--+","++--"]

# Example #2:
# Input: current_state = "+"
# Output: []


# Problem 2: Intersection of Two Lists
# Given two lists of integers nums1 and nums2, return a list of their intersection. Each element in the result list must be unique and you may return the result in any order.

# def intersection(nums1, nums2):
# 	pass

# Example Usage:

# Example #1:
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]

# Example #2:
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Expected Output: [9, 4]
# [4, 9] is also an acceptable answer.


# Problem 3: Buildings with an Ocean View
# There are n buildings in a line. You are given an list of integers heights of size n that represents the heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

# Return a list of indices of buildings that have an ocean view, sorted in increasing order.

# def find_buildings(heights):
# 	pass
# Example Usage:

# Example #1:
# Input: heights = [4,2,3,1]
# Output: [0,2,3]
# xplanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

# Example #2:
# Input: heights = [4,3,2,1]
# Output: [0,1,2,3]
# Explanation: All the buildings have an ocean view.

# Example #1:
# Input: heights = [1,3,2,4]
# Output: [3]
# Explanation: Only building 3 has an ocean view.


# Problem 4: Leaf-Similar Trees
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def leaf_similar(root1, root2):
# 	pass

# Example 1

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return True if and only if the two given trees with root nodes root1 and root2 are leaf-similar. Otherwise, return False.

# Example Usage:

# Input Tree #1:

#         root1                   root2
#           3                       3  
#          / \                     / \
#         /   \                   /   \
#        /     \                 /     \
#       5       1               5       1
#      / \     / \             / \     / \
#     6   2   9   8           6   7   4   2
#        / \                             / \
#       7   4                           9   8

# Input: root1 = 3, root2 = 3
# Output: True

# Input Tree #2

#        root1           root2
#           1               1
#          / \             / \
#         2   3           3   2

# Input: root1 = 1, root2 = 1
# Output: False

# Problem 5: Insert into a Sorted Circular Linked List
# Given a linked list node start_node that is a node in a circularly linked list sorted in non-descending order, write a function insert() that inserts a value insert_val into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def insert(start_node, insert_val):
# 	pass

# Example Usage:

# Example Input List
# 1 ---> 3
# ^      |
# |      | 
# 4 <-----
# Example Input: start_node = 3, insert_val = 2
# Expected Output: 3
# Expected Output List:
# 1 ---> 2  --> 3
# ^             |
# |             | 
# 4 <------------
# Explanation: In the figure above, there is a sorted circular list of three elements. 
# You are given a reference to the node with value 3, and we need to insert 2 into the list. 
# The new node should be inserted between node 1 and node 3. 
# After the insertion, the list should look like this, and we should still return node 3.

# Example Input List: Empty List
# Example Input: start_node = None, insert_val = 1
# Expected Output: 1
# Explanation: The list is empty (given start_ndoe is None). 
# Create a new single circular linked list and return the reference to that single node. 
# The node's next value should be itself. 


# Problem 6: Sequential Digits
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# def sequential_digits(low, high):
# 	pass

# Example Usage:

# Example #1:
# Input: low = 100, high = 300
# Output: [123,234]

# Example #2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]


# Problem Set Version 3
# Problem 1: Count of Matches in Tournament
# You are given an integer n, the number of teams in a tournament that has strange rules:

# If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
# If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
# Return the number of matches played in the tournament until a winner is decided.

# def number_of_matches(n):
# 	pass

# Example Usage:

# Example #1:
# Input: n = 7
# Output: 6
# Explanation: Details of the tournament: 
# - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 3 + 2 + 1 = 6.

# Example #2:
# Input: n = 14
# Expected Output: 13
# Explanation: Details of the tournament:
# - 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
# - 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 7 + 3 + 2 + 1 = 13.


# Problem 2: Intersection of Two Linked Lists
# Given the heads of two singly linked lists, return the node at which the two lists intersect. If the two linked lists do not intersect, return None. You may not modify either of the linked lists.

# class Node:
#     def __init__(self, val = 0, next_node = None):
#         self.val = val
#         self.next = next_node

# def find_intersection(headA, headB):
# 	pass
# Example 1


# Problem 3: Power of Four
# Given an integer n, return True if it is a power of four. Otherwise, return False.

# An integer n is a power of four, if there exists an integer x such that n == 4ˣ.

# def is_power_of_four(n):
# 	pass

# Example #1:
# Input: n = 16
# Output: True

# Example #2:
# Input: n = 5
# Output: False

# Example #2:
# Input: n = 1
# Output: True


# Problem 4: Leaves of a Binary Tree
# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def find_leaves(root):
# 	pass

# Example 2

# Example Usage:

# Example 
# Input: root = 1
# Output: [[4, 5, 3], [2], [1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers 
# since per each level it does not matter the order on which elements are returned.


# Problem 5: Custom Sort String
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Rearrange the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# def custom_sort_string(order, s):
# 	pass

# Example Usage:

# Example #1:
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# "dcba", "cdba", "cbda" are also valid outputs.
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. 

# Example #2:
# Input: order = "bcafg", s = "abcd"
# Expected Output: "bcad"
# Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s.
# The character "d" in s does not appear in order, so its position is flexible.
# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". 
# "d" can be placed at any position since it's not in order. 
# The output "bcad" correctly follows this rule. 

# Problem 6: Find Sum Pair
# Given a list of integers numbers, return the list of four integers in the list, a, b, c, and d, such that a + b = c + d. You may return the numbers in any order. If no such integers exist, return an empty list.

# def find_sum_pair(numbers):
# 	pass
# Example Usage:

# Example #1:
# Input: numbers = [3, 10, 4, 5, 2, 14]
# Output: [3, 4, 2, 5]
# [2, 3, 4, 5] or any permutation of these 4 numbers is also acceptable.
# Explanation: 3 + 4 = 2 + 5.

# Example #2:
# Input: numbers = [60, 0, 10, -35, 90]
# Output: []