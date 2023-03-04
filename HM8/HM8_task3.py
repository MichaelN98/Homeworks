# Comprehensions

divisible_by7 = [num for num in range(1, 1001) if num % 7 == 0]

if __name__ == '__main__':
    print(divisible_by7)

# def divisible_by_7(func):
#     def wrapper():
#         for number in range(1, 1001):
#             if number % 7 == 0:
#                 func(number)
#     return wrapper
#
# @divisible_by_7
# def print_number(num):
#     print(num)
#
# print_number()
