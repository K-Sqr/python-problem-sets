# Problem 1: Cast Vote
# Write a function cast_vote() that records a vote for a candidate in an election. 
# The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for.
#  If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

def cast_vote(votes, candidate):
    if candidate in votes.keys():
        votes[candidate] += 1
    else:
        votes[candidate] = 1

# Example Usage:
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
# Example Output:

# {"Alice": 6, "Bob": 3}
# {"Alice": 6, "Bob": 3, "Gina": 1}
# ✨ AI Hint: Accessing Values in a Dictionary
# 💡 Hint: Dictionary Access options

# Problem 2: Keys in Common
# Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries.
#  The function returns a list of common keys.

# def common_keys(dict1, dict2):
# 	pass
# Example Usage:

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)
# Example Output:

# ['b', 'c']
# 💡 Hint: Accessing Keys, Values, and Key-Value Pairs
# 💡 Hint: Looping over Key-Value Pairs

# Problem 3: Highest Priority Task
# Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
# If two tasks have the same priority, return the task that comes first in the alphabet.

# def get_highest_priority_task(tasks):
# 	pass
# Example Usage:

# tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# print(tasks)
# Example Output:

# task2
# task4
# task3
# {"task1": 8, "task5": 7}
# 💡 Hint: Removing Key-Value Pairs from a Dict

# Problem 4: Frequency Count
# Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.

# def count_occurrences(nums):
#     pass
# Example Input: nums = [1, 2, 2, 3, 3, 3, 4]
# Example Output: {1: 1, 2: 2, 3: 3, 4: 1}

# ✨ AI Hint: Frequency Maps

# Problem 5: Find Majority Element
# Write a function find_majority_element() that takes in a list of integers elements and finds the majority element in the list. A majority element is an element that appears more than n/2 times where n is the size of the list. If there is no majority element, return None.

# def find_majority_element(elements):
#     pass
# Example Usage:

# elements = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements))
# Example Output: 2


# Problem 6: Has Duplicates
# Write a function hasDuplicates() that takes in a list of integers nums and a positive number k as parameters. The function returns True if the list contains any duplicate elements within the range 0 to k (inclusive). If k is greater than the list's length, the solution should check for duplicates in the complete list. The function should return False otherwise.

# def hasDuplicates(nums, k):
# 	pass
# Example Usage:

# nums = [5, 6, 8, 2, 6, 4, 9]
# check1 = hasDuplicates(nums, 3)
# print(check1)
# check2 = hasDuplicates(nums, 5)
# print(check2)
# Example Output:

# False
# True

# Problem 7: Make Pairs
# Write a function divideList() that takes in an integer list nums consisting of 2*n integers as parameters. The function divides nums into n pairs such that:

# Each element belongs to exactly one pair
# The elements present in a pair are equal
# Return True if nums can be divided into n pairs, otherwise return False.

# def divideList(nums):
#     pass
# Example Input: nums = [3,2,3,2,2,2]
# Example Output: True
# Explanation: There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs. If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

# Example Input: nums = [1,2,3,4]
# Example Output: False
# Explanation: There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.


# Problem Set Version 2
# Problem 1: Update Score
# Write a function update_score() that takes in a dictionary scores that maps player names to current scores, a string player, and an integer points as parameters. The function adds the points to the current score of player in the dictionary and returns the updated dictionary. If the player does not exist in scores, then add them.

# def update_score(scores, players, points):
#     pass
# Example Usage:

# scores = {"Alice": 100, "Bob": 90}
# update_score(scores, "Alice", 10)
# print(scores)
# update_score(scores, "Calvin", 20)
# print(scores)
# update_score(scores, "Calvin", 5)
# print(scores)
# Example Output:

# {"Alice": 110, "Bob": 90}
# {"Alice": 110, "Bob": 90, "Calvin": 20}
# {"Alice": 110, "Bob": 90, "Calvin": 25}
# ✨ AI Hint: Accessing Values in a Dictionary
# 💡 Hint: Dictionary Access options

# Problem 2: Dictionary Intersection
# Write a function dict_intersection() that takes in two dictionaries as parameters and returns a new dictionary containing the key-value pairs found in both dictionaries.

# def dict_intersection(d1, d2):
#     pass
# Example Input:

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 4}
# Example Output: {'b': 2}

# 💡 Hint: Accessing Keys, Values, and Key-Value Pairs
# 💡 Hint: Looping over Key-Value Pairs

# Problem 3: Filter by Price
# Write a function that takes in a dictionary of items and a price_threshold as parameters. The function should iterate through the dictionary and remove all items that has a value less than price_threshold. The function also returns a list of all items that are removed. If no item satisfies the condition, return None.

# def remove_items_below_price(items, price_threshold):
#     pass
# Example Usage:

# items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
# removed_list = remove_items_below_price(items, 1.00)
# print(removed_list)
# removed_list_two = remove_items_below_price(items, 1.00)
# print(removed_list_two)
# Example Output:

# ["banana", "date"]
# None
# 💡 Hint: Removing Key-Value Pairs from a Dict

# Problem 4: Find Odd Occurrences
# Write a function find_odd_occurrences() that takes in a list of integers nums where all numbers occur an even number of times except for two unique numbers that occur an odd number of times. The function should find the two unique numbers and return them as a list. Assume each problem has exactly one solution.

# def find_odd_occurrences(nums):
#     pass
# Example Usage:

# nums = [1,4,2,3,2,3,3,4,4,4]
# odd_list = find_odd_occurrences(nums)
# print(odd_list)
# Example Output:

# [1,3]
# ✨ AI Hint: Frequency Maps

# Problem 5: Find Mode
# Write a function find_mode() that takes in a non-empty list of integers lst as a parameter. The function returns the mode (the most frequently occurring number) and if there is a tie, return the element which appeared first in the list.

# def find_mode(lst):
#     pass
# Example Usage:

# lst = [1,2,3,2,3,3,4,4,4,4]
# mode = find_mode(lst)
# print(mode)
# Example Output: 4


# Problem 6: How Many Smaller
# Write a function smallerNumbersThanCurrent() that takes in a list of numbers nums as a parameter. For each nums[i], the function should find out how many numbers in the list are smaller than it. (For each nums[i], count the number of valid j's such that j!=i and nums[j] < nums[i])

# Return the answers in a list.

# def smallerNumbersThanCurrent(nums):
#     pass
# Example:

# nums = [6,1,2,2,3]
# ans = smallerNumbersThanCurrent(nums)
# # ans == [4,0,1,1,3]
# Explanation:

# nums[0] == 6
# There exists four smaller numbers than it (1, 2, 2 and 3) --> ans[0]=4

# nums[1] == 1 
# There does not exist any smaller number than it --> ans[1]=0

# nums[2] == 2 
# There exists one smaller number than it (1) --> ans[2]=1

# nums[3] == 2 
# There exists one smaller number than it (1) --> ans[3]=1

# nums[4] == 3 
# There exists three smaller numbers than it (1, 2 and 2) --> ans[4]=3

# Problem 7: Good Pairs
# Write a function numIdenticalPairs() that takes in a list of integers nums and returns the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# def numIdenticalPairs(nums):
#     pass
# Example 1:

# nums = [1,2,3,1,1,3]
# ans = numIdenticalPairs(nums)
# # ans == 4
# Explanation:

# nums[0] == 1
# - nums[0] == nums[3]
# - nums[0] == nums[4]
# Good Pairs: (0,3) and (0,4) --> count = 2

# nums[1] == 2
# No identical pairs found

# nums[2] == 3
# - nums[2] == nums[5]
# Good Pairs: (2,5) --> count = 3

# nums[3] == 1
# *will not check any any indices less than current index*
# - nums[3] == nums[4]
# Good Pairs: (3,4) --> count = 4

# nums[4] == 1
# *will not check any any indices less than current index*
# No identical pairs found

# nums[5] == 3
# *will not check any any indices less than current index*
# No identical pairs found
# Example 2:

# nums = [1,1,1,1]
# ans = numIdenticalPairs(nums)
# # ans == 6
# Example 3:

# nums = [1,2,3]
# ans = numIdenticalPairs(nums)
# # ans == 0

# Problem Set Version 3
# Problem 1: Return Book
# Write a function return_book() that accepts a string title and a dictionary library as parameters. library maps book titles to the number of copies the library currently has in stock. The function should increment the quantity of the book title in library by 1 and return the updated dictionary. If title is not in the library, then add it and set quantity to 1.

# def return_book(title, library):
#     pass
# Example Usage:

# library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

# updated_lib = return_book("1984", library)
# print(updated_lib)

# updated_lib = return_book("The Giver", library)
# print(updated_lib)

# Example Output:

# {"The Hobbit": 2, "1984": 2, "The Great Gatsby": 4}
# {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4, "The Giver": 1}
# ✨ AI Hint: Accessing Values in a Dictionary
# 💡 Hint: Dictionary Access options

# Problem 2: Dictionary Difference
# Write a function dict_difference() that takes two dictionaries and returns a new dictionary that contains only the key-value pairs found exclusively in the first dictionary but not in the second.

# def dict_difference(d1, d2):
#     pass
# Example Input:

# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 2, 'd': 1}
# Example Output: {'a': 1, 'c': 3, 'd': 4}

# 💡 Hint: Accessing Keys, Values, and Key-Value Pairs
# 💡 Hint: Looping over Key-Value Pairs

# Problem 3: Take from Stock
# Write a function pop_stock() that takes a dictionary of items items that keeps track of an item and its stock quantity, an item_name, and a quantity to be removed as parameters. The function should remove the specified quantity for that item.
# If the item does not exist, return the string "Item does not exist."
# If the specified quantity is greater than the stock, return a string "Not enough stock."
# If the specified item and quantity do exist within items, decrement the item's stock by the specified quantity and return the updated dictionary.

# def pop_stock(items, item_name, quantity):
#     pass
# Example Usage:

# items = {"chocolate": 20, "candy": 5, "chips": 10}

# resultA = pop_stock(items, "candy", 2)
# resultB = pop_stock(items, "candy", 5)
# resultC = pop_stock(items, "lollipops", 5)
# resultD = pop_stock(items, "chocolate", 5)

# print(resultA)
# print(resultB)
# print(resultC)
# print(resultD)
# Example Output:

# {"chocolate": 20, "candy": 3, "chips": 10}
# Not enough stock
# Item does not exist
# {"chocolate": 15, "candy": 3, "chips": 10}
# 💡 Hint: Removing Key-Value Pairs from a Dict

# Problem 4: Group By Frequency
# Write a function group_by_frequency() that takes in a list lst and returns a dictionary where keys represent the frequency of unique elements within lst and values represent a list of elements with the same frequency.

# def group_by_frequency(lst):
#     pass
# Example Usage:

# lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
# print(group_by_frequency(lst))
# Example Output:

# { 1 : ['a', 'b'], 2: ['c', 'd'], 3: ['e']}
# ✨ AI Hint: Frequency Maps

# Problem 5: No Duplicates Allowed
# Write a function that takes in a list of integers nums as a parameter and removes all duplicates. The function should return a list containing the unique elements in the order of their last occurrence in the original list.

# def remove_duplicates_from_front(nums):
#     pass
# Example Input: nums = [6,5,3,5,2,8,3]
# Example Output: nums = [6,5,2,8,3]


# Problem 6: First Repeating Element
# Write a function find_min_index_of_repeating() that takes in an integer list nums as a parameter and returns the minimum index of an element that has a duplicate value. The function should only do a single traversal of the list. If there are no repeating elements, return None.

# def find_min_index_of_repeating(nums):
#     pass
# Example Usage:

# nums = [5, 6, 3, 4, 3, 6, 4]
# nums2 = [5, 6, 3, 4]
# nums3 = [ 5, 6, 2, 4, 3, 4, 3]
# print(find_min_index_of_repeating(nums))
# print(find_min_index_of_repeating(nums2))
# print(find_min_index_of_repeating(nums3))
# Example Output:

# 1
# None
# 3

# Problem 7: Target Sum
# Write a function two_sum() that takes in a list of integers nums and an integer target as parameters. The function should return the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution and you may not use the same element twice. The function can return the indices in any order.

# def two_sum(nums, target):
#     pass
# Example Input:

# nums = [2,7,11,15]
# q_1 = two_sum(nums,9)
# q_2 = two_sum(nums,18)

# nums2 = [3,3]
# q_3 = two_sum(nums2,6)

# print(q_1)
# print(q_2)
# print(q_3)
# Example Output:

# [0,1]
# [1,2]
# [0,1]