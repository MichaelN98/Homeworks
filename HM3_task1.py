numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for index, item in enumerate(numbers):
    if item == 1 or item == 3 or item == 5 or item == 7:
        print(index,  'odd')
    if item == 0 or item == 2 or item ==4  or item == 6:
        print(index, 'even')

