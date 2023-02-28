def square_evens_comp(numbers):
  return [num*num for num in range(numbers) if num % 2 == 0]

print(square_evens_comp(1000000000))
