import unittest
import sys

sys.path.append("../Josephusproblem")
from Josephus.josephus import Josephus


class JosephsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.people = ["python", "c++", "R", "java"]
        return super().setUp()

    def test_step_is_zero(self):
        self.josephus = Josephus(self.people, 1, 0)
        out_list = []
        for out_person in self.josephus:
            out_list.append(out_person)
        self.assertEqual(out_list, ["python", "java", "R", "c++"])

    def test_step_is_negetive(self):
        self.josephus = Josephus(self.people, 1, -1)
        out_list = []
        for out_person in self.josephus:
            out_list.append(out_person)
        self.assertEqual(out_list, ["java", "c++", "R", "python"])

    def test_start_is_negetive(self):
        self.josephus = Josephus(self.people, -2, 1)
        out_list = []
        for out_person in self.josephus:
            out_list.append(out_person)
        self.assertEqual(out_list, ["R", "java", "python", "c++"])

    def test_people_is_none(self):
        people = []
        self.josephus = Josephus(people, 2, 1)
        out_list = []
        for out_person in self.josephus:
            out_list.append(out_person)
        self.assertEqual(out_list, [])


if __name__ == "__main__":
    unittest.main()
