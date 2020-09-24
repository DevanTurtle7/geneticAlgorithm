MUTATION_RATE = 0.01
charset = 'abcdefghijklmnopwrstuvwxyz '

def change_string_index(string, index, new_char):
    # Setup
    length = len(string)
    new_string = ""
    first_half = ""
    second_half = ""

    if index == 0: # If the index is the first character there won't be a first half
        second_half = string[1:length]
    elif index == length - 1: # If the index is the last character there won't be a second half
        first_half = string[0:length-1]
    else:
        first_half = string[0:index]
        second_half = string[index+1:length]

    new_string = first_half + new_char + second_half
    return new_string
