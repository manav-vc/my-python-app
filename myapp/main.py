# myapp/main.py
#Testing 
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This block runs when main.py is executed directly
    user_name = input("Enter your name: ")
    print(greet(user_name))