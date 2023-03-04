import random
import pickle



if __name__ == '__main__':
    list = []

    for n in range(100):
        my_tuple = random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)
        list.append(my_tuple)
    for items in list:
        if items[2] == 1:
            res = items[0] + items[1]
        elif items[2] == 2:
            res = items[0] - items[1]
        elif items[2] == 3:
            res = items[0] * items[1]
        print(res)


