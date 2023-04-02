class Wagon:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passengers(self, passengers):
        if len(self.passengers) < 10:
            self.passengers.append(passengers)
        else:
            print('Wagon is full')

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f'{self.number}'
