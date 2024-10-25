#Given a tuple of numbers, e.g., (10, 20, 30, 40, 50), write a Python function using a loop that returns
# the largest number in the tuple.
def largest_in_tuple(numbers):
    # Assume the first number is the largest
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
numbers = (10, 20, 30, 40, 50)
print("The largest number in the tuple is:", largest_in_tuple(numbers))
