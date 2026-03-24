# Problem Set Version 1
# Problem 1: Pokemon Class
# Step 1: Copy the following code into Replit.

# Step 2: Add a line of code (outside of the class) to instantiate an instance of the class Pokemon and store it in a variable named my_pokemon.
#  The Pokemon instance created should have name "Pikachu" and its types should be ["Electric"].

# class Pokemon:
#     def __init__(self, name, types, attack):
#         self.name = name
#         self.types = types
#         self.attack = attack
#         self.is_caught = False

# my_pokemon = Pokemon("Pikachu", ["Electric"],"fire")
# ✨ AI Hint: Intro to Object Oriented Programming
# Key Skill: Use AI to explain code concepts

# This problem may require you to be familiar with Object Oriented Programming (OOP) basics, including classes, instances, objects, and constructors. To help, we've included an "intro to OOP" review Unit 5 Cheatsheet

# You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Can you help me understand OOP conceptually, using analogies to real-world objects?"

# Once you understand the concept, you can also ask follow-up questions like:

# "Can you provide an example of a class, instance, and constructor in python?"

# "What does self mean in Python, and how is it used in OOP?"


# Problem 2: Create Squirtle
# Step 1: Add the print_pokemon definition below to your code on Replit.

# Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. 
# The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

# Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

# class Pokemon:

#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = True


#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#          "is_caught": self.is_caught # Output: "is_caught": False
#          })

# squirtle = Pokemon("Squirtle",["Water"])

# squirtle.print_pokemon()

# ✨ AI Hint: Class Methods
# Key Skill: Use AI to explain code concepts

# This question requires you to be familiar with class methods, which are functions attached to an object. To help, we've included more info Unit 5 Cheatsheet

# If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Please provide 2-3 examples of how Class Methods are used in Python, and explain how each one works."

# You might also want to ask questions like:

# "Can you explain the difference between class methods, instance methods, and functions?"


# Problem 3: Is Caught
# Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True.
#  Use the print_pokemon() function to verify that squirtle's is_caught property was updated.

# Expected Output:

# class Pokemon:

#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = True


#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#          "is_caught": self.is_caught # Output: "is_caught": False
#          })

# squirtle = Pokemon("Squirtle",["Water"])

# squirtle.print_pokemon()

# {
#     "name": "Squirtle",
#     "types": ["Water"],
#     "is_caught": True
# }
# ✨ AI Hint: Class Attributes
# Key Skill: Use AI to explain code concepts

# This problem may require you to be familiar with class attributes, which are variables attached to an object. To help, we've included more info Unit 5 Cheatsheet

# If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Please provide 2-3 examples of how Class Attributes are used in Python, and explain how each one works."


# Problem 4: Catch Pokemon
# Update the Pokemon class with a new method catch() that takes in no parameters except self.

# The method should update the Pokemon's is_caught attribute to True and not return any value.

class Pokemon:
       
	def __init__(self, name, types):
		self.name = name
		self.types = types
		self.is_caught = False
		
	def print_pokemon(self):
		print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
            })
	def catch(self):
 	    self.is_caught = True

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()

# ✨ AI Hint: Writing Methods
# Key Skill: Use AI to explain code concepts

# This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:

# Check out the Unit 5 Cheatsheet
# Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python

# Problem 5: Choose Pokemon
# Update the Pokemon class with a new method choose() that takes in no parameters except self.

# If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

# Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".

class Pokemon:
	   
	def __init__(self, name, types):
		self.name = name
		self.types = types
		self.is_caught = False
		
	def print_pokemon(self):
		print({
			"name": self.name,   # Output: "name": "Squirtle",
			"types": self.types, # Output: "types": ["Water"],
			"is_caught": self.is_caught # Output: "is_caught": False
			})
	def catch(self):
		self.is_caught = True
		 
	def choose(self):
		if self.is_caught == True:
			print(f"{self.name} I choose you!")
		else:
			print(f"{self.name} is wild! Catch them if you can!")


#my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

# my_pokemon.choose()
my_pokemon.catch()
#my_pokemon.choose()
# Example Output:

# {
#     "name": "Rattata",
#     "types": ["Normal"],
#     "is_caught": False
# }

# Rattata is wild! Catch them if you can!
# Rattata I choose you!

# Problem 6: Add Pokemon Type
# Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

# It should add new_type to the Pokemon's list of types.

class Pokemon():
	def __init__(self, name, types):
		self.name = name
		self.types = types
		self.is_caught = False

	def print_pokemon(self):
		print({
			"name": self.name,   # Output: "name": "Squirtle",
			"types": self.types, # Output: "types": ["Water"],
			"is_caught": self.is_caught # Output: "is_caught": False
		})

	def catch(self):
		self.is_caught = True

	def add_type(self, new_type):
		self.new_type = new_type
		self.types.append(new_type)

# Example Usage:

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
# Example Output:

# {
#     "name": "Jigglypuff",
#     "types": ["Normal"]
#     "is_caught": False
# }

# {
#     "name": "Jigglypuff",
#     "types": ["Normal", "Fairy"]
#     "is_caught": False
# }

# Problem 7: Get Pokemon
# Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

# The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

# Hint: To test, loop over Pokemon in return list and print the Pokemon's name

def get_by_type(my_pokemon, pokemon_type):
	lst = []
	# for i in range(len(pokemon_type)):
	# 	if pokemon_type[i] == pokemon_type:
	# 		lst.append(my_pokemon)
	for i in my_pokemon:
		for type in i.types:
			if type == pokemon_type:
				lst.append(i.name)

	return lst
	

#Example Usage:

jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)
# Example Output: [jigglypuff, meowth, pidgeot]


# Problem 8: Pokemon Evolution
# Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an attribute evolution.
#  The attribute will either be the default value of None or another Pokemon instance.

# Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

# The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.

class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution

# U
# Returns back a list of itself and pokemons it can evolve into
# P
# create a list variable
# frist append the name of the pokemon
# check evolution until it's None (break down on Implementation)

# I
def get_evolutionary_line(starter_pokemon):
	evo_list = []
 #  pointer to keep track of current poke
	current_pokemon = starter_pokemon
	#loop stops if current pokemon is None
	while current_pokemon:
		evo_list.append(current_pokemon.name) 
		current_pokemon = current_pokemon.evolution
	return evo_list


# Example Usage:

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
# Example Output:

# [`Charmander`, `Charmeleon`, `Charizard`]
# [`Charmeleon`, `Charizard`]
# ['Charizard']


# Problem 9: Node Class
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class below, create two nodes:

# The first node should have value a and be stored in a variable node_one.
# The second node should have value b and be stored in a variable node_two.
# You do not need to connect the nodes together yet.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# Example Usage:

# print(node_one.value) 
# print(node_one.next) 
# print(node_two.value)
# print(node_two.next) 
# Example Output:

# a
# None
# b
# None
# ✨ AI Hint: Linked Lists
# Key Skill: Use AI to explain code concepts

# This question requires you to be familiar with Linked Lists, a incredibly useful but sometimes tricky data structure. To help, we've included a review of linked lists Unit 5 Cheatsheet

# You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Can you help me understand linked lists conceptually, using analogies to real-world objects?"

# Once you understand the concept of Linked Lists, you can also ask follow-up questions like:

# "Can you provide examples of how to implement a linked list in Python, and explain how each part works?"

# "Here is a provided Linked List class: (CODE). Can you give me an example of how to access the data in this linked list?"


# Problem 10: Linking Nodes
# Building off the Node class from Problem 9, now we will link the nodes together.

# To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9 to point to node_two.

# Example Usage (after updating node_one's next property):

# print(node_one.value)
# print(node_one.next.value)
# print(node_two.value)
# Example Output:

# a
# b
# b

# Problem 11: Mario Party
# Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# Result Linked List would be: Mario -> Luigi -> Wario -> Toad

# Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4.):

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)
# Example Output:

# Mario -> Luigi
# Luigi -> Wario
# Wario -> Toad
# Toad -> None

# Problem 12: Printing Linked List
# Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.

# Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next= next
		
# def print_linked_list(head):
# 	pass
# Example Input:

# # input linked list: a->b->c->d->e
# print_linked_list(a)
# Example Output:

# a -> b -> c -> d -> e
# 💡 Hint: Linked List Traversal
# This problem requires you to traverse a linked list. In other words, it requires you to iterate over the nodes of a linked list. For a break down of how to traverse a linked list, check out the Unit 5 Cheatsheet.


# Problem Set Version 2
# Problem 1: Card Class
# Step 1: Copy the following code into Replit.

# Step 2: Instantiate an instance of the class Card and store it in a variable named card. The Card object should have the suit "Spades" and the rank "8".

# class Card():
# 	def  __init__(self, suit, rank):
# 		self.suit = suit
# 		self.rank = rank
# ✨ AI Hint: Intro to Object Oriented Programming
# Key Skill: Use AI to explain code concepts

# This problem may require you to be familiar with Object Oriented Programming (OOP) basics, including classes, instances, objects, and constructors. To help, we've included an "intro to OOP" review Unit 5 Cheatsheet

# You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Can you help me understand OOP conceptually, using analogies to real-world objects?"

# Once you understand the concept, you can also ask follow-up questions like:

# "Can you provide an example of a class, instance, and constructor in python?"

# "What does self mean in Python, and how is it used in OOP?"


# Problem 2: Print Card
# Step 1: Update the Card class with the new method print_card() provided below:

# def print_card(self):
# 	print(f"{self.rank} of {self.suit}")
# Step 2: Create an instance of the class and store it in a variable named card. The object should have suit "Clubs" and rank "Ace".

# Step 3: Then, call the method print_card() on your card.

# Expected Output: Ace of Clubs

# ✨ AI Hint: Class Methods
# Key Skill: Use AI to explain code concepts

# This question requires you to be familiar with class methods, which are functions attached to an object. To help, we've included more info Unit 5 Cheatsheet

# If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Please provide 2-3 examples of how Class Methods are used in Python, and explain how each one works."

# You might also want to ask questions like:

# "Can you explain the difference between class methods, instance methods, and functions?"


# Problem 3: Verify Update
# Step 1: Using the same Card class from Problem 2, update your code so that the suit of card is "Hearts" instead of "Clubs".

# Step 2: Use the print_card() method to verify that card was updated.

# Expected Output: Ace of Hearts

# ✨ AI Hint: Class Attributes
# Key Skill: Use AI to explain code concepts

# This problem may require you to be familiar with class attributes, which are variables attached to an object. To help, we've included more info Unit 5 Cheatsheet

# If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Please provide 2-3 examples of how Class Attributes are used in Python, and explain how each one works."

# Problem 4: Valid Card
# Update the Card class with a new method is_valid() that takes in no parameters except self. The method should return True if:

# The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
# The rank is one of the following values: "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
# Otherwise, the method should return False

# class Card():
# 	...
	
# 	def is_valid(self):
# 		pass
# Example Usage:

# my_card = Card("Hearts", "7")
# print(my_card.is_valid())

# second_draw = Card("Spades", "Joker")
# print(second_draw.is_valid())
# Example Output:

# True
# False
# ✨ AI Hint: Writing Methods
# Key Skill: Use AI to explain code concepts

# This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:

# Check out the Unit 5 Cheatsheet
# Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python

# Problem 5: Get Value
# Update the Card class with a new method get_value() that takes in no parameters except self.

# The function returns the card's value depending on the card's rank:

# If the card has rank 2, 3, 4, 5, 6, 7, 8, 9, 10, the method should return the rank as an integer
# If the card has rank Ace, the method should return 1 as the card's value
# If the card has rank Jack, the method should return 11 as the card's value
# If the card has rank Queen, the method should return 12 as the card's value
# If the card has rank King, the method should return 13 as the card's value
# If the card is invalid, the method should return None
# class Card():
# 	...
	
# 	def get_value(self):
# 		pass
# Example Usage:

# card = Card("Hearts", "7")
# print(card.get_value())

# card_two = Card("Spades", "Jack")
# print(card_two.get_value())
# Example Output:

# 7
# 11

# Problem 6: Hand Class
# Step 1: Add the following Hand class to your code that represents a player's hand of cards.

# A new instance of Hand is always empty.
# class Hand:
#     def __init__(self):
#         self.cards = []
     
#     def add_card(self, card):
# 	    pass
	    
# 	def remove_card(self, card):
# 		pass
# Step 2: Add two methods add_card() and remove_card() to the Hand class that each accept a Card object as a parameter.

# add_card() should add the Card to the player's Hand
# remove_card() should remove the card from the player's Hand.
# Example Usage:

# card_one = Card("Hearts", "3")
# card_two = Card("Spades", "8")

# player1_hand = Hand()
# # cards = []

# player1_hand.add_card(card_one)
# # cards = [card_one]

# player1_hand.add_card(card_two)
# # cards = [card_one, card_two]

# player1_hand.remove_card(card_one)
# # cards = [card_two]

# Problem 7: Sum of Cards
# Write a function sum_hand() that takes in an instance of Hand as a parameter and returns the summed value of all cards in the hand.

# Use the methods from Problems 5-7 to assist you.
# If any card in the hand is invalid, return None.
# class Card():
#     def  __init__(self, suit, rank):
# 		self.suit = suit
# 		self.rank = rank
		
# 	#... methods from previous problems

# class Hand:
#     def __init__(self):
#         self.cards = []
        
# 	# ... methods from previous problems
		
	
# def sum_hand(hand):
# 	pass
# Example Usage:

# card_one = Card("Hearts", "3")
# card_two = Card("Hearts", "Jack")
# card_three = Card("Spades", "3")

# hand = Hand()
# hand.add_card(card_one)
# hand.add_card(card_two)
# hand.add_card(card_three)

# sum = sum_hand(hand)
# print(sum)
# Example Output: 17


# Problem 8: Print Hand
# The class Card has been updated below with a new attribute next to represent the card that comes after it in a hand of cards.

# Write a function print_hand() that accepts a Card object and returns a list of all cards in the hand that come after it.

# class Card():
# 	def  __init__(self, suit, rank, next = None):
# 		self.suit = suit
# 		self.rank = rank
# 		self.next = next
		
# def print_hand(starting_card):
# 	pass
# Example Usage:

# card_one = Card("Hearts", "3")
# card_two = Card("Hearts", "4")
# card_three = Card("Diamonds", "King")

# card_one.next = card_two
# card_two.next = card_three

# print_hand(card_one)
# Example Output: [card_one, card_two, card_three]


# Problem 9: Head and Tail Nodes
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class below, create two nodes.

# The first node should have value 100 and be stored in a variable head.
# The second node should have value 200 and be stored in a variable tail.
# Set head to point to tail.
# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# Example Usage:

# print(head.value) 
# print(head.next) 
# print(tail.value) 
# print(tail.next) 
# Example Output:

# 100
# 200
# 200
# None
# ✨ AI Hint: Linked Lists
# Key Skill: Use AI to explain code concepts

# This question requires you to be familiar with Linked Lists, a incredibly useful but sometimes tricky data structure. To help, we've included a review of linked lists Unit 5 Cheatsheet

# You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Can you help me understand linked lists conceptually, using analogies to real-world objects?"

# Once you understand the concept of Linked Lists, you can also ask follow-up questions like:

# "Can you provide examples of how to implement a linked list in Python, and explain how each part works?"

# "Here is a provided Linked List class: (CODE). Can you give me an example of how to access the data in this linked list?"


# Problem 10: Middle Node
# Within a linked list, we can redirect pointers to insert nodes at any place in the list.

# Create a new Node middle with value 150 and insert it between head and tail from Problem 9.

# Example Usage:

# print(head.next.value) 
# print(middle.next.value)
# print(tail.next.value) 
# Example Output:

# 150
# 200
# None
# Problem 11: Zodiac Signs
# Create the list ["aries", "taurus", "gemini", "cancer"] as a linked list using the Node class:

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4.):

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)
# Example Output:

# aries -> taurus
# taurus -> gemini
# gemini -> cancer
# cancer -> None

# Problem 12: Print Linked List
# Write a function print_linked_list() that takes in a head of a linked list as a parameter. The function prints and returns a list of all the values in the linked list in the order they appear in the linked list.

# Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next= next
		
# def print_linked_list(head):
# 	pass
# Example Usage:

# # input linked list: a->b->c->d->e
# print_linked_list(a)
# Example Output:

# [`a`,`b`,`c`,`d`,`e`]
# 💡 Hint: Linked List Traversal
# This problem requires you to traverse a linked list. In other words, it requires you to iterate over the nodes of a linked list. For a break down of how to traverse a linked list, check out the Unit 5 Cheatsheet.


# Problem Set Version 3
# Problem 1: Player Class
# Step 1: Copy the following code into Replit.

# Step 2: Instantiate an instance of the class Player and store it in a variable named player_one.

# The Player object should have the character "Yoshi" and the kart "Super Blooper".
# class Player():
# 	def  __init__(self, character, kart):
# 		self.character = character
# 		self.kart = kart
#         self.items = []
# ✨ AI Hint: Intro to Object Oriented Programming
# Key Skill: Use AI to explain code concepts

# This problem may require you to be familiar with Object Oriented Programming (OOP) basics, including classes, instances, objects, and constructors. To help, we've included an "intro to OOP" review Unit 5 Cheatsheet

# You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Can you help me understand OOP conceptually, using analogies to real-world objects?"

# Once you understand the concept, you can also ask follow-up questions like:

# "Can you provide an example of a class, instance, and constructor in python?"

# "What does self mean in Python, and how is it used in OOP?"


# Problem 2: Get Player
# Step 1: Using the Player class from Problem 1, add the following get_player() method to your Replit code:

# def get_player(self):
#     return f"{self.character} driving the {self.kart}"
# Step 2: Create a second instance of Player in a variable named player_two.

# The Player object created should have character "Bowser" and kart "Pirahna Prowler".
# Step 3: Use the method get_player() below to print out "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler".

# ✨ AI Hint: Class Methods
# Key Skill: Use AI to explain code concepts

# This question requires you to be familiar with class methods, which are functions attached to an object. To help, we've included more info Unit 5 Cheatsheet

# If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Please provide 2-3 examples of how Class Methods are used in Python, and explain how each one works."

# You might also want to ask questions like:

# "Can you explain the difference between class methods, instance methods, and functions?"


# Problem 3: Update Kart
# Players might want to update their choice of kart for their next race.

# Update player_one so that their kart is "Dolphin Dasher" instead of it's current value, "Super Blooper".

# Example Usage:

# print(player_one.get_player())

# # < your code to update kart>

# print(player_one.get_player())
# Example Output:

# Yoshi driving the Super Blooper
# Yoshi driving the Dolphin Dasher
# ✨ AI Hint: Class Attributes
# Key Skill: Use AI to explain code concepts

# This problem may require you to be familiar with class attributes, which are variables attached to an object. To help, we've included more info Unit 5 Cheatsheet

# If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Please provide 2-3 examples of how Class Attributes are used in Python, and explain how each one works."


# Problem 4: Set Character
# In the previous exercise, we accessed and modified a player’s kart attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

# Update your Player class with a method set_character() that takes in one parameter name.

# If name is valid, it should update the player’s character attribute to have value name and print "Character updated".
# Otherwise, it should print out "Invalid character".
# Valid character names are "Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", and "Bowser".

# class Player():
# 	def  __init__(self, character, kart):
# 		self.character = character
# 		self.kart = kart
# 		self.items = []
		
# 	def set_player(self, name):
# 		pass
# Example Usage:

# player_one.set_player("Peach")
# player_two.set_player("Kermit")
# Example Output:

# Character updated
# Invalid character
# ✨ AI Hint: Writing Methods
# Key Skill: Use AI to explain code concepts

# This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:

# Check out the Unit 5 Cheatsheet
# Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python

# Problem 5: Add Special Item
# Players can pick up special items as they race.

# Update the Player class with a new method add_item() that takes in one parameter, item_name.

# The method should validate the item_name.

# If the item is valid, add item_name to the player’s items attribute.
# The method does not need to return any values.
# item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".

# class Player():
# 	def  __init__(self, character, kart):
# 		self.character = character
# 		self.kart = kart
# 		self.items = []
		
# 	def add_item(self, item_name):
# 		pass
# Example Usage:

# player_one = Player("Yoshi", "Dolphin Dasher")
# # items = []

# player_one.add_item("red shell")
# # items = ["red shell"]

# player_one.add_item("super star")
# # items = ["red shell", "super star"]

# player_one.add_item("super smash")
# # items = ["red shell", "super star"]
# ✨ AI Hint: Writing Methods
# Key Skill: Use AI to explain code concepts

# This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:

# Check out the Unit 5 Cheatsheet
# Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python

# Problem 6: Print Inventory
# Update the Player class with a method print_inventory() that accepts no parameters except for self.

# The method should print the name and quantity of each item in a player’s items list.

# If the player has no items, the function should print "Inventory empty".
# class Player():
# 	...
	
# 	def print_inventory(self):
# 		pass
# Example Usage:

# player_one = Player("Yoshi", "Super Blooper")
# player_one.items = ["banana", "bob-omb", "banana", "super star"]
# player_two = Player("Peach", "Dolphin Dasher")

# player_one.print_inventory()
# player_two.print_inventory()
# Example Output:

# Inventory: banana: 2, bob-omb: 1, super star: 1
# Inventory empty

# Problem 7: Race Results
# Given a list race_results of Player objects where the first player in the list came first in the race, second player in the list came second, etc., write a function print_results() that prints the players in place.

# class Player:
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
# 	#... methods from previous problems
	
	
# def print_results(race_results):
# 	pass
# Example Usage:

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M")
# luigi = Player("Luigi", "Super Blooper")
# race_one = [peach, mario, luigi]

# print_results(race_one)
# Example Output:

# 1. Peach
# 2. Mario
# 3. Luigi

# Problem 8: Get Rank
# The Player class has been updated below with a new attribute ahead to represent the player currently directly ahead of them in the race.

# Write a function get_rank() that accepts a Player object my_player and returns their current place number in the race.

# class Player:
#     def __init__(self, character, kart, opponent=None):
#         self.character = character
#         self.kart = kart
#         self.items = []
#         self.ahead = opponent
        
# def get_place(my_player):
# 	pass
# Example Usage:

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M", peach)
# luigi = Player("Luigi", "Super Blooper", mario)

# player1_rank = get_place("Luigi")
# print(player1_rank)

# player2_rank = get_place("Peach")
# print(player2_rank)

# player3_rank = get_place("Mario")
# print(player3_rank)
# Example Output:

# 3
# 1
# 2

# Problem 9: Tom and Jerry
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class below, create a linked list cat -> mouse where the instance cat has value "Tom" which points to the instance mouse that has value "Jerry".

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# Example Usage:

# print(cat.value)
# print(cat.next)
# print(cat.next.value)
# print(mouse.value)
# print(mouse.next)
# Example Output:

# Tom
# mouse
# Jerry
# Jerry
# None
# ✨ AI Hint: Linked Lists
# Key Skill: Use AI to explain code concepts

# This question requires you to be familiar with Linked Lists, a incredibly useful but sometimes tricky data structure. To help, we've included a review of linked lists Unit 5 Cheatsheet

# You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:

# "You're an expert computer science tutor. Can you help me understand linked lists conceptually, using analogies to real-world objects?"

# Once you understand the concept of Linked Lists, you can also ask follow-up questions like:

# "Can you provide examples of how to implement a linked list in Python, and explain how each part works?"

# "Here is a provided Linked List class: (CODE). Can you give me an example of how to access the data in this linked list?"


# Problem 10: Chase List
# In a linked list, pointers can be redirected at any place in the list.

# Using the linked list from Problem 9, create a new Node dog with value "Spike" and point it to the cat node so that the full list now looks like dog -> cat -> mouse.

# Example Usage:

# print(dog.value)
# print(dog.next)
# print(dog.next.value)
# print(cat.next)
# print(cat.next.value)
# print(mouse.next.value)
# Example Output:

# Spike
# cat
# Tom
# mouse
# Jerry
# None

# Problem 11: Update Chase
# Using the linked list from Problem 10, remove the dog node and add in a node cheese with value "Gouda" to the end of the list so that the resulting list is cat -> mouse -> cheese.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# Problem 12: Chase String
# Write a function chase_list() that takes in a head of a linked list and returns a string linking together the values of the list with the separator "chases".

# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

# Example Usage:

# dog = Node("Spike")
# cat = Node("Tom")
# mouse = Node("Jerry")
# cheese = Node("Gouda")

# dog.next = cat
# cat.next = mouse
# mouse.next = cheese

# print(chase_list(dog))
# Example Output: "Spike chases Tom chases Jerry chases Gouda"

# 💡 Hint: Linked List Traversal
# This problem requires you to traverse a linked list. In other words, it requires you to iterate over the nodes of a linked list. For a break down of how to traverse a linked list, check out the Unit 5 Cheatsheet.