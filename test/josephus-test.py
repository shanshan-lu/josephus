import unittest
import sys
sys.path.append('F:\\LSS\\LSS\\Josephus problem')
from Josephus.josephus import Josephus

class JosephsTest(unittest.TestCase):
    def test_add_person(self):
        people = ['python','c++']
        start = 1
        step = 2
        person = 'java'
        josephus_sample= Josephus(people,start,step).add_people(person)
        self.assertEquals(['python','c++','java'],josephus_sample)

    def test_del_person(self):
        people = [0,1,2]
        start = 1
        step = 2
        adress = 1
        josephus_sample= Josephus(people,start,step).del_people(adress)
        self.assertEquals([0,2],josephus_sample)

    def test_kill_people(self):
        people = [1,2,3,4,5,6,7,8,9,10]
        start = 5
        step = 2
        josephus_sample = Josephus(people,start,step).kill_people()
        self.assertEquals(5,josephus_sample)

if __name__ =="__main__":
    unittest.main()