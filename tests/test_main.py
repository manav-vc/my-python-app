# tests/test_main.py
from myapp.main import greet

def test_greet_with_name():
    """Test that greet function returns correct message with a name."""
    assert greet("Alice") == "Hello, Alice!"

def test_greet_empty_name():
    """Test that greet function handles an empty name."""
    assert greet("") == "Hello"

def test_greet_numeric_name():
    """Test that greet function handles numeric input (though not strictly required for this simple function, good for example)."""
    assert greet("123") == "Hello, 123!"