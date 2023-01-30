numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for index, item in enumerate(numbers):
    if index == 1 or index == 3 or index == 5 or index == 7:
        print(index,  'even')
    if index == 0 or index == 2 or index ==4 or index == 6:
        print(index, 'odd')

