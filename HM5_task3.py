import pandas as pd

if __name__ == '__main__':
    with open('text_HM5.txt', 'r') as file:
        file_data = file.read()
        phrase = file_data
        print(pd.Series(list(phrase)).value_counts())
