print("Welcome to ProbSet1!")
###############################
# ProbSet1
###############################
# Problem 1: Hello User!
def greet_user(name):
    print(f"Hello {name}")

# greet_user("Bob")

# Problem 2: Calculate Difference
def difference(a, b):
    print(b-a)

# Problem 3: Calculate Difference

def concatenate_list(nums):
    ans = nums.copy()
    for num in nums:
        ans.append(num)
    return ans
ints = [1,2,3,4,5,6]
#print(concatenate_list(ints))


# Problem 4:  Sleep Assessment
def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go bak to bed!")
    elif hours > 10:
        print("You're a sleep prodigy!")
    else:
        print("You got a good night's rest!" )

#sleep_assessment(10)
#sleep_assessment(4)
#sleep_assessment(12)
#sleep_assessment(9)


# Problem 5: Calculate Tip
def calculate_tip(bill, service_quality):
    if (service_quality == "poor"):
        return bill *.10
    elif (service_quality == "average"):
        return bill *.15
    elif (service_quality == "excellent"):
        return bill *.20
    else:
        return None
'''
tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
'''   
# Problem 6: Rock, Paper, Scissors
def rock_paper_scissors(player1, player2):
    if player1 == "rock" and player2 == "scissors":
        print("Player 1 wins")
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 wins")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 wins")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins")
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 wins")
    else:
        print("It's a tie!")

'''rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")'''       

#Problem 9: Counetdown
def countdown(m,n):
    for num in range(m,n-1,-1):
        print(num)
#ecountdown(13,1)
# Problem 10: Calculate Power
def power(base,exponent):
    result = 1
    for num in range(exponent):
        result *= base
    return result
print(power(3,4))

# Problem 12: Calculate Factorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(2))

lst = [5,2,3,4,12,34,21,4,2,13,53,13]
#Problem 13: Calculate the Squares
def squares(nums):
    lst1 = []
    for num in nums:
        lst1.append(num*num)
    return lst1 
print(squares(lst))


###############################
# ProbSet2
###############################

# Prob 7 Evens list

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

# #################################
# prob set 3
############################
# Problem 2: Average Score
def average(scores):
    average = 0
    for num in scores:
        average += num
    return average/len(scores)

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)


def check_num(lst, num):
    for i in lst:
        if i == num:
            return True
    return False

lst = [5,2,3,9,10]
print(check_num(lst,9))
print(check_num(lst,4))

def find_missing(nums):
    check = 0
    nums.sort()
    for i in nums:
        if i == check:
            check += 1
        else: 
            return check

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)

# Problem 6: Reverse List
def reverse_list(lst):
    new_list = []
    for i in range(len(lst) - 1,-1,-1):
        new_list.append(lst[i])
    return new_list

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)

# Problem 7: Get Odd Numbers
def get_odds(nums):
    return[num for num in nums if num%2 !=0]

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)

# Problem 9: Create Number
def list_to_number(digits):
    number = 0
    for i in range(0,len(digits)):
        number += digits[i] * 10 ** (len(digits) -i -1) 
    return number

digits = [1,0,3]
number = list_to_number(digits)
print(number)
# Problem 10: Move Zeroes
def move_zeroes(nums):
    new_list = []
    for num in nums:
        if num != 0:
            new_list.append(num)
    for num in nums:
        if num == 0:
            new_list.append(num)
    return new_list

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)

# Problem 11: Odd Indices
def print_odd_indices(nums):
    return[num for num in nums if nums.index(num) %2 ==1]

nums = [3,4,8,1,5,2]
print(print_odd_indices(nums))

# Problem 12: List Occurrences
def find_all_occurrences(lst, target):
    new_list = []
    for i in range(0, len(lst)):
        if lst[i] == target:
            new_list.append(i)
    return new_list

lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)


         



