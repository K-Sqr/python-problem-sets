from collections import deque
# Problem Set Version 1
# Problem 1: Arrange Guest Arrival Order
# You are organizing a prestigious event, 
# and you must arrange the order in which guests arrive based on a set of instructions.

# The instructions are provided as a 0-indexed string arrival_pattern of length n, 
# consisting of the characters:

# 'I' - The next guest should have a higher number than the previous guest.
# 'D' - The next guest should have a lower number than the previous guest.
# You need to create a string guest_order of length n + 1 that satisfies the following conditions:

# guest_order contains each number from 1 to str(n + 1) exactly once. These numbers represent the guests' assigned numbers.
# For every index i from 0 to n - 1:
# If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
# If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
# Among all valid orders, return the lexicographically smallest one.
def arrange_guest_arrival_order(arrival_pattern):
    guests = []
    n = len(arrival_pattern)
    guest_order = []

      
    for i in range(n + 1):
        guests.append(str(i + 1))
        if i == n or arrival_pattern[i] == 'I':
            while guests:
                guest_order.append(guests.pop())

    return "".join(guest_order)

# Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  
# Example Output:

# 123549876
# 4321 
# ✨ AI Hint: Stacks

# Problem 2: Reveal Attendee List in Order
# You are planning a special event where each attendee has a unique registration number. 
# These numbers are listed in the provided array attendees, but they are currently out of order.

# At the event, attendees will walk on stage one by one following this special reveal process:

# The person at the front of the line walks on stage (this number is revealed).
# If there are still people left in line, the next person in front moves to the back of the line.
# Steps 1 and 2 repeat until everyone has walked on stage.
# Your task is to rearrange the attendees list before the process starts so that the attendees walk on stage by registration number in increasing order.

# Write a function reveal_attendee_list_in_order(attendees) that returns an array with the correct starting order, 
# such that when the attendees follow the above reveal process they walk on stage from smallest registration number to largest registration number.

def reveal_attendee_list_in_order(attendees):
    n = len(attendees)
    sorted_attendees = sorted(attendees)
    result_index = deque(range(n))
    result_queue = [0] * n
    for i in sorted_attendees:
        result_queue[result_index.popleft()] = i
        if result_index:
            result_index.append(result_index.popleft())

        
    return result_queue

# Example Usage:

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))# [2,3,5,7,11,13,17]
print(reveal_attendee_list_in_order([1,1000]))  
# Example Output:

# [2,13,3,11,5,17,7]
# [1,1000]
# Example 1 Explanation
# ✨ AI Hint: Queues
# Problem 3: Arrange Event Attendees by Priority
# You are organizing a large event and need to arrange the attendees based on their priority levels. You are given a 0-indexed list attendees, where each element represents the priority level of an attendee, and an integer priority that indicates a particular level of priority.

# Your task is to rearrange the attendees list such that the following conditions are met:

# Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
# Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
# The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
# Return the attendees list after the rearrangement.

# def arrange_attendees_by_priority(attendees, priority):
#   pass
# Example Usage:

# print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
# print(arrange_attendees_by_priority([-3,4,3,2], 2)) 
# Example Output:

# [9,5,3,10,10,12,14]
# [-3,2,4,3]
# 💡 Hint: Two Pointer Variation
# Problem 4: Rearrange Guests by Attendance and Absence
# You are organizing an event, and you have a 0-indexed list guests of even length, where each element represents either an attendee (positive integers) or an absence (negative integers). The list contains an equal number of attendees and absences.

# You should return the guests list rearranged to satisfy the following conditions:

# Every consecutive pair of elements must have opposite signs, indicating that each attendee is followed by an absence or vice versa.
# For all elements with the same sign, the order in which they appear in the original list must be preserved.
# The rearranged list must begin with an attendee (positive integer).
# Return the rearranged list after organizing the guests according to the conditions.

# def rearrange_guests(guests):
#   pass
# Example Usage:

# print(rearrange_guests([3,1,-2,-5,2,-4]))  
# print(rearrange_guests([-1,1])) 
# Example Output:

# [3,-2,1,-5,2,-4]
# [1,-1]
# Problem 5: Minimum Changes to Make Schedule Balanced
# You are organizing a series of events, and each event is represented by a parenthesis in the string schedule, where an opening parenthesis ( represents the start of an event, and a closing parenthesis ) represents the end of an event. A balanced schedule means every event that starts has a corresponding end.

# However, due to some scheduling issues, the current schedule might not be balanced. In one move, you can insert either a start or an end at any position in the schedule.

# Return the minimum number of moves required to make the schedule balanced.

# def min_changes_to_make_balanced(schedule):
#   pass
# Example Usage:

# print(min_changes_to_make_balanced("())"))
# print(min_changes_to_make_balanced("(((")) 
# Example Output:

# 1
# 3
# 💡 Hint: Choosing the Right Approach
# Problem 6: Marking the Event Timeline
# You are organizing a large event, and you need to mark the timeline for a series of scheduled activities.

# You are given two strings:

# event: A short string representing an event name.
# timeline: A longer string representing the full timeline for the event.
# Initially, the timeline is empty and represented by a string t of the same length as timeline, where every character is '?'.

# In one turn, you can "mark" the timeline by placing the event string over any valid position in t and copying its letters onto t. This replaces the corresponding '?' characters in t.

# Rules:

# You can only place event where it fully fits within t.
# Each time you mark the timeline, the corresponding letters in t are updated.
# Your goal is to perform a sequence of marks so that t becomes exactly equal to timeline.
# You may use at most 10 * len(timeline) marks.
# Return a list of the starting indices where you placed the event string during each mark. If it is impossible to turn t into timeline following these rules, return an empty list.

# def mark_event_timeline(event, timeline):
#   pass
# Example Usage:

# print(mark_event_timeline("abc", "ababc"))  
# print(mark_event_timeline("abca", "aabcaca")) 
# Example Output:

# [0, 2]
# [3, 0, 1]
# Explanation

# For "ababc":

# Start with t = "?????"
# Place "abc" at index 0 → t = "abc??"
# Place "abc" at index 2 → t = "ababc" — timeline is complete.