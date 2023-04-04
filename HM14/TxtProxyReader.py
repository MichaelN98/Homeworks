from HM14 import txt_writer
from HM14.reader import Reader
from HM14.txt_reader import TxtReader
from txt_writer import TxtWriter
from writer import Writer


class TxtProxyReader(Reader, Writer):
    def __init__(self, txt_reader: TxtReader, txt_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader
        self.__writer = txt_writer

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

    def write(self, new_data):
        if self.__result != new_data:
            self.__writer.write(new_data)
            self.__is_actual = False

