import sys
sys.path.append('../Josephus Problem')
from achieve.achieve import Achieve
from src.conf import Flag

if __name__ == '__main__':
    sample = Achieve()
    file_name = '../Josephus problem/data/zip.zip'
    sample.select_reader(file_name)
    sample.create_people()
    sample.set_start(2)
    sample.set_step(1)
    sample.set_josephus_sample()
    sample.output()
    sample.display(flag=Flag.LAST)


