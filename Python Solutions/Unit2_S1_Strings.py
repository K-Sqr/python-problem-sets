# Problem Set 1: Dictionaries
#  
# Problem 1: Subsequence
'''Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters.
 Given these two lists, determine whether the sequence list is a subsequence of the lst list.
   A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list.
     Return True if sequence is a subsequence, and False otherwise.'''
    
def is_subsequence(lst, sequence):
    if not sequence:
        return True
    if not lst:
        return False
    subIndex = 0
    for i in lst:
        if i == sequence[subIndex]:
            subIndex += 1
        if subIndex == len(sequence):
            return True
    return False

    
# Problem 2: Create a Dictionary
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]   ## should return true
sequence1 = [1, 8, -1, 10]   ## should return false
print(is_subsequence(lst, sequence1))

# Problem 2: Create a Dictionary
def create_dictionary(keys, values):
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

print(create_dictionary(keys,values))

# Problem 3: Print Pair
def print_pair(dictionary, target):
    if target in dictionary: 
        print(f"Key: {target}")
        print(f"Value: {dictionary[target]}")
    else:
        print("That pair does not exist")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

# Problem 4: Keys Versus Values
def keys_v_values(d):
    key_tot = 0
    val_tot = 0
    for k in d.keys():
        key_tot += k
    for val in d.values():
        val_tot += val
    if key_tot > val_tot:
        return "Keys"
    elif key_tot < val_tot:
        return "Values"
    else:
        return "Balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)
dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
# Problem 5: Restock Inventory
def restock_inventory(current_inventory, restock_list): 
    for k,v in restock_list.items():
        if k in current_inventory:
            current_inventory[k] += v 
        else:
            current_inventory[k] = v
    return current_inventory
    
current_inventory = {
 "apples": 30,
 "bananas": 15,
 "oranges": 10
}
restock_list = {
 "oranges": 20,
 "apples": 10,
 "pears": 5
}

print(restock_inventory(current_inventory, restock_list))

# Problem 6: Calculate GPA

def calculate_gpa(report_card):
    tot = 0.0
    for v in report_card.values():
        if v == "A":
            tot += 4
        elif v == "B":
            tot += 3
        elif v == "C":
            tot += 2
        elif v == "D":
            tot += 1
        else:
            tot =+ 0
    return tot/len(report_card.values())

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B"}
print(calculate_gpa(report_card))
# Problem 7: Best Book
def highest_rated(books):
    rating = 0.0
    dic = {}
    for d in books:
        if float(d.get("rating")) > rating:
            rating = float(d.get("rating"))
            dic = d
    return dic

books = [
 {"title": "Tomorrow, and Tomorrow, and Tomorrow",
 "author": "Gabrielle Zevin",
 "rating": 4.18
 },
 {"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
 },
 {"title": "The Seven Husbands of Evenlyn Hugo",
 "author": "Taylor Jenkins Reid",
 "rating": 4.40
 }
]

print(highest_rated(books))

# Problem 8: Index-Value Map
def index_to_value_map(lst):
    d = {}
    for index,i in enumerate(lst):
        d[index] = i
    return d

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))

# Problem 1: Is Monotonic
def is_monotonic(nums):
    if not nums:
        return True
    if nums[0] <= nums[1]:
        for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
    else:
        for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
    return True

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))
nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))
nums3 = [1,1,1]
print(is_monotonic(nums3))
nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))

# Problem 2: Student Directory
def student_directory(student_names):
    d = {}
    for index, student in enumerate(student_names):
        d[student] = index + 1
    return d

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee",]

print(student_directory(student_names))

# Problem 3: Dictionary Description
def get_description(info, keys):
    for key in keys:
        if key in info:
            print(info[key])
        else:
            print(None)


info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)

#  Problem 5: Merge Catalogs
def merge_catalogs(catalog1, catalog2):
    d={}
    for k,v in catalog1.items():
        d[k] = v
    for k,v in catalog2.items():
        d[k] = v
    return d

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}

print(merge_catalogs(catalog1,catalog2))      

def contains_duplicate(nums):
    d ={}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1 
    for value in d.values():
        if value > 1:
            return True
    return False

        #!/bin/python3



#
# Complete the 'ransom_note' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING message
#  2. STRING magazine
#

def ransom_note(message, magazine):
    message_list = [char for char in message.lower() if char.isalpha()]
    magazine_list = [char for char in magazine.lower() if char.isalpha()]
    messageD ={}
    magazineD = {}
    for char in message_list:
        if char not in messageD:
            messageD[char] = 1
        else:
            messageD[char] += 1
    for char in magazine_list:
        if char not in magazineD:
            magazineD[char] = 1
        else:
            magazineD[char] += 1
    for k in messageD.keys():
        if k not in magazineD.keys() or messageD[k] != magazineD[k]:
            return False
    return True
            
  

            

            
            
            






    

