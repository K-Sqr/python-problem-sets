# Problem 1: Detect Circular Linked List
# A circular linked list is a linked list where the tail node points at the head node. 
# Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.

# Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.

# Evaluate the time and space complexity of your solution.
#  Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
# understand: return true or false if the a linked list is circular (tail node points to the head node)
def is_circular(head):
        if not head:
            return False
    # plan: 
        # store the head 
        # created a curr variable to iterate to the tail
        # check if tail.next is the head variable we created??
        current = head
        while current.next:
            current = current.next
            if current == head:
                return True
        return False
# node1 = Node(2, Node(3,(Node(4))))
#node2 = Node(4,node1)
# Example Usage:
num1 = Node(0)
num2 = Node(1)
num3 = Node(2)
num1.next = num2
num2.next = num3
# num1 -> num2 -> num3 -> num1
# print(is_circular(num1))

# # var1 -> var2 -> var3
# print(is_circular(var1))
# Example Output:

# True
# False

# Problem 2: Find Last Node in a Linked List Cycle
# Given the head of a singly linked list, write a function that returns the last node in the cycle.
#  If there is no cycle in the linked list, return None.

def find_last_node_in_cycle(head):
    if not head or not head.next:
        return None
    
    slow = head  # Starts at the head
    fast = head  # Also starts at the head
    has_cycle = False
    # Detecting if there is a cycle
    while fast and fast.next:
        slow = slow.next          # Move slow pointer by one
        fast = fast.next.next     # Move fast pointer by two
        if slow == fast:          # If they meet, there's a cycle
            has_cycle = True
            break
    if has_cycle == False:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    



# Example Input: num1 -> num2 -> num3 -> num4 -> num2

# Example Output: num4

node1 = Node(2, Node(3,(Node(4))))
node2 = Node(4,node1)

num1 = Node(0)
num2 = Node(1)
num3 = Node(2)
num4 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2
# print(find_last_node_in_cycle(num1).value)


# ✨ AI Hint: Multiple Pass Technique

# Problem 3: Partition List Around Value
# Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def partition(head, val):
# 	pass
# Example Input:

# # 1 -> 4 -> 3 -> 2 -> 5 -> 2
# # head = 1, val = 3
# Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3

# 💡 Hint: Temporary Head Technique

# Problem 4: Convert Binary Number in a Linked List to Integer
# You are given the head of a linked list. Each value in the linked list is either 0 or 1, and the entire linked list represents a binary number. Return an integer that is the decimal value of the number represented by the linked list. The most significant bit is at the head of the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def binary_to_int(head):
# 	pass
# Example Usage:

# # 1 -> 0 -> 1
# num1 = 1
# num2 = 0
# num3 = 1
# int_num = binary_to_int(num1)
# # 101 in binary 

# print(int_num)
# Example Output: 5

# ✨ AI Hint: Binary to Decimal

# Problem 5: Add Two Numbers Represented by Linked Lists
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def add_two_numbers(head_a, head_b):
#     pass

# Example Usage:

# # list 1: 2 -> 4 -> 3 (342)
# # list 2: 5 -> 6 -> 4 (465)
# # head_a = 2, head_b = 5

# sum = add_two_numbers(head_a, head_b)
# print(sum)
# Example Output: 7 -> 0 -> 8

# Explanation: 342 + 465 = 807, so the list is 7 -> 0 -> 8.


# Problem 6: Reverse Sublist of a Linked List
# Given the head of a linked list and indices m and n, reverse the linked list between positions m and n. Assume the linked list uses 1-based indexing and the 0 <= m <= n <= length of list. Return the head of the list.

# def reverse_between(head, m, n):
# 	pass
# Example Usage:

# # input list: 1 -> 2 -> 3 -> 4 -> 5
# reverse_between(head, 2, 5)
# Result Linked List: 1 -> 5 -> 4 -> 3 -> 2


# Problem Set Version 2
# Problem 1: Convert a Singly Linked List to a Circular Linked List
# A circular linked list is a linked list where the tail node points at the head node.
#  Write a function that transforms a singly linked list into a circular linked list. 
# Return the head of the linked list. Evaluate the time and space complexity of your solution.
#  Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

#U 
# takes a regular linked list and returns the head back but circular
# so basicallt make the tail of the list point back to the head

#P
#check for edge cases
    # if the head in None and it has one element, return None and head 
# I'm going to pass the linked list to find the tail
# and then connect the tail to the head

#I
def make_circular(head):
    if not head or not head.next:
        return None
    #linked list pointer
    current = head
    # stops when current.next is None, current has to the tail
    while current.next:
        current = current.next
    # current(tail) is now pointing to head
    current.next = head 
    return head
# 	pass
# Example Usage:
def print_list(head):
    current = head
    values = []
    while current:
        values.append(str(current.value))
        current = current.next
    print (" -> ".join(values))
# # Input List: num1 -> num2 -> num3
node = Node(4,(Node(3,Node(2,Node(3,Node(1,Node(3)))))))
num1 = Node(0)
num2 = Node(1)
num3 = Node(2)
num4 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num4
print_list(make_circular(num1))
# Result Linked List: num1 -> num2 -> num3 -> num1


# Problem 2: Collect Nodes of a Cycle in a Linked List
# Given the head of a linked list, return the elements of any cycle in the linked list as a list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def collect_cycle_nodes(head):
# 	pass
# Example Usage

# # num1 -> num2 -> num3 -> num4 -> num2
# lst = collect_cycle_nodes(num1)
# print(lst)

# # var1 -> var2 -> var3 -> var4
# lst2 = collect_cycle_nodes(var1)
# print(lst2)
# Example Output:

# [num2, num3, num4]
# []
# ✨ AI Hint: Multiple Pass Technique

# Problem 3: Delete Duplicates in a Linked List
# Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). The resulting list should maintain sorted order. Return the head of the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def delete_dupes(head):
# 	pass
# Example Input: 1 -> 2 -> 3 -> 3 -> 4 -> 5

# Example Output: 1 -> 2 -> 4 -> 5

# 💡 Hint: Temporary Head Technique

# Problem 4: Identical Linked Lists
# Two linked lists are identical when they have the same values and the same order of values. Given the heads of two linked lists, write a function that returns True if the the linked lists are identical and False otherwise.

# def is_identical(head_a, head_b):
# 	pass
# Example 1:

# # list1: 1->2->3->4
# # list2: 1->2->3->4
# # head_a = 1, head_b = 1,
# print(is_identical(head_a, head_b))
# Expected Output: True

# Example 2:

# # list1: 1->2->3->4
# # list2: 1->3->4->2
# # head_a = 1, head_b = 1,
# print(is_identical(head_a, head_b))
# Expected Output: False


# Problem 5: Circular Linked List Rotate
# Given the head of a linked list and a non-negative integer k, rotate the list to the right by k places. Return the head of the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value

#         self.next = next


# def rotate_right(head, k):
# 	pass
# Example 1:

# # num1 -> num2 -> num3 -> num4 -> num5
# new_head = rotate_right(num1, 2)
# Expected Output: num4 -> num5 -> num1 -> num2 -> num3

# Example 2:

# # num1 -> num2 -> num3
# new_head = rotate_right(num1, 4)
# Expected Output: num3 -> num1 -> num2


# Problem 6: Circular Linked List Delete
# Given the head of a circularly linked list and a value val, write a function that deletes the first node in the list with value val. Return the head of the modified list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def delete_node(head, val):
# 	pass
# Example 1:

# # num1 -> num2 -> num3 -> num1
# num1 = 1
# num2 = 2
# num3 = 3
# delete_node(num1, 2)
# Result Linked List: num1 -> num3 -> num1

# Example 2:

# # num1 -> num2 -> num3 -> num1
# num1 = 1
# num2 = 2
# num3 = 3
# delete_node(num1, 1)
# Result Linked List: num2 -> num3 -> num2


# Problem Set Version 3
# Problem 1: Circular List Length
# A circular linked list is a linked list where the tail node points at the head node. Write a function that returns the length of the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def circular_list_length(head):
# 	pass
# Example Usage:

# """
# Input List:
# 1 -> 2 -> 3
# ^         |
# |_________|
# Input: head = 1
# """
# # Expected Return Valuet: 3
# Problem 2: Detect and Remove Cycle in a Linked List
# Given the head of a linked list, write a function that removes any cycles in the linked list. Return the head of the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def detect_and_remove_cycle(head):
# 	pass
# Example Usage:

# """
# Input List
# 1 -> 2 -> 3
# ^         |
# |_________|
# Input: head = 1
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 3

# """
# ✨ AI Hint: Multiple Pass Technique
# Problem 3: Merge Two Sorted Linked Lists
# Given the heads of two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the input lists. Return the head of the result list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def merge_two_lists(head_a, head_b):
# 	pass
# Example Usage:

# """
# Input: List 1: 1 -> 2 -> 4, List 2: 2 -> 3 -> 4
# Input: head_a = 1, head_b = 2
# Output: 1 -> 2 -> 2 -> 3 -> 4 -> 4
# """
# 💡 Hint: Temporary Head Technique
# Problem 4: Skip and Remove Nodes in a Linked List
# Given the head of a linked list and two integers m and n, traverse the list such that you keep the first m nodes then delete the next n nodes. Continue with this pattern until the end of the list is reached. Return the head of the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


# """
# Example usage:

# Input: List 1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
# Input: head = 1, m = 2, n = 3

# Output: 1 -> 2 -> 6 -> 7 
# Explanation: Keep first two nodes 1 & 2, delete next three nodes 3, 4, & 5
# Keep next two nodes 6 & 7, delete remaining three nodes 8, 9, & 10


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
# """

# def skip_and_remove(head, m, n):
# 	pass

# Problem 5: Rotate a Doubly Linked List to the Left
# Given the head of a doubly linked list and a non-negative integer k, rotate the list to the left by k places. Return the head of the linked list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


# """
# Input List
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# Input: head = 1, k = 2

# Expected Return value: 4
# Expected Output List: 3 <-> 4 <-> 5 <-> 1 <-> 2

# Explanation: 
# Rotation 1: 2 <-> 3 <-> 4 <-> 5 <-> 1
# Rotation 2: 3 <-> 4 <-> 5 <-> 1 <-> 2

# Input List
# 0 <-> 1 <-> 2
# Input: head = 0, k = 4

# Expected Return value: 4
# Expected Output List: 1 <-> 2 <-> 0
# Explanation: 

# Rotation 1: 1 <-> 2 <-> 0
# Rotation 2: 2 <-> 0 <-> 1 
# Rotation 3: 0 <-> 1 -> 2
# Rotation 4: 1 <-> 2 <-> 0

# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
# """

# def rotate_doubly_linked_list(head, k):
# 	pass

# Problem 6: Merge Nodes Between Zeros in a Linked List
# Given the head of a linked list which contains a series of integers separated by 0s, merge the nodes lying between two zero nodes into a single node whose value is the sum of all the merged nodes. The modified list should not contain any zeroes. The head and tail of the list will be nodes with value zero. Return the head of the merged list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# """
# Input List:
# 0 -> 3- > 1 -> 0 -> 4 -> 5 -> 2 -> 0
# Input: head = 0

# Expected Return value: 4
# Expected Result list: 4 -> 11

# Explanation: 3 + 1 = 4, 4 + 5 + 2 = 11

# Input List: 
# O -> 1 -> 0 -> 3 -> 0 -> 2 -> 2-> 0
# Input: head = 0

# Expected Return Value: 1
# Expected Result List: 1 -> 3 -> 4

# Explanation: 1, 3, 2+ 2 = 4

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
# """

# def merge_nodes(head):
# 	pass