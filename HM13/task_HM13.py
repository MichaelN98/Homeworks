class CustomIterator:
    def __init__(self, sequence: int, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index and self.__start_index < len(self.__sequence) and len(str(self.__start_index)) <= 1:
            value = self.__sequence[self.__start_index]
            self.__start_index += 1
            return value
        else:
            raise StopIteration
