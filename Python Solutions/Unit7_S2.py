# Problem Set Version 1
# Problem 1: Neatly Nested
# Given a string, return True if it is a nesting of zero or more pairs of parentheses.
#  Return False otherwise. A valid pair of parentheses is defined as (). 
# The input string will only contain the characters ( or ). Your solution must be recursive.

# Evaluate the time and space complexity of your solution.

def is_nested(paren_s):
    if paren_s == "":
        return True
    elif len(paren_s) >= 2 and paren_s[0] =='(' and paren_s[-1] == ')':
        return is_nested(paren_s[1:-1])
    return False
# Example Usage:
s = '(())'
# print(is_nested(s))
# # Example Input: "(())"
# Example Output:

# # Expected Output: True
# 💡 Hint: Writing Recursive Functions

# Problem 2: How Many 1s
# Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.

# def count_ones(lst):
#     total = 0 
#     if not lst:
#         return total
#     if lst[0] == 1:
#         total += 1
#     else:
#         return count_ones(lst[1:])
    

def count_ones(lst):
    low,high = 0,len(lst)-1
    while low <= high:
        mid = (low + high)//2
        if lst[mid] == 0:
            low = mid +1
            if lst[mid + 1] == 1:
                return len(lst) - low
                break
    
lst = [0, 0, 0, 0, 1, 1]
print(count_ones(lst))
    
# Example Usage:

# # Example Input: [-1,0, 0, 0, 0, 1, 1] 
# Example Output:
# # Expected Output: 3
# ✨ AI Hint: Binary Search

# Problem 3: Binary Search IV
# Thus far, we’ve mostly been using an iterative implementation of the binary search algorithm. Recursive implementations of binary search are also very common. 
# Implement binary_search() recursively.

def binary_search(nums, target):
    low,high = 0, len(nums)-1
    while low <= high:
        mid = (low +high)//2
        if lst[mid] == target:
            return mid
        else:
            low = mid +1
    
# 	
# Example Usage:

# # Example Input: nums = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output:

# # Expected Output: 5
# # Explanation: 11 has index 5 in the list
# ✨ AI Hint: Divide and Conquer

# Problem 4: Count Rotations
# You are given a circularly sorted list of integers.
#  A circularly sorted list of integers is a sorted list whose elements have then been rotated some number of times such that the last element of the array becomes the first element of the array. Write a function count_rotations() that returns the total number of times the array is rotated. Assume there are no duplicates in the array.

# def count_rotations(nums):
# 	pass
# Example Usage:

# # Example Input: [8, 9, 10, 2, 5, 6]
# Example Output:

# # Expected Output: 3
# # Explanation: Array is rotated 3 times:
# 	# Sorted Array: [2, 5, 6, 8, 9, 10]
# 	# First Rotation: [10, 2, 5, 6, 8, 9]
# 	# Second Rotation: [9, 10, 2, 5, 6, 8]
# 	# Third Rotation: [8, 9, 10, 2, 5, 6]

# Problem 5: Merge Sort I
# Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

# Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

# Given the pseudo-code and helper function merge() below, implement the merge_sort() function.

# # Helper function: Merges two sorted lists into one sorted list
# def merge(left, right):
# 	result = [] # List to store the merged result
# 	i = j = 0 # Pointers to iterate over left and right input arrays
	
# 	# Compare elements from left and right halves of the list and add them to the
# 	# result list in the correct order
#   while i < len(left) and j < len(right):
#     if left[i] <= right[j]:
#         result.append(left[i])
#         i += 1
#     else:
#         result.append(right[j])
#         j += 1
#   # Add any remaining elements from the left half to the result list
#   while i < len(left):
#       result.append(left[i])
#       i += 1
  
#   # Add any remaining elements from the right half to the result list
#   while j < len(right):
#       result.append(right[j])
#       j += 1
  
#   return result

# def merge_sort(lst):
# 	pass
# Example Usage:

# # Example Input: [5,3,4,2,1]
# Example Output:

# # Expected Output: [1,2,3,4,5]
# ✨ AI Hint: Divide and Conquer

# Problem 6: Circle Search
# Given a circularly sorted list of integers, return the index of a given target. Assume there are no duplicates in the list.

# def search_circular_list(nums, target):
# 	pass
# Example Usage:

# # Example Input: nums = [8, 9, 10, 2, 5, 6], target = 10
# Example Output:

# # Expected Output: 2
# # Explanation: 10 is at index 2 in the list
# Problem Set Version 2
# Problem 1: Substring Search
# Given two strings s and sub, write a function count_substring() that returns the number of times the substring sub occurs in s. Occurrences should not overlap. A substring is a sequence of adjacent characters within a larger string.

# Your solution must be recursive.

# Evaluate the time complexity of your solution.

# def count_substring(s, sub):
# 	pass
# Example Usage:

# # Example Input: s = "abcdeabcde" sub = "abc"
# Example Output:

# # Expected Output: 2
# # Explanation: 'abc' occurs twice in 'abcdeabcde'
# 💡 Hint: Writing Recursive Functions

# Problem 2: How Many 0s (Iterative)
# Given a sorted list of integers containing only 0s and 1s, count the total number of 0’s in the array in O(log n) time.

# def count_zeroes(lst):
# 	pass
# Example Usage:

# # Example Input: [0, 0, 0, 0, 1, 1, 1]
# Example Output:

# # Expected Output: 4
# ✨ AI Hint: Binary Search

# Problem 3: How Many 0s (Recursive)
# Implement count_zeroes() recursively.

# def count_zeroes(lst):
# 	pass
# Example Usage:

# # Example Input: [0, 0, 0, 1, 1, 1, 1]
# Example Output:

# # Expected Output: 3
# ✨ AI Hint: Divide and Conquer

# Problem 4: Special Numbers
# You are given a sorted list of non-negative integers nums. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

# def is_special(nums):
# 	pass
# Example Usage:

# # Example Input: nums = [3,5]
# Example Output:

# # Expected Output: 2
# # Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# Problem 5: Merge Sort II
# Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

# Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

# Given the main function merge_sort() below, implement the helper function merge() below. merge() accepts two sorted lists left and right and returns a sorted list.

# def merge_sort(lst):
# 		# If the length of the list is 0-1, the list is already sorted. 
#     if len(lst) <= 1:
#         return arr
    
#     # Find the middle index of the array
#     mid = len(arr) // 2
#     # Divide the array into two halves
#     left_half = arr[:mid]
#     right_half = arr[mid:]
    
#     # Recursive calls to merge_sort for sorting the left and right halves
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
    
#     # Merge the sorted arrays
#     return merge(left_half, right_half)

# def merge(left, right):
# 	pass
# Example Usage:

# # Example Input:  left = [1,3,5], right = [2,4]
# Example Output:

# # Expected Output: [1,2,3,4,5]
# ✨ AI Hint: Divide and Conquer

# Problem 6: Circle Majority
# Given an array nums of size n, use a divide and conquer approach to write a function return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# def search_circular_list(nums, target):
# 	pass
# Example Usage:

# # Example Input: nums = [3,2,3]
# Example Output:

# # Expected Output: 3
# Problem Set Version 3
# Problem 1: Remove Char
# Given a string s and a single character char, write a function remove_char() that recursively removes all instances of char from s and returns the new string.

# Evaluate the time complexity of your solution.

# def remove_char(s, char):
# 	pass
# Example Usage:

# # Example Input: s = "xaxbxc", char = 'x'
# Example Output:

# # Expected Output: 'abc'
# 💡 Hint: Writing Recursive Functions

# Problem 2: Where Does it Go (Iterative)
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

# def search_insert(nums, target):
#     left, right = 0, len(nums) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         # Check if the middle element is the target
#         if nums[mid] == target:
#             return mid
        
#         # If the target is less than the middle element, search in the left half
#         if target < nums[mid]:
#             right = mid - 1
#         # Otherwise, search in the right half
#         else:
#             left = mid + 1
    
#     # If the target is not found, 'left' will be the index where it can be inserted.
#     return left

# def binary_search_recursive(arr, target, left, right):
#     pass
# Example Usage:

# # Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 20, left = 0, right = len(lst) - 1
# Example Output:

# # Expected Output: -1
# # Explanation: 20 is not in the list
# ✨ AI Hint: Binary Search

# Problem 3: Where Does it Go (Recursive)
# Rewrite the search_insert() function above recursively.

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

# def search_insert_recursive(nums, target):
# 	pass
# Example Usage:

# # Example Input: nums = [1, 3, 5, 6], target = 5
# Example Output:

# # Expected Output: 5
# # Explanation: 11 has index 5 in the list
# ✨ AI Hint: Divide and Conquer

# Problem 4: Find Frequencies
# Given a sorted list of integers containing duplicates, write a function find_frequencies() that finds each element’s frequency in less than O(n) time.

# def find_frequencies(lst):
# 	pass
# Example Usage:

# # Example Input: [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]
# Example Output:

# # Expected Output: {2: 3, 4: 3, 5: 2, 6: 1, 8: 2, 9: 1}

# Problem 5: Merge Sort III
# Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

# Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

# Given the pseudo-code below, implement the merge_sort() function.

# def merge(left, right):
# 	# Initialize an empty list to store the merged result
# 	# Initialize a pointer to iterate over the left input list
# 	# Initialize a pointer to iterate over the right input list
	
# 	# Iterate over left & right lists simultaneously
# 		# Compare elements at same indices of left and right halves of the list 
# 		# Add them to the result list in the correct order
#   # Add any remaining elements from the left half to the result list
#   # Add any remaining elements from the right half to the result list

# def merge_sort(lst):
#     pass
# Example Usage:

# # Example Input: [5,3,4,2,1]
# Example Output:

# # Expected Output: [1,2,3,4,5]
# ✨ AI Hint: Divide and Conquer

# Problem 6: What a Nice String
# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Using the divide and conquer approach, write a function longest_nice_substring() that takes in a string s and returns the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

# def longest_nice_substring(s):
# 	pass
# Example Usage:

# # Example Input: s = "YazaAay"
# Example Output:

# # Expected Output: "aAa"
# # Explanation:"aAa" is a nice string because 'A/a' is the only letter of the alphabet in s
# # where both 'A' and 'a' appear. "aAa" is the longest nice substring.