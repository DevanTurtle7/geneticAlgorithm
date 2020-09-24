import globals

def test_change_string_first():
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
    test_change_string_first()
    test_change_string_last()
    test_change_string_middle()

run_all_tests()
