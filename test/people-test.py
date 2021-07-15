import sys
sys.path.append("../Josephusproblem")
import unittest
from People.people import Person

class PeopleTest(unittest.TestCase):
    def test_gen_one_person(self):
        peoson = Person("闪闪",'女',3)
        self.assertEqual("姓名：闪闪，性别：女，年龄：3",peoson.__str__())
    
if __name__ == '__main__':
    unittest.main()