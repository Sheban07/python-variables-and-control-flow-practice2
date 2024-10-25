#Write a Python function that accepts a list of integers and a target sum. The function should
# return True if there are two distinct numbers in the list that add up to the target sum, and False otherwise.
def has_pair_with_sum(numbers, target_sum):
    seen = set()
    for number in numbers:
        complement = target_sum - number
        if complement in seen:
            return True
        seen.add(number)
    return False
numbers = [1, 2, 3, 4, 5]
target_sum = 8
print("Pair with target sum exists:", has_pair_with_sum(numbers, target_sum))
