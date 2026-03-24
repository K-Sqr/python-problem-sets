# 📚 Learning Guide - How to Use This Repository

## Quick Start

### 1. **Set Up Your Environment**
```bash
# Install pytest (Python testing framework)
pip install -r requirements.txt

# Verify installation
pytest --version
```

### 2. **Understand the Test Structure**
Tests are organized by unit and provide:
- ✅ Example solutions you can learn from
- ✅ Test cases showing expected behavior
- ✅ Edge case examples
- ✅ Documentation of problem requirements

### 3. **Run Tests to Validate Your Work**
```bash
# Run all tests
pytest

# Run tests for a specific unit
pytest tests/test_unit1.py -v

# Run a specific test
pytest tests/test_unit1.py::TestUnit1Fundamentals::test_linear_search -v
```

---

## 🎯 Effective Learning Workflow

### Step 1: Read the Problem
1. Open the problem file (e.g., `Python Solutions/Unit1_S1.py`)
2. Read the problem description carefully
3. Understand what the function should do

### Step 2: Try to Solve It
- **Don't look at the solution first!**
- Write your own function
- Test it mentally with examples
- Try edge cases

### Step 3: Check the Tests
```bash
# See what test cases exist for your problem
pytest tests/test_unit1.py::TestUnit1Fundamentals -v
```

This shows you:
- What inputs should be tested
- What the expected outputs are
- Edge cases you might have missed

### Step 4: Compare & Analyze
1. Look at test cases that failed
2. Trace through your code with test inputs
3. Read the solution in the original file
4. Understand the approach used

### Step 5: Document Complexity
For each solved problem, add a comment:
```python
# Problem 12: Linear Search
# Time: O(n) - iterate through all elements once
# Space: O(1) - no extra space needed
# Key insight: Start from beginning, return as soon as found

def linear_search(lst, target):
    for num in range(len(lst)):
        if target == lst[num]:
            return num
    return -1
```

---

## 📊 Using Tests to Learn

### Finding Your Weaknesses
```bash
# Run tests verbosely to see what fails
pytest tests/test_unit1.py -v

# Run with extra details
pytest tests/test_unit1.py -vv --tb=long
```

### Understanding Edge Cases
Look at test methods with names like:
- `test_*_empty_list` → How to handle empty input
- `test_*_single_*` → Minimum case
- `test_*_none` → Null/None handling
- `test_*_prime` → Special cases

### Learning from Test Code
Each test file shows:
```python
# The problem statement as comments
# Example trees, lists, inputs shown

# The function implementation you should learn from
def check_tree(root):
    return root.val == (root.left.val + root.right.val)

# Multiple test cases showing different scenarios
assert check_tree(tree_true) is True
assert check_tree(tree_false) is False
```

---

## 💪 Building a Learning Habit

### Daily (10-15 min)
```bash
# Pick one problem to solve
# 1. Read the problem
# 2. Code without reference (10 min)
# 3. Run tests: pytest tests/test_unit1.py::TestUnit1Fundamentals::test_linear_search -v
# 4. Review your solution vs expected solution
```

### Weekly (30-45 min)
```bash
# Complete all problems in one unit
# Run all unit tests: pytest tests/test_unit1.py -v
# Analyze your complexity notes
# Review patterns you learned
```

### Bi-Weekly Review (1 hour)
```bash
# Re-solve problems from 2 weeks ago
# Don't look at solutions first
# See how much you've improved
# Time yourself to gauge progress
```

---

## 🔍 Test-Driven Learning

### Understanding Test Output

**PASSED ✅**
```
tests/test_unit1.py::TestUnit1Fundamentals::test_linear_search PASSED [ 75%]
```
Your solution works for this test case!

**FAILED ❌**
```
tests/test_unit1.py::TestUnit1Fundamentals::test_linear_search FAILED
AssertionError: assert 5 != 4
```
Your solution returned 5, but expected 4. Debug by:
1. Trace through the algorithm with this test input
2. Print intermediate values
3. Compare with working solution

---

## 📈 Progress Tracking

### Create a Study Checklist
```markdown
# Unit 1 Progress

- [x] Problem 7 (Filter Evens): Completed 3/3/25, Reviewed 3/10/25
- [x] Problem 8 (Multiples): Completed 3/3/25
- [ ] Problem 9 (Divisors): Completed 3/4/25, Need to review
- [ ] Problem 10 (FizzBuzz): Attempted, need to finish
- [ ] Problem 11 (Print Indices): Not started
- [ ] Problem 12 (Linear Search): Completed 3/4/25

## Complexity Analysis Checklist
- [ ] All functions have time/space complexity documented
- [ ] Compared with test cases
- [ ] Alternatives considered and analyzed
```

---

## 🎓 Learning Tips

### Tip 1: Understand Before Memorizing
**Instead of:** "I memorized the linear search code"
**Do:** "I understand why we check each element and return immediately"

Test your understanding:
```bash
# Read only the test docstrings
# Predict what the function should do
# Never look at code
pytest tests/test_unit1.py -v
```

### Tip 2: Add Your Own Test Cases
When you understand a problem, write tests:
```python
# Add to test file
def test_linear_search_with_duplicates(self):
    """Test: Linear search returns first occurrence"""
    def linear_search(lst, target):
        for num in range(len(lst)):
            if target == lst[num]:
                return num
        return -1
    
    # Multiple occurrences - should return first
    assert linear_search([1, 2, 3, 2, 4], 2) == 1
```

### Tip 3: Teach It to Someone
Try explaining without looking at code:
1. "This problem is about..."
2. "The approach is to..."
3. "The key insight is..."
4. Then run tests to validate

### Tip 4: Compare Approaches
```bash
# Your approach
def linear_search_v1(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Alternative approach
def linear_search_v2(lst, target):
    return lst.index(target) if target in lst else -1

# Both correct! But different readability/efficiency
# Test with: pytest -v
```

---

## 🚀 When You're Stuck

1. **Look at similar test cases** - they show expected behavior
2. **Print debug values** - what's actually happening?
3. **Check edge cases** - empty list? None values?
4. **Read test docstring** - what's the test actually checking?
5. **Compare with test solution** - what's different?

### Debug Template
```python
def linear_search(lst, target):
    print(f"Searching for {target} in {lst}")
    for num in range(len(lst)):
        print(f"  Checking index {num}: {lst[num]}")
        if target == lst[num]:
            print(f"  Found at index {num}!")
            return num
    print("  Not found, returning -1")
    return -1

# Run with: python -c "from tests.test_unit1 import *; linear_search([5,2,3,4], 34)"
```

---

## ✨ Next: Add More Tests

Want to expand the test suite?

1. **Copy an existing test structure**
2. **Understand the problem** from the solution file
3. **Create test cases** for different scenarios
4. **Run pytest** to verify
5. **Commit and push** to GitHub

```bash
# Run new tests
pytest tests/test_unitX.py -v

# View coverage (if you install pytest-cov)
pytest --cov=tests tests/
```

---

## 🎯 Your Learning Goal

By the end of each unit, you should be able to:
- ✅ Solve all problems **without looking at solutions**
- ✅ Explain your approach in simple terms
- ✅ Analyze time/space complexity accurately
- ✅ Identify edge cases before testing
- ✅ Write clear, efficient code

Use the tests to validate you've achieved these goals!

---

**Remember: Learning to code is like learning a language. Tests are your conversation partners. 🗣️**
