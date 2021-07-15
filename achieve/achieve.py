# encoding:utf-8
import sys

sys.path.append("../Josephusproblem")
import pathlib
from Josephus.josephus import Josephus
from Create.reader import CsvReader, XlsxReader, ZipReader, TxtReader, JsonReader
from People.people import Person


class Achieve():
    def __init__(self):
        self._reader = None
        self._start = 0
        self._step = 0
        self._people = []
        self.out_list = []

    def select_reader(self, file_name):  # 选择reader
        file_extension = pathlib.Path(file_name).suffix

        if file_extension == ".csv":
            self._reader = CsvReader(file_name)

        if file_extension == ".xlsx":
            self._reader = XlsxReader(file_name)

        if file_extension == ".zip":
            self._reader = ZipReader(file_name)

        if file_extension == ".txt":
            self._reader = TxtReader(file_name)

        if file_extension == ".json":
            self._reader = JsonReader(file_name)
        else:
            ValueError

        file = self._reader.read_file()

        return self._reader.save_to_list(file)

    def create_people(self):  # 创建人员列表
        for i in range(len(self._reader.content)):
            person = Person(
                self._reader.content[i][0],
                self._reader.content[i][1],
                self._reader.content[i][2],
            )
            self._people.append(person)
        return self._people

    def set_start(self, start_pos):  # 创建起始位置
        self._start = int(start_pos)

        if start_pos <= 0:
            ValueError

    def set_step(self, step):  # 设置步长
        self._step = int(step)

        if step <= 0:
            ValueError

    def set_josephus_sample(self):  # 创建约瑟夫环
        self.josephus = Josephus(self._people, self._start, self._step)
        return self.josephus

    
