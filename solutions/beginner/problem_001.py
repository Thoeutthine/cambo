"""
Solution for Problem 1: Hello World
Difficulty: Beginner

This is a simple function that returns a string literal.
"""

def hello_world():
    """
    Returns the string "Hello, World!"
    
    Returns:
        str: "Hello, World!"
    """
    return "Hello, World!"

# Test cases
def test_hello_world():
    result = hello_world()
    assert result == "Hello, World!", f"Expected 'Hello, World!', got {result}"
    print("✅ Test passed!")

if __name__ == "__main__":
    test_hello_world()
