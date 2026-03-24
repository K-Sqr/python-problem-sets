
# Add your program code here.
# Prob 7 Evens list
print("Welcome to ProbSet1!")
lst = [5,2,3,4,12,34,21,4,2,13,53,13]

def get_evens(lst):
    new_list =[]
    for num in lst:
        if(num % 2 == 0):
            new_list.append(num)
    return new_list


def get_evens_optimized(lst):
    # This single line does the same as your loop and append!
    return [num for num in lst if num % 2 == 0]

evens_lst = get_evens(lst)
print(evens_lst)
# Prob 8 Multiples of Five
def multiples_of_five():
    for num in range(1,101):
        if num % 5 == 0:
            print(num)

def multiples_of_five_optimized_2():
    # Start from 5, go up to (but not including) 101, in steps of 5
    for num in range(5, 101, 5):
        print(num)
# multiples_of_five()
# Problem 9: Divisors
'''Write a function find_divisors() that takes in an integer n as a parameter 
that returns a list of all divisors of n.'''
def find_divisors(n):
    return [num for num in range(1,n+1) if n % num == 0]
print(find_divisors(9)) 
# Problem 10: FizzBuzz
'''Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.'''
def fizzbuzz(n):
    for num in range(1,n+1):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Buzz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

#fizzbuzz(30)
# Problem 11: Print the Index
'''Write a function print_indices() that takes in an integer list lst as a parameter 
and prints out the index of each item in the given list.'''

def print_indices(lst):
    for index, num in enumerate(lst):
        print(index)
#print_indices(lst)

def print_indices1(lst):
    for num in range(len(lst)):
        print(num)
#print_indices1(lst)
# Problem 12: Linear Search
'''Write a function linear_search() that takes in a list lst and value target as parameters. 
The function returns the index of target in lst if found. If target is not found in lst, return -1.'''
def linear_search(lst, target):
   for num in range(len(lst)):
        if target == lst[num]:
            print(num)
linear_search(lst, 34)

