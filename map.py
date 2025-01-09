# def square_numbers(numbers):
#     return list(map(lambda x: x**2, numbers))
#
# numbers = [1, 2, 3, 4]
# print(square_numbers(numbers))  # Output: [1, 4, 9, 16]
#
#
# def convert_to_strings(data):
#     return list(map(str, data))
#
# data = [1, 2, 3]
# data_tuple = (4, 5, 6)
# print(convert_to_strings(data + list(data_tuple)))  # Output: ['1', '2', '3', '4', '5', '6']
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
#
# def add_three_lists(a, b, c):
#     return list(map(lambda x, y, z: x + y + z, a, b, c))
#
#
# print(add_three_lists(a, b, c))  # Output: [12, 15, 18]
#
#
#
# def add_and_diff_lists(a, b):
#     return list(map(lambda x, y: (x + y, abs(x - y)), a, b))
#
# a = [1, 2, 3]
# b = [3, 2, 1]
# print(add_and_diff_lists(a, b))  # Output: [(4, 2), (4, 0), (4, 2)]

def filter_integers(numbers):
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 != 0, numbers))
    return evens, odds

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = filter_integers(numbers)
print("Even numbers:", evens)  # Output: [2, 4, 6, 8, 10]
print("Odd numbers:", odds)  # Output: [1, 3, 5, 7, 9]