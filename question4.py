#Write a function that accepts a list of strings and returns a new list where each string is reversed.
# For example, for the input ["apple", "banana", "cherry"], the function should return ["elppa", "ananab", "yrrehc"].
def reverse_strings(strings):
    reversed_list = []
    for string in strings:
        reversed_list.append(string[::-1])
    return reversed_list
input_strings = ["apple", "banana", "cherry"]
print("Reversed strings:", reverse_strings(input_strings))
