import numpy as np
import pandas as pd
import sys
sys.path.append('../Josephus problem')
from  Create.ReaderBaseClass import ReaderBaseClass as rb
import openpyxl
import json
import zipfile

class CsvReader(rb):
    def __init__(self,file_name):
        super().__init__(file_name)

    def read_file(self):
        csv_file = np.loadtxt(self.name,dtype=np.str, delimiter=',')  #load data from the text
        return csv_file

    def save_to_list(self,file):
        data = file.tolist()
        for item in data:
            self.content.append(item)
        return self.content



class XlsxReader(rb):
    def __init__(self,file_name):
        super().__init__(file_name)

    def read_file(self):
        xlsx = openpyxl.load_workbook(self.name)
        sheet = xlsx.active
        return sheet

    def save_to_list(self,sheet):
        rows = sheet.rows
        
        for row in rows:
            values = [cell.value for cell in row]
            self.content.append(values)
        return self.content


class ZipReader(rb):
    def __init__(self,file_name):
        super().__init__(file_name)
        self.file_list = []

    def read_file(self):
        self.zip_file = zipfile.ZipFile(self.name,'r')
        for each_file in self.zip_file.namelist():
            self.file_list.append(each_file)
        return self.file_list

    def save_to_list(self,file):
        file = self.file_list
        for read_name in file:
            zip_content = self.zip_file.open(read_name,'r')
            for line in zip_content.readlines():
                line = line.decode("utf-8")
                self.content.append(line.split())
            zip_content.close()
        return self.content
    

class TxtReader(rb):
    def __init__(self,file_name):
        super().__init__(file_name)

    def read_file(self):
        txt_file = open(self.name,'r',encoding = 'UTF-8')
        return txt_file

    def save_to_list(self, file):
        for line in file.readlines():
            self.content.append(line.split())
        file.close()
        return self.content


class JsonReader(rb):
    def __init__(self,file_name):
        super().__init__(file_name)

    def read_file(self):
        with open(self.name, encoding='utf-8') as f:
            line = f.read()
        return line

    def save_to_list(self, file):
        data = []
        convert_line = json.loads(file)
        data.append(convert_line) 
        dataframe = pd.DataFrame() 
        for row in data:
            for i in row:
                values = pd.DataFrame([i])
                dataframe = dataframe.append(values) 
        order = ['姓名','性别','年龄']
        dataframe = dataframe[order]
        dataframe.to_excel('data.xlsx', sheet_name='Sheet1', startcol=0, index=False,header=False)
        xlsx_file = XlsxReader('data.xlsx').read_file()
        self.content = XlsxReader('data.xlsx').save_to_list(xlsx_file)
        return self.content
    


    

        