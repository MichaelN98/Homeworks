class CustomIterator:
    def __init__(self, sequence: int, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index
        self.__current_position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index <= self.__current_position <= self.__end_index:
            value = self.__sequence[self.__current_position]
            self.__current_position += 1
            return value
        else:
            raise StopIteration


