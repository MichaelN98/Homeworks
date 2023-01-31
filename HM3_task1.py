numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for index, item in enumerate(numbers):
    if item % 2 == 0:
        print(index,  'odd')
    if not item % 2 == 0:
        print(index, 'even')

