# # Problem 1: Greatest Node
# # Write a function find_max() that takes in the head of a linked list and returns the maximum value in the linked list. You can assume the linked list will contain only numeric values.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next

# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value, end=" -> " if current.next else "\n")
# #         current = current.next

# # def find_max(head):
# #     pass  
# # Example Usage:

# # head1 = Node(5, Node(6, Node(7, Node(8))))

# # # Linked List: 5 -> 6 -> 7 -> 8
# # print(find_max(head1))

# # head2 = Node(5, Node(8, Node(6, Node(7))))

# # # Linked List: 5 -> 8 -> 6 -> 7
# # print(find_max(head2))
# # Expected Output:

# # 8
# # 8
# # 💡 Hint: Linked List Traversal

# # Problem 2: Remove Tail
# # The following code incorrectly implements the function remove_tail(). 
# # When correctly implemented, remove_tail() accepts the head of a singly linked list and removes the last node (the tail) in the list.
# #  The function should return the head of the modified list.

# # Step 1: Copy this code into your IDE.

# # Step 2: Create your own test cases to run the code against.
# #  Use print statements, print_linked_list(), and the stack trace to identify and fix any bugs so that the function correctly removes the last node from the list.

# # class Node:
# #     def __init__(self, value=None, next=None):
# #         self.value = value
# #         self.next = next
        
# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value, end=" -> " if current.next else "\n")
# #         current = current.next

# # def remove_tail(head):
# #     if head is None:
# #         return None
# #     if head.next is None:
# #         return None 
        
# #     current = head
# #     while current.next: 
# #         current = current.next

# #     current.next = None 
# #     return head
# # Example Usage:

# # head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# # # Linked List: Isabelle -> Alfonso -> Cyd
# # print_linked_list(remove_tail(head))
# # Expected Output:

# # Isabelle -> Alfonso

# # Problem 3: Delete Duplicates in a Linked List
# # Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates).
# #  The resulting list should maintain sorted order. Return the head of the linked list.

# # Evaluate the time and space complexity of your solution.
# #  Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next



# # For testing 
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# #U: 
#     #I: sorted linked list
#     #O: the same list with the duplicates removed
#     #C: if a node has a duplicate, the node and it's duplicates are removed
#     #E: 
#         #Everyting is a duplicate
#         # is the list is empty or has no dupicates return list,
# #P:

#     #create a prev, current pointer

#     #loop through the list
#         # find duplicates
#             # link around them

# #I

#     prev, current = Node(0), head

#     while current:
        
#         while current.next and current.value == current.next.val:
#             current = current.next
        
#         prev.next = current
        


# #Normal case # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5 => # # Linked List: 1 -> 2 -> 4 -> 5
# # Edge case 
#    # Linked List: 5 -> 5 -> 5 ->5 ->5 -> 5 -> 5 => # # Linked List: None
#    # Linked List: 5 -> 5 -> 5 ->5 ->5 -> 5 -> 5 => # # Linked List: None
# def delete_dupes(head):
#     return head


# # head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# # # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# # print_linked_list(delete_dupes(head))
# # Example Output:

# # 1 -> 2 -> 4 -> 5
# # 💡 Hint: Temporary Head Technique

# # Problem 4: Does it Cycle?
# # A variation of the two-pointer technique introduced earlier in the course is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to write a function has_cycle() that returns True if the list has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next

# # def has_cycle(head):
# #     pass
# # Example Usage:

# # Linked list with four nodes where fourth node points back to second node

# # peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# # # Toad.next = Luigi
# # peach.next.next.next = peach.next

# # print(has_cycle(peach))
# # Example Output:

# # True
# # ✨ AI Hint: Slow and Fast Pointers

# # Problem 5: Remove Nth Node From End of List
# # Given the head of a linked list and an integer n, write a function remove_nth_from_end() that removes the nth node from the end of the list. The function should return the head of the modified list.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next

# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value, end=" -> " if current.next else "\n")
# #         current = current.next

# # def remove_nth_from_end(head, n):
# #     pass
# # Example Usage:

# # head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
# # head2 = Node("Rainbow Trout", Node("Ray"))
# # head3 = Node("Rainbow Stag")


# # print_linked_list(remove_nth_from_end(head1, 2))
# # print_linked_list(remove_nth_from_end(head2, 1))
# # print_linked_list(remove_nth_from_end(head3, 1))
# # Example Output:

# # apple -> cherry -> orange -> pear
# # Rainbow Trout

# # Example 3 Explanation: The last example returns an empty list.

# # Problem 6: Careful Reverse
# # Given the head of a singly linked list and an integer k, reverse the first k elements of the linked list. Return the new head of the linked list. If k is larger than the length of the list, reverse the entire list.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# # class Node:
# # 	def __init__(self, value, next=None):
# # 		self.value = value
# # 		self.next = next

# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value, end=" -> " if current.next else "\n")
# #         current = current.next
        
# # def reverse_first_k(head, k):
# # 	pass
# # Example Usage:

# # head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

# # print_linked_list(reverse_first_k(head, 3))
# # Example Output:

# # orange -> cherry -> apple -> peach -> 


# # Problem #2
# # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# # Input: haystack = "sadbutsad", needle = "sad"
# # Output: 0
# # Input: haystack = "leetcode", needle = "leeto"
# # Output: -1


# #U
# #M
# #P
# #I

def findNeedle(haystack, needle):
    needle_len =  len(needle) #3
    haystack_len = len(haystack) #9

    if needle_len > haystack_len: # Checks if needle is longer than haystack
        return - 1
                    #8 - 3 = 5
    for i in range(len(haystack) - needle_len +2): # the loop should stop when the pointer at the end of the window reaches the end of the array
        if haystack[i:needle_len+i] == needle:
            return i
    return -1


print(findNeedle("saddadsad","sad")) #9
print(findNeedle("saadsad","sad"))
print(findNeedle("sdad","sad"))
print(findNeedle("sa","sad"))

