"""
Test file template for the Unit Testing with pytest assignment.
This file demonstrates pytest structure and includes examples.

To run these tests:
    pytest test_utils.py -v

To see test coverage:
    pytest test_utils.py --cov=utils
"""

import pytest
from utils import Calculator, validate_email, process_user, fetch_user_data


# ============================================================================
# TASK 1: Basic Unit Tests
# ============================================================================
# TODO: Write at least 5 test functions for the Calculator class and
# validate_email function. Include tests for normal cases and edge cases.

class TestCalculator:
    """Test cases for the Calculator class."""
    
    def test_add_positive_numbers(self):
        """Example: Test adding two positive numbers."""
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
    
    def test_add_negative_numbers(self):
        """Example: Test adding negative numbers."""
        calc = Calculator()
        result = calc.add(-2, -3)
        assert result == -5
    
    # TODO: Add more test cases for add() with edge cases like:
    # - Zero values
    # - Floating point numbers
    # - Large numbers
    
    # TODO: Write tests for divide():
    # - Normal division
    # - Division resulting in float
    
    # TODO: Write tests for is_even():
    # - Even numbers
    # - Odd numbers
    # - Zero
    # - Negative numbers


class TestEmailValidation:
    """Test cases for email validation."""
    
    def test_valid_email(self):
        """Example: Test a valid email address."""
        assert validate_email("student@example.com") == True
    
    # TODO: Add test cases for:
    # - Email without @ symbol
    # - Email without domain extension
    # - Empty string
    # - Various valid email formats


# ============================================================================
# TASK 2: Error Handling and Exception Testing
# ============================================================================
# TODO: Write tests that verify exceptions are raised for invalid input.
# Use pytest.raises() context manager.

def test_calculator_type_error():
    """Example: Test that Calculator raises TypeError for non-numeric input."""
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add("5", 3)


def test_divide_by_zero():
    """Example: Test that divide raises ValueError when dividing by zero."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


# TODO: Add more error handling tests for:
# - Calculator.is_even() with invalid input
# - validate_email() with invalid formats
# - Edge cases that should raise exceptions


# ============================================================================
# TASK 3: Mocking and Test Isolation
# ============================================================================
# TODO: Write tests that mock external dependencies.
# Use unittest.mock.patch or pytest-mock to avoid making real API calls.

# Example using pytest-mock fixture (requires installing pytest-mock)
def test_process_user_success(mocker):
    """Example: Test process_user without making real API calls."""
    # Mock the fetch_user_data function to return sample data
    mock_data = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }
    mocker.patch("utils.fetch_user_data", return_value=mock_data)
    
    result = process_user(1)
    
    assert result["id"] == 1
    assert result["name"] == "Alice"
    assert result["display_name"] == "Alice (alice@example.com)"


# TODO: Add more mocking tests:
# - Mock fetch_user_data to raise exceptions
# - Verify that fetch_user_data is called with correct arguments using
#   mocker.assert_called_with()
# - Test error handling in process_user


# ============================================================================
# Running Tests
# ============================================================================
# Run all tests:
#   pytest test_utils.py -v
#
# Run with coverage:
#   pytest test_utils.py --cov=utils --cov-report=html
#
# Run a specific test:
#   pytest test_utils.py::TestCalculator::test_add_positive_numbers -v
#
# Run tests matching a pattern:
#   pytest test_utils.py -k "add" -v
