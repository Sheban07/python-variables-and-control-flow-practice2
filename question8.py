#Write a function that takes a dictionary and an integer n as input and returns a list of keys from
# the dictionary where the value is greater than n. For example, for the dictionary {'a': 5, 'b': 12, 'c': 3} and n = 4,
# the function should return ['a', 'b'].
def keys_greater_than_n(input_dict, n):
    keys_list = []
    for key, value in input_dict.items():
        if value > n:
            keys_list.append(key)
    return keys_list
input_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print("Keys with values greater than", n, ":", keys_greater_than_n(input_dict, n))
