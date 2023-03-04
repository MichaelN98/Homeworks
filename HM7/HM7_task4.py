
numbers = [1, 2, 3, 5, 6, 7, 10, 123, 587, 11, 12, 999]
def max_two_values(lst):
    max1 = max2 = float('-inf')
    for number in lst:
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2:
            max2 = number
    return (max1, max2)
def min_two_values(lst):
    smallest = min(lst)
    lst.remove(smallest)
    second_smallest = min(lst)
    return smallest, second_smallest

if __name__ == '__main__':
    print(min_two_values(numbers))
    print(max_two_values(numbers))
