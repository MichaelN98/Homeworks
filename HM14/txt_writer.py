from writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def write(self, new_data: str):
        with open(self.file_path, 'w') as file:
            file.write(new_data)
