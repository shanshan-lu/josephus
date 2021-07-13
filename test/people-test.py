import sys
sys.path.append('E:\\LSS\\LSS\\Josephus problem')
import unittest
from People.people import People

class PeopleTest(unittest.TestCase):
    def test_judge_age(self):
        people_sample = People('lisa','女',-1)
        sample = people_sample.judge_age()
        self.assertEqual('年龄错误',sample)
    
    def test_judge_gender(self):
        people_sample = People('lisa','女',-1)
        sample = people_sample.judge_gender()
        self.assertEqual('性别错误',sample)

if __name__ == '__main__':
    unittest.main()