# encoding:utf-8
import unittest
import sys

sys.path.append("../Josephusproblem")
from Create.reader import CsvReader, TxtReader, ZipReader, XlsxReader


class CreateTest(unittest.TestCase):
    def test_csv_reader(self):
        file_name = "../Josephusproblem/data/csv.csv"
        csv_sample = CsvReader(file_name).read_file()
        self.assertEqual(
            [["黄丽", "女", "12"], ["王磊", "男", "18"], ["谢菲", "男", "19"]], csv_sample
        )

    def test_xlsx_reader(self):
        file_name = "../Josephusproblem/data/xlsx.xlsx"
        xlsx_sample = XlsxReader(file_name).read_file()
        self.assertEqual(
            [["黄丽", "女", 12], ["王磊", "男", 18], ["谢菲", "女", 19]], xlsx_sample
        )

    def test_txt_reader(self):
        file_name = "../Josephusproblem/data/txt.txt"
        txt_sample = TxtReader(file_name).read_file()
        self.assertEqual(
            [["黄丽", "女", "12"], ["王磊", "男", "18"], ["谢菲", "女", "19"]], txt_sample
        )

    def test_zip_reader(self):
        file_name = "../Josephusproblem/data/zip.zip"
        zip_sample = ZipReader(file_name, "players.txt").read_file()
        self.assertEqual(
            [["华夏", "女", "1"], ["西安", "男", "33"], ["西北", "女", "22"]], zip_sample
        )


if __name__ == "__main__":
    unittest.main()
