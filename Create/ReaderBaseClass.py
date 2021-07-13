from abc import ABCMeta, abstractmethod

class ReaderBaseClass(metaclass=ABCMeta):
    def __init__(self,file_name):
        self.name = file_name
        self.content = []

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_to_list(self,file):
        pass