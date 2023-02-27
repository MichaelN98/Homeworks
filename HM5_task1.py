import random
import os
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

#     print(os.getcwd())
#     os.makedirs('test/data')              #  script directory tree
    with open('expressions.txt', 'w') as file:
        file.write(str(list))
    with open('expressions.txt', 'r') as file:
        for line in file:
            str =line.replace(',', ' ')    # убрал пробелы
            print(str)
        for value in str:             # хочу прогнать через цикл каждое значение и после записать
            print(value)




#    через pickle

    # numbers_bytes = pickle.dumps(list)
    # print(numbers_bytes)
    # with open('expressions.txt', 'w+b') as file:
    #     file.write(numbers_bytes)
    #
    # with open('expressions.txt', 'rb') as file:
    #     result = file.read()
    # print(result)
    # final_res = pickle.loads(result)
    # print(final_res)
    # final_res_1 = final_res.split(',', ' ')
    # for res in final_res:
    #     res = final_res.split(',', ' ')
    #     print(res)
    #     final_res_1 = final_res.replace('\n', '').split(',')
    #     print(final_res_1)

