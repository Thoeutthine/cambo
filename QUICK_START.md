# Quick Start Guide

## 🚀 Getting Started with Algorithm Exercises

### 1. Choose Your Level
- **Beginner (100 problems)**: Basic programming concepts, loops, strings, lists
- **Medium (100 problems)**: Data structures, sorting, searching, trees, graphs
- **Hard (100 problems)**: Advanced algorithms, dynamic programming, optimization

### 2. Running Exercises

#### Run a single exercise:
```bash
python exercises/beginner/problem_001.py
```

#### Test your solution:
```bash
python test_runner.py single beginner 1
```

#### Track your progress:
```bash
python progress_tracker.py show
```

#### Mark a problem as completed:
```bash
python progress_tracker.py complete beginner 1
```

### 3. Exercise Structure

Each exercise file contains:
- Problem description
- Example input/output
- Function template to implement
- Test cases
- Time/space complexity hints (for medium/hard)

### 4. Workflow

1. **Read** the problem description
2. **Understand** the requirements and examples
3. **Implement** your solution in the provided function
4. **Test** your solution using the test cases
5. **Optimize** if needed (especially for hard problems)
6. **Mark as completed** using the progress tracker

### 5. Tips for Success

#### Beginner Level:
- Focus on understanding basic Python syntax
- Practice with loops, conditionals, and data types
- Don't worry about optimization yet

#### Medium Level:
- Learn common data structures (stacks, queues, trees)
- Understand time and space complexity
- Practice algorithmic thinking

#### Hard Level:
- Master dynamic programming concepts
- Study advanced graph algorithms
- Focus on optimization and edge cases
- Consider multiple approaches

### 6. Useful Commands

```bash
# Show overall progress
python progress_tracker.py show

# Get next 5 problems to solve
python progress_tracker.py next

# Get next 3 medium problems
python progress_tracker.py next medium 3

# Run all beginner tests
python test_runner.py category beginner

# Run tests for problems 1-10 in medium
python test_runner.py category medium 1 10

# Validate problem structure
python test_runner.py validate hard 1
```

### 7. Sample Problems

#### Beginner Example:
```python
# Problem: Add Two Numbers
def add_two_numbers(a, b):
    return a + b
```

#### Medium Example:
```python
# Problem: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#### Hard Example:
```python
# Problem: Longest Valid Parentheses
def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len
```

### 8. Learning Path

1. **Week 1-2**: Complete 20-30 beginner problems
2. **Week 3-4**: Complete remaining beginner + start medium
3. **Week 5-8**: Focus on medium problems
4. **Week 9-12**: Tackle hard problems
5. **Ongoing**: Review and optimize solutions

### 9. Resources

- **Time Complexity**: Learn Big O notation
- **Data Structures**: Arrays, Lists, Stacks, Queues, Trees, Graphs
- **Algorithms**: Sorting, Searching, Dynamic Programming, Greedy
- **Practice**: Solve problems daily, even if just 1-2

Happy coding! 🎉
