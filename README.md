# Python Problem Sets - LeetCode Style Challenges

A comprehensive collection of LeetCode-style problems organized by data structures and algorithms, designed for learning and interview preparation.

## 📚 Repository Structure

```
.
├── Python Solutions/      # Main problem solutions
├── TIPS 102/             # Second version/variant problems  
├── TIPS 103/             # Third version/variant problems
├── tests/                # Pytest test suite
├── pytest.ini            # Pytest configuration
└── README.md             # This file
```

## 🎯 Learning Outcomes by Unit

### **Unit 1: Fundamentals** 
*Lists, Loops, Functions, Basic Algorithms*

#### Key Concepts
- List manipulation and filtering
- Control flow (loops, conditionals)
- Linear search algorithm
- Index and enumeration

#### Problems & Keywords
| Problem | Topic | Key Skill | Complexity |
|---------|-------|-----------|-----------|
| Problem 7 | Filter Evens | List comprehension, filtering | O(n) |
| Problem 8 | Multiples of Five | Range operations, iteration | O(1) |
| Problem 9 | Divisors | Modulo operator, list generation | O(n) |
| Problem 10 | FizzBuzz | Conditionals, modulo logic | O(n) |
| Problem 11 | Print Indices | Enumeration, index access | O(n) |
| Problem 12 | Linear Search | Basic search algorithm | O(n) |

#### Learning Goals
- [x] Understand list iteration and comprehensions
- [x] Master conditionals and loop control
- [x] Implement basic search (linear search)
- [x] Work with indices and enumeration

---

### **Unit 2: Strings**
*String Manipulation, Parsing, Pattern Matching*

#### Key Concepts
- String indexing and slicing
- Character iteration
- String methods
- Pattern recognition

#### Recommended Approaches
- Iterate through strings with `for char in string`
- Use string methods: `.split()`, `.join()`, `.replace()`, `.find()`
- Practice string slicing notation
- Consider immutability when modifying strings

---

### **Unit 3: Dictionaries & Hash Maps**
*Key-Value Storage, Hashing, Lookups*

#### Key Concepts
- Dictionary/hash map construction
- Key-value relationships
- Hash collisions (conceptual)
- O(1) average-case lookups

#### Common Patterns
- Counting frequencies: `dict[key] = dict.get(key, 0) + 1`
- Grouping elements by properties
- Using tuples as keys: `dict[(x, y)]`

---

### **Unit 4: Two Pointers**
*Dual-Index Traversal, Optimization Technique*

#### Key Concepts
- Two pointer technique
- Fast and slow pointers
- Convergent pointers
- Space optimization

#### Problem Types
- Finding pairs in sorted arrays
- Reversing sequences
- Partition/rearrangement problems
- Cycle detection (slow/fast pointers)

---

### **Unit 5: Classes & Object-Oriented Design**
*Objects, Methods, Attributes, Encapsulation*

#### Key Concepts
- Class definition and instantiation
- Constructor (`__init__`)
- Instance methods and attributes
- Basic OOP principles

#### Design Patterns
- State management with instance variables
- Methods that modify instance state
- Creating multiple instances

---

### **Unit 6: Advanced Linked Lists**
*Complex Node Operations, Multi-Pass Algorithms*

#### Key Concepts
- Linked list traversal and manipulation
- Detecting cycles (Floyd's algorithm)
- Finding middle nodes (two pointers)
- Reversing linked lists

#### Common Challenges
- Working with `None` for tail/head
- Single vs. double linked lists
- Handling edge cases (empty list, single node)
- Memory efficiency with pointers

---

### **Unit 7: Divide & Conquer + Recursion**
*Breaking Problems into Subproblems, Recursive Solutions*

#### Key Concepts
- Recursive base cases and recursive cases
- Memoization (dynamic programming foundation)
- Divide and conquer strategy
- Backtracking

#### Classic Problems
- Binary search (recursive & iterative)
- Merge sort
- Quick sort
- Permutations and combinations

#### Recursion Tips
```python
# Template
def solve(n):
    # Base case
    if n <= 1:
        return base_value
    
    # Recursive case
    return combine(solve(n-1), solve(n-2), ...)
```

---

### **Unit 8: Binary Trees I**
*Tree Construction, Basic Properties, Simple Traversals*

#### Key Concepts
- Tree node structure
- Binary tree properties (root, leaves, height)
- Tree relationships (parent, child, sibling)
- Basic tree traversals

#### Core Operations
- Building trees programmatically
- Checking tree properties
- Finding specific nodes
- Calculating tree metrics

#### Problems in This Unit
| Problem | Topic | Time | Space |
|---------|-------|------|-------|
| Build Binary Tree | Tree construction | O(1) | O(1) |
| 3-Node Sum | Property validation | O(1) | O(1) |
| 3-Node Sum II | Handling missing nodes | O(1) | O(1) |
| Find Leftmost Node | Tree traversal | O(h) | O(1) |

#### Learning Goals
- [x] Understand tree node references
- [x] Build tree structures from scratch
- [x] Validate tree properties
- [x] Traverse trees (depth-first left traversal)

---

### **Unit 9: Advanced Binary Trees**
*Complex Traversals, Level-Order, Path Finding*

#### Key Concepts
- In-order, pre-order, post-order traversals
- Level-order (breadth-first) traversal
- Finding paths in trees
- Tree balancing concepts

#### Advanced Patterns
- Reconstructing trees from traversals
- Finding Lowest Common Ancestor (LCA)
- Path sum problems
- Serialization/deserialization

---

### **Unit 10: Miscellaneous & Review**
*Mixed Problems, Interview Prep, Non-Standard Algorithms*

#### Topics Covered
- Bit manipulation
- String/array edge cases
- Problem-solving strategies
- Integration of multiple concepts

---

## 🧪 Running Tests

### Prerequisites
```bash
pip install pytest
```

### Run All Tests
```bash
pytest
```

### Run Tests by Unit
```bash
pytest tests/test_unit1.py    # Unit 1 tests
pytest tests/test_unit8.py    # Unit 8 tests
```

### Run with Verbose Output
```bash
pytest -v
```

### Run Specific Test
```bash
pytest tests/test_unit1.py::TestUnit1Fundamentals::test_linear_search -v
```

---

## 📊 Complexity Analysis Guide

When reviewing your solutions, use this checklist:

### Time Complexity
- **O(1)**: Constant time (single operation)
- **O(n)**: Linear (iterate once)
- **O(n²)**: Quadratic (nested loops)
- **O(log n)**: Logarithmic (binary search)
- **O(n log n)**: Linearithmic (efficient sorting)

### Space Complexity
- **O(1)**: No extra space
- **O(n)**: Extra space proportional to input
- **O(h)**: Height of tree (recursion depth)
- **O(log n)**: Logarithmic extra space

### Question Checklist
For each problem, ask:
- [ ] What's the time complexity?
- [ ] What's the space complexity?
- [ ] Can I optimize further?
- [ ] What are edge cases?
- [ ] Is there a trade-off (speed vs. space)?

---

## 💡 Study Tips

### For Real Learning (Not Just Completing Problems)

1. **Understand Before Implementing**
   - Read problem carefully 2-3 times
   - Write out approach in comments
   - Think through examples manually first

2. **Trace Through Your Code**
   - Run through example inputs step-by-step
   - Print intermediate values
   - Verify assumptions

3. **Analyze Complexity**
   - Count loops and nested iterations
   - Understand recursion depth
   - Compare approaches for optimization

4. **Test Edge Cases**
   - Empty inputs
   - Single element
   - Large values
   - Negative numbers (if applicable)

5. **Connect to Data Structures**
   - Why use a dictionary vs. list?
   - When is a linked list better than array?
   - How does tree structure help?

---

## 🔄 Spaced Repetition Strategy

### First Pass (Learning): 
- Solve problem as best you can
- Read solution if stuck
- Understand the approach

### Second Pass (1-3 days): 
- Solve from scratch again
- Note what you forgot
- Identify patterns

### Third Pass (1-2 weeks): 
- Implement without references
- Optimize if possible
- Teach the approach to someone

---

## 📝 File Organization Tips

### Naming Convention
- `Unit{N}_S{1|2}.py` - Problem set files
- Files contain multiple related problems
- Test files: `test_unit{N}.py`

### Adding Comments
Include for each problem:
```python
# Problem X: [Problem Name]
# Given: [Input description]
# Return: [Output description]
# Time: O(?) Space: O(?)

def solution(input):
    pass
```

---

## 🚀 Next Steps

1. **Run the test suite** to validate your implementations
2. **Add complexity analysis** to each solution
3. **Create study groups** to discuss approaches
4. **Practice variations** by modifying constraints
5. **Review weekly** to reinforce learning

---

## 📚 Additional Resources

### Data Structures Cheatsheet
- **Arrays/Lists**: Sequential access, O(1) index lookup
- **Dictionaries**: Key lookup in O(1), for counting/grouping
- **Linked Lists**: O(1) insertion/deletion (with pointer), but O(n) access
- **Trees**: Hierarchical organization, efficient searching with BST
- **Graphs**: Represent networks and relationships

### Algorithm Patterns  
- **Divide & Conquer**: Break problem into subproblems
- **Dynamic Programming**: Store intermediate results (memoization)
- **Greedy**: Make locally optimal choices
- **Backtracking**: Explore all possibilities, undo when stuck

---

## 📈 Progress Tracking

### Create a Personal Study Log
Track for each unit:
- [ ] Date started
- [ ] Key concepts learned
- [ ] Problems completed
- [ ] Complexity analysis done
- [ ] Date for review (2 weeks later)

---

## ⚠️ Common Pitfalls to Avoid

- ❌ Skipping edge case testing
- ❌ Not analyzing complexity before submitting
- ❌ Copying solutions without understanding
- ❌ Not practicing similar problems
- ❌ Ignoring error messages

---

## Contributing

To add new test cases or solutions:
1. Follow the existing code style
2. Add docstrings explaining the problem
3. Include test cases with examples
4. Document time/space complexity

---

**Happy Learning! 🎓**

For interview prep, focus on understanding *why* a solution works, not just writing code that passes tests.
