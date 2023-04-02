

from train import Train
from wagon import Wagon

if __name__ == '__main__':

    locomotive = "Locomotive"
    train = Train(locomotive)

    for numbers in range(1, 5):
        wagon = Wagon(numbers)
        for number in range(10):
            wagon.add_passengers(f"Passenger {number + 1}")
        train.add_wagon(wagon)

    print("Number of wagons:", len(train))
    print("Wagon numbers:", train)

    for wagon in train.wagons:
        print("Wagon number:", wagon)
        print("Number of passengers:", len(wagon))


