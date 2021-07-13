# encoding:utf-8
import sys
sys.path.append('../Josephus problem')
import pathlib 
from Josephus.josephus import Josephus
from Create.reader import CsvReader,XlsxReader,ZipReader,TxtReader,JsonReader
from People.people import Person
from src.conf import Flag

class Achieve():
    def __init__(self):
        self._reader = None
        self._start = 0
        self._step = 0
        self._people = []


    def select_reader(self,file_name):  #选择reader
        file_extension = pathlib.Path(file_name).suffix

        if file_extension == ".csv":
            self._reader = CsvReader(file_name)

        if file_extension == ".xlsx":
            self._reader = XlsxReader(file_name)

        if file_extension == '.zip':
            self._reader = ZipReader(file_name)

        if file_extension == ".txt":
            self._reader = TxtReader(file_name)

        if file_extension == ".json":
            self._reader = JsonReader(file_name)
        else:
            ValueError

        file = self._reader.read_file()

        return self._reader.save_to_list(file)


    def create_people(self):  #创建人员列表
        for i in range(len(self._reader.content)):
            person = Person(self._reader.content[i][0],self._reader.content[i][1],self._reader.content[i][2])
            self._people.append(person)
        return self._people


    def set_start(self,start_pos):  #创建起始位置
        self._start = int(start_pos)

        if start_pos <= 0:
            ValueError


    def set_step(self,step):  #设置步长
        self._step = int(step)

        if step <= 0:
            ValueError

    def set_josephus_sample(self):  #创建约瑟夫环
        self.josephus = Josephus(self._people,self._start,self._step)


    def output(self):  #输出结果
        for i in range(self.josephus.total_number):
            self.josephus.__next__()
        self.display(flag=Flag.SELECT)
        return self.josephus.out_list

    def display(self,flag):
        if flag == Flag.SELECT:
            for i in range(len(self.josephus.out_list)):
                print('出去的人是{},性别{},年龄{}'.format(self.josephus.out_list[i].name,self.josephus.out_list[i].gender,self.josephus.out_list[i].age))

        if flag == Flag.LAST:
            print('存活的人是{},性别{},年龄{}'.format(self._people[0].name,self._people[0].gender,self._people[0].age))
