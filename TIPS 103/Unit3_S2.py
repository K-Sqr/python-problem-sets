from collections import deque

# Problem 1: Blueprint Approval Process
# You are in charge of overseeing the blueprint approval process for various architectural designs. 
# Each blueprint has a specific complexity level, represented by an integer.
#  Due to the complex nature of the designs, the approval process follows a strict order:

# Blueprints with lower complexity should be reviewed first.
# If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
# Your task is to simulate the blueprint approval process using a queue.
#  You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. 
# Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

# Return the order in which the blueprints are approved.

# The idea is you want to look at the queue and then if the number is smaller you want to insert to the front 


# Idea
# Create a result array 
# Create a deque 


def blueprint_approval(blueprints):
    blueprints.sort()
    queue = deque()
    for n in blueprints:
        queue.append(n)
    
    result = []
    for i in range(len(blueprints)):
        result.append(queue.popleft())
    
    return result
# Example Usage:

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 
# Example Output:

# [1, 2, 3, 4, 5]
# [2, 4, 5, 6, 7]


# Problem 2: Build the Tallest Skyscraper
# You are given an array floors representing the heights of different building floors.
#  Your task is to design a skyscraper using these floors, where each floor must be placed on top of a floor with equal or greater height.
#  However, you can only start a new skyscraper when necessary, meaning when no more floors can be added to the current skyscraper according to the rules.

# Return the number of skyscrapers you can build using the given floors.



# 10 5 
# 8 3 
# 7 2
# 9

# Plan 
# Create a stack
# counter = 0 
# iterate through the floors 
# check if current value is greater than stack.pop(), if it is while stack: - pop everything else 
# increment the counter 
# return the counter at the end 

#I
def build_skyscrapers(floors):
    stack  = []
    counter  = 0
    for floor in floors:
        # if stack empty, create a new skyscraper(coutner)
        if not stack:
            stack.append(floor)
            counter += 1
        elif stack[-1] >= floor:
            stack.append(floor)
        elif stack[-1] < floor:
            while stack:
                stack.pop()
            stack.append(floor)
            counter +=1
    return counter


# Example Usage:


print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 
# Example Output:

# 4
# 4
# 2
# Problem 3: Dream Corridor Design
# You are an architect designing a corridor for a futuristic dream space. The corridor is represented by a list of integer values where each value represents the width of a segment of the corridor. Your goal is to find two segments such that the corridor formed between them (including the two segments) has the maximum possible area. The area is defined as the minimum width of the two segments multiplied by the distance between them.

# You need to return the maximum possible area that can be achieved.

# def max_corridor_area(segments):
#     pass
# Example Usage:

# print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
# print(max_corridor_area([1, 1])) 
# Example Output:

# 49
# 1
# Problem 4: Dream Building Layout
# You are an architect tasked with designing a dream building layout. The building layout is represented by a string s of even length n. The string consists of exactly n / 2 left walls '[' and n / 2 right walls ']'.

# A layout is considered balanced if and only if:

# It is an empty space, or
# It can be divided into two separate balanced layouts, or
# It can be surrounded by left and right walls that balance each other out.
# You may swap the positions of any two walls any number of times.

# Return the minimum number of swaps needed to make the building layout balanced.

# def min_swaps(s):
#     pass
# Example Usage:

# print(min_swaps("][][")) 
# print(min_swaps("]]][[[")) 
# print(min_swaps("[]"))  
# Example Output:

# 1
# 2
# 0