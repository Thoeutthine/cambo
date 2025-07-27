"""
Solution for Problem 2: Add Two Numbers
Difficulty: Beginner

Simple addition of two numbers.
"""

def add_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Sum of a and b
    """
    return a + b

# Test cases
def test_add_two_numbers():
    assert add_two_numbers(5, 3) == 8
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(0, 0) == 0
    assert add_two_numbers(2.5, 1.5) == 4.0
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_add_two_numbers()
