# 📘 Assignment: Unit Testing with pytest

## 🎯 Objective

Learn professional testing practices using pytest, Python's leading testing framework. You'll write unit tests to verify code behavior, use mocking to isolate dependencies, and measure test coverage. By the end, you'll understand how to write testable code and catch bugs before they reach production.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests

#### Description
Create a test file that verifies the functionality of a provided utility module. Practice writing assertions, running tests with pytest, and interpreting test results.

#### Requirements
Completed program should:

- Import pytest and write at least 5 test functions using `def test_*` naming convention
- Test both successful operations and edge cases (empty input, invalid values, boundary conditions)
- Use `assert` statements to verify expected outcomes
- Run tests with `pytest` and see all tests pass
- Include descriptive test names that explain what is being tested (e.g., `test_add_positive_numbers`)

### 🛠️ Test-Driven Development and Error Handling

#### Description
Write tests for error cases and validate that your code handles invalid input gracefully. Then implement the code to pass these tests.

#### Requirements
Completed program should:

- Write tests that verify exceptions are raised for invalid input (use `pytest.raises()`)
- Test boundary conditions and edge cases systematically
- Implement functions that pass both success and error case tests
- Test different exception types and error messages
- Achieve at least 90% test coverage for the tested module

### 🛠️ Mocking and Test Isolation (Stretch Goal)

#### Description
Write tests for code that depends on external services or complex dependencies. Use mocking to isolate the code under test and verify it interacts correctly with dependencies.

#### Requirements
Completed program should:

- Use `unittest.mock` or `pytest-mock` to mock external function calls
- Verify that mocked functions are called with correct arguments
- Test code that makes HTTP requests or database calls without actually making those requests
- Assert the behavior of your code independent of external dependencies
- Include at least 3 mocked test cases demonstrating different mock scenarios
