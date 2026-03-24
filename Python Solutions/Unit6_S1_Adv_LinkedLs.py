# Problem Set Version 1
# Problem 1: Nested Constructors
# Step 1: Copy the following code into Replit.

# Step 2: Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 in a single assignment statement.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
# 💡 Hint: Nested Constructors

node = Node(4,(Node (3,Node(2))))

def print_list(head):
    current = head
    values = []
    while current:
        values.append(str(current.value))
        current = current.next
    print (" -> ".join(values))
    
print_list(node)

# Problem 2: Find Frequency
# Given the head of a linked list and a value val, return the frequency of val in the list. Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

def count_element(head, val):
    if not head:
        return 0
    count = 0
    current = head
    while current:
        if current.value == val:
            count += 1
        current = current.next
    return count
    
          
	
# Example Usage:

# # Input List: 3 -> 1 -> 2 -> 1
# # Input: head = 3, val = 1
# Example Output:
node = Node(4,(Node (3,Node(2,Node(3,Node(1,Node(3)))))))

print(count_element(node,3))

# # 2

# Problem 3: Remove Tail
# The following code attempts to remove the tail of a singly linked list. However, it has a bug!

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes the tail of the list.

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
        
        
# # Helper function to print the linked list
# def print_list(node):
#     current = node
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()


# # I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head
# Example Usage:

node = Node(4,(Node(3,Node(2,Node(3,Node(1,Node(3)))))))

print_list(remove_tail(node))
# # Input List: 1 -> 2 -> 3 -> 4
# # Input: head = 1
# Example Output:

# # Expected Return Value: 1
# # Expected Result List: 1 -> 2 -> 3

# Problem 4: Find the Middle
# A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. 
# Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. 
# If there are two middle nodes, return the second middle node.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

def find_middle_element(head):
    if not head:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

node = Node(4,(Node(3,Node(2,Node(3,Node(1,Node(3)))))))
print(find_middle_element(node).value)
        
	
# Example Usage:

# # Input List:
# # 1 -> 2 -> 3
# # Input: head = 1
# Example Output:

# # Expected Return Value: 2
# ✨ AI Hint: Slow and Fast Pointers

# Problem 5: Is Palindrome?
# Given the head of a singly linked list, return True if the values of the linked list are palindromic and False otherwise.
# Use the two-pointer technique in your solution.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

def is_palindrome(head):
    if not head:
         return False
    if not head.next:
         return True
    
    slow = fast = head
    while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
    
    prev = None
    while slow:
         next_node = slow.next
         slow.next = prev
         prev = slow
         slow = next_node
     
    
# Example Usage:

# # Input List:
# # 1 -> 2 -> 1
# # Input: head = 1
# Example Output:

# # True
# ✨ AI Hint: Multiple Pass Technique

# Problem 6: Put it in Reverse
# Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse the list in place. Return the head of the reversed list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def reverse(head):
# 	pass
# Example Usage:

# # Input List: 1 -> 2 -> 3 -> 4
# # Input: head = 1
# Example Output:

# # Expected Return Value: 4
# # Expected Result List: 4 -> 3 -> 2 -> 1
# 💡 Hint: Which technique?
# Problem Set Version 2
# Problem 1: One to Many
# The assignment statement to the head variable below creates the linked list Mario -> Luigi -> Wario. Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# head = Node("Mario", Node("Luigi", Node("Wario")))
# 💡 Hint: Nested Constructors

# Problem 2: Find Max
# Given the head of a linked list where each node is an integer value, return the maximum value in the linked list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# def find_max(head):
# 	pass
# Example Usage:

# # Linked List: 5 -> 6 -> 7 -> 8 
# # Input: head = 5
# Example Output:

# # Expected Output: 8

# Problem 3: Remove First Value
# The following code attempts to remove the first node with a given value from a singly linked list based but it contains a bug!

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list.

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

# # Helper function to print the linked list
# def print_list(node):
#     current = node
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()

# # Function with a bug!
# def remove_by_value(head, val):
#     # Check if the list is empty
#     if head is None:
#         return head

#     # If the node to be removed is the head of the list
#     if head.value == val:
#         return head.next

#     # Initialize pointers
#     current = head.next
#     previous = head

#     # Traverse the list to find the node to remove
#     while current.next:
#         if current.value == val:
#             previous.next = current.next
#             return head
#         previous = current
#         current = current.next

#     # If no node was found with the value `val`, return the original head
#     return head
# Example Usage:

# # Input List: 1 -> 2 -> 3 -> 4
# # Value to Remove: 3
# Example Output:

# # Expected Return Value: 1
# # Expected Result List: 1 -> 2 -> 4

# Problem 4: Middle Match
# A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, and a value val, use the slow-fast pointer technique to determine if val matches the middle node of the list. If there are two middle nodes, return True if the second middle node matches the value val.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def middle_match(head, val):
# 	pass
# Example Usage:

# # Input List:
# # 1 -> 2 -> 3
# # Input: head = 1, val = 2

# # Input List:
# # 1 -> 2 -> 3 -> 4
# # Input: head = 1, val = 2
# Example Output:

# # Expected Return Value: True
# # Expected Return Value: False
# ✨ AI Hint: Slow and Fast Pointers

# Problem 5: Where Do We Begin?
# A linked list contains a cycle if the tail element points back to another element in the list. Given the head of a linked list, use the fast and slow pointer method to determine the node where the cycle starts. If the linked list does not contain a cycle, return None.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def get_loop_start(head):
# 	pass
# Example Usage:

# # Input List:
# # 1 -> 2 -> 3 -> 4
# #      ^         | 
# #      |---------|
# # Input: head = 1
# Example Output:

# # Output: 2
# ✨ AI Hint: Multiple Pass Technique

# Problem 6: Was That a Crit?
# Given the head of a singly linked list, return the number of critical points. A critical point is a local minima or maxima. - The head and tail nodes are not considered critical points. - A node is a local minima if both the next and previous elements are greater than the current element - A node is a local maxima if both the next and previous elements are greater than the current element.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def count_critical_points(head):
# 	pass
# Example Usage:

# # Input List: 1 -> 2 -> 3 -> 3 -> 3 -> 5 -> 1 -> 3
# # Input: head = 3
# Example Output:

# # Expected Return Value: 2
# # Explanation:
# #  - Critical point 1 (local maxima) 3 -> 5 -> 1
# #  - Critical point 2 (local minima): 5 -> 1 -> 3
# 💡 Hint: Which technique?
# Problem Set Version 3
# Problem 1: The Power of One
# The following code creates the linked list Ash -> Misty -> Brock. Refactor the code to create the same list with a single line of code.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# # Recreate this list in a single line of code
# head = Node("Ash")
# misty = Node("Misty")
# brock = Node("Brock")
# head.next = misty
# luigi.next = brock
# 💡 Hint: Nested Constructors

# Problem 2: Frequency Map
# Given the head of a linked list, return a dictionary that maps each unique element in the list to its frequency.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# def frequency_map(head):
# 	pass
# Example Usage:

# # Input List: 1 -> 2 -> 3 -> 4 -> 2 -> 3
# # Input: head = 1
# Example Output:

# # Expected Output: { 1: 1, 2: 2, 3: 2, 4: 1}

# Problem 3: Get it Out of Here!
# The following code attempts to remove the first node with a given value from a singly linked list based but it contains a bug!

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list.

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

# # Helper function to print the linked list
# def print_list(node):
#     current = node
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()

# # Function with a bug!
# def remove_by_value(head, val):
#     # Handle empty list and removal from the head
#     if not head:
#         return None
#     if head.value == val:
#         return head.next  # Return the second node as the new head

#     current = head
#     while current.next:
#         if current.next.value == val:
#             current = current.next.next  # Skip the node with the value
#             return head  # Return the original head
#         current = current.next

#     # If no node was found with the value `val`, return the original head
#     return head
# Example Usage:

# # Input List: 1 -> 2 -> 3 -> 4
# # Value to Remove: 3
# Example Output:

# # Expected Return Value: 1
# # Expected Result List: 1 -> 2 -> 4

# Problem 4: Does it Cycle?
# Given the head of a linked list, return True if the list has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def has_cycle(head):
# 	pass
# Example Usage:

# # Input List:
# # 1 -> 2 -> 3 -> 4
# #      ^         | 
# #      |---------|
# # Input: head = 1
# Example Output:

# # True
# ✨ AI Hint: Slow and Fast Pointers

# Problem 5: Are We There Yet?
# Given the head of a linked list, return the length of its cycle.
# A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def cycle_length(head):
# 	pass
# Example Usage:

# # Input List
# # 1 -> 2 -> 3 -> 4
# #      ^         |
# #      |_________|
# # Input: head = 1
# Example Output:

# # Output: 3
# ✨ AI Hint: Multiple Pass Technique

# Problem 6: Reverse Them, K?
# Given the head of a singly linked list and an integer k, reverse the first k elements of the linked list. Return the new head of the linked list. If k is larger than the length of the list, reverse the entire list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def reverse_first_k(head, k):
# 	pass
# Example Usage:

# # Input List: 1 —> 2 —> 3 —> 4 —> 5
# # Input: head = 1, k = 3
# Example Output:

# # 3 -> 2 -> 1 -> 4 -> 5