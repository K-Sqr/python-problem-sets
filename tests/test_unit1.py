"""
Test Suite for Unit 1 - Fundamentals
Topics: Lists, Loops, Functions, Basic Algorithms
"""
import pytest
import sys
from io import StringIO

# These tests validate understanding of:
# - List manipulation and filtering
# - Control flow (loops, conditionals)
# - Search algorithms (linear search)
# - Index/enumeration operations


class TestUnit1Fundamentals:
    """Unit 1: Lists, Loops, and Basic Functions"""
    
    def test_get_evens(self):
        """Test: Filter even numbers from a list"""
        # Problem 7: Extract even numbers
        def get_evens(lst):
            new_list = []
            for num in lst:
                if(num % 2 == 0):
                    new_list.append(num)
            return new_list
        
        lst = [5, 2, 3, 4, 12, 34, 21, 4, 2, 13, 53, 13]
        result = get_evens(lst)
        
        assert result == [2, 4, 12, 34, 4, 2]
        assert all(num % 2 == 0 for num in result), "All results should be even"
    
    def test_get_evens_empty_list(self):
        """Test: get_evens with empty list"""
        def get_evens(lst):
            new_list = []
            for num in lst:
                if(num % 2 == 0):
                    new_list.append(num)
            return new_list
        
        assert get_evens([]) == []
    
    def test_get_evens_no_evens(self):
        """Test: get_evens with only odd numbers"""
        def get_evens(lst):
            new_list = []
            for num in lst:
                if(num % 2 == 0):
                    new_list.append(num)
            return new_list
        
        assert get_evens([1, 3, 5, 7]) == []
    
    def test_find_divisors(self):
        """Test: Find all divisors of a number"""
        # Problem 9: Find divisors
        def find_divisors(n):
            return [num for num in range(1, n+1) if n % num == 0]
        
        assert find_divisors(9) == [1, 3, 9]
        assert find_divisors(12) == [1, 2, 3, 4, 6, 12]
        assert find_divisors(1) == [1]
    
    def test_find_divisors_prime(self):
        """Test: Divisors of a prime number"""
        def find_divisors(n):
            return [num for num in range(1, n+1) if n % num == 0]
        
        assert find_divisors(7) == [1, 7]
    
    def test_linear_search(self):
        """Test: Linear search for index of target value"""
        # Problem 12: Linear search
        def linear_search(lst, target):
            for num in range(len(lst)):
                if target == lst[num]:
                    return num
            return -1
        
        lst = [5, 2, 3, 4, 12, 34, 21, 4, 2, 13, 53, 13]
        
        assert linear_search(lst, 34) == 5
        assert linear_search(lst, 5) == 0
        assert linear_search(lst, 13) == 9  # First occurrence
        assert linear_search(lst, 100) == -1  # Not found
    
    def test_linear_search_empty_list(self):
        """Test: Linear search in empty list"""
        def linear_search(lst, target):
            for num in range(len(lst)):
                if target == lst[num]:
                    return num
            return -1
        
        assert linear_search([], 5) == -1
    
    def test_multiples_of_five(self):
        """Test: Generate multiples of 5"""
        # Problem 8: Test that we can identify multiples of 5
        def is_multiple_of_five(n):
            return n % 5 == 0
        
        for num in range(5, 101, 5):
            assert is_multiple_of_five(num)
        
        assert is_multiple_of_five(5)
        assert is_multiple_of_five(100)
        assert not is_multiple_of_five(4)
