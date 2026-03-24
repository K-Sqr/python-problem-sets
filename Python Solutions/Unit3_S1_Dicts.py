# Problem 1: Calling Mississippi
# In a new Replit, copy and paste the following function:

def count_mississippi(limit):
    for num in range(1, limit):
	    print( f"{num} mississippi")
# Call the function so that it prints out the following to the console (without calling the function more than once):
#count_mississippi(6)
# 1 mississipi
# 2 mississipi
# 3 mississipi
# 4 mississipi
# 5 mississipi
# ✨ AI Hint: String Interpolation

# Problem 2: Swap Ends
# Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
    first = my_str[0]
    last = my_str[-1]
    middle = my_str[1:-1]
    return last + middle + first
# Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
# print(swapped)
# Example Output: toab

# ✨ AI Hint: String Indexing
# 💡 What's the difference between strings and lists?

# Problem 3: Is Pangram
# Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
    new_str = my_str.lower()
    new_set = set(char for char in new_str if char.isalpha())
    
    return len(new_set) == 26
# Example Usage:

# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))
# Example Output:

# True
# False
# 💡 Hint: Capitalization
# ✨ AI Hint: String Looping

# Problem 4: Reverse String
# Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    reversed_str = []
    length = len(my_str)
    for i in range(length-1,-1,-1):
        reversed_str.append(my_str[i])
    final = ''.join(reversed_str)
    return final

# Example Usage:

my_str = "live"
print(reverse_string(my_str))
# Example Output: evil


# Problem 5: First Unique
# Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

def first_unique_char(my_str):
    # create a dictionary
    my_dict = {}
    # add elements of str to dictionary
    #keep going
    for char in my_str:
        if char not in my_dict:
             my_dict[char] = 1
        else:
             my_dict[char] += 1
    for key,value in my_dict.items():
        if value == 1:
            return my_str.index(key)
    return -1
# Example Usage:

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
# Example Output

# 0
# 2
# -1

# Problem 6: Minimum Distance
# Write a function min_distance() that takes in a list of strings words and two strings word1 and word2' as parameters.
#  The function should return the minimum distance between word1 and word2 in the list of words. 
# The distance between one word and an adjacent word in the list is 1.

def min_distance(words, word1, word2):
     return abs(words.index(word1)-words.index(word2))
# Example Usage:

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
# Example Output:

# 3
# 1
# 2
date = "23-12-2004"
is_valid_month = 1 < int(date[3:5]) < 12
print(is_valid_month)