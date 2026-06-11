"""
Utility module with functions to test for the Unit Testing with pytest assignment.
Students will write tests for these functions.
"""

class Calculator:
    """Simple calculator for demonstrating unit testing."""
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a + b
    
    def divide(self, a, b):
        """Divide a by b and return the result."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def is_even(self, n):
        """Check if a number is even."""
        if not isinstance(n, int):
            raise TypeError("Argument must be an integer")
        return n % 2 == 0


def validate_email(email):
    """
    Validate an email address.
    Returns True if valid, raises ValueError if invalid.
    """
    if not email:
        raise ValueError("Email cannot be empty")
    if "@" not in email:
        raise ValueError("Email must contain @")
    if "." not in email.split("@")[1]:
        raise ValueError("Email domain must contain a dot")
    return True


def fetch_user_data(user_id):
    """
    Fetch user data from an API.
    This function will be mocked in testing.
    """
    import requests
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()


def process_user(user_id):
    """
    Process user data by fetching and transforming it.
    This will be tested using mocks for fetch_user_data.
    """
    user = fetch_user_data(user_id)
    return {
        "id": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email"),
        "display_name": f"{user.get('name')} ({user.get('email')})"
    }
