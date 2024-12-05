# # # #
# # # # numbers = [1, 2, 3, 4, 5]
# # # #
# # # # def pakelt_kvadratu (numbers: list) -> list:
# # # #     kvadratu = []
# # # #     for number in numbers:
# # # #         number = number**2
# # # #         kvadratu.append(number)
# # # #     return kvadratu
# # # #
# # # # print (pakelt_kvadratu(numbers))
# # # #
# # # # def square (numbers):
# # # #     return [number**2 for number in numbers]
# # # #
# # # # numbers = [1, 2, 3, 4, 5]
# # # #
# # # # print(square(numbers))
# # # #
# # # # fruits= ["apple", "banana", "apple"]
# # # #
# # # # def count_fruits(fruits):
# # # #     counts = {}
# # # #     for fruit in fruits:
# # # #         counts[fruit] = counts.get(fruit,0) + 1
# # # #     return counts
# # # #
# # # # print(count_fruits(fruits))
# # # #
# # # #
# # # # def divide_by_ten():
# # # #     try:
# # # #         x = int(input("Įveskite skaičių: "))
# # # #         print(x)
# # # #         return 10 / x
# # # #     except ValueError:
# # # #         print("Klaida: įvestas ne skaičius.")
# # # #     except ZeroDivisionError:
# # # #         print("Klaida: dalyba iš nulio.")
# # #
# # #
# # # # print("Rezultatas:", divide_by_ten())
# # #
# # # #
# # # # numbers = [2, 234, 3, 34, 234, 34, 5, 46, 56, 65]
# # # # even = []
# # # # for n in numbers:
# # # #     if n % 2 == 0:
# #  #         even.append(n)
# # # # print()a
# # # #
# # # # ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
# # # #
# # # # print(ages["Alice"])
# # #
# # #
# # # class InvalidAgeError(Exception):
# # #     def __init__(self, age, message="Age is not valid for this action."):
# # #         self.age = age
# # #         self.message = message
# # #         super().__init__(f"InvalidAgeError: Age is {self.age}. {self.message}")
# # #
# # #
# # # def validate_age(age, min_age=18):
# # #     if age < min_age:
# # #         raise InvalidAgeError(age, f"Minimum age is {min_age}.")
# # #
# # #
# # # validate_age(18
# # #              )
# #
# # def group_by_first (strings):
# #     grouped{}
# #     for letter in strings:
# #         key = letter[0].lower()
# #         if key in grouped:
# #             grouped[key].append(letter)
# d = {"a": 10, "b": 20, "c": 30}
# print(list(d.items()))
#
#
# # You are given a list called "users".
#
# # Implement the following two functions:
#
# # 1. function "filter_all_or_nothing_people" - takes the "users" list as an argument and
# # for the given list returns a list of users who either have no pets at all or have both a dog and a cat.
#
#
# # 2. function "filter_underaged_owners" - takes the "users" list as an argument and
# # for the given list returns a list of users who are not yet of legal age but already have at least one pet.
#
# users = [
#     {'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True}, #
#     {'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False},
#     {'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True}, #
#     {'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False},
#     {'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False}, #
#     {'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True},
#     {'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False},
#     {'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True},
#     {'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False}, #
# ]
#
# def filter_all_or_nothing_people (list_users:list) -> list:
#     list_pet_status = []
#     names = []
#     for user in list_users:
#         if (user["hasDog"] == True and user["hasCat"] == True) or (user["hasDog"] == False and user["hasCat"] == False):
#             list_pet_status.append(user)
#             # names = user["name"]
#         # print(names)
#             print(list_pet_status)
#     return list_pet_status
#
# def filter_underaged_owners (list_users) -> list:
#     list_legal_age =[]
#     for user in list_users:
#         if user["age"] < 18 and (user["hasDog"] == True or user["hasCat"] == True):
#             list_legal_age.append(user)
#     return list_legal_age
#
#
#
#
#
# print(filter_all_or_nothing_people (users))
# print(filter_underaged_owners (users))
#
#
# You are given a list called "users".

# Implement the following two functions:

# 1. function "filter_all_or_nothing_people" - takes the "users" list as an argument and
# for the given list returns a list of users who either have no pets at all or have both a dog and a cat.


# 2. function "filter_underaged_owners" - takes the "users" list as an argument and
# for the given list returns a list of users who are not yet of legal age but already have at least one pet.

users = [
    {'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True},  # filter
    {'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False},
    {'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True},  # filter
    {'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False},
    {'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False},  # filter
    {'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True},
    {'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False},
    {'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True},
    {'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False},  # filter
]


def filter_all_or_nothing_people(list_users: list) -> list:
    list_pet_status = []
    names = []
    for user in list_users:
        if (user["hasDog"] == True and user["hasCat"] == True) or (user["hasDog"] == False and user["hasCat"] == False):
            list_pet_status.append(user)
    for user2 in list_pet_status:
        names.append(user2["name"])

    print(names)

    return list_pet_status


def filter_underaged_owners(list_users) -> list:
    list_legal_age = []
    for user in list_users:
        if user["age"] < 18 and (user["hasDog"] == True or user["hasCat"] == True):
            list_legal_age.append(user)
    return list_legal_age


print(filter_all_or_nothing_people(users))
print(filter_underaged_owners(users))


