# Standard Problem Set Version 1
# Problem 1: Hundred Acre Wood
# Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".

def welcome():
	print("Welcome to The Hundred Acre Wood!")
# Example Usage:

welcome()
# Example Output:

# Welcome to The Hundred Acre Wood!
# 💡 Hint: Python Functions
# 💡 Hint: Python Strings
# 💡 Hint: print() function

# Problem 2: Greeting
# Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
	print(f"Welcome to The Hundred Acre Wood {name} !My name is Christopher Robin.")
# Example Usage:

greeting("Rhode")
# greeting("Winnie the Pooh")
# Example Output:

# Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
# Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.
# 💡 Hint: Variables
# 💡 Hint: Parameters
# 💡 Hint: Formatted Strings

# Problem 3: Catchphrase
# Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

# Character	Catchphrase
# "Pooh"	"Oh bother!"
# "Tigger"	"TTFN: Ta-ta for now!"
# "Eeyore"	"Thanks for noticing me."
# "Christopher Robin"	"Silly old bear."
# If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"

def print_catchphrase(character):
	table = {"Pooh" : "Oh bother!", "Tigger" : "TTFN: Ta-ta for now!", "Eeyore": "Thanks for noticing me.", "Christopher Robin" : "Silly old bear."}
	if character in table:
		print(table[character])
	else:
		print(f"Sorry! I don't know {character}'s catchphrase!")
# Example Usage

character = "Poo"
print_catchphrase(character)

# character = "Piglet"
# print_catchphrase(character)
# Example Output:

# "Oh bother!"
# "Sorry! I don't know Piglet's catchphrase!"
# ✨ AI Hint: Conditionals

# Problem 4: Return Item
# Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.

def get_item(items, x):
    if x >= len(items):
        return None
    
    return items[x]
# 	pass
# Example Usage

items = ["piglet", "pooh", "roo", "rabbit"]
x = 7
print(get_item(items, x))

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# get_item(items, x)
# Example Output:

# "roo"
# None
# ✨ AI Hint: List indexing
# ✨ AI Hint: To Print or to Return?

# Problem 5: Total Honey
# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

# def sum_honey(hunny_jars):
# 	sum = 0
# 	for i in range(len(hunny_jars)):
# 		sum+= hunny_jars[i]
# 	return sum
def sum_honey(hunny_jars):
	sum = 0
	for i in hunny_jars:
		sum+=i
	return sum
# Example Usage

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

# hunny_jars = []
# sum_honey(hunny_jars)
# Example Output:

# 14
# 0
# ✨ AI Hint: For Loops
# ✨ AI Hint: Accumulator Variable

# Problem 6: Double Trouble
# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.

def doubled(hunny_jars):
	return[i*2 for i in hunny_jars]
# Example Usage

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
# Example Output:

# [2, 4, 6]

# Problem 7: Poohsticks
# Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them.
#  They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

# Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks.
#  count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.

def count_less_than(race_times, threshold):
	return len([i for i in race_times if i < threshold])

# 	pass
# Example Usage

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

# race_times = []
# threshold = 4
# count_less_than(race_times, threshold)
# Example Output:

# 3
# 0

# Problem 8: Pooh's To Do's
# Write a function print_todo_list() that accepts a list of strings named tasks.
#  The function should then number and print each task on a new line using the format:

# Pooh's To Dos:
# 1. Task 1
# 2. Task 2
# ...

def print_todo_list(task):
	for i in range(len(task)):
		print(f"{i}. {task[i]}")


# Example Usage
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
# Example Output:

# Pooh's To Dos:
# 1. Count all the bees in the hive
# 2. Chase all the clouds from the sky
# 3. Think
# 4. Stoutness Exercises

# Pooh's To Dos:
# ✨ AI Hint: range()

# Problem 9: Pairs
# Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
# Write a function can_pair() that accepts a list of integers item_quantities.
#  Return True if each number in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
	if not item_quantities:
		return True
	for q in item_quantities:
		if q % 2 != 0:
			return False
	return True
# 	pass
# Example Usage

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))	

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))


item_quantities = []
print(can_pair(item_quantities))

# Example Output:

# True
# False
# True
# 💡 Remainders with Modulus Division

# Problem 10: Split Haycorns
# Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
# Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. 
# split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.

def split_haycorns(quantity):
	return[i for i in range(1,quantity + 1) if quantity % i == 0]
# 	pass
# Example Usage

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))
# Example Output:

# [1, 2, 3, 6]
# [1]


# Problem 11: T-I-Double Guh-ER
# Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. 
# Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r removed from it.

def tiggerfy(s):

	for chr in s:
		if chr in "tiger":
			s.delete(chr)
	return s
# 	pass
# Example Usage

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
# Example Output:

# "suspcous"
# ""
# "Hunny"
# 💡Hint: String Methods

# Problem 12: Thistle Hunt
# Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.

# def locate_thistles(items):
# 	pass
# Example Usage

# items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
# locate_thistles(items)

# items = ["book", "bouncy ball", "leaf", "red balloon"]
# locate_thistles(items)
# Example Output:

# [0, 3]
# []

# Standard Problem Set Version 2
# Problem 1: Batman
# Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".

# def batman():
# 	pass
# Example Usage:

# batman()
# Example Output:

# I am vengeance. I am the night. I am Batman!
# 💡 Hint: Python Functions
# 💡 Hint: Python Strings
# 💡 Hint: print() function

# Problem 2: Mad Libs
# Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".

# def madlib(verb):
# 	pass
# Example Usage

# verb = "give up"
# madlib(verb)

# verb = "nap"
# madlib(verb)
# Example Output:

# "I have one power. I never give up. - Batman"
# "I have one power. I never nap. - Batman"
# 💡 Hint: Variables
# 💡 Hint: Parameters
# 💡 Hint: Formatted Strings

# Problem 3: Trilogy
# Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

# Year	Movie Title
# 2005	"Batman Begins"
# 2008	"The Dark Knight"
# 2012	"The Dark Knight Rises"
# If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."

# def trilogy(year):
# 	pass
# Example Usage:

# year = 2008
# trilogy(year)

# year = 1998
# trilogy(year)
# Example Output:

# "The Dark Knight"
# "Christopher Nolan did not release a Batman movie in 1998."
# ✨ AI Hint: Conditionals

# Problem 4: Last
# Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None.

# def get_last(items):
# 	pass
# Example Usage

# items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
# get_last(items)

# items = []
# get_last(items)
# Example Output:

# "black adam"
# None
# ✨ AI Hint: List indexing
# ✨ AI Hint: To Print or to Return?

# Problem 5: Concatenate
# Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

# def concatenate(words):
# 	pass
# Example Usage

# words = ["vengeance", "darkness", "batman"]
# concatenate(words)

# words = []
# concatenate(words)
# Example Output:

# "vengeancedarknessbatman"
# ""
# ✨ AI Hint: For Loops
# ✨ AI Hint: Accumulator Variable

# Problem 6: Squared
# Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.

# def squared(numbers):
# 	pass
# Example Usage

# numbers = [1, 2, 3]
# squared(numbers)
# Example Output:

# [1, 4, 9]

# Problem 7: NaNaNa Batman!
# Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

# def nanana_batman(x):
# 	pass
# Example Usage

# x = 6
# nanana_batman(x)

# x = 0
# nanana_batman(x)
# Example Output:

# "nananananana batman!"
# "batman!"
# ✨ AI Hint: range()

# Problem 8: Find the Villain
# Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.

# def find_villain(crowd, villain):
# 	pass
# Example Usage

# crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
# villain = 'The Joker'
# find_villain(crowd, villain)
# Example Output:

# [1, 4, 6]

# Problem 9: Odd
# Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.

# def get_odds(nums):
# 	pass
# Example Usage

# nums = [1, 2, 3, 4]
# get_odds(nums)

# nums = [2, 4, 6, 8]
# get_odds(nums)
# Example Output:

# [1, 3]
# []
# 💡 Remainders with Modulus Division

# Problem 10: Up and Down
# Write a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the number of odd numbers minus the number of even numbers in the list.

# def up_and_down(lst):
# 	pass
# Example Usage

# lst = [1, 2, 3]
# up_and_down(lst)

# lst = [1, 3, 5]
# up_and_down(lst)

# lst = [2, 4, 10, 2]
# up_and_down(lst)
# Example Output:

# 1
# 3
# -4

# Problem 11: Running Sum
# Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). You must modify the list in place; you may not create any new lists as part of your solution.

# def running_sum(superhero_stats):
# 	pass
# Example Usage

# superhero_stats = [1, 2, 3, 4]
# running_sum(superhero_stats)

# superhero_stats = [1, 1, 1, 1, 1]
# running_sum(superhero_stats)

# superhero_stats = [3, 1, 2, 10, 1]
# running_sum(superhero_stats)
# Example Output:

# [1, 3, 6, 10]
# [1, 2, 3, 4, 5]
# [3, 4, 6, 16, 17]

# Problem 12: Shuffle
# Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].

# def shuffle(cards):
# 	pass
# Example Usage

# cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
# shuffle(cards)

# cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
# shuffle(cards)

# cards = [10, 10, 2, 2]
# shuffle(cards)
# Example Output:

# ['Joker', 3, 'Queen', 'Ace', 2, 7]
# [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
# [10, 2, 10, 2]

# Advanced Problem Set Version 1
# Problem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.

# def linear_search(items, target):
# 	pass
# Example Usage:

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
# linear_search(items, target)

# items = ['bed', 'blue jacket', 'red shirt', 'hunny']
# target = 'red balloon'
# linear_search(items, target)
# Example Output:

# 3
# -1
# 💡Hint: Python Basics

# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

# def final_value_after_operations(operations):
# 	pass
# Example Usage:

# operations = ["trouncy", "flouncy", "flouncy"]
# final_value_after_operations(operations)

# operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)
# Example Output:

# 2
# 4

# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

# def tiggerfy(word):
# 	pass
# Example Usage:

# word = "Trigger"
# tiggerfy(word)

# word = "eggplant"
# tiggerfy(word)

# word = "Choir"
# tiggerfy(word)
# Example Output:

# "r"
# "eplan"
# "Chor"

# 💡Hint: String Methods
# Problem 4: Non-decreasing Array
# Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# def non_decreasing(nums):
# 	pass
# Example Usage:

# nums = [4, 2, 3]
# non_decreasing(nums)

# nums = [4, 2, 1]
# non_decreasing(nums)
# Example Output:

# True
# False

# Problem 5: Missing Clues
# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

# def find_missing_clues(clues, lower, upper):
#    pass
# Example Usage:

# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# find_missing_clues(clues, lower, upper)

# clues = [-1]
# lower = -1
# upper = -1
# find_missing_clues(clues, lower, upper)
# Example Output:

# [[2, 2], [4, 49], [51, 74], [76, 99]]
# []
# ✨ AI Hint: Nested Lists
# 💡Hint: String Methods

# Problem 6: Vegetable Harvest
# Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that are ready to harvest in the vegetable patch. A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.

# Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.

# def harvest(vegetable_patch):
# 	pass
# Example Usage:

# vegetable_patch = [
# 	['x', 'c', 'x'],
# 	['x', 'x', 'x'],
# 	['x', 'c', 'c'],
# 	['c', 'c', 'c']
# ]
# harvest(vegetable_patch)
# Example Output:

# 6
# ✨ AI Hint: Nested Loops

# Problem 7: Eeyore's House
# Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. The function should return the number of good pairs.

# A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1.

# def good_pairs(pile1, pile2, k):
# 	pass
# Example Usage:

# pile1 = [1, 3, 4]
# pile2 = [1, 3, 4]
# k = 1
# good_pairs(pile1, pile2, k)

# pile1 = [1, 2, 4, 12]
# pile2 = [2, 4]
# k = 3
# good_pairs(pile1, pile2, k)
# Example Output:

# 5
# 2
# 💡 Remainders with Modulus Division

# Problem 8: Local Maximums
# Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

# local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

# def local_maximums(grid):
# 	pass
# 4x4 matrix with cells numbered according to Example 1 input next to 2x2 matrix numbered according Example 1 output

# Example Usage:

# grid = [
# 	[9, 9, 8, 1],
# 	[5, 6, 2, 6],
# 	[8, 2, 6, 4],
# 	[6, 2, 2, 2]
# ]
# local_maximums(grid)

# grid = [
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 2, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1]
# ]
# local_maximums(grid)
# Example Output:

# [[9, 9], [8, 6]]
# [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
# Advanced Problem Set Version 2
# Problem 1: Words Containing Character
# Write a function words_with_char() that accepts a list of strings words and a character x. Return a list of indices representing the words that contain the character x. The returned list may be in any order.

# def words_with_char(words, x):
# 	pass
# Example Usage:

# words = ["batman", "superman"]
# x = "a"
# words_with_char(words, x)

# words = ["black panther", "hulk", "black widow", "thor"]
# x = "a"
# words_with_char(words, x)

# words = ["star-lord", "gamora", "groot", "rocket"]
# x = "z"
# words_with_char(words, x)
# Example Output:

# [0, 1]
# [0, 2]
# []
# 💡Hint: Python Basics

# Problem 2: HulkSmash
# Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:

# answer[i] == "HulkSmash" if i is divisible by 3 and 5.
# answer[i] == "Hulk" if i is divisible by 3.
# answer[i] == "Smash" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
# def hulk_smash(n):
# 	pass
# Example Usage:

# n = 3
# hulk_smash(n)

# n = 5
# hulk_smash(n)

# n = 15
# hulk_smash(n)
# Example Output:

# ["1", "2", "Hulk"]
# ["1", "2", "Hulk", "4", "Smash"]
# ["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]

# Problem 3: Encode
# The Riddler is planning to leave a coded message to lead Batman into a trap. Write a function shuffle() that takes in a string, the Riddler's message, and encodes it using an integer array indices. The message will be shuffled such that the character at the ith position in message moves to index indices[i] in the shuffled string. You may assume len(message) is equal to the len(indices).

# def shuffle(message, indices):
# 	pass
# Example Usage:

# message = "evil"
# indices = [3, 1, 2, 0]
# shuffle(message, indices)

# message = "findme"
# indices = [0, 1, 2, 3, 4, 5]
# shuffle(message, indices)
# Example Output:

# "lvie"
# "findme"
# 💡Hint: String Methods

# Problem 4: Good Samaritan
# Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. He wants to distribute meals in the least number of trips possible.

# Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. There are also m empty boxes which can contain up to capacity[i] meals.

# Given an array meals of length n and capacity of size m, write a function minimum_boxes() that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.

# Note that meals from the same pack can be distributed into different boxes.

# def minimum_boxes(meals, capacity):
# 	pass
# Example Usage:

# meals = [1, 3, 2]
# capacity = [4, 3, 1, 5, 2]
# minimum_boxes(meals, capacity)

# meals = [5, 5, 5]
# capacity = [2, 4, 2, 7]
# minimum_boxes(meals, capacity)
# Example Output:

# 2
# 4
# 💡Hint: Sorting Lists

# Problem 5: Heist
# The legendary outlaw Robin Hood is looking for the target of his next heist. Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.

# If multiple customers have the highest wealth, return the index of any customer.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# def wealthiest_customer(accounts):
# 	pass
# Example Usage:

# accounts = [
# 	[1, 2, 3],
# 	[3, 2, 1]
# ]
# wealthiest_customer(accounts)

# accounts = [
# 	[1, 5],
# 	[7, 3],
# 	[3, 5]
# ]
# wealthiest_customer(accounts)

# accounts = [
# 	[2, 8, 7],
# 	[7, 1, 3],
# 	[1, 9, 5]
# ]
# wealthiest_customer(accounts)
# Example Output:

# [0, 6]
# [1, 10]
# [0, 17]
# ✨ AI Hint: Nested Lists

# Problem 6: Smaller Than
# Write a function smaller_than_current that accepts a list of integers nums and, for each element in the list nums[i], determines the number of other elements in the array that are smaller than it. More formally, for each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer as a list.

# def smaller_than_current(nums):
# 	pass
# Example Usage:

# nums = [8, 1, 2, 2, 3]
# smaller_than_current(nums)

# nums = [6, 5, 4, 8]
# smaller_than_current(nums)

# nums = [7, 7, 7, 7]
# smaller_than_current(nums)
# Example Output:

# [4, 0, 1, 1, 3]
# [2, 1, 0, 3]
# [0, 0, 0, 0]
# ✨ AI Hint: Nested Loops

# Problem 7: Diagonal
# Write a function diagonal_sum() that accepts a 2D n x n matrix grid and returns the sum of the matrix diagonals. Only include the sum of all the elements on the primary diagonal and all the elements in the secondary diagonal that are not part of the primary diagonal.

# The primary diagonal is all cells in the matrix along a line drawn from the top-left cell in the matrix to the bottom-right cell. The secondary diagonal is all cells in the matrix along a line drawn from the top-right cell in the matrix to the bottom-left cell.

# def diagonal_sum(grid):
# 	pass
# Example 1 input matrix with primary and secondary diagonals labelled

# Example Usage

# grid = [
# 	[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# diagonal_sum(grid)

# grid = [
# 	[1, 1, 1, 1],
#     [1, 1, 1, 1],
# 	[1, 1, 1, 1],
#     [1, 1, 1, 1]
# ]
# diagonal_sum(grid)

# grid = [
# 	[5]
# ]
# diagonal_sum(grid)
# Example Output:

# 25
# 8
# 5

# Problem 8: Defuse the Bomb
# Batman has a bomb to defuse, and his time is running out! His butler, Alfred, is on the phone providing him with a circular array code of length n and key k.

# To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!

# def defuse(code, k):
# 	pass
# Example Usage:

# code = [5, 7, 1, 4]
# k = 3
# defuse(code, k)

# code = [1, 2, 3, 4]
# k = 0
# defuse(code, k)

# code = [2, 4, 9, 3]
# k = -2
# defuse(code, k)
# Example Output:

# [12, 10, 16, 13]
# [0, 0, 0, 0]
# [12, 5, 6, 13]