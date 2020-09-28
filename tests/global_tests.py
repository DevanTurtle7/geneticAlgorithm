"""
Tests the global functions to make sure it they are functioning properly.

author: Devan Kavalchek
"""

import globals

def test_change_string_first():
    """
    Tests the change_string_first() function by giving it a standard input
    and checking that the expected string is being returned
    """
    # Setup
    string = "hello"
    index = 0
    new_char = "t"
    expected_string = "tello"

    # Invoke
    result = globals.change_string_index(string, index, new_char)

    # Analyze
    assert(expected_string == result)

    print("test_change_string_index_0 passed!") # Prints if the test passes

def test_change_string_last():
    """
    Tests the change_string_first() function by giving it a standard input
    and checking that the expected string is being returned
    """
    # Setup
    string = "racecar"
    index = 6
    new_char = "t"
    expected_string = "racecat"

    # Invoke
    result = globals.change_string_index(string, index, new_char)

    # Analyze
    assert(expected_string == result)

    print("test_change_string_index_last passed!") # Prints if the test passes

def test_change_string_middle():
    """
    Tests the change_string_first() function by giving it a standard input
    and checking that the expected string is being returned
    """
    # Setup
    string = "turtoise"
    index = 4
    new_char = "i"
    expected_string = "turtiise"

    # Invoke
    result = globals.change_string_index(string, index, new_char)

    # Analyze
    assert(expected_string == result)

    print("test_change_string_index_middle passed!") # Prints if the test passes

def run_all_tests():
    """
    Runs all the tests
    """
    test_change_string_first()
    test_change_string_last()
    test_change_string_middle()

run_all_tests()
