# The original list
numbers = [1, 2, 3, 4, 5]

# Using a lambda function with map() to double each value
doubled_numbers = list(map(lambda x: x ** 10, numbers))
print(doubled_numbers)