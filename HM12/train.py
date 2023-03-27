

class Train:
    def __init__(self, locomotive):
        self.wagons = []
        self.locomotive = locomotive

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        result = ""
        for wagon in self.wagons:
            result += str(wagon) + ' '
        return result

