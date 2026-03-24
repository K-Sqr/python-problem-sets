# Problem Set Version 1
# Problem 1: Battle Pokemon
# Given the Pokemon class below, copy the code and add it to your Replit.

class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
# 	def attack(self, opponent):
# 		pass
# Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

# If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

# Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".

# Example Usage:

# pikachu = Pokemon("Pikachu", 35, 20)
# bulbasaur = Pokemon("Bulbasaur", 45, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)
# Example Output: "Pikachu dealt 20 damage to Bulbasaur"

# ✨ AI Hint: Writing Methods

# Problem 2: Convert to Linked List
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially.
#  The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list.
#  If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. 
# Each node may be stored in an unrelated memory location. 
# To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_2 = Node("Wigglytuff")	
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2
# Example Usage (after completing the problem with variable names node_1 and node_2):

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
# Example Output:

# Jigglypuff -> Wigglytuff
# Wigglytuff -> None
# Result Linked list: Jigglypuff -> Wigglytuff

# ✨ AI Hint: Linked Lists

# Problem 3: Add First
# Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

# It should insert new_node as the new head of the linked_list. The function returns new_node.

# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		

		
def add_first(head, new_node):
    new_node.next = head 
    return new_node
# Example Usage:

# # Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)
# Example Output:

# Jigglypuff -> Wigglytuff 
# Ditto -> Jigglypuff

# Problem 4: Get Tail
# Write a function get_tail() that takes in the head of a linked list as a parameter.

# It should print out the value of the tail of the list.

# If the list is empty (head is None), return None.
# Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

def get_tail(head):
    curNode = head
    while curNode.next:
            curNode = curNode.next
    return curNode
		

num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)
tail = get_tail(num1)
print(tail.value)
# Example Output: num3

# 💡 Hint: Linked List Traversal

# Problem 5: Replace Node
# Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original and replacement as parameters.

# The function updates any node with value original to have value replacement.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

#Understand

# function takes in two values, original and replacement as parameters.
# Updates any node with value of original with the value of replacement


# Plan

# assign head to a pointer (current)
# Treat the cases (this is needed because this is a singly linked lis and accessing the previous node is not allowed)
    # When the value is in the head
    # When the value is in the tail
    # When the value is not in the corner
# Edge Cases
    # When the linked list is empty
    # Has just one element

def ll_replace(head, original, replacement):
    current = head
    while current:
        if current.value == original:
             current.value = replacement          
        current = current.next
# Example Usage:

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# # initial linked list: 5 -> 6 -> 5
head = num1
ll_replace(head, 5, "banana")
print(num1.value, num2.value, num3.value)
# # updated linked list: "banana" -> 6 -> "banana"

# Problem 6: List Nodes
# Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.

# The function returns a list of values of the first n nodes.

# If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# Understand 
# returns a list of the vlaues of the first n nodes

# Plan
#  initialize three variables: 
    # List: store the values

def listify_first_n(head, n):
    lst = []
    count  = 0
    current = head
    while count < n and current:
        lst.append(current.value)
        count += 1
        current = current.next
    return lst
          
    

# Example Usage:

# # linked list: a -> b -> c
# head = a
# lst = listify_first_n(head,2)
# print(lst)

# # linked list: j -> k -> l 
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)
# Example Output:

# [`a`, `b`]
# [`j`, `k`, `l`]

# Problem 7: Insert Value
# Write a function ll_insert() that takes in a head of a linked list, a value val, and an index i as parameters.

# The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.

# If i is greater than the length of the list, insert the new node at the end of the list.
# Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
# Understand
#insert a value in index i of the linked list
#return the head

# Plan
 # use a count variabl to track index
 # use a current pointer vairable to track the nodes
 # In any case, a new value will be inserted so, I can instaiate a new node from the value in the param
 # Cases
    # the place to insert is in index 0
    # head is null
 # loop with a while loop
    # loop till current is null and count >= i(unsure if it's >= or >)
    # use current to track the spot before the insertion stop
    # link the new Node next link to the current Node's next
    # Then current Node's next link to new Node.

#I
def ll_insert(head, val, i):
    new_node = Node(val)
    if i == 0 or not head:
        new_node.next = head
        return new_node
    current = head
    count = 0
    prev = None
    while count < i and current:
        prev = current
        current = current.next
        count += 1
    # Insert at the end if i > length
    prev.next = new_node
    new_node.next = current
    return head
   
# 	pass
# Example Usage:

# # linked list: 3 -> 8 -> 12 -> 9
# ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9

# Problem 8: Linked Listify
# Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. 
# The function should return the head of the linked list.


# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

#Undersand
# turn a list into a linked list
# return the head of the list

#plan
#cases
# lst is empty: return 	
def list_to_linked_list(lst):
    if len(lst) < 1:
        return None
    head = Node(lst[0])
    current = head
    for i in range(1,len(lst)):
        n = Node(lst[i])
        current.next = n
        current = n
    return head

# Example Usage:

# normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
# linked_list = list_to_linked_list(normal_list)
# print(linked_list) # Only prints the head element!
# Example Output:

# Betty # Linked list : Betty -> Veronica -> Archie -> Jughead

# Problem 9: Doubly Linked List
# One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

# A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

# Given the Node class for a doubly linked list below, recreate the list ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list.

class Node:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev  
        
          
        
def print_list(self):
    current = self
    values = []
    while current:
        values.append(str(current.value))
        current = current.next
    return " -> ".join(values)
        
        
     
# Example Usage: (after completing the problem with variable names poliwag, poliwhirl, and poliwrath):

node_1 = Node("Poliwag")
node_2 = Node("Poliwhirl")
node_3 = Node("Poliwrath")
node_1.next = node_2
node_2.next = node_3
node_2.prev = node_1
node_3.prev = node_2

# print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
# Example Output:

# 'Poliwag' <-> 'Poliwhirl' <-> 'Poliwrath'`

# Problem 10: Print Backwards
# Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.

# It should print out the values of the linked list in reverse order, each separated by a space.

# class Node:
# 	def __init__(self, value, next = None, prev = None):
# 		self.value = value
# 		self.next = next
# 		self.prev = prev
		
def print_reverse(tail):
    if not tail:
        return
    lst = []
    current = tail
    while current:
        lst.append(current.value)
        current = current.prev
    print(" ".join(lst))
        
         
    
    
        
# Example Usage: (using the doubly linked list from Problem 9)

# #              (head)                       (tail)
# # Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
# print_reverse(poliwrath)
# Example Output: Poliwrath Poliwhirl Poliwag


# Problem Set Version 2
# Problem 1: Poker Two-Pair Hand
# In poker, players are given a hand of five cards. A player has a "two-pair" hand if they have two cards of the same rank and another two cards of another rank. The fifth card isn’t used here.

# Given the Card class below, write a function is_two_pair() that takes in a list player_hand that contains 5 Card objects.

# The function returns True if the player has a two pair hand and False otherwise.

# Cards in the hand are guaranteed to be unique and are guaranteed to have on the following suits and ranks:

# The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
# The rank is one of the following values: '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
# class Card():
# 	def  __init__(self, suit, rank):
# 		self.suit = suit
# 		self.rank = rank

# def is_two_pair(player_hand):
# 	pass
# Example Usage:

# card_one = Card("Hearts", "Ace")
# card_two = Card("Hearts", "4")
# card_three = Card("Diamonds", "Ace")
# card_four = Card("Diamonds", "4")
# card_five = Card("Diamonds", "6")
# card_six = Card("Diamonds", "7")

# player_one_hand = [card_one, card_two, card_three, card_four, card_five]
# print(is_two_pair(player_one_hand))

# player_two_hand = [card_two, card_three, card_four, card_five, card_six]
# print(is_two_pair(player_two_hand))
# Example Output:

# True  # Two Aces + Two 4s (+ Unused 6)
# False # Two 4s (+ Ace + 6 + 7)
# ✨ AI Hint: Writing Methods

# Problem 2: Barbie Linked List
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class below, recreate the list ['Barbie', 'President Barbie', 'Weird Barbie', 'Ken'] as a linked list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4):

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)
# Example Output:

# Barbie -> President Barbie
# President Barbie -> Weird Barbie
# Weird Barbie -> Ken
# Ken -> None
# Result Linked list: Barbie -> President Barbie -> Weird Barbie -> Ken

# ✨ AI Hint: Linked Lists

# Problem 3: Insert Value First
# Using the Node class, write a function add_first() that takes in the head of a linked list and a value object val as parameters.

# The function should insert a new Node object with value val as the new head of the linked list and return the new node.

# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
		
# def add_first(head, val):
# 	pass
# Example:

# # Linked List: A -> B -> C
# new_list = add_first(node_a, 0)
# # New List: 0 -> A -> B -> C

# Problem 4: Linked List Length
# Write a function ll_length() that takes in a head of a linked list as a parameter and returns the length of the linked list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# def ll_length(head):
# 	pass
# Example Usage:

# # Linked List: num1 -> num2 -> num3
# head = num1
# print(ll_length(head))

# # Empty Linked List
# head = None
# print(ll_length(head))
# Example Output:

# 3
# 0
# 💡 Hint: Linked List Traversal

# Problem 5: Delete Tail
# Write a function delete_tail() that takes in a head of a linked list as a parameter and removes the tail from the end of the list.

# The function does not need to return any value, as it modifies the linked list in place.

# Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# def delete_tail(head):
# 	pass
# Example Usage:

# # linked list: num1 -> num2 -> num3
# delete_tail(num1)

# # linked list: num1 -> num2

# Problem 6: Greatest Node
# Write a function find_max() that takes in a head of a linked list as a parameter where each node is an integer value.

# The function should return the maximum value in the linked list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
# def find_max(head):
# 	pass
# Example Usage:

# num1 = 20
# num2 = 15
# num3 = 30
# num4 = 10

# # linked list: num1 -> num2 -> num3 -> num4
# max_val = find_max(num1)
# print(max_val)
# Example Output: 30


# Problem 7: Pop Node
# Write a function ll_pop() that takes in the head of a linked list and an index i as parameters.

# The function should remove the node at index i of the linked list and return the head of the list.

# If i is greater than the length of the list, do nothing.
# Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
# def ll_pop(head, i):
# 	pass
# Example Usage:

# # linked list: num1 -> num2 -> num3
# ll_pop(num1, 1)
# # result: num1 -> num3

# Problem 8: Find Middle Node
# Write a function find_middle_node() that takes in the head of a linked list and returns the "middle" node.

# If the linked list has an even length and there are two "middle" nodes, return the first middle node.
# (E.g., "1 -> 2 -> 3 -> 4" would return 2, not 3.)
# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
# def find_middle_node(head):
# 	pass
# Example Usage:

# # linked list: num1 -> num2 -> num3 -> num4
# head = num1
# mid = find_middle_node(head)
# # mid == num2

# Problem 9: Create Double Links
# One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

# A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

# Update the Node constructor below so that the code creates a doubly linked list with head <-> tail.

# class Node:
# 	def __init__(self, value, next = None):
# 	    self.value = value
# 		self.next = next

# head = Node("First")
# tail = Node("Last")

# head.next = tail
# tail.prev = head
# Example Usage:

# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)
# Example Output:

# First <-> Last
# First <-> Last

# Problem 10: Double to Single
# Below are the node classes for a singly linked list and a doubly linked list. Write a function dll_to_sll() that takes in the head of a doubly linked list as a parameter and recreates it as a singly linked list.

# The function returns the head of the new singly linked list.

# class SLLNode:
# 	def __init__(self, value, next = None):
# 		self.value = value
# 		self.next = next

# class DLLNode:
# 	def __init__(self, value, next = None, prev = None):
# 		self.value = value
# 		self.next = next
# 		self.prev = prev
		
# def dll_to_sll(dll_head):
# 	pass
# Example Usage:

# # DLL: Ice <-> Water <-> Steam
# dll_head = Ice
# sll_head = dll_to_sll(dll_head)

# #SLL: Ice -> Water -> Steam

# Problem Set Version 3
# Problem 1: Calculate Tournament Placement
# In the Player class below, each player has a race_outcomes attribute which holds a list of integers describing what place they came in for each race in a tournament.

# Write a method get_tournament_place() that takes in one parameter opponents, a list of other player objects also participating in the tournament, and returns the place in the overall tournament.

# Rank in the tournament is determined by the lowest average race outcome. (1st place is better than 2nd!)
# Each opponent in opponents is guaranteed to have participated in the same number of races as the current player.
# class Player:
#     def __init__(self, character, kart, outcomes):
#         self.character = character
#         self.kart = kart
#         self.items = []
#         self.race_outcomes = outcomes

#         def get_tournament_place(self, opponents):
#             pass
# Example Usage:

# player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
# player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
# player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

# opponents = [player2, player3]
# print(f"{player1.character} was number {player1.get_tournament_place(opponents)}")
# Example Output:

# Mario was number 1 # Mario's average place is 1.6, Luigi's is 2.0, and Peach's is 2.4
# ✨ AI Hint: Writing Methods

# Problem 2: Update Linked List Sequence
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class and linked list below, update the current linked list red -> yellow -> blue to be red -> orange -> yellow -> green -> blue.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# red = Node('red')
# yellow = Node('yellow')
# blue = Node('blue')
# red.next = yellow
# yellow.next = blue
# Example:

# # Current list: red -> yellow -> blue
# # Desired list: red -> orange -> yellow -> green -> blue
# ✨ AI Hint: Linked Lists

# Problem 3: Insert Node as Second Element
# Write a function add_second() that takes in the head of a linked list and a value object val as parameters. It should insert val as the second node in the linked list and return the head of the linked list. (You can assume head is not None.)

# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
        
#     def add_second(head, val):
#         pass
# Example:

# # linked list: 1 -> 3 -> 4
# # add_second(head, 2)
# # result: 1 -> 2 -> 3 -> 4

# Problem 4: Increment Linked List Node Values
# Write a function increment_ll() that takes in the head of a linked list of integer values and returns the same list, but with each node's value incremented by 1. Return the head of the list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def increment_ll(head):
#     pass  
# Example Usage:

# # my_list: 5 -> 6 -> 7
# print(my_list.value)

# my_list = increment_ll(my_list)
# # my_list: 6 -> 7 -> 8
# print(my_list.value)

# my_list = increment_ll(my_list)
# # my_list: 7 -> 8 -> 9
# print(my_list.value)
# Example Output:

# 5
# 6
# 7
# 💡 Hint: Linked List Traversal

# Problem 5: Copy Linked List
# Write a function copy_ll() that takes in the head of a linked_list, and creates a complete copy of that linked list.

# The function should return the head of a new linked list which is identical to the given list in terms of its structure and contents, but does not use any of the node objects from the original list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def copy_ll(head):
#     pass
# Example Usage:

# # Linked List: 5 -> 6 -> 7
# copy = copy_ll(head) # Linked List Copy: 5 -> 6 -> 7
# print(head.value, copy.value)

# # Change original list -- should not affect the copy
# head.value = 10
# print(head.value, copy.value)
# Example Output:

# 5 5
# 10 5

# Problem 6: Find Minimum in Linked List
# Write a function find_min() that takes in the head of a linked_list, and returns the minimum value in the linked list. You can assume the linked list will contain only numeric values.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def find_min(head):
#     pass  
# Example:

# # Linked List: 5 -> 6 -> 7 -> 8
# # Input: head = 5
# # Expected Output: 5

# # Linked List: 8 -> 5 -> 6 -> 7
# # Input: head = 8
# # Expected Output: 5

# Problem 7: Remove Node by Value from Linked List
# Write a function ll_remove() that takes in the head of a linked list and a value val as parameters.

# The function should remove the first node it finds in the linked list with value val and return the head of the linked list. If no node can be found with the value val, return the list unchanged.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def ll_remove(head, val):
#     pass 
# Example:

# # Linked List: 5 -> 6 -> 7 -> 8
# # Input: head = 5, val = 6
# # Expected Output: 5 -> 7 -> 8

# Problem 8: Move Tail to Front of Linked List
# Write a function tail_to_head() that takes in the head of a linked list as a parameter, and moves the tail of the linked list to the front.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def tail_to_head(head):
#     pass 
# Example:

# # Input: 1 -> 2 -> 3 -> 4
# # Output: 4 -> 1 -> 2 -> 3

# Problem 9: Convert Singly Linked List to Doubly Linked List
# One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

# A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

# Update the code below to convert the singly linked list a doubly linked list.

# class Node:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

# crazy_in_love = Node("Crazy in Love")
# formation = Node("Formation")
# texas_hold_em = Node("Texas Hold 'Em")
# crazy_in_love.next = formation
# formation.next = texas_hold_em
# Example:

# # Current Singly Linked List: Crazy in Love -> Formation -> Texas Hold 'Em
# # Desired Doubly Linked List: Crazy in Love <-> Formation <-> Texas Hold 'Em

# Problem 10: Find Length of Doubly Linked List from Any Node
# Write a function get_length() that takes in a node at an unknown position within a doubly linked list. The function should return the length of the entire list.

# class Node:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         this.next = next
#         this.prev = prev

# def get_length(node):
#     pass 