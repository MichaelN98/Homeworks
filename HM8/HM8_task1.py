def log_func(func):
    def wrapper(*args):
        print(f'{func.__name__} was called with {args}')
        return func(*args)
    return wrapper

@log_func
def suma(left_operand, right_operand):
    return left_operand + right_operand

@log_func
def multiple(left_operand, right_operand):
    return left_operand * right_operand

print(suma(4, 4))
print(multiple(4, 4))
