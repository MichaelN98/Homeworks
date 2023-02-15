def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5

    result = (p, s, d)

    return result


print(square(16))
