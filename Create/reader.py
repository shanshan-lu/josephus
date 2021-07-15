import numpy as np
import pandas as pd
import pathlib
import sys

sys.path.append("../Josephusproblem")
from Create.ReaderBaseClass import Reader as rd
import openpyxl
import json
import zipfile


class CsvReader(rd):
    def __init__(self, file_name):
        super().__init__(file_name)

    def read_file(self):
        file = np.loadtxt(
            self.name, dtype=np.str, delimiter=","
        )  # load data from the text
        data = file.tolist()
        for item in data:
            self.content.append(item)
        return self.content


class XlsxReader(rd):
    def __init__(self, file_name):
        super().__init__(file_name)

    def read_file(self):
        xlsx = openpyxl.load_workbook(self.name)
        sheet = xlsx.active
        rows = sheet.rows
        for row in rows:
            values = [cell.value for cell in row]
            self.content.append(values)
        return self.content


class TxtReader(rd):
    def __init__(self, file_name):
        super().__init__(file_name)

    def read_file(self):
        file = open(self.name, "r", encoding="UTF-8")

        for count, line in enumerate(file):
            self.content.append(line.split())
        file.close()
        return self.content


class ZipReader:
    def __init__(self, file_name, inter_file_name):
        self.name = file_name
        self.content = []
        self.inter_file_name = inter_file_name

    def read_file(self):
        file = zipfile.ZipFile(self.name, "r")
        if self.inter_file_name in file.namelist():
            filepath = file.extract(self.inter_file_name)
            file_extension = pathlib.Path(filepath).suffix
            if file_extension == ".txt":
                self.content = TxtReader(filepath).read_file()
            if file_extension == ".csv":
                self.content = CsvReader(filepath).read_file()
            if file_extension == ".xlsx":
                self.content = XlsxReader(filepath).read_file()
        return self.content


class JsonReader(rd):
    def __init__(self, file_name):
        super().__init__(file_name)

    def read_file(self):
        with open(self.name, encoding="utf-8") as f:
            line = f.read()

        data = []
        convert_line = json.loads(line)
        data.append(convert_line)
        dataframe = pd.DataFrame()
        for row in data:
            for i in row:
                values = pd.DataFrame([i])
                dataframe = dataframe.append(values)
        order = ["姓名", "性别", "年龄"]
        dataframe = dataframe[order]
        dataframe.to_excel(
            "data.xlsx", sheet_name="Sheet1", startcol=0, index=False, header=False
        )
        xlsx_file = XlsxReader("data.xlsx").read_file()
        self.content = XlsxReader("data.xlsx").save_to_list(xlsx_file)
        return self.content
