# Problem Set Version 1
# Problem 1: Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def is_valid(s):
	"""Return True if the bracket string s is valid, False otherwise.

	A string is valid when every opening bracket is closed by the same type
	of bracket and in the correct order.
	"""
	stack = []
	pairs = {')': '(', ']': '[', '}': '{'}
	for ch in s:
		if ch in pairs.values():
			stack.append(ch)
		elif ch in pairs:
			if not stack or stack.pop() != pairs[ch]:
				return False
		else:
			# ignore any other characters (input is expected to be only brackets)
			continue
	return not stack


if __name__ == "__main__":
	# Example usage / quick smoke tests from the problem statement
	examples = [
		("()", True),
		("()[]{}", True),
		("(())", True),
		("(]", False),
		("([)]", False),
	]

	for s, expected in examples:
		result = is_valid(s)
		print(f"is_valid({s!r}) -> {result} (expected: {expected})")

# Example Usage:

# Example #1:
# Input: s = "()"
# Expected Output: True

# Example #2:
# s = "()[]{}"
# Expected Output: True

# Example #3: 
# s = "(())"
# Expected Output: True

# Example #4:
# s = "(]"
# Expected Output: False

# Example #5:
# s = "([)]"
# Expected Output: False


# Problem 2: Best Time to Buy & Sell Stock
# You are given a list of integers prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# def max_profit(prices):
# 	pass

# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example #2:
# Input: prices = [7,6,4,3,1]
# Expected Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Problem 3: Shuffle Merge
# Given the heads of two singly linked lists of integers, merge their nodes to make one list, taking nodes alternately between the two lists. If either list runs out of elements before the other, all nodes from the list with remaining nodes should be appended onto the end of the merged list. Return the head of the merged list.

# def shuffle_merge(head_a, head_b):
# 	pass


# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4 —> 5 —> 6
# Input: head_a = 1, head_b = 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 5 —> 3 —> 6

# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 3


# Problem 4: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# def group_anagrams(strs):
# 	pass

# Example Usage:

# Example #1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example #2:
# Input: strs = [""]
# Expected Output: [[""]]

# Example #3:
# Input: strs = ["a"]
# Expected Output: [["a"]]


# Problem 5: Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.

# A leaf node is a node with no children.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def sum_numbers(root):
# 	pass 

# Example Usage:

#  Example Input Tree #1:

#       1
#      / \
#     2   3

# Example Input: root = 1
# Expected Output: 25
# Explanation: 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example Input Tree #2:

#       4
#      / \
#     9   0
#    / \
#   5   1

# Input: root = 4
# Expected Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Problem Set Version 2
# Problem 1: Flowerbed
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given a list of integers flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return True if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and False otherwise.

# def can_place_flowers(flowerbed, n):
# 	pass
# # Example Input: flowerbed = [1,0,0,0,1], n = 1
# # Expected Output: True

# # Example Input: flowerbed = [1,0,0,0,1], n = 2
# # Expected Output: False

# Problem 2: Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the head of the reversed list.

# class Node:
#  	def __init__(self, value, next=None):
#  		self.value = value
# 		self.next = next

# def reverse(head):
# 	pass

# Example #1:
# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 3, val = 1
# Expected Return Value: 4
# Expected Result List: 4 -> 3 -> 2 -> 1


# Problem 3: Valid Word Abbreviation
# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return True if the string matches the given abbreviation. Return False otherwise.

# A substring is a contiguous non-empty sequence of characters within a string.

# def valid_word_abbreviation(word, abbr):
# 	pass
# Example  #1:
# Input: word = "internationalization", abbr = "i12iz4n"
# Expected Output: True
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

# Example #2:
# Input: word = "apple", abbr = "a2e"
# Expected Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".


# Problem 4: Sum Tree
# Given the root of a binary tree, write a function that returns True if the value of root is equal to the sum of the values of all its descendants. Return False otherwise.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_root_sum(root):
# 	pass

# Example  #1:
# Define the tree
#     14
#    / \
#   4   6
#  / \
# 3   1
# Input: root = 14
# Expected Output: True (4+3+1+6 = 14)


# Problem 5: Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# def max_area(height):
# 	pass

# Example 1

# Example #1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Expected Output: 49
# Explanation: The above vertical lines are represented by the list [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example #2:
# Input: height = [1,1]
# Expected Output: 1


# Problem Set Version 3
# Problem 1: Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. Return the number of distinct ways you can climb to the top.

# def climb_stairs(n):
# 	pass

# Example Usage:

# Example #1:
# Input: n = 2
# Expected Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example #2:
# Input: n = 3
# Expected Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step



# Problem 2: Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given a list of integers nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of a list.

# def find_error_nums(nums):
# 	pass


# Example #1:
# Input: nums = [1, 2, 2, 4]
# Expected Output: [2, 3]

# Example #2:
# Input: nums = [1, 1]
# Expected Output: [1, 2]


# Problem 3: Delete N Nodes after M Nodes
# You are given the head of a linked list and two integers m and n.

# Traverse the linked list and remove some nodes in the following way:

# Start with the head as the current node.
# Keep the first m nodes starting with the current node.
# Remove the next n nodes
# Keep repeating steps 2 and 3 until you reach the end of the list.
# Return the head of the modified list after removing the mentioned nodes.

# class Node:
#     def __init__(self, val=0, next=None):
#         self.value = val
#         self.next = next

# def delete_nodes(head, m, n):
# 	pass

# Example #1:Example 1

# Input List #1:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13
# Input: head = 1, m = 2, n = 3
# Expected Output: 1
# Expected Output List: 1 -> 2 -> 6 -> 7 -> 11 -> 12
# Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  
# (1 ->2) show in black nodes.
# Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
# Continue with the same procedure until reaching the tail of the Linked List.
# Head of the linked list after removing nodes is returned.
# Example #2:Examlple 2

# Input List #2: 
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11
# Input: head = 1, m = 1, n = 3
# Expected Output: 1 
# Expected Output List: 1 -> 5 -> 9


# Problem 4: Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def get_diameter(root):
# 	pass

# Example Input Tree:

#       1
#      / \
#     2   3
#    / \  
#   4   5

# Example Input: root = 1
# Output: 3 


# Problem 5: Two Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (0-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution. Your solution must use O(1) additional space.

# def two_sum(numbers, target):
# 	pass

# Example Usage:

# Example:
# Input: numbers = [1,2,3,4], target = 3
# Output: [0, 1]
# The sum of 1 and 2 is 3. Since we are assuming a 0-indexed array
# index1 = 1, index2 = 2. We return [0, 1].