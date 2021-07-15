from abc import ABCMeta, abstractmethod

class Reader(metaclass=ABCMeta):
    def __init__(self,file_name):
        self.name = file_name
        self.content = []

    @abstractmethod
    def read_file(self):
        pass

    