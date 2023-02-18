def square(a):
    perimetr = 4 * a
    square_quadrate = a * a
    diagonal = (a ** 2) / 2
    diagonal = diagonal ** 0.5

    result = (perimetr, square_quadrate, diagonal)

    return result


print(square(16))
