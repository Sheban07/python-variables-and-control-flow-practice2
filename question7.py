#Write a function called remove_duplicates that takes a list as input and returns a new list with all
# duplicate elements removed. You cannot use the set function to solve this problem.
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_list = [1, 2, 2, 3, 4, 4, 5]
print("List with duplicates removed:", remove_duplicates(input_list))
