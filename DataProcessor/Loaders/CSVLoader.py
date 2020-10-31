import csv
from io import TextIOWrapper

from .Loader import Loader


class CSVLoader(Loader):
    path = ''  # type: str

    header = ['tweet', 'tag']

    file = None  # type: None or TextIOWrapper

    reader = None  # type: None or csv.DictReader

    writer = None  # type: None or csv.DictWriter

    state = None  # type: None or int

    delimiter = '^'

    def __init__(self, save_path: str, header=None):
        self.path = save_path
        if header is not None:
            self.header = header

    def open(self, append=True):
        try:
            self.file = open(self.path, mode=('a+' if append else 'w+'), newline='', encoding='utf-8')
        except PermissionError:
            raise Exception('Permission error, file might be opened by other process')

        self.__create_file_handler()
        self.__set_state(self.STATE.READY)
        return self

    def write(self, model):
        if self.state == self.STATE.READY:
            self.writer.writerow(dict(zip(self.header, [
                model.getText(),
                model.getTag() if callable(getattr(model, 'getTag')) else None
            ])))
            return self
        else:
            raise Exception('CSV File stream is not ready')

    def close(self):
        # Close if not closed
        if self.state != self.STATE.CLOSED:
            self.reader = None
            self.file.close()

        # Set closed state
        self.__set_state(self.STATE.CLOSED)
        return self

    def __set_state(self, state):
        self.state = state

    def __create_file_handler(self):
        # Check if first row is not empty
        temp_reader = csv.reader(self.file)
        try:
            header = next(temp_reader)
            if isinstance(header, list):
                self.__create_csv_handler()
        except StopIteration:
            temp_writer = csv.writer(self.file, delimiter=self.delimiter)
            temp_writer.writerow(self.header)
            self.__create_csv_handler()

    def __create_csv_handler(self):
        self.reader = csv.DictReader(self.file, delimiter=self.delimiter)
        self.writer = csv.DictWriter(self.file, fieldnames=self.header, delimiter=self.delimiter)
