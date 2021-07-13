# encoding:utf-8
import unittest
import sys
sys.path.append('E:\\LSS\\LSS\\Josephus problem')
from Create.create import CSV_reader,XLSX_reader,TXT_reader,JSON_reader


class CreateTest(unittest.TestCase):
    def test_csv(self):
        file_name = 'E:\\LSS\\LSS\\Josephus problem\\data\\csv.csv'
        csv_sample = CSV_reader(file_name).read_file()
        self.assertEqual(['黄丽,女,12'],csv_sample)

    def test_xlsx(self):
        file_name = 'E:\\LSS\\LSS\\Josephus problem\\data\\xlsx.xlsx'
        xlsx_sample = XLSX_reader(file_name).read_file()
        self.assertEqual([['黄丽', '女', 12],['王磊', '男', 18],['谢菲', '女', 19]],xlsx_sample)


    def test_txt(self):
        file_name = 'E:\\LSS\\LSS\\Josephus problem\\data\\txt.txt'
        txt_sample = TXT_reader(file_name).read_file()
        self.assertEqual([['黄丽女12']],txt_sample)

    def test_josn(self):
        file_name ='E:\\LSS\\LSS\\Josephus problem\\data\\json.json'
        json_sample = JSON_reader(file_name).read_file()
        self.assertEqual([['黄丽女12']],json_sample)
    



if __name__ == '__main__':
    unittest.main()


