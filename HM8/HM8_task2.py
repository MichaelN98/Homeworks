
def get_even_squares():
  for number in range(0, 1000000001):
    if number % 2 == 0:
      print(number ** 2)

if __name__ == '__main__':
  get_even_squares()
