import random

number = random.randrange(2, 1000)

def is_prime(n):
    if n >= 2 and n <= 1000:
        for number in range(2, n):
            if (n % number) == 0:
                return False
        return True
    else:
        print("n incorect")

print(number, is_prime(number))
